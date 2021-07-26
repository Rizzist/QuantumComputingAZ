from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum BCD Encoder/Decoder").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class enc(Scene):
	def construct(self):
		text = Text("Quantum BCD Encoder/Decoder").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("Quantum BCD Encoder").shift(UP*3.5)
		self.play(Write(title))

		itsdecimal = Text(r"Decimal").shift(DOWN*3 + LEFT*3)
		itsbin = Text(r"Binary").shift(DOWN*3 + RIGHT*3)
		self.play(FadeIn(itsbin), FadeIn(itsdecimal))


		#encoder
		enc1 = Rectangle(fill_opacity=1, fill_color=YELLOW).rotate(PI/2).scale(1.2).set_color(YELLOW)
		enc2 = Text("Enc").set_color(BLACK)
		encx = []
		ency = []
		for i in range(0, 10):
			encx.append(Line(np.array([-5, (i+0.5)/2-2.5, 0]), np.array([0, (i+0.5)/2-2.5, 0])))
			encx[i].generate_target()
		for i in range(0, 4):
			ency.append(Line(np.array([0, (i+0.5)/2-1, 0]), np.array([5, (i+0.5)/2-1, 0])))
			ency[i].generate_target()
		enc = Group(*encx, *ency, enc1, enc2)
		self.play(FadeIn(enc))

		for k in range(0, 4):
			for i in range(0, 10):
				encx[i].target.set_color(RED)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (int(current[j]) == 1):
						ency[j].target.set_color(RED)
					else:
						ency[j].target.set_color(WHITE)
				for j in range(len(current),  4):
					ency[j].target.set_color(WHITE)
				for q in range(0, 10):
					self.play(MoveToTarget(encx[q], run_time=0.01))
				for r in range(0, 4):
					self.play(MoveToTarget(ency[r], run_time=0.01))
				encx[i].target.set_color(WHITE)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (current[j] == 1):
						ency[j].target.set_color(WHITE)
				self.wait(0.1)
		self.play(FadeOut(enc), FadeOut(itsdecimal), FadeOut(itsbin))
		title2 = Text("4-to-2 BCD Encoder").shift(UP*3.5)
		self.play(Transform(title, title2))



		#draw the circuit
		base = 2
		offset = 1
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight):
				self.n = m
				self.dq = r"\ket{0}"
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq) + "_" + str(self.n)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([5, -offset*self.n + base, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=BLUE))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*5.75).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)


		qubits = []
		for i in range(0, 6):
			if (i == 0):
				qubits.append(qubit(i, 'I_0', 'g_1'))
			elif (i == 1):
				qubits.append(qubit(i, 'I_2', 'g_2'))
			elif (i == 2):
				qubits.append(qubit(i, 'I_1', 'g_3'))
			elif (i == 3):
				qubits.append(qubit(i, 'I_0', 'g_4'))
			elif (i == 4):
				qubits.append(qubit(i, '1', 'A'))
			elif (i == 5):
				qubits.append(qubit(i, '1', 'B'))
			else:
				qubits.append(qubit(i, '0', '-'))
			self.add(qubits[i].get())

		def toffoli(pos,up, mid, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot11 = Dot(np.array([cx,-offset*mid+ base,0]), fill_color=RED)
			q = max(mid, down)
			r = min(up, mid)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*r, 0]), np.array([cx, -offset*q + base, 0]))
			cnot = Group(cnot1, cnot11, cnot2, cnot3)
			return cnot
		def xgate(pos,down):
			cx = pos
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot = Group(cnot2)
			return cnot
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def swapgate(pos,up, down):
			cx = pos
			cnot1 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*up + RIGHT*cx + UP*base).set_color(RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot

		t1 = toffoli(0, 0, 1, 4)
		t2 = toffoli(2, 0, 2, 5)
		x1 = xgate(-2, 0)
		x2 = xgate(-2, 1)
		x3 = xgate(-2, 2)

		gates = Group(t1, t2, x1, x2, x3)
		self.play(FadeIn(gates))






		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)



		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)

		self.wait(2)
		for i in range(0, 6):
			self.remove(qubits[i].get())
		self.play(FadeOut(gates))


























		#DECODER
		title3 = Text("Decoder").shift(UP*3.5)
		self.play(Transform(title, title3))
		#encoder
		denc1 = Rectangle(fill_opacity=1, fill_color=YELLOW).rotate(PI/2).scale(1.2).set_color(YELLOW)
		denc2 = Text("Denc").set_color(BLACK)
		dencx = []
		dency = []
		for i in range(0, 10):
			dencx.append(Line(np.array([0, (i+0.5)/2-2.5, 0]), np.array([5, (i+0.5)/2-2.5, 0])))
			dencx[i].generate_target()
		for i in range(0, 4):
			dency.append(Line(np.array([-5, (i+0.5)/2-1, 0]), np.array([0, (i+0.5)/2-1, 0])))
			dency[i].generate_target()
		denc = Group(*dencx, *dency, denc1, denc2)
		self.play(FadeIn(denc))
		for k in range(0, 4):
			for i in range(0, 10):
				dencx[i].target.set_color(RED)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (int(current[j]) == 1):
						dency[j].target.set_color(RED)
					else:
						dency[j].target.set_color(WHITE)
				for j in range(len(current),  4):
					dency[j].target.set_color(WHITE)
				for r in range(0, 4):
					self.play(MoveToTarget(dency[r], run_time=0.01))
				for q in range(0, 10):
					self.play(MoveToTarget(dencx[q], run_time=0.01))
				dencx[i].target.set_color(WHITE)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (current[j] == 1):
						dency[j].target.set_color(WHITE)
				self.wait(0.1)
		self.wait(2)
		self.play(FadeOut(denc))



		#make circuit
		x = -5
		qubits = []
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, 'A', 'I_3'))
			elif (i == 1):
				qubits.append(qubit(i, 'B', 'I_2'))
			elif (i == 2):
				qubits.append(qubit(i, '0', 'I_1'))
			elif (i == 3):
				qubits.append(qubit(i, '1', 'I_0'))
			else:
				qubits.append(qubit(i, '0', '-'))
			self.add(qubits[i].get())

		cx1 = cxgate(-2, 0, 3)
		t1 = toffoli(-1, 1, 3, 2)
		cx2 = cxgate(0, 2, 1)
		cx3 = cxgate(1, 2, 3)
		swap1 = swapgate(1, 0, 1)
		cx4 = cxgate(2, 0, 1)

		gates = Group(cx1, t1, cx2, cx3, swap1, cx4)
		self.play(FadeIn(gates))

		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		while(x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(10)

































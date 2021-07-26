from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Latch, Counter").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class latch(Scene):
	def construct(self):
		text = Text("Quantum Latch, Counter").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Quantum Latch").shift(UP*3.5)
		corona= ImageMobject("./latch.jpeg")
		self.play(FadeIn(title), FadeIn(corona))

		why = Text("Asynchronous Bit Storage").shift(DOWN*3)
		self.play(FadeIn(why))

		self.wait(17)
		#draw the circuit
		self.play(FadeOut(why), FadeOut(corona))
		base = 2
		offset = 1.1
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, show=1):
				self.n = m
				self.show = show
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
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)


		qubits = []
		for i in range(0, 5):
			if (i == 0):
				qubits.append(qubit(i, 'E', 'E'))
			elif (i == 1):
				qubits.append(qubit(i, 'T', 'T'))
			elif (i == 2):
				qubits.append(qubit(i, '', 'Q'))
			elif (i == 3):
				qubits.append(qubit(i, '0', ''))
			else:
				qubits.append(qubit(i, '', '', 0))
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
		def vgate(pos, up, down):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"V").scale(1.5).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot4, vnot3, vnot1, vnot2)
			return vnot
		def vngate(pos, up, down):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"V^\dag").scale(1.5).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot4, vnot3, vnot1, vnot2)
			return vnot

		t1 = vgate(-3, 1, 2)
		t2 = cxgate(-2, 0, 1)
		x1 = vngate(-1, 1, 2)
		x2 = vgate(1, 0, 2)
		x3 = cxgate(2, 2, 3)

		gates = Group(t1, t2, x1, x2, x3)
		self.add(gates)

		makeCont = Line(np.array([5, -offset*3 + base, 0]), np.array([5, -offset*4 + base, 0]))
		makeCont2 = Line(np.array([-5, -offset*4 + base, 0]), np.array([-6, -offset*4+ base, 0]))
		makeCont3 = Line(np.array([-6, -offset*4 + base, 0]), np.array([-6, -offset*2+ base, 0]))
		makeCont4 = Line(np.array([-6, -offset*2 + base, 0]), np.array([-5, -offset*2+ base, 0]))

		cont = Group(makeCont4, makeCont3, makeCont2, makeCont)
		self.play(FadeIn(cont))



		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(5)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{+i}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{+i}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(5)




		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(5)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{-i}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{-i}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(6)

		for i in range(0, 5):
			self.remove(qubits[i].get())
		self.play(FadeOut(cont), FadeOut(gates))
































		title2 = Text("Quantum Counter").shift(UP*3.5)
		self.play(Transform(title, title2))

		#counter
		qubits = []
		for i in range(0, 5):
			if (i == 0):
				qubits.append(qubit(i, 'T', 'T'))
			elif (i == 1):
				qubits.append(qubit(i, 'E', ''))
			elif (i == 2):
				qubits.append(qubit(i, '0', ''))
			elif (i == 3):
				qubits.append(qubit(i, '0', ''))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"

		def latcher(width, height, p1, p2, p3):
			vx = -width/2.3
			latch1 = Rectangle(color=GREEN,fill_color=GREEN, fill_opacity=1, width=width, height=height)
			latch2 = Text("T Latch", color=BLACK)
			a1 = Tex(r"1").shift(DOWN*offset*p1 + RIGHT*vx + UP*1).set_color(WHITE)
			a2 = Tex(r"2").shift(DOWN*offset*p2 + RIGHT*vx + UP*1).set_color(WHITE)
			a3 = Tex(r"3").shift(DOWN*offset*p3 + RIGHT*vx + UP*1).set_color(WHITE)
			latch = Group(latch1, latch2, a1, a2, a3)
			return latch

		latch1 = latcher(2.6, 2.6, 0, 1, 2).shift(LEFT*3 + UP*1)
		latch2 = latcher(2.6, 3.8, -0.3, 1.4, 2.4).shift(LEFT*0 + UP*0.5)
		latch3 = latcher(2.6, 5, -0.8, 1.8, 2.8).shift(RIGHT*3)
		latches= Group(latch1, latch2, latch3)
		self.play(FadeIn(latches))


		implement = Text("Exercise: Implement in Qiskit").shift(DOWN*3.2)
		self.play(Write(implement))

		self.wait(10)



























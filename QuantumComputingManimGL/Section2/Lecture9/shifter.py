from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Barrel Shifter, Rotator").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class shifter(Scene):
	def construct(self):
		text = Text("Quantum Barrel Shifter, Rotator").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Barrel Shifter").shift(UP*3.5)
		self.play(Write(title))
		
		item = Tex(r"0000x_3x_2x_1x_00000")
		self.play(Write(item))

		shiftRight = Tex(r">>").shift(LEFT * 4)

		item.generate_target()
		item.target = Tex(r"00000x_3x_2x_1x_0000")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"000000x_3x_2x_1x_000")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"0000000x_3x_2x_1x_00")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"00000000x_3x_2x_1x_0")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"000000000x_3x_2x_1")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"0000000000x_3x_2")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"00000000000x_3")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		item.generate_target()
		item.target = Tex(r"000000000000")
		self.add(shiftRight)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftRight))
		self.wait(0.3)

		self.wait(3)
		
		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"0000x_3x_2x_1x_00000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"000x_3x_2x_1x_000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"00x_3x_2x_1x_0000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"0x_3x_2x_1x_00000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"x_3x_2x_1x_000000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"x_2x_1x_0000000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"x_1x_00000000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"x_000000000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		shiftLeft = Tex(r"<<").shift(RIGHT * 4)
		item.generate_target()
		item.target = Tex(r"000000000000")
		self.add(shiftLeft)
		self.play(MoveToTarget(item, run_time=0.001), FadeOut(shiftLeft))
		self.wait(0.3)

		self.wait(2)
		self.play(FadeOut(item))
		

		#make a 
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
		for i in range(0, 6):
			if (i == 0):
				qubits.append(qubit(i, 'Shifter', 'Shifter'))
			elif (i == 1):
				qubits.append(qubit(i, 'X_0', 'X_1'))
			elif (i == 2):
				qubits.append(qubit(i, 'X_1', 'X_2'))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())

		def cswap(pos,up, mid, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot11 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*mid + RIGHT*cx + UP*base).set_color(RED)
			q = max(mid, down)
			r = min(up, mid)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*r, 0]), np.array([cx, -offset*q + base, 0]))
			cnot = Group(cnot1, cnot11, cnot2, cnot3)
			return cnot

		f = []
		for i in range(0, 4):
			c = cswap(i-2, 0, i+1, i+2)
			f.append(c)
			self.add(f[i])

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(5)
		while(x < -1):
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
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)








		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(3)
		qubs = Group(*f)
		for i in range(0, 6):
			self.remove(qubits[i].get())
		self.play(FadeOut(qubs))

		title2 = Text("Rotator").shift(UP*3.5)
		self.play(Transform(title, title2))





		quantity = Tex(r"ABCDEFG")
		latest = Tex(r"\hookrightarrow").shift(LEFT*3)
		self.play(Write(quantity))

		quantity.generate_target()
		quantity.target = Tex(r"GABCDEF")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)

		quantity.target = Tex(r"FGABCDE")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)

		quantity.target = Tex(r"EFGABCD")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)

		quantity.target = Tex(r"DEFGABC")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)


		quantity.target = Tex(r"CDEFGAB")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)

		quantity.target = Tex(r"BCDEFGA")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(0.5)

		quantity.target = Tex(r"ABCDEFG")
		self.add(latest)
		self.play(MoveToTarget(quantity, run_time=0.1), FadeOut(latest))
		self.wait(1)

		self.play(FadeOut(quantity))


		qubits = []
		for i in range(0, 6):
			if (i == 0):
				qubits.append(qubit(i, 'Rotate', 'Rotate'))
			elif (i == 1):
				qubits.append(qubit(i, 'X_0', 'X_1'))
			elif (i == 2):
				qubits.append(qubit(i, 'X_1', 'X_2'))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', 'X_4'))
			elif (i == 5):
				qubits.append(qubit(i, 'X_4', 'X_0'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())
		f = []
		for i in range(0, 4):
			c = cswap(i-2, 0, i+1, i+2)
			f.append(c)
			self.add(f[i])



		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 0):
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
		while(x < 5):
			x += 0.05
			self.wait(0.001)








		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)









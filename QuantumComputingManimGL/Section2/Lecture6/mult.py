from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Multiplication Circuit").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class mult(Scene):
	def construct(self):
		text = Text("Quantum Multiplication Circuit").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))
		
		a = Tex(r"10").shift(UP*2.5)
		b = Tex(r"101").shift(UP*2 + LEFT*0.1)
		x = Tex(r"\times").shift(UP*2 + LEFT*1)
		line = Line(np.array([-1.5, 1.5, 0]), np.array([0.5, 1.5, 0]))
		multGroup = Group(a, b, x, line)
		self.play(FadeIn(multGroup))


		title = Text("Partial Product").shift(UP*3.5)
		self.play(Write(title))

		c = Tex(r"1\ 0 * 1").shift(UP*1)
		d = Tex(r"1\ 0\times * \ 0").shift(UP*0.5 + LEFT*0.2)
		e = Tex(r"1\ 0\times\times * 1").shift(UP*0 + LEFT*0.4)
		partial = Group(c, d, e)
		line2 = Line(np.array([-1.5, -0.5, 0]), np.array([0.5, -0.5, 0]))
		self.play(FadeIn(partial), FadeIn(line2))
		self.wait(5)

		c2 = Tex(r"1\ 0").shift(UP*1 + LEFT*0.2)
		d2 = Tex(r"----").shift(UP*0.5 + LEFT*0.4)
		e2 = Tex(r"1\ 0\times\times").shift(UP*0 + LEFT*0.6)
		partial2 = Group(c2, d2, e2)
		self.play(Transform(partial, partial2))
		self.wait(5)


		added = Tex(r"1\ 0\ 1\ 0").shift(DOWN*1 + LEFT * 0.6)
		self.play(FadeIn(added))

		self.wait(5)

		self.play(FadeOut(partial), FadeOut(multGroup), FadeOut(added), FadeOut(line2))
		


		#draw the circuit
		base = 2.2
		offset = 0.6
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
		for i in range(0, 10):
			if (i == 0):
				qubits.append(qubit(i, 'c', 'c'))
			elif (i == 1):
				qubits.append(qubit(i, 'x_0', 'x_0'))
			elif (i == 2):
				qubits.append(qubit(i, 'x_1', 'x_1'))
			elif (i == 5):
				qubits.append(qubit(i, 'd_0', 'd_0'))
			elif (i == 6):
				qubits.append(qubit(i, 'd_1', 'd_1'))
			elif (i == 9):
				qubits.append(qubit(i, 'd_2', 'd_2'))
			else:
				qubits.append(qubit(i, '0', '-'))
			self.add(qubits[i].get())
		equation = Tex(r"x_1x_0 * c = d_2d_1d_0").shift(UP*3)
		self.play(Write(equation))
	




		#toffoli
		

		def toffoli(pos,up, mid, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot11 = Dot(np.array([cx,-offset*mid+ base,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot11, cnot2, cnot3)
			return cnot
		t1 = toffoli(-4, 0, 1, 3)
		t2 = toffoli(-3, 0, 2, 7)
		self.play(FadeIn(t1), FadeIn(t2))


		#adder 1
		fadder1 = Square(color=RED, fill_color=RED, fill_opacity=1).scale(1.2)
		fadder2 = Text("QFA").set_color(BLACK)
		fin1 = Tex("0").shift(UP*0.9 + LEFT*1)
		fin2 = Tex("1").shift(UP*0.3 + LEFT*1)
		fin3 = Tex("2").shift(DOWN*0.3 + LEFT*1)
		fin4 = Tex("3").shift(DOWN*0.9 + LEFT*1)
		fadder = Group(fadder1, fadder2, fin1, fin2, fin3, fin4).shift(DOWN*0.5 + LEFT*1)
		self.play(FadeIn(fadder))

		#adder 2
		fadder11 = Rectangle(color=RED, fill_color=RED, fill_opacity=1).rotate(PI/2).scale(1)
		fadder21 = Text("QFA").set_color(BLACK)
		fin11 = Tex("0").shift(DOWN*0.9 + UP*0.25 + LEFT*0.8)
		fin21 = Tex("1").shift(DOWN*1.5 + UP*0.25 + LEFT*0.8)
		fin31 = Tex("2").shift(DOWN*0.3 + UP*0.25 + LEFT*0.8)
		fin41 = Tex("3").shift(DOWN*2.1 + UP*0.25 + LEFT*0.8)
		fadderq = Group(fadder11, fadder21, fin11, fin21, fin31, fin41).shift(DOWN*1.35 + RIGHT*2)
		self.play(FadeIn(fadderq))


		


		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		self.wait(5)
		while(x < -4):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < -3):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[7].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -1):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		while(x < 2):
			x += 0.025
			self.wait(0.001)
		qubits[6].dq = r"\ket{1}"
		qubits[8].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.025
			self.wait(0.001)
		self.wait(2)

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"

		qubits[6].dq = r"\ket{0}"
		qubits[7].dq = r"\ket{0}"
		qubits[8].dq = r"\ket{0}"
		self.wait(5)
		while(x < -4):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -3):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[7].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -1):
			x += 0.025
			self.wait(0.001)
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 2):
			x += 0.025
			self.wait(0.001)
		qubits[6].dq = r"\ket{1}"
		qubits[8].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.025
			self.wait(0.001)
		self.wait(2)

		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		for i in range(3, 10):
			qubits[i].dq = r"\ket{0}"
		self.wait(6)
		while(x < -4):
			x += 0.05
			self.wait(0.001)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
		while(x < -1):
			x += 0.05
			self.wait(0.001)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(6)







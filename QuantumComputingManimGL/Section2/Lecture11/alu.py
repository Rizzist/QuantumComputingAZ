from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum ALU").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class alu(Scene):
	def construct(self):
		text = Text("Quantum ALU").scale(1.3)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))	

		title = Text("Quantum ALU").shift(UP*3.5)
		self.play(FadeIn(title))


		alu1 = Rectangle(fill_opacity=1, fill_color=YELLOW, width=7, height=6).set_color(YELLOW)
		alu2 = Text("ALU").set_color(BLACK)
		alui1 = Text("Op Code").shift(LEFT * 2 + UP*2).set_color(GREY)
		alui2 = Text("A").shift(LEFT * 3 + UP*0).set_color(GREY)
		alui3 = Text("B").shift(LEFT * 3 + DOWN*2).set_color(GREY)
		alui4 = Text("Result").shift(RIGHT * 2.5 + UP*0).set_color(GREY)

		alu = Group(alu1, alu2, alui1, alui2, alui3, alui4)
		self.play(FadeIn(alu))

		def operate(a, b, op, result):
			a1 = Tex(a).shift(LEFT*4.5).set_color(RED)
			b1 = Tex(b).shift(LEFT*4.5 + DOWN*2).set_color(RED)
			op1 = Tex(op).shift(LEFT*4.5 + UP*2).set_color(RED)
			result1 = Tex(result).shift(RIGHT*4.5).set_color(RED)
			return Group(a1, b1, op1, result1)


		op1 = operate(r'A', r'B', r'+', r'A+B')
		self.play(FadeIn(op1))
		self.wait(0.5)

		op2 = operate(r'A', r'B', r'-', r'A-B')
		self.play(Transform(op1, op2))
		self.wait(0.5)

		op3 = operate(r'A', r'B', r'\vee', r'A \vee B')
		self.play(Transform(op1, op3))
		self.wait(0.5)

		op3 = operate(r'A', r'B', r'\wedge', r'A \wedge B')
		self.play(Transform(op1, op3))
		self.wait(0.5)

		op4 = operate(r'A', r'B', r'\neg', r'\neg B')
		self.play(Transform(op1, op4))
		self.wait(0.5)

		self.wait(2)
		self.play(FadeOut(op1), FadeOut(alu))

		isgreater2 = Tex(r"\begin{tabular}{||c c c c c||} \hline S0 & S1 & S2 & S3 & ALU Op \\ [0.5ex] \hline\hline 1 & 1 & 0 & 0 & A+B\\ \hline 1 & 0 & 0 & 0 & A xor B\\ \hline 0 & 0 & 0 & 0 & B\\ \hline 1 & 0 & 1 & 0 & A xnor B\\ \hline 0 & 0 & 1 & 0 & negB\\  [1ex]  \hline \end{tabular}")
		isgreater2.shift(DOWN*0.5)
		self.play(FadeIn(isgreater2))
		self.wait(7)
		self.play(FadeOut(isgreater2))




















		#make a 
		base = 2.5
		offset = 0.8
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
		for i in range(0, 7):
			if (i == 0):
				qubits.append(qubit(i, 'S_0', 'S_0'))
			elif (i == 1):
				qubits.append(qubit(i, 'S_0', 'S_0'))
			elif (i == 2):
				qubits.append(qubit(i, 'S_0', 'S_0'))
			elif (i == 3):
				qubits.append(qubit(i, 'S_0', 'S_0'))
			elif (i == 4):
				qubits.append(qubit(i, 'S_0', 'S_0'))
			elif (i == 5):
				qubits.append(qubit(i, 'A', 'A'))
			elif (i == 6):
				qubits.append(qubit(i, 'B', 'Result'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())

		def vgate(pos, up, down):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"V").scale(0.9).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.2).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot4, vnot3, vnot1, vnot2)
			return vnot
		def vngate(pos, up, down):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"V^\dag").scale(0.9).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.2).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot4, vnot3, vnot1, vnot2)
			return vnot
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot

		#add gates
		v1 = vgate(-3, 0, 6)
		v2 = vgate(-2.5, 5, 6)
		c1 = cxgate(-2, 0, 5)
		v3 = vngate(-1.5, 5, 6)
		c2 = cxgate(-1, 0, 5)
		v4 = vgate(-0.5, 1, 6)
		v5 = vgate(0, 3, 6)
		c3 = cxgate(0.5, 1, 3)
		v6 = vngate(1, 3, 6)
		c4 = cxgate(1.5, 1, 3)
		c5 = cxgate(2, 2, 6)
		c6 = cxgate(2.5, 4, 6)

		gates = Group(v1, v2, v3, v4, v5, v6, c1, c2, c3, c4, c5, c6)
		self.add(gates)

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{0}"
		self.wait(5)

		while(x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{+i}"
		self.wait(0.5)

		while(x < -2.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -0.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{-i}"
		self.wait(0.5)


		while(x < 0.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{-i}"
		self.wait(0.5)

		while(x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < 1.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{1}"
		qubits[6].dq = r"\ket{1}"
		self.wait(0.5)

		self.wait(8)



































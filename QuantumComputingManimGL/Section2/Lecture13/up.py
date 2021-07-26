from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Barrel Shifter, Rotator").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class up(Scene):
	def construct(self):
		text = Text("Quantum Increment, Decrement").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))




		title = Text("Quantum Increment").shift(UP*3.5)
		self.play(FadeIn(title))

		#show qubits
		#make a 
		base = 2
		offset = 0.75
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
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, '0', ''))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"

		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def ccxgate(pos,up, up2, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot4 = Dot(np.array([cx,base-offset*up2,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot4, cnot2, cnot3)
			return cnot
		def cccxgate(pos,up, up2, up3, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot4 = Dot(np.array([cx,base-offset*up2,0]), fill_color=RED)
			cnot5 = Dot(np.array([cx,base-offset*up3,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot4, cnot5, cnot2, cnot3)
			return cnot
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"H").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def xgate(pos,down, on):
			hx = pos
			h2 = Tex(r"X").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=GREEN, fill_opacity=on, color=GREEN).scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def zgate(pos,down, on):
			hx = pos
			h2 = Tex(r"Z").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=RED, fill_opacity=on, color=RED).scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.5)
			measure2 = Text('M').set_color(BLACK)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def identity(pos, down):
			measure1 = Square(fill_color=WHITE, fill_opacity=1, color=WHITE).scale(0.5)
			measure2 = Text('I').set_color(BLACK)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure


		gates = []
		gates.append( xgate(3, 3, 1) )
		gates.append( cxgate(1, 3, 2) )
		gates.append( ccxgate(-1, 3, 2, 1) )
		gates.append( cccxgate(-3, 3, 2, 1, 0) )
		self.play(FadeIn(Group(*gates)))

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(5)
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(1)

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		while(x < -1):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 1):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(1)


		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(1)




		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		while(x < 1):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(1)



		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(1)





		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		while(x < -3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -1):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 1):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 3):
			x += 0.1
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)
		while(x<5):
			x += 0.1
			self.wait(0.001)
		self.wait(5)
		self.play(FadeOut(Group(*gates)))








		title2 = Text("Quantum Decrement").shift(UP*3.5)
		self.play(Transform(title, title2))

		gates = []
		gates.append( xgate(-3, 3, 1) )
		gates.append( cxgate(-1, 3, 2) )
		gates.append( ccxgate(1, 3, 2, 1) )
		gates.append( cccxgate(3, 3, 2, 1, 0) )
		self.play(FadeIn(Group(*gates)))
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{0}"
		self.wait(4)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x<5):
			x += 0.05
			self.wait(0.001)
		self.wait(10)


















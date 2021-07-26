from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Support Vector Machine (QSVM)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class qsvm(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Support Vector Machine (QSVM)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Quantum Support Vector Machine (QSVM)").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Quantum Feature Map}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{Map Higher Dimension to Classify Using Kernel } \mathbb{K}").shift(UP*1.8) )
		stuff.append( Tex(r"\text{Training Data: } \{ \vec{x}_j: j = 1, 2, ..., M\}").shift(UP*1.0) )
		stuff.append( Tex(r"\begin{bmatrix} 0 & \vec{1}^T \\ \vec{1} & \mathbb{K} + \gamma^{-1}\mathbb{I} \end{bmatrix} \begin{bmatrix} b \\ \vec{a} \end{bmatrix} = \begin{bmatrix} 0 \\ \vec{x} \end{bmatrix}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{1. Train/Calculate Kernel: }K_{ij} = \vec{x}_i \cdot \vec{x}_j \to \text{Quantum Inner Product Algorithm}").shift(DOWN*1.8).scale(0.8) )
		stuff.append( Tex(r"\text{2. Solve using HHL for } \ket{b, \vec{a}} ").shift(DOWN*2.5) )
		stuff.append( Tex(r"\text{3. Predict } \vec{x} \text{ using training results, classify w/ output: } \ket{b_o, \vec{a}_o} ").shift(DOWN*3.3) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))
		












		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Use Quantum Only for Kernel, Quantum Function}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{Best Quantum Method for Big Data!}").shift(UP*1.7) )
		stuff.append( Tex(r"\text{1. Quantum Embedding(Angle, Basis, Amplitude) }").shift(UP*0.5) )
		stuff.append( Tex(r"\text{2. Calculate Kernel w/ Circuit} \ket{b, \vec{a}} ").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{3. Train Machine Learning Model with Quantum Function Output ").shift(DOWN*1.5).scale(0.9) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(7)
		self.play(FadeOut(Group(*stuff)))


		







		title2 = Text("Quantum Inner Product Circuit").shift(UP*3.5)
		self.play(Transform(title, title2))

		#make a 
		base = 2
		offset = 0.6
		x = -5
		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
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
			qubits.append(qubit(i, str(i), ''))
			self.add(qubits[i].get())
		
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def xgate(pos,down, on=1):
			hx = pos
			h2 = Tex(r"X").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=GREEN, fill_opacity=on, color=GREEN).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"H").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.2)
			measure2 = Text('M').set_color(BLACK).scale(0.6)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def gCGate(pos, up, down, control, color):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"" + control).scale(1.1).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=color, fill_opacity=1, color=color).scale(0.325).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot3, vnot4, vnot1, vnot2)
			return vnot
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gGate(pos, depth, down, name):
			qft1 = Rectangle(width=2.5, height=offset*down*depth + 0.5, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
			qft2 = Tex(str(name)).scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gCGateN(pos, up, down, control, color, depth):
			qft1 = Rectangle(width=0.5, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gates = []
		gates.append( gGate(-2, 2, 1.5, r'S(x_1)') )
		gates.append( gGate(2, 2, 1.5, r'S(x_2)^\dag') )
		self.play(FadeIn(Group(*gates)))


		gatesm = []
		for i in range(0, 4):
			gatesm.append( measure(5, i) )
		self.play(FadeIn(Group(*gatesm)))
		waiter(5)
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		waiter(5)


		frame = self.camera.frame
		frame.generate_target()
		self.play(MoveToTarget(frame, run_time=2.0))
		steps = []
		steps.append(  Tex(r"\mathbb{M} = \ket{0_n}\bra{0_n}").shift(DOWN*1)  )
		steps.append(  Tex(r"\bra{0_n}\ \ S(x_2)\ \  S(x_1)^\dag\ \  \mathbb{M}\ \  S(x_2)^\dag \ \ S(x_1) \ \ \ket{0_n}").shift(DOWN*2)  )
		
		steps.append(  Tex(r"\bigg(\bra{0_n}S(x_2) S(x_1)^\dag \ket{0_n}\bigg) \bigg(\bra{0_n} S(x_2)^\dag S(x_1)\ket{0_n}\bigg)").shift(DOWN*3)  )
		steps.append(  Tex(r"\vert \bra{0_n}S(x_2)^\dag S(x_1)\ket{0_n} \vert^2").shift(DOWN*4)  )
		steps.append(  Tex(r"\vert \bra{x_2}\ket{x_1} \vert^2 \to \text{Quantum Inner Product}").shift(DOWN*5)  )
		#
		
		for i in steps:
			frame.target.shift(DOWN*0.5)
			self.play(MoveToTarget(frame, run_time=2.0))
			self.play(FadeIn(i))
			waiter(10)
		
		waiter(10)







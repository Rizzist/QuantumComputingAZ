from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Superdense Coding").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class super(Scene):
	def construct(self):
		text = Text("Quantum Communication: Superdense Coding").scale(0.9)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("Superdense Coding").shift(UP*3.5)
		self.play(FadeIn(title))

		concept = Text("Sending Information using Entangled Qubits").shift(UP*2).scale(0.7)
		self.play(Write(concept))
		#show it
		psi = Tex(r"\ket{\psi}")
		psic = Circle(color=YELLOW)
		psG = Group(psi, psic)
		psG.shift(DOWN*2 + LEFT*1)
		self.play(FadeIn(psG))

		phi = Tex(r"\ket{\phi}")
		phic = Circle(color=YELLOW)
		phG = Group(phi, phic)
		phG.shift(DOWN*2 + RIGHT*1)
		self.play(FadeIn(phG))

		psG.generate_target()
		psG.target.shift(LEFT*3)
		phG.generate_target()
		phG.target.shift(RIGHT*3)
		self.play(MoveToTarget(psG), MoveToTarget(phG))

		psi.generate_target()
		psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)

		phi.generate_target()
		phi.target = Tex(r"\ket{?}").shift(DOWN*2 + RIGHT*4)

		self.play(MoveToTarget(psi), MoveToTarget(phi))
		self.wait(1)

		psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)
		phi.target = Tex(r"\ket{0}").shift(DOWN*2 + RIGHT*4)
		self.play(MoveToTarget(psi), MoveToTarget(phi))

		psi.target = Tex(r"\ket{1}").shift(DOWN*2 + LEFT*4)
		phi.target = Tex(r"\ket{1}").shift(DOWN*2 + RIGHT*4)
		self.play(MoveToTarget(psi), MoveToTarget(phi))

		for i in range(0, 2):
			psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)
			phi.target = Tex(r"\ket{0}").shift(DOWN*2 + RIGHT*4)
			self.play(MoveToTarget(psi), MoveToTarget(phi))

			psi.target = Tex(r"\ket{1}").shift(DOWN*2 + LEFT*4)
			phi.target = Tex(r"\ket{1}").shift(DOWN*2 + RIGHT*4)
			self.play(MoveToTarget(psi), MoveToTarget(phi))
		self.wait(1)

		objs = Group(psG, phG, concept)
		self.play(FadeOut(objs))

		steps = []
		steps.append( Text("Step 1: Entangle Qubits").shift(UP*2).scale(0.7) )
		steps.append( Text("Step 2: Give Qubits to 2 different people (Alice and Bob)").shift(UP*1).scale(0.7) )
		steps.append( Text("Step 3: Alice encode first Qubit with 2 bits of Info").shift(UP*0).scale(0.7) )
		steps.append( Text("Step 4: Alice sends Bob her Qubit").shift(DOWN*1).scale(0.7) )
		steps.append( Text("Step 5: Bob desentagles Qubits and gets information").shift(DOWN*2).scale(0.7) )
		for i in range(0, len(steps)):
			self.play(FadeIn(steps[i]))
			self.wait(6)
		self.play(FadeOut(Group(*steps)))

		#why it works
		table = Tex(r"\begin{tabular}{||c c||} \hline Qubit & State\\ [0.5ex] \hline\hline \begin{math}B_0\end{math} & \begin{math}\frac{(\ket{00} + \ket{11})}{(\sqrt{2})}\end{math} \\ \hline \begin{math}B_1\end{math} & \begin{math}\frac{(\ket{01} + \ket{10})}{(\sqrt{2})}\end{math} \\ \hline \begin{math}B_2\end{math} & \begin{math}\frac{(\ket{00} - \ket{11})}{(\sqrt{2})}\end{math} \\ \hline \begin{math}B_3\end{math} & \begin{math}\frac{(\ket{01} - \ket{10})}{(\sqrt{2})}\end{math} \\  [1ex]  \hline \end{tabular}").shift(DOWN*0.5)
		self.play(FadeIn(table))
		self.wait(8)
		self.play(FadeOut(table))

		toencode = Text('Encode: 10').shift(UP*3).scale(0.7)
		self.play(FadeIn(toencode))
		#show qubits
		#make a 
		base = 1.5
		offset = 1.5
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.45, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				self.q = Tex(r"").shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([5, -offset*self.n + base, 0]))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*5.75).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)
			def shift(dir):
				pass

		
		qubits = []
		for i in range(0, 2):
			if (i == 0):
				qubits.append(qubit(i, 'x', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'y', ''))
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


		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
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
		gates.append( cxgate(12, 0, 1) )
		gates.append( hadamard(10, 0) )

		gates.append( xgate(33, 0, 0) )
		gates.append( zgate(36, 0, 1) )
		gates.append( identity(36, 3) )

		gates.append( cxgate(57, 2, 3) )
		gates.append( hadamard(59, 2) )
		gates.append( identity(59, 3) )

		gates.append( measure(82, 2) )
		gates.append( measure(82, 3) )

		self.add(*gates)

		for i in range(0, len(gates)):
			gates[i].generate_target()

		def moveGates(n, m):
			for i in range(0, 10):
				gates[i].target.shift(LEFT*n)
			self.play(MoveToTarget(gates[0], rate_func=linear, run_time=m), MoveToTarget(gates[1], rate_func=linear, run_time=m), MoveToTarget(gates[2], rate_func=linear, run_time=m), MoveToTarget(gates[3], rate_func=linear, run_time=m), MoveToTarget(gates[4], rate_func=linear, run_time=m), MoveToTarget(gates[5], rate_func=linear, run_time=m), MoveToTarget(gates[6], rate_func=linear, run_time=m), MoveToTarget(gates[7], rate_func=linear, run_time=m), MoveToTarget(gates[8], rate_func=linear, run_time=m), MoveToTarget(gates[9], rate_func=linear, run_time=m))
		
		qubits[0].dq = r"-"
		qubits[1].dq = r"-"

		moveGates(23, 10)

		state = Tex(r"B_0 = \frac{1}{\sqrt{(2})}(\ket{00} + \ket{11}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}").shift(DOWN*0.5)
		self.play(FadeIn(state))

		c = qubits[1].get()
		c.generate_target()
		c.target.shift(DOWN*offset*2)
		self.play(MoveToTarget(c))

		moveGates(18, 10)

		state2 = Tex(r"B_2 = \frac{1}{\sqrt{(2})} (\ket{00} - \ket{11}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 1 \\ 0 \\ 0 \\ -1 \end{bmatrix}").shift(DOWN*0.5)
		self.play(Transform(state, state2))
		self.wait(3)

		moveGates(7, 10)

		d = qubits[0].get()
		d.generate_target()
		d.target.shift(DOWN*offset*2)
		self.play(MoveToTarget(d))

		moveGates(14, 10)

		state3 = Tex(r"State = \frac{1}{\sqrt{(2})} (\ket{00} - \ket{10}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 1 \\ 0 \\ -1 \\ 0 \end{bmatrix}").shift(DOWN*0.5)
		self.play(Transform(state, state3))
		self.wait(3)
		moveGates(2, 3)
		hadi = Tex(r"H \otimes I = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -1  \end{bmatrix}").shift(UP*1.5 + LEFT*3)
		self.play(FadeIn(hadi))
		self.wait(6)

		state3 = Tex(r"State = \ket{10} = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}").shift(UP*1.5 + RIGHT*3)
		self.play(Transform(state, state3))
		self.wait(3)
		self.play(FadeOut(hadi))

		moveGates(8, 2)
		moveGates(15, 3)
		state4 = Text(r"Measured: 10").shift(UP*1.5)
		self.play(Transform(state, state4))
		self.wait(5)
		moveGates(15, 1)
		self.play(FadeOut(state))
		c.target.shift(UP*offset*2)
		self.play(MoveToTarget(c))
		d.target.shift(UP*offset*2)
		self.play(MoveToTarget(d))














		#try 01
		toencode2 = Text('Encode: 01').shift(UP*3).scale(0.7)
		self.play(Transform(toencode, toencode2))
		gates = []
		gates.append( cxgate(12, 0, 1) )
		gates.append( hadamard(10, 0) )

		gates.append( xgate(33, 0, 1) )
		gates.append( zgate(36, 0, 0) )
		gates.append( identity(33, 3) )

		gates.append( cxgate(57, 2, 3) )
		gates.append( hadamard(59, 2) )
		gates.append( identity(59, 3) )

		gates.append( measure(82, 2) )
		gates.append( measure(82, 3) )

		self.add(*gates)

		for i in range(0, len(gates)):
			gates[i].generate_target()

		qubits[0].dq = r"-"
		qubits[1].dq = r"-"

		moveGates(23, 10)

		state = Tex(r"B_0 = \frac{1}{\sqrt{(2})}(\ket{00} + \ket{11}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}").shift(DOWN*0.5)
		self.play(FadeIn(state))

		c = qubits[1].get()
		c.generate_target()
		c.target.shift(DOWN*offset*2)
		self.play(MoveToTarget(c))

		moveGates(15, 10)

		state2 = Tex(r"B_1 = \frac{1}{\sqrt{(2})} (\ket{01} + \ket{10}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 0 \\ 1 \\ 1 \\ 0 \end{bmatrix}").shift(DOWN*0.5)
		self.play(Transform(state, state2))
		self.wait(3)

		moveGates(10, 10)

		d = qubits[0].get()
		d.generate_target()
		d.target.shift(DOWN*offset*2)
		self.play(MoveToTarget(d))

		moveGates(14, 10)

		state3 = Tex(r"State = \frac{1}{\sqrt{(2})} (\ket{01} + \ket{11}) = \frac{1}{\sqrt{(2})} \begin{bmatrix} 0 \\ 1 \\ 0 \\ 1 \end{bmatrix}").shift(DOWN*0.5)
		self.play(Transform(state, state3))
		self.wait(3)
		moveGates(2, 3)
		hadi = Tex(r"H \otimes I = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -1  \end{bmatrix}").shift(UP*1.5 + LEFT*3)
		self.play(FadeIn(hadi))
		self.wait(6)

		state3 = Tex(r"State = \ket{01} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}").shift(UP*1.5 + RIGHT*3)
		self.play(Transform(state, state3))
		self.wait(3)
		self.play(FadeOut(hadi))

		moveGates(8, 2)
		moveGates(15, 3)
		state4 = Text(r"Measured: 01").shift(UP*1.5)
		self.play(Transform(state, state4))
		moveGates(15, 1)
		self.wait(25)
		










from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Teleportation").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class teleport(Scene):
	def construct(self):
		text = Text("Quantum Teleportation").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text('Quantum "Teleportation"').shift(UP*3.5)
		self.play(FadeIn(title))
		
		concept = Text("Sending Information for Qubit Reconstruction using Classical Bits").shift(UP*2).scale(0.6)
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
		steps.append( Text("Step 3: Alice entangles first Qubit with Her PERSONAL Qubit").shift(UP*0).scale(0.7) )
		steps.append( Text("Step 4: Alice measures both qubits and sends bits to Bob").shift(DOWN*1).scale(0.7) )
		steps.append( Text("Step 5: Bob applies X or Z depending on Info, Reconstructs Alices PERSONAL Qubit").shift(DOWN*2).scale(0.525) )
		for i in range(0, len(steps)):
			self.play(FadeIn(steps[i]))
			self.wait(6)
		self.play(FadeOut(Group(*steps)))










	
		toencode = Tex(r'Encode: a\ket{0} + b\ket{1}').shift(UP*2.75)
		self.play(FadeIn(toencode))
		#show qubits
		#make a 
		base = 2
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
		for i in range(0, 3):
			if (i == 0):
				qubits.append(qubit(i, r'\psi', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'x', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'y', ''))
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
		gates.append( cxgate(12, 1, 2) )
		gates.append( hadamard(10, 1) )

		#gates.append( xgate(33, 0, 0) )
		#gates.append( zgate(36, 0, 1) )
		gates.append( cxgate(33, 0, 1) )
		gates.append( identity(33, 3) )
		gates.append( identity(36, 3) )
		gates.append( identity(36, 1) )
		gates.append( hadamard(36, 0) )

		gates.append( measure(59, 0) )
		gates.append( measure(59, 1) )

		gates.append( xgate(59+23, 3, 0) )
		gates.append( zgate(59+23+3, 3, 1) )

		self.add(*gates)

		for i in range(0, len(gates)):
			gates[i].generate_target()

		def moveGates(n, m):
			for i in range(0, len(gates)):
				gates[i].target.shift(LEFT*n)
			self.play(MoveToTarget(gates[0], rate_func=linear, run_time=m), MoveToTarget(gates[1], rate_func=linear, run_time=m), MoveToTarget(gates[2], rate_func=linear, run_time=m), MoveToTarget(gates[3], rate_func=linear, run_time=m), MoveToTarget(gates[4], rate_func=linear, run_time=m), MoveToTarget(gates[5], rate_func=linear, run_time=m), MoveToTarget(gates[6], rate_func=linear, run_time=m), MoveToTarget(gates[7], rate_func=linear, run_time=m), MoveToTarget(gates[8], rate_func=linear, run_time=m), MoveToTarget(gates[9], rate_func=linear, run_time=m), MoveToTarget(gates[10], rate_func=linear, run_time=m))
		
		qubits[0].dq = r"-"
		qubits[1].dq = r"-"

		moveGates(23, 10)

		c = qubits[2].get()
		c.generate_target()
		c.target.shift(DOWN*offset*1)
		self.play(MoveToTarget(c))

		moveGates(18, 10)
		self.wait(2)
		moveGates(23, 10)
		self.wait(2)
		#show measures
		toencode2 = Tex(r'Encode: a\ket{0} + b\ket{1} \to 10').shift(UP*2.75)
		self.play(Transform(toencode, toencode2))

		moveGates(50, 10)
		self.wait(30)



















from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Hamiltonian Simulation").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class hamiltonian(Scene):
	def construct(self):
		text = Text("Hamiltonian Simulation").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Hamiltonian Simulation").shift(UP*3.5)
		self.play(FadeIn(title))

		discuss = []
		discuss.append( Text("Original Incentive for Quantum Computer - Richard Feynman").shift(UP*3).scale(0.5) )
		discuss.append( Text("H - operator/matrix that encodes energy of a system").shift(UP*2.5).scale(0.5) )
		discuss.append( Tex(r"\text{Create Unitary Matrix } U \mid U = e^{-iHt} \text{ - Time Evolution Operator}").shift(UP*2).scale(0.7) )
		discuss.append( Text("Solution to Shrondinger Equation - Simulate Quantum Mechanics!").shift(UP*1.5).scale(0.5) )
		discuss.append( Text("How to calculate? - H must be hermitian").shift(UP*1).scale(0.7) )
		discuss.append( Tex(r"\begin{bmatrix} 0 & H \\ H^\dagger & 0 \end{bmatrix}").shift(UP*0).scale(1) )
		discuss.append( Tex(r"Taylor Series: e^{-iHt} = \mathbb{I} - iHt - (Ht)^2/2 \cdots").shift(DOWN*1) )
		discuss.append( Text("- Trotter-Suzuki Algorithm").shift(DOWN*1.75 + RIGHT*2).scale(0.7) )
		discuss.append( Text("- Qubitization").shift(DOWN*2.25 + RIGHT*0.78).scale(0.7) )
		discuss.append( Text("- Density Matrix Exponentiation").shift(DOWN*2.8 + RIGHT*2.65).scale(0.7) )
		for i in discuss:
			self.play(FadeIn(i))
			self.wait(10)
		self.play(FadeOut(Group(*discuss)))

		title2 = Text("Trotter-Suzuki Algorithm").shift(UP*3.5)
		self.play(Transform(title, title2))
		methods = []
		methods.append( Tex(r"H = \sum_{i=0}^n a_iH_i").shift(UP*2.5 + LEFT*3) )
		methods.append( Tex(r"e^{-iHt} = \prod_{j=0}^n e^{-ia_jH_jt}").shift(UP*2.5 + RIGHT*3) )
		methods.append( Text("Matrix must be sparse! ie: Lots of zeros").shift(UP*1.5).scale(0.5) )
		methods.append( Tex(r"Example: H_j = X \otimes X").shift(UP*1) )
		methods.append( Tex(r"\text{1. Diagonalize: } H_j = PD_jP^{-1} \to D_j = Z \otimes Z \to H^{\otimes 2}(Z \otimes Z)H^{\otimes 2}").shift(UP*0).scale(0.9) )
		methods.append( Tex(r"\text{2. Eigenvalues (QPE): } D_j\ket{kj} = (-1)^{k+j}\ket{kj}").shift(DOWN*1) )
		methods.append( Tex(r"\text{3. Calculate Gates: } e^{-i(-1)^{k+j}Zt}\ket{kj} \to e^{-iHt} = Pe^{-iDt}P^{-1}").shift(DOWN*2) )
		methods.append( Tex(r"\text{4. Implement Circuit }").shift(DOWN*3) )
		for i in methods:
			self.play(FadeIn(i))
			self.wait(18)

		self.play(FadeOut(Group(*methods)))












		#make a 
		base = 0.5
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
		for i in range(0, 2):
			if (i == 0):
				qubits.append(qubit(i, '1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'C', ''))
			elif (i == 3):
				qubits.append(qubit(i, r'\psi', ''))
			else:
				qubits.append(qubit(i, r'\psi', ''))
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
		def gCGate(pos, up, down, control, color, depth=1):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"" + control).scale(1.1).shift(DOWN*offset*down + RIGHT*vx + UP*base + DOWN*offset*(depth-1)/2).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			longitude = []
			for i in range(0, depth):
				longitude.append( Square(fill_color=color, fill_opacity=1, color=color).scale(0.325).shift(DOWN*offset*down + RIGHT*vx + UP*base + DOWN*offset*i)  )
			vnot = Group(vnot3, *longitude, vnot1, vnot2)
			return vnot
		def gGate(pos,down, name):
			hx = pos
			h2 = Tex(r"" + name).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=5, height=2.5, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		
		for i in range(0, 2):
			gates.append( hadamard(-2.5, i) )
		gates.append( cxgate(-1.5, 0, 1) )

		gates.append( gGate(0, 1, r'R_z(t)') )

		gates.append( cxgate(1.5, 0, 1) )
		for i in range(0, 2):
			gates.append( hadamard(2.5, i) )
		self.play(FadeIn(Group(*gates)))


		x = -5
		qubits[0].dq = r"\ket{\psi}"
		qubits[1].dq = r"\ket{\phi}"
		self.wait(25)







		
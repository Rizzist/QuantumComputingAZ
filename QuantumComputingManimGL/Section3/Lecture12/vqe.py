from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Variational Quantum Eigensolver").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class vqe(Scene):
	def construct(self):
		text = Text("Variational Quantum Eigensolver").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Circuit Variation").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
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
		self.wait(10)
		for i in range(0, 2):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates)))



		stuff = []
		stuff.append( Text("1. Circuit Ansatz - H2 Atoms").shift(UP*2) )
		stuff.append( Text("2. Cost-function - Hamiltonian, Minimize Energy").shift(UP*0.5).scale(0.9) )
		stuff.append( Text("3. Training Procedure - Gradient Descent").shift(UP*1*-1).scale(0.9) )


		for i in stuff:
			self.play(FadeIn(i))
			self.wait(8)
		self.wait(10)
		self.play(FadeOut(Group(*stuff)))





		title2 = Text("1. Circuit Ansatz").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2.5) )
		stuff.append( Tex(r"H\ket{\psi} \to H = -\sum_i (\frac{\nabla^2}{2} - \sum \frac{z_i}{R_j-r_i})").shift(UP*2.55) )
		stuff.append( Tex(r"\text{1. Second Quantization: } H = \sum h_{pq}a_pa_q^\dag + \frac{1}{2} \sum h_{pqrs}a_p^\dag a_q^\dag a_ra_s").shift(UP*1.5).scale(0.9)  )
		stuff.append( Tex(r"\text{2. Trotter Decomposition} \to H = \sum h_i \to (h_i^{\frac{1}{r}})^r").shift(UP*0.5) )
		stuff.append( Tex(r"\text{3. Hamiltonian to Pauli Matrices: Jordan-Wigner Transformation} ").shift(DOWN*0.5).scale(0.9) )
		stuff.append( Tex(r"\sigma^+ = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \ \ \ \ \ \sigma^- = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}").shift(DOWN*1.5) )
		stuff.append( Tex(r"\sigma_j^+ = f_j^\dag").shift(DOWN*1.5 + LEFT*4.5) )
		stuff.append( Tex(r"\sigma_j^- = f_j").shift(DOWN*2.25 + LEFT*4.5) )
		stuff.append( Tex(r"\sigma_j^Z = 2*f_j^\dag f_j - 1").shift(DOWN*3 + LEFT*4.5) )
		stuff.append( Tex(r"a_j^\dag a_j = f_j^\dag f_j").shift(DOWN*2.5) )
		stuff.append( Tex(r"a_j = I^{j-1} \otimes \sigma^+ \otimes Z^{N-j-1}").shift(DOWN*3.25 + RIGHT*1) )
		for i in stuff:
			self.play(FadeIn(i))
			self.wait(10)
		self.wait(10)
		self.play(FadeOut(Group(*stuff)))


		#stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2.5) )
		#stuff.append( Tex(r"").shift(UP*2.5) )
		title3 = Text("2. Cost Function - Hamiltonian").shift(UP*3.5)
		self.play(Transform(title, title3))
		objit = Tex(r"\text{4. Implement Hamiltonian: } e^{Z_0Z_1Z_2Z_3}").shift(UP*2.5)
		self.play(FadeIn(objit))


		qubits = []
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, '1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2', ''))
			elif (i == 2):
				qubits.append(qubit(i, '3', ''))
			elif (i == 3):
				qubits.append(qubit(i, '4', ''))
			else:
				qubits.append(qubit(i, r'\psi', ''))
			self.add(qubits[i].get())
		gates = []
		#for i in range(0, 4):
		#	gates.append( hadamard(-2.5, i) )
		gates.append( cxgate(-3, 0, 1) )
		gates.append( cxgate(-2.25, 1, 2) )
		gates.append( cxgate(-1.5, 2, 3) )
		gates.append( gGate(0, 3, r'R_z(t)') )
		gates.append( cxgate(1.5, 2, 3) )
		gates.append( cxgate(2.25, 1, 2) )
		gates.append( cxgate(3, 0, 1) )
		#for i in range(0, 2):
		#	gates.append( hadamard(2.5, i) )
		self.play(FadeIn(Group(*gates)))


		self.wait(20)

		objit2 = Tex(r"\text{4. Implement Hamiltonian: } e^{X_0X_1X_2X_3}").shift(UP*2.5)
		self.play(Transform(objit, objit2))
		self.remove(Group(*gates))
		for i in range(0, 4):
			gates.append( hadamard(-4, i) )
			gates.append( hadamard(4, i) )
		self.play(FadeIn(Group(*gates)))

		self.wait(10)


		objit3 = Tex(r"\text{4. Implement Hamiltonian: } e^{Z_0X_1Z_2X_3}").shift(UP*2.5)
		self.play(Transform(objit, objit3))
		self.remove(Group(*gates))
		gates = []
		gates.append( hadamard(-4, 1) )
		gates.append( hadamard(-4, 3) )

		gates.append( cxgate(-3, 0, 1) )
		gates.append( cxgate(-2.25, 1, 2) )
		gates.append( cxgate(-1.5, 2, 3) )
		gates.append( gGate(0, 3, r'R_z(t)') )
		gates.append( cxgate(1.5, 2, 3) )
		gates.append( cxgate(2.25, 1, 2) )
		gates.append( cxgate(3, 0, 1) )

		gates.append( hadamard(4, 1) )
		gates.append( hadamard(4, 3) )
		self.play(FadeIn(Group(*gates)))

		self.wait(10)








		objit4 = Tex(r"\text{4. Implement Hamiltonian: } e^{I_0I_1Z_2X_3}").shift(UP*2.5)
		self.play(Transform(objit, objit4))
		self.remove(Group(*gates))
		gates = []
		gates.append( hadamard(-4, 3) )
		gates.append( cxgate(-1.5, 2, 3) )
		gates.append( gGate(0, 3, r'R_z(t)') )
		gates.append( cxgate(1.5, 2, 3) )
		gates.append( hadamard(4, 3) )
		self.play(FadeIn(Group(*gates)))
		self.wait(10)

		for i in range(0, 4):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates)))
		

		optimizer = ImageMobject("./optimized.png").scale(1.5).shift(DOWN*0.5)
		self.play(FadeIn(optimizer))
		self.wait(10)
		self.play(FadeOut(optimizer))
		
		

		
		objit42 = Tex(r"\text{5. Quantum Phase Estimation } \to \text{Get Energy Measurement}").shift(UP*2)
		self.play(FadeIn(objit42))
		
		process = ImageMobject("./trotterwork.png").shift(DOWN*1).scale(0.6)
		self.play(FadeIn(process))
		self.wait(10)
		self.play(FadeOut(process))
		process = ImageMobject("./encodeco.png").shift(DOWN*1)
		self.play(FadeIn(process))
		self.wait(10)

		self.play(FadeOut(Group(process, objit42, objit)))

		
		title3 = Text("3. Training Procedure - Gradient Descent").shift(UP*3.5)
		self.play(Transform(title, title3))
		
		corona = ImageMobject("./descent.png").scale(1.5).shift(DOWN*0.5)
		self.play(FadeIn(corona))



		#self.play(FadeOut(Group(objit, objit42)))

		self.wait(30)
		







from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Physical vs. Logical Qubits & Shor Code").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class shor(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Physical vs. Logical Qubits & Shor Code").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Physical vs. Logical Qubits").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		#stuff.append( Tex(r"") )
		stuff.append( Tex(r"\ket{\psi} = a_0\ket{0} + a_1\ket{1}") )

		for i in stuff:
			self.play(FadeIn(i))
		waiter(2)
		self.remove(stuff[0])
		stuff[0] = Tex(r"\ket{\psi} = a_0\ket{0} - a_1\ket{1}")
		self.add(stuff[0])
		waiter(2)
		self.remove(stuff[0])
		stuff[0] = Tex(r"\ket{\psi} = -a_1\ket{0} + a_0\ket{1}")
		self.add(stuff[0])
		waiter(2)
		self.remove(stuff[0])
		stuff[0] = Tex(r"\ket{\psi} = -a_1\ket{0} - a_0\ket{1}")
		self.add(stuff[0])
		waiter(2)
		self.remove(stuff[0])
		stuff = []
		for i in range(0, 3):
			for j in range(0, 3):
				stuff.append(  Tex(r"\ket{\psi}").shift(RIGHT*j + DOWN*i + UP*1)  )
		stuff.append( SurroundingRectangle(Group(*stuff)) )
		stuff.append( Tex(r"\ket{\psi}_L = ").shift(LEFT*2).scale(2) )
		stuff.append( Text(r"Logical Qubits are Error Resistant").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i, run_time=0.2))
		waiter(10)
		self.play(FadeOut(Group(*stuff)))

		
		title2 = Text("Example: Bit Errors").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"") )
		stuff.append( Tex(r"\ket{0}_L = \ket{000}").shift(UP*2.75) )
		stuff.append( Tex(r"\ket{1}_L = \ket{111}").shift(UP*2) )
		stuff.append( Tex(r"\ket{\psi}_L = a_0\ket{0}_L + a_1\ket{1}_L = a_0\ket{000} + a_1\ket{111}").shift(UP*1) )
		stuff.append( Tex(r"a_0\ket{010} + a_1\ket{101}").shift(UP*0) )
		stuff.append( Tex(r"\sigma_x(2)(a_0\ket{010} + a_1\ket{101}) = a_0\ket{000} + a_1\ket{111}").shift(DOWN*1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))



		#make a 
		base = 2
		offset = 0.5
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1, length=5):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-length, -offset*self.n + base, 0]), np.array([length, -offset*self.n + base, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=BLUE))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*1.5 + LEFT*length).set_color(GREEN).scale(0.7)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*1.5 + RIGHT*length).set_color(GREEN).scale(0.7)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)

		qubits = []
		for i in range(0, 5):
			if (i == 0):
				qubits.append(qubit(i, '1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2', ''))
			elif (i == 2):
				qubits.append(qubit(i, '3', ''))
			else:
				qubits.append(qubit(i, r'Ancilla', 'Error Syndrome', length=4))
			self.add(qubits[i].get())
		
		def ccxgate(pos,up, up2, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot4 = Dot(np.array([cx,base-offset*up2,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot4, cnot2, cnot3)
			return cnot
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
			h3 = Rectangle(width=6.25, height=2.5, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def gGate2(pos,down, name):
			hx = pos
			h2 = Tex(name).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=3, height=14, fill_color=RED, fill_opacity=1, color=RED).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		gates.append( cxgate(-2, 0, 3) )
		gates.append( cxgate(-1, 1, 3) )
		gates.append( cxgate(0, 1, 4) )
		gates.append( cxgate(1, 2, 4) )

		gates.append( measure(4, 3) )
		gates.append( measure(4, 4) )

		gates.append( xgate(5.3, 0, 0) )
		gates.append( xgate(5.3, 1, 1) )
		gates.append( xgate(5.3, 2, 0) )
		x = -4
		qubits[0].dq = r"\ket{x}"
		qubits[1].dq = r"\ket{x}"
		qubits[2].dq = r"\ket{x}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		self.play(FadeIn(Group(*gates)))
		waiter(10)

		stuff = []
		#stuff.append( Tex(r"").shift(UP*2) )
		stuff.append( Tex(r"\ket{10} \to \text{Flip Qubit 1}").shift(DOWN*1) )
		stuff.append( Tex(r"\ket{11} \to \text{Flip Qubit 2}").shift(DOWN*1.8) )
		stuff.append( Tex(r"\ket{01} \to \text{Flip Qubit 3}").shift(DOWN*2.6) )

		for i in stuff:
			self.play(FadeIn(i, run_time=0.2))
		waiter(10)
		
		self.play(FadeOut(Group(*stuff)))
		for i in range(0, 5):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates)))
		

		title2 = Text("Example: Phase Errors").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"") )
		stuff.append( Tex(r"\ket{0}_L = \frac{1}{2} (\ket{000} + \ket{011} + \ket{101} + \ket{110} )").shift(UP*2.75) )
		stuff.append( Tex(r"\ket{1}_L = \frac{1}{2} (\ket{001} + \ket{010} + \ket{100} + \ket{111} )").shift(UP*1.75) )
		stuff.append( Tex(r"\ket{\psi}_L = a_0\ket{0}_L + a_1\ket{1}_L").shift(UP*0.75) )
		stuff.append( Tex(r"\ket{\psi}_{Le} = \frac{1}{2} (\ket{000} - \ket{011} - \ket{101} + \ket{110} ) + \frac{1}{2} (-\ket{001} - \ket{010} + \ket{100} + \ket{111} )").shift(DOWN*0.25).scale(0.8) )
		stuff.append( Tex(r"\sigma_z(3)(\ket{\psi}_{Le}) = \ket{\psi}_{L}").shift(DOWN*1.25) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))



		title2 = Text("Shor Code").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"") )
		
		stuff.append( Tex(r"\text{Encode 1 Qubit into 3 Qubits}").shift(UP*2.75) )
		stuff.append( Tex(r"\text{Encode each of 3 Qubit into 3 Qubits} \to \text{9 Qubits}").shift(UP*2) )
		stuff.append( Tex(r"\ket{\psi}_L = a_0\ket{0}_L + a_1\ket{1}_L").shift(UP*1) )
		stuff.append( Tex(r"\ket{0}_L = \frac{1}{2} (\ket{000000000} + \ket{000111111} + \ket{111000111} + \ket{111111000} )").shift(UP*0) )
		stuff.append( Tex(r"\ket{1}_L = \frac{1}{2} (\ket{111111111} + \ket{000000111} + \ket{000111000} + \ket{111000000} )").shift(DOWN*1.25) )
		stuff.append( Tex(r"\text{Outer Kets} \to \text{Phase Errors}").shift(DOWN*2.25) )
		stuff.append( Tex(r"\text{Inner Kets} \to \text{Bit Errors}").shift(DOWN*3.25) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))



		qubits = []
		for i in range(0, 9):
			if (i == 0):
				qubits.append(qubit(i, r'\ket{\psi}', '', length=6))
			else:
				qubits.append(qubit(i, r'\ket{0}', '', length=6))
			self.add(qubits[i].get())


		gates = []
		gates.append( cxgate(-5, 0, 3) )
		gates.append( cxgate(-4, 0, 6) )
		gates.append( hadamard(-3, 0) )
		gates.append( hadamard(-3, 3) )
		gates.append( hadamard(-3, 6) )
		gates.append( cxgate(-2, 0, 1) )
		gates.append( cxgate(-2, 3, 4) )
		gates.append( cxgate(-2, 6, 7) )
		gates.append( cxgate(-1, 0, 2) )
		gates.append( cxgate(-1, 3, 5) )
		gates.append( cxgate(-1, 6, 8) )
		#error gate
		gates.append( gGate2(0, 4, r'E') )
		#error gate
		gates.append( cxgate(1, 0, 1) )
		gates.append( cxgate(1, 3, 4) )
		gates.append( cxgate(1, 6, 7) )
		gates.append( cxgate(2, 0, 2) )
		gates.append( cxgate(2, 3, 5) )
		gates.append( cxgate(2, 6, 8) )
		gates.append( ccxgate(3, 2, 1, 0) )
		gates.append( ccxgate(3, 5, 4, 3) )
		gates.append( ccxgate(3, 8, 7, 6) )
		gates.append( hadamard(4, 0) )
		gates.append( hadamard(4, 3) )
		gates.append( hadamard(4, 6) )
		gates.append( cxgate(5, 0, 3) )
		gates.append( cxgate(5, 0, 6) )
		gates.append( ccxgate(6, 6, 3, 0) )

		x = -6
		qubits[0].dq = r"\ket{\psi}"
		self.play(FadeIn(Group(*gates)))
		waiter(30)









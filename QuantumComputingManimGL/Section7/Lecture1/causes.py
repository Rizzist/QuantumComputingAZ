from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Causes of Quantum Errors & Quantum Noise(BF, NF, BNF)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class causes(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Causes of Quantum Errors & Quantum Noise(BF, NF, BNF)").scale(0.8)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Causes of Quantum Errors & Quantum Noise(BF, NF, BNF)").shift(UP*3.5).scale(0.8)
		self.play(FadeIn(title))

		stuff = []
		stuff.append( Text("Quantum Noise & Decoherence cause Quantum Error").shift(UP*2.75).scale(0.7) )
		stuff.append( Text("Interaction w/ Environment - Not Fully Isolated").shift(UP*2.2).scale(0.7) )
		stuff.append( Text("Time Until Decoherence - Limit to QC").shift(UP*1.7).scale(0.7) )
		stuff.append( Tex(r"\ket{x} \to \ket{1-x} \quad \text{Bit Flip  } \sigma_x").shift(DOWN*0) )
		stuff.append( Tex(r"\ket{x} \to (-1)^x\ket{x} \quad \text{Noise Flip  } \sigma_z").shift(DOWN*0.75) )
		stuff.append( Tex(r"\ket{x} \to (-1)^x\ket{1-x} \quad \text{Bit-Noise Flip  } \sigma_x \sigma_z").shift(DOWN*1.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))


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
		for i in range(0, 3):
			if (i == 0):
				qubits.append(qubit(i, '1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2', ''))
			elif (i == 2):
				qubits.append(qubit(i, '3', ''))
			elif (i == 3):
				qubits.append(qubit(i, r'\psi', ''))
			else:
				qubits.append(qubit(i, r'\psi', ''))
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
			h3 = Rectangle(width=5, height=5, fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		gates.append( cxgate(-3, 0, 1) )
		gates.append( cxgate(-2, 0, 2) )
		gates.append( gGate2(0, 1, r'E_{bit}') )
		gates.append( cxgate(2, 0, 1) )
		gates.append( cxgate(3, 0, 2) )
		gates.append( ccxgate(4, 2, 1, 0) )
		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		
		self.play(FadeIn(Group(*gates)))

		waiter(5)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
	
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
	
		while(x < -2):
			x += 0.05
			self.wait(0.001)
	
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 3):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 4):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		waiter(5)


		#0 to 1
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		waiter(5)
		while(x < -3):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		while(x < 3):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 4):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		waiter(5)


		for i in range(0, 3):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates)))











		#hadamard basis
		qubits = []
		for i in range(0, 3):
			if (i == 0):
				qubits.append(qubit(i, '1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2', ''))
			elif (i == 2):
				qubits.append(qubit(i, '3', ''))
			elif (i == 3):
				qubits.append(qubit(i, r'\psi', ''))
			else:
				qubits.append(qubit(i, r'\psi', ''))
			self.add(qubits[i].get())


		gates = []
		gates.append( cxgate(-4, 0, 1) )
		gates.append( cxgate(-3, 0, 2) )
		for i in range(3):
			gates.append( hadamard(-2, i) )
		gates.append( gGate2(0, 1, r'E_{phase}') )
		for i in range(3):
			gates.append( hadamard(2, i) )
		gates.append( cxgate(3, 0, 1) )
		gates.append( cxgate(4, 0, 2) )
		gates.append( ccxgate(5, 2, 1, 0) )
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		self.play(FadeIn(Group(*gates)))
		waiter(10)






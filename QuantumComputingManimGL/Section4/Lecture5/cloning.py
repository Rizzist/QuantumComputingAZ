from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Teleportation & Gaussian Cloning").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class cloning(Scene):
	def construct(self):
		text = Text("Quantum Teleportation & Gaussian Cloning")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Quantum Teleportation").shift(UP*3.5)
		self.play(FadeIn(title))

		#make a 
		base = 2
		offset = 0.6
		x = -5
		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1, length=5, radius=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				self.radius=radius
				self.length = length
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([self.length, -offset*self.n + base, 0]))
				def update_qub(self2):
					qubcol = BLUE
					if (self.radius==1):
						qubcol = RED
					elif (self.radius<1):
						qubcol = YELLOW
					elif (self.radius > 2):
						qubcol = WHITE
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=qubcol).scale(self.radius))
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
				qubits.append(qubit(i, 'A', '', length=1, radius=1))
			elif (i == 1):
				qubits.append(qubit(i, '0', '', show=1, length=2))
			elif (i == 2):
				qubits.append(qubit(i, '0', 'A', show=1))
			elif (i == 3):
				qubits.append(qubit(i, '0', '', show=0, length=5))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		qubits[0].dq = r"\ket{\psi}"
		def squeeze(pos,down):
			hx = pos
			h2 = Tex(r"S").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def rotation(pos,down):
			hx = pos
			h2 = Tex(r"R(\theta_"+str(down)+")").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def beamsplitter(pos,down):
			hx = pos
			h2 = Tex(r"BS").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=1, height=1.1,fill_color=WHITE, fill_opacity=1, color=WHITE).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).shift(DOWN*0.375)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.25)
			measure2 = Tex(r'M').set_color(BLACK).scale(0.85)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def cxgate(pos,up, down):
			cx = pos
			hx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			h2 = Tex(r"X").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			h3 = Square(fill_color=RED, fill_opacity=1, color=RED).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			cnot = Group(cnot1, cnot3, h3, h2)
			return cnot
		def czgate(pos,up, down):
			cx = pos
			hx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			h2 = Tex(r"Z").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			h3 = Square(fill_color=GREEN, fill_opacity=1, color=GREEN).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			cnot = Group(cnot1, cnot3, h3, h2)
			return cnot
		def bbeamsplitter(pos,down):
			hx = pos
			h2 = Tex(r"BS").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=1, height=2.1,fill_color=WHITE, fill_opacity=1, color=WHITE).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).shift(DOWN*0.375*2)
			return hadamard


		gates = []
		gates.append( beamsplitter(-4, 1) )
		gates.append( beamsplitter(-2, 0) )
		gates.append( measure(0, 0) )
		gates.append( measure(0, 1) )
		gates.append( cxgate(1, 0, 2) )
		gates.append( czgate(2, 1, 2) )
		self.play(FadeIn(Group(*gates)))


		self.wait(10)
		stuff = Tex(r"\text{Replace Hadamard-CNOT w/ BS:50-50 = Maximally Entangle}").shift(DOWN*1)
		self.play(FadeIn(stuff))
		self.wait(15)
		self.play(FadeOut(Group(*gates, stuff)))
		for i in range(0, 3):
			self.remove(qubits[i].get())




















		title2 = Text("Gaussian Cloning").shift(UP*3.5)
		self.play(Transform(title, title2))
		qubits = []
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, 'A', '', length=5, radius=2))
			elif (i == 1):
				qubits.append(qubit(i, '0', '', show=0, length=1))
			elif (i == 2):
				qubits.append(qubit(i, '0', '', show=0, length=2))
			elif (i == 3):
				qubits.append(qubit(i, '0', '', show=0, length=5))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		
		

		gates = []
		gates.append( beamsplitter(-4, 0) )
		gates.append( beamsplitter(-2, 1) )
		gates.append( cxgate(1, 1, 0) )
		gates.append( czgate(2, 2, 0) )
		gates.append( measure(0, 1) )
		gates.append( measure(0, 2) )
		gates.append( bbeamsplitter(4, 0.25) )
		self.play(FadeIn(Group(*gates)))


		x = -5
		qubits[0].dq = r"\ket{\psi}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(15)
		while(x < -4):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{\psi /\sqrt{2} }"
		qubits[0].radius = 1
		qubits[1].dq = r"\ket{\psi /\sqrt{2}}"
		qubits[1].radius = 1
		qubits[1].show = 1
		self.add(qubits[1].get())
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)

		while(x < -2):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{\psi /\sqrt{2}}"
		qubits[0].radius = 1
		qubits[1].dq = r"\ket{\psi /2}"
		qubits[1].radius = 0.5
		qubits[1].show = 1
		qubits[2].dq = r"\ket{\psi /2}"
		qubits[2].radius = 0.5
		qubits[2].show = 1
		self.add(qubits[2].get())
		qubits[3].dq = r"\ket{0}"
		self.wait(0.5)


		while(x < 0):
			x += 0.025
			self.wait(0.001)
		
		while(x < 1):
			x += 0.025
			self.wait(0.001)
		self.remove(qubits[1].get())
		qubits[1].show = 0
		self.add(qubits[1].get())
		qubits[0].radius = 2
		self.wait(2)
		while(x < 2):
			x += 0.025
			self.wait(0.001)
		self.remove(qubits[2].get())
		qubits[2].show = 0
		self.add(qubits[2].get())
		qubits[0].radius = 4
		self.wait(2)
		while(x < 4):
			x += 0.025
			self.wait(0.001)
		qubits[0].dq = r"\ket{\psi^\prime}"
		qubits[0].radius = 2
		qubits[0].show = 1
		qubits[3].dq = r"\ket{\psi^\prime}"
		qubits[3].radius = 2
		qubits[3].show = 1
		self.add(qubits[3].get())
		while(x < 5):
			x += 0.025
			self.wait(0.001)


		stuff = []
		stuff.append( Tex(r"\ket{\psi}\otimes\ket{0}\otimes\ket{0}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{BS 50-50} \to \ket{\frac{1}{\sqrt{(2})}\psi}\otimes\ket{\frac{1}{\sqrt{(2})}\psi}\otimes\ket{0}").shift(DOWN*2) )
		stuff.append( Tex(r"\text{BS 50-50} \to \ket{\frac{1}{\sqrt{(2})}\psi}\otimes\ket{\frac{1}{2}\psi}\otimes\ket{\frac{1}{2}\psi}").shift(DOWN*3.5) )
		stuff.append( Tex(r"\text{Homodyne} \to \ket{\frac{1}{2}\psi} \to u \simeq N(Re(\psi)) \ \ \ \ \ \ \ \ \ \ket{\frac{1}{2}\psi} \to v \simeq N(Im(\psi))").shift(DOWN*5).scale(0.85) )
		stuff.append( Tex(r"\text{Controlled Displacement} \to D(u + iv)\ket{\frac{1}{\sqrt{(2})}\psi} = \ket{\frac{1}{\sqrt{(2})}\psi + (u + iv)} = \ket{\psi^l}").shift(DOWN*6.5).scale(0.8) )
		stuff.append( Tex(r"\text{BS 50-50} \to \ket{\frac{1}{\sqrt{(2})}\psi + (u + iv)}\otimes\ket{0} = \ket{\frac{1}{\sqrt{(2})}\psi^l}\otimes\ket{\frac{1}{\sqrt{(2})}\psi^l} = \ket{\psi^\prime}\otimes\ket{\psi^\prime}").shift(DOWN*8).scale(0.8) )
		stuff.append( Tex(r"\ket{\psi^\prime} \approx N(\mu, \eta), \mu = (Re(\psi), Im(\psi)), \eta = I/4").shift(DOWN*9.5) )
		
		frame = self.camera.frame
		frame.generate_target()
		self.play(MoveToTarget(frame, run_time=2.0))
		for i in stuff:
			frame.target.shift(DOWN*1)
			self.play(MoveToTarget(frame, run_time=2.0))
			self.play(FadeIn(i))
			self.wait(10)
		self.wait(30)








from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum K-Means Clustering (KMC)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class kmeans(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum K-Means Clustering (KMC)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("K-Means Clustering (KMC)").shift(UP*3.5)
		self.play(FadeIn(title))

		
		axes = Axes(x_range=(-2, 2, 0.5), y_range=(-1, 1, 0.5), height=6, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } )
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(DOWN*0.5).scale(0.9)

		centers = []
		dotsc = []
		points = []
		dots0 = []
		dots = []
		clines = []
		for j in range(3):
			mx = random.randint(-1500, 1500)/1000
			my = random.randint(-800, 800)/1000
			col = GREEN
			centers.append([mx, my])
			dotsc.append( Dot(color=YELLOW).move_to(axes.c2p(*centers[-1])).scale(1.5) )
			if (j == 0):
				col = RED
			elif (j == 1):
				col = BLUE
			for i in range(10):
				sx = random.randint(-1000, 1000)/4500
				sy = random.randint(-1000, 1000)/4500
				points.append([mx + sx, my + sy])
				dots0.append( Dot(color=WHITE).move_to(axes.c2p(*points[-1])) )
				dots.append( Dot(color=col).move_to(axes.c2p(*points[-1])) )
		for i in centers:
			clines.append( Line(axes.c2p(-0.2, -0.1), axes.c2p(*i)).set_color(GREY) )
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Based on Mean and Choosen K Value (\# of Groups)}").shift(UP*2.75) )
		stuff.append( Group(*dots0, axes) )
		stuff.append( Group(*dots) )
		stuff.append( Dot(color=ORANGE).move_to(axes.c2p(-0.2, -0.1)).scale(2.5)  )
		stuff.append( Group(*dotsc, *clines) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		
		stuff[-2].generate_target()
		stuff[-2].target = Dot(color=GREEN).move_to(axes.c2p(-0.2, -0.1)) 
		self.play(MoveToTarget(stuff[-2]), FadeOut(stuff[-1]))
		self.wait(2)
		waiter(8)
		stuff.pop(-1)
		self.play(FadeOut(Group(*stuff)))








		
		title2 = Text("Swap Test and Vector Distance").shift(UP*3.5)
		self.play(Transform(title, title2))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{How similar are 2 quantum states}").shift(UP*2.75) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(1)
		

		#make a 
		base = 2
		offset = 1
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
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*6).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)

		qubits = []
		for i in range(0, 3):
			if (i == 0):
				qubits.append(qubit(i, 'Ancilla', ''))
			elif (i == 1):
				qubits.append(qubit(i, r'\ket{\psi}_n', ''))
			elif (i == 2):
				qubits.append(qubit(i, r'\ket{\phi}_n', ''))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def cswap(pos,up, down, down2):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0])).scale(1.5).set_color(RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down2 + RIGHT*cx + UP*base).set_color(RED)
			cnot4 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down2 + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3, cnot4)
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
		def gCGateN(pos, up, down, control, color, depth):
			qft1 = Rectangle(width=0.5, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gates = []
		gates.append( hadamard(-2, 0) )
		gates.append( cswap(0, 0, 1, 2) )
		gates.append( hadamard(2, 0) )
		self.play(FadeIn(Group(*gates)))


		gatesm = []
		gatesm.append( measure(5, 0) )
		self.play(FadeIn(Group(*gatesm)))
		waiter(5)
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{\psi}_n"
		qubits[2].dq = r"\ket{\phi}_n"
		waiter(10)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{+}"
		qubits[1].dq = r"\ket{\psi}_n"
		qubits[2].dq = r"\ket{\phi}_n"
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		waiter(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"f(\ket{\psi}_n, \ket{\phi}_n)"
		qubits[2].dq = r"g(\ket{\phi}_n, \ket{\psi}_n)"
		waiter(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		waiter(0.5)
		qubits[0].dq = r"P(\ket{0} or \ket{1})"
		qubits[1].dq = r"f(\ket{\psi}_n, \ket{\phi}_n)"
		qubits[2].dq = r"g(\ket{\phi}_n, \ket{\psi}_n)"
		waiter(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		waiter(0.5)

		frame = self.camera.frame
		frame.generate_target()

		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"\text{Initialize: } \ket{0}\ket{\psi}_n\ket{\phi}_n \to \ket{0}\ket{\Omega}").shift(DOWN*(0.8*1)) )
		stuff2.append( Tex(r"\text{H: }  \ket{0}\ket{\Omega} \to \frac{1}{\sqrt{(2})}(\ket{0} + \ket{1}) \ket{\Omega}").shift(DOWN*(0.9*2)) )
		stuff2.append( Tex(r"\text{F: }  \frac{1}{\sqrt{(2})}(\ket{0}\ket{\Omega} + \ket{1}\ket{\Omega}) \to \frac{1}{\sqrt{(2})}(\ket{0}\ket{\Omega} + \ket{1}F(\ket{\Omega}))").shift(DOWN*(1*3)) )
		stuff2.append( Tex(r"\text{H: }  \frac{1}{\sqrt{(2})}(\ket{0}\ket{\Omega} + \ket{1}F(\ket{\Omega})) \to \frac{1}{2}(\ket{0}\ket{I+F \Omega} + \ket{1}\ket{I-F \Omega})").shift(DOWN*(1*4.5)) )
		stuff2.append( Tex(r"\text{Probability 1: }  P(\ket{1}) = \bra{\Omega}P_1\ket{\Omega} = \bra{\Omega}\frac{I-F}{2}\ket{\Omega}").shift(DOWN*(1*5.5)) )
		stuff2.append( Tex(r"P(\ket{1}) = \frac{1}{2}\langle{\psi_n\phi_n \mid (\ket{\psi}_n\ket{\phi}_n - \ket{\phi}_n\ket{\psi}_n)}\rangle").shift(DOWN*(1*6.75)) )
		stuff2.append( Tex(r"P(\ket{1}) = 0.5 - 0.5*\braket{\psi_n \mid \phi_n} \to d = (\ket{\psi}_n - \ket{\phi}_n)").shift(DOWN*(1*7.75)) )
		stuff2.append( Tex(r"d = 2*\sqrt{P(\ket{1})} \to \text{Lowest } P_{\phi \psi}(\ket{1})").shift(DOWN*(1*8.75)) )
		for i in stuff2:
			frame.target.shift(DOWN*0.75)
			self.play(MoveToTarget(frame), FadeIn(i))
			waiter(4)
		waiter(3)
		frame.target.shift(UP*6)
		for i in range(0, 3):
			self.remove(qubits[i].get())
		self.play(MoveToTarget(frame), FadeOut(Group(*stuff2, *gates, *gatesm, *stuff)))
		
		snop = Text("Coding Exercise!")
		self.play(Write(snop))
		waiter(15)

















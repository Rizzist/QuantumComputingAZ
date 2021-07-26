from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Circuit Ansatz, Hybrid Computation & Quantum Node").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class ansatz(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Circuit Ansatz, Hybrid Computation & Quantum Node").scale(0.8)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Circuit Ansatz").shift(UP*3.5)
		self.play(FadeIn(title))

		#make a 
		base = 1.5
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
		def gGate(pos,down, name, val):
			hx = pos
			h2 = Tex(name + "{:.3f}".format(float(val))).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=8, height=2.5, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def gGate2(pos,down, name):
			hx = pos
			h2 = Tex(name).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=2.5, height=2.125, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gBlock(pos, depth, down, name, color, opacity):
			qft1 = Rectangle(width=3.5, height=offset*down*depth + 0.5, color=color, fill_color=color, fill_opacity=opacity)
			qft2 = Tex(name).scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		for i in range(0, 3):
			gates.append( hadamard(-3, i) )
		gates.append( xgate(-3, 3) )
		

		gates.append( cxgate(0.825, 0, 1) )
		gates.append( cxgate(3.25, 3, 2) )
		gates.append( gGate2(0.825, 2, r"U(\theta)") )
		gates.append( hadamard(3.25, 0) )

		gates.append( gBlock(-2, 2.25, 1.5, r"A(\alpha)", ORANGE, 1) )
		gates.append( gBlock(2, 2.25, 1.5, r"B(\beta)", BLUE, 1) )
		#gates.append(  )

		self.play(FadeIn(Group(*gates)))

		waiter(10)

		tlen = len(gates)
		nalpha = gBlock(-2, 2.25, 1.5, r"A(\alpha)", ORANGE, 0.4)
		nbeta = gBlock(2, 2.25, 1.5, r"B(\beta)", BLUE, 0.4)
		self.play(Transform(gates[tlen-2], nalpha))
		self.play(Transform(gates[tlen-1], nbeta))

		waiter(25)

		punchline = Text("The actual circuit of the algorithm is the Circuit Ansatz").shift(DOWN*2).scale(0.7)
		self.play(FadeIn(punchline))
		waiter(10)

		for i in range(0, 4):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates, punchline, nalpha, nbeta)))


















		title2 = Text("Hybrid Computation").shift(UP*3.5)
		self.play(Transform(title, title2))

		stuff = []
		stuff.append( Tex("QC = ").shift(LEFT*4 + UP*2.5) )
		stuff.append( Tex("CC = ").shift(RIGHT*3 + UP*2.5) )
		stuff.append( Dot(np.array([-3, 2.5, 0]), color=RED).scale(3) )
		stuff.append( Dot(np.array([4, 2.5, 0]), color=BLUE).scale(3) )

		for i in stuff:
			self.play(FadeIn(i))

		stuff2 = []
		stuff2.append( Dot(np.array([-3, -2, 0]), color=RED).scale(3) )
		stuff2.append( Dot(np.array([-3, 0, 0]), color=BLUE).scale(3) )
		stuff2.append( Dot(np.array([0, 0, 0]), color=RED).scale(3) )
		stuff2.append( Dot(np.array([-1, -1, 0]), color=BLUE).scale(3) )
		stuff2.append( Dot(np.array([1, 1, 0]), color=BLUE).scale(3) )
		stuff2.append( Dot(np.array([1, -1, 0]), color=RED).scale(3) )

		stuff2.append( Dot(np.array([3, -2, 0]), color=RED).scale(3) )
		stuff2.append( Dot(np.array([3, 0, 0]), color=BLUE).scale(3) )
		stuff2.append( Dot(np.array([3, 1, 0]), color=BLUE).scale(3) )
		stuff2.append( CurvedArrow(np.array([-3, -2, 0]), np.array([-1, -1, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([-3, 0, 0]), np.array([0, 0, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([-3, 0, 0]), np.array([-1, -1, 0]), angle=0.0) )

		stuff2.append( CurvedArrow(np.array([-3, 0, 0]), np.array([1, 1, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([-3, -2, 0]), np.array([1, -1, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([0, 0, 0]), np.array([1, 1, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([-1, -1, 0]), np.array([1, -1, 0]), angle=0.0) )

		stuff2.append( CurvedArrow(np.array([1, 1, 0]), np.array([3, -2, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([1, -1, 0]), np.array([3, 1, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([1, -1, 0]), np.array([3, 0, 0]), angle=0.0) )
		stuff2.append( CurvedArrow(np.array([1, -1, 0]), np.array([3, -2, 0]), angle=0.0) )
		for i in stuff2:
			self.play(FadeIn(i))
		waiter(10)

		title3 = Text("Quantum Node").shift(UP*3.5)
		self.play(Transform(title, title3))
		waiter(10)
		self.play(FadeOut(Group(*stuff2)))

		stuff3 = []
		stuff3.append( Dot(np.array([-3, 0, 0]), color=RED).scale(3) )
		stuff3.append( Dot(np.array([3, 0, 0]), color=BLUE).scale(3) )
		stuff3.append( CurvedArrow(np.array([-3, 0, 0]), np.array([3, 0, 0])) )
		stuff3.append( CurvedArrow(np.array([3, 0, 0]), np.array([-3, 0, 0])) )
		stuff3.append( Text("Quantum Machine Learning").shift(DOWN*3) )
		for i in stuff3:
			self.play(FadeIn(i))
		waiter(20)











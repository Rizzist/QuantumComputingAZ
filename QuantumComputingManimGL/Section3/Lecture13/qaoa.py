from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Approximate Optimization Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class qaoa(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Approximate Optimization Algorithm").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		random.seed(20)

		class graph():
			def __init__(self, verticesO, edgesO, colors0):
				self.vertices = verticesO
				self.edges = edgesO
				self.colors = colors0
				self.labels = []
				self.dots = []
				self.lines = []
				self.linecols = []
				for i in range(len(self.vertices)):
					self.dots.append( Dot(np.array(self.vertices[i]), color=self.colors[i]).scale(3) )
					def update_qube(self2, i=i):
						self2.become( Dot(np.array(self.vertices[i]), color=self.colors[i]).scale(3) )
					self.dots[i].add_updater(update_qube)

					dlabel = Tex(r"" + str(i)).shift(RIGHT*self.vertices[i][0] + UP*self.vertices[i][1]).set_color(BLACK)
					self.labels.append(dlabel)
				for i in range(len(self.edges)):
					self.linecols.append( WHITE )
					def update_liner(self2, i=i):
						self2.become( Line( np.array(self.vertices[self.edges[i][0]]) , np.array(self.vertices[self.edges[i][1]]), color=self.linecols[i] ) )
					self.lines.append( Line( np.array(self.vertices[self.edges[i][0]]) , np.array(self.vertices[self.edges[i][1]]) ).add_updater(update_liner) )
			def getDots(self):	
				return Group(*self.dots, *self.labels)
			def setDot(self, i, col):
				self.colors[i] = col
			def getLines(self):	
				return Group(*self.lines)
			def addDot(self,dot, color, i):
				self.vertices.append(dot)
				currentIndex = len(self.vertices)-1
				self.colors.append(color)
				self.dots.append( Dot(np.array(self.vertices[currentIndex]), color=self.colors[currentIndex]).scale(3) )
				def update_qub(self2, i=i):
					self2.become( Dot(np.array(self.vertices[currentIndex]), color=self.colors[currentIndex]).scale(3) )
				self.dots[currentIndex].add_updater(update_qub)
				dlabel = Tex(r"" + str(currentIndex)).shift(RIGHT*self.vertices[currentIndex][0] + UP*self.vertices[currentIndex][1]).set_color(BLACK)
				self.labels.append(dlabel)
			def addEdge(self,edge, i):
				self.edges.append(edge)
				self.linecols.append( WHITE )
				currentIndex = len(self.edges)-1
				def update_liner(self2, i=i):
					self2.become( Line( np.array(self.vertices[self.edges[currentIndex][0]]) , np.array(self.vertices[self.edges[currentIndex][1]]), color=self.linecols[currentIndex] ) )
				self.lines.append( Line( np.array(self.vertices[self.edges[currentIndex][0]]) , np.array(self.vertices[self.edges[currentIndex][1]]) ).add_updater(update_liner) )
			def updateCuts(self):
				count = 0
				for i in range(len(self.edges)):
					if ( self.colors[self.edges[i][0]] == self.colors[self.edges[i][1]] ):
						self.linecols[i] = WHITE
					else:
						self.linecols[i] = RED
						count += 1
				return count
			def generateGraph(self, n):
				for i in range(n):
					self.addDot([ (random.randint(0, 2000)-1000)/150 , (random.randint(0, 2000)-1100)/330, 0], BLUE_C if random.randint(0, 1) == 0 else GREEN_C, i)
					for j in range(len(self.vertices)):
						if random.randint(0, 10) < 3:
							self.addEdge([random.randint(0, len(self.vertices) - 2), len(self.vertices) - 1], j)


		title = Text("Graphs").shift(UP*3.5)
		self.play(FadeIn(title))


		agraph = graph( [[0, 0, 0]], [], [GREEN_C]  )
		cdgraph=agraph.getDots()
		clgraph=agraph.getLines()
		#generate dots and edges
		#agraph.addDot([-1, 2, 0], GREEN, 0)
		#agraph.addEdge([1, 3], 0)




		def redrawGraph(cdgraph, clgraph):
			self.remove(Group(cdgraph, clgraph))
			cdgraph=agraph.getDots()
			clgraph=agraph.getLines()
			self.add(clgraph)
			self.add(cdgraph)
			return Group(clgraph, cdgraph)
		


		agraph.generateGraph(4)
		dgraph = redrawGraph(cdgraph, clgraph)
		waiter(30)

		numcuts = agraph.updateCuts()
		count = Text("Num Cuts: " + str(numcuts)).shift(LEFT*4.5 + DOWN*3)
		self.add(count)
		self.remove(dgraph)
		dgraph = redrawGraph(cdgraph, clgraph)
		waiter(10)


		for i in range(5):
			self.remove(count)
			random.seed(random.randint(0, 999999))
			self.remove(dgraph)
			agraph = graph( [[0, 0, 0]], [], [GREEN_C]  )
			agraph.generateGraph(random.randint(3, 15))
			cdgraph=agraph.getDots()
			clgraph=agraph.getLines()
			dgraph = redrawGraph(cdgraph, clgraph)
			waiter(5)

			numcuts = agraph.updateCuts()
			if (i > 0):
				numcuts -= 1
			count = Text("Num Cuts: " + str(numcuts)).shift(LEFT*5 + DOWN*3.5)
			self.add(count)
			dgraph = redrawGraph(cdgraph, clgraph)
			waiter(5)

		prob = Text("Maximize # of Cuts").shift(DOWN*3.5 + RIGHT*4).scale(0.7)
		self.play(FadeIn(prob))
		waiter(5)
		for i in range(5):
			agraph.setDot(i, GREEN_C)
		self.remove(count)
		numcuts = agraph.updateCuts()
		count = Text("Num Cuts: " + str(numcuts)).shift(LEFT*5 + DOWN*3.5)
		self.add(count)
		dgraph = redrawGraph(cdgraph, clgraph)
		waiter(15)

		#0, 3
		self.remove(count)
		agraph.setDot(0, BLUE_C)
		for j in range(5):
			if (j!=0):
				agraph.setDot(j, GREEN_C)
		numcuts = agraph.updateCuts() - 1
		count = Text("Num Cuts: " + str(numcuts)).shift(LEFT*5 + DOWN*3.5)
		self.add(count)
		dgraph = redrawGraph(cdgraph, clgraph)
		waiter(15)

		self.remove(count)
		agraph.setDot(3, BLUE_C)
		numcuts = agraph.updateCuts() - 1
		count = Text("Num Cuts: " + str(numcuts)).shift(LEFT*5 + DOWN*3.5)
		self.add(count)
		dgraph = redrawGraph(cdgraph, clgraph)
		waiter(5)

		stuff = []
		stuff.append( Tex(r"C = \sum_{(a, b) \in E} (1-\sigma_a\sigma_b)").shift(DOWN*2.5 + RIGHT*4) )
		stuff.append( Tex(r"\sigma_i = \{-1, 1\} \to Blue=1 \ \ \ Green=-1").shift(UP*2.75) )
		stuff.append( Tex(r"\sum_{(a, b) \in E} (\mathbb{I}-Z_aZ_b) \to C_{ij} = (\mathbb{I}-Z_aZ_b)").shift(UP*1 + LEFT*2.5) )
		stuff.append( Tex(r"\ket{\psi}_o = e^{-i\gamma C}\ket{\psi}").shift(UP*1.25 + RIGHT*4) )
		stuff.append( Tex(r"Answer: 10110").shift(DOWN*1.5 + RIGHT*4) )
		stuff.append( Tex(r"Answer: 01001").shift(DOWN*0.75 + RIGHT*4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff, dgraph, count, prob)))






		agraph = graph( [[0, -3, 0], [-1, -2, 0], [1, -2, 0], [0, -1, 0]], [], [GREEN_C, GREEN_C, GREEN_C, GREEN_C]  )
		cdgraph=agraph.getDots()
		clgraph=agraph.getLines()
		dgraph = redrawGraph(cdgraph, clgraph)
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
			if (i == 0):
				qubits.append(qubit(i, '', ''))
			elif (i == 1):
				qubits.append(qubit(i, '', ''))
			elif (i == 2):
				qubits.append(qubit(i, '', ''))
			elif (i == 3):
				qubits.append(qubit(i, '', ''))
			elif (i == 7):
				qubits.append(qubit(i, 'Inp1', ''))
			else:
				qubits.append(qubit(i, 'Inp4', ''))
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
		def zgate(pos,down, on=1):
			hx = pos
			h2 = Tex(r"Z(\lambda)").scale(0.7).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=TEAL, fill_opacity=on, color=TEAL).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
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
		def U3(pos,down):
			hx = pos
			h2 = Tex(r"U3(\phi)").scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=ORANGE, fill_opacity=1, color=ORANGE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
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
			qft1 = Rectangle(width=1, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gatesH = []
		for i in range(0, 4):
			gatesH.append( hadamard(-4.25, i) )
		gates1 = []
		gates1.append( cxgate(-3-0.25, 0, 1) )
		gates1.append( zgate(-2.25-0.25, 1) )
		gates1.append( cxgate(-1.5-0.25, 0, 1) )

		gates2 = []
		gates2.append( cxgate(-0.5-0.25, 1, 2) )
		gates2.append( zgate(0.25-0.25, 2) )
		gates2.append( cxgate(1-0.25, 1, 2) )

		gates3 = []
		gates3.append( cxgate(2-0.25, 0, 3) )
		gates3.append( zgate(2.75-0.25, 3) )
		gates3.append( cxgate(3.5-0.25, 0, 3) )
		#gates.append( xgate(0, 0) )
		#gates.append( gCGateN(-2, 0, 1.75, r'++', PURPLE, 1.75) )
		#gates.append( gCGateN(2, 0, 1.75, r'--', PURPLE, 1.75) )
		waiter(10)
		agraph.addEdge([0, 1], 0)
		dgraph = redrawGraph(cdgraph, clgraph)
		self.play(FadeIn(Group(*gates1)))
		waiter(10)

		agraph.addEdge([1, 2], 0)
		dgraph = redrawGraph(cdgraph, clgraph)
		self.play(FadeIn(Group(*gates2)))
		waiter(10)

		agraph.addEdge([0, 3], 0)
		dgraph = redrawGraph(cdgraph, clgraph)
		self.play(FadeIn(Group(*gates3)))
		waiter(10)

		self.play(FadeIn(Group(*gatesH)))
		gatesU3 = []
		for i in range(0, 4):
			gatesU3.append( U3(4.25-0.25, i) )
		self.play(FadeIn(Group(*gatesU3)))
		waiter(10)

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

		waiter(30)


		
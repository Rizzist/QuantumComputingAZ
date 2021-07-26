from manimlib import *
import numpy as np
import random
import scipy.integrate

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Walk").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)



class walk(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)

		text = Text("Quantum Walk").scale(1.1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		
		
		title = Text("Coin Operator").shift(UP*3.5)
		self.play(FadeIn(title))
		
		coin = Tex(r"\hat{C} = \begin{bmatrix} cos(\theta) & isin(\theta) \\ isin(\theta) & -cos(\theta) \end{bmatrix}").shift(UP*2)
		self.play(FadeIn(coin))
		waiter(5)

		coin2 = Tex(r"\hat{C}(\frac{\pi}{4}) = HadamardCoin")
		self.play(FadeIn(coin2))
		waiter(5)
		self.play(FadeOut(coin2))

		coin3 = Tex(r"\hat{C}\ket{0} = a\ket{0} + b\ket{1}")
		self.play(FadeIn(coin3))
		waiter(7)
		self.play(FadeOut(coin3))

		title2 = Text("Conditional Shift Operator").shift(UP*3.5)
		self.play(Transform(title, title2))

		shift = Tex(r"\hat{S} = \ket{1}\bra{1} \otimes \sum_{i} \ket{i+1}\bra{i} + \ket{0}\bra{0} \otimes \sum_{i} \ket{i-1}\bra{i}")
		self.play(FadeIn(shift))
		waiter(8)

		shift2 = Tex(r"\hat{S}(\ket{0}\ket{i}) = \ket{0}\ket{i-1}").shift(DOWN*1)
		self.play(FadeIn(shift2))
		waiter(8)

		shift3 = Tex(r"\hat{S}(\ket{1}\ket{i}) = \ket{1}\ket{i+1}").shift(DOWN*2)
		self.play(FadeIn(shift3))
		waiter(8)

		shift4 = Tex(r"\hat{C}(\frac{\pi}{4}) \to \hat{S}(\ket{+}\ket{i}) = \frac{1}{\sqrt{(2})}\ket{0}\ket{i-1} + \frac{1}{\sqrt{(2})}\ket{1}\ket{i+1}").shift(DOWN*3)
		self.play(FadeIn(shift4))
		waiter(8)

		self.play(FadeOut(Group(shift4, shift3, shift2, shift, coin)))






















		
		title3 = Text("Quantum Walk").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title3))
	

		ypos = -3
		line = Line(np.array([-8, ypos, 0]), np.array([8, ypos, 0]))
		self.play(FadeIn(line))
		dots = []
		ranges = 16
		for i in range(-ranges+1, ranges):
			dots.append( Dot(np.array([i/2, ypos, 0]), color=RED) )
		self.play(FadeIn(Group(*dots)))

		def rectP(h, x):
			return Rectangle(height=h*6, width=0.5, fill_color=BLUE, color=BLUE, fill_opacity=1.0).shift(UP*ypos + UP*h*3 + RIGHT*x/2)
		vals = []
		rects = []
		
		for i in range(-ranges+1, ranges):
			if (i == 0):
				rects.append( rectP(1, i) )
			else: 
				rects.append( rectP(0, i) )
		self.play(FadeIn(Group(*rects)))
		a = 1
		b = 0
		for i in range(-ranges+1, ranges):
			if(i == 0):
				vals.append((a + b*1j)/((a**2 + b**2)**0.5))
			else:
				vals.append(1j)




		coinA = 1
		coinB = 1
		for i in range(0, 46):
			trects = []
			tvals = vals.copy()
			placeholders = []
			for j in range(0, len(vals)):
				if (np.real(vals[j]) > 0 or np.real(vals[j]) < 0):
					placeholders.append(j)
					if j > 0:
						tvals[j-1] *= vals[j]*(coinA + coinB*1j)/((coinA**2 + coinB**2)**0.5)
					if j < len(vals)-1:
						tvals[j+1] *= vals[j]*(-coinA + coinB*1j)/((coinA**2 + coinB**2)**0.5)
					vals[j] *= 1j
			for j in placeholders:
				tvals[j] *= 1j
			norm = 0
			for k in range(0, len(tvals)):
				norm += np.absolute(np.real(tvals[k]))
			norm = norm**0.5
			for k in range(-ranges+1, ranges):
				trects.append( rectP(np.absolute(np.real(tvals[k+ranges-1]))/norm, k) )
			self.play(FadeOut(Group(*rects), run_time=0.05), FadeIn(Group(*trects), run_time=0.05))
			vals = tvals.copy()
			rects = trects.copy()

		waiter(5)
		title4 = Text("Quantum Walk VS. Classical Walk").shift(UP*3.5)
		self.play(FadeOut(title3), FadeIn(title4))
		#now do the classical version
		ypos2 = 0
		line2 = Line(np.array([-8, ypos2, 0]), np.array([8, ypos2, 0]))
		self.play(FadeIn(line2))
		dots2 = []
		ranges2 = 16
		for i in range(-ranges2+1, ranges2):
			dots2.append( Dot(np.array([i/2, ypos2, 0]), color=RED) )
		self.play(FadeIn(Group(*dots2)))
		def dotP(x):
			return Dot(point=np.array([x/2, ypos2, 0]), radius=0.2, fill_color=BLUE, color=BLUE, fill_opacity=1.0)
		rando = 0
		current = dotP(rando)
		self.play(FadeIn(current))
		waiter(5)
		for i in range(0, 46):
			self.play(FadeOut(current), run_time=0.05)
			rando += 2*random.randint(0, 1) - 1
			current = dotP(rando)
			self.play(FadeIn(current), run_time=0.05)
		self.play(FadeOut(Group(current, line2, *dots2, *rects, line, *dots)))
		waiter(5)

		corona2 = ImageMobject("./distribution.jpeg").scale(1.5)
		self.play(FadeIn(corona2))
		waiter(15)
		self.play(FadeOut(corona2))
		corona = ImageMobject("./graph.jpeg").scale(1.5)
		self.play(FadeIn(corona))
		waiter(15)
		self.play(FadeOut(corona))
		

		
		

		#self.play(FadeOut(corona))


		title5 = Text("Quantum Walk Circuit").shift(UP*3.5)
		self.play(Transform(title4, title5))
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
		for i in range(0, 5):
			if (i == 0):
				qubits.append(qubit(i, 'Coin', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'Inp1', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'Inp2', ''))
			elif (i == 3):
				qubits.append(qubit(i, 'Inp3', ''))
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
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"C").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
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
			qft1 = Rectangle(width=1, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gates = []
		gates.append( hadamard(-4, 0) )
		gates.append( xgate(0, 0) )
		gates.append( gCGateN(-2, 0, 1.75, r'++', PURPLE, 1.75) )
		gates.append( gCGateN(2, 0, 1.75, r'--', PURPLE, 1.75) )
		self.play(FadeIn(Group(*gates)))


		gatesm = []
		for i in range(0, 5):
			gatesm.append( measure(5, i) )
		self.play(FadeIn(Group(*gatesm)))
		waiter(5)
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"


		seeit = Text("Increment & Decrement Circuit Prev. Section").shift(DOWN*2).scale(0.7)
		self.play(FadeIn(seeit))
		waiter(30)













from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Embedding").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class qembed(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Embedding").scale(1.1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Quantum Embedding").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		stuff.append(  Text("Given a data set: ").shift(UP*2+LEFT*4).scale(0.7)  )
		stuff.append(  Text("How to Represent it in a Quantum Computer?").shift(UP*1).scale(0.7) )
		stuff.append(  Text("1. Angle Embedding").shift(UP*0) )
		stuff.append(  Text("2. Basis Embedding").shift(DOWN*1) )
		stuff.append(  Text("3. Amplitude Embedding").shift(DOWN*2) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff)))












		title2 = Text("Data Set").shift(UP*3.5)
		self.play(Transform(title, title2))

		def createBerry(x, y, col, redness):
			q = Tex("{:.2f}".format(redness)).shift(RIGHT*x + UP*y + UP*0.5 + RIGHT*0.5)
			p = Dot(np.array([x, y, 0]), color=col).scale(3)
			return Group(q, p)
		def getCol():
			result = random.randint(0, 4)
			toreturn = []
			if result == 0:
				toreturn = [RED, 1.0]
			elif result == 1:
				toreturn = [ORANGE, 0.81 + random.randint(0, 10)/100]
			elif result == 2:
				toreturn = [GREEN, 0.42 + random.randint(0, 10)/100]
			elif result == 3:
				toreturn = [BLUE, 0.11 + random.randint(0, 10)/100]
			elif result == 4:
				toreturn = [GREY, 0.02 + random.randint(0, 10)/200]
			return toreturn

		berries = []
		for i in range(15):
			thecol = getCol()
			berries.append( createBerry(random.randint(-6, -2) + 0.5, random.randint(-3, 2) + 0.25, thecol[0], thecol[1]) )

		for i in berries:
			self.play(FadeIn(i, run_time=0.3))

		stuff = []
		stuff.append(  DashedLine(np.array([0, -2.5, 0]), np.array([0,2.5, 0]), color=WHITE)  )
		stuff.append(  Text("Correlation w/ Redness & Being Eaten?").shift(RIGHT*3.25 + DOWN*3.25).scale(0.5)  )
		#stuff.append(  Tex(r"")  )
		stuff.append(  Tex(r"\vec{x} = \begin{bmatrix} Redness \\ P(Eaten) \end{bmatrix}").shift(RIGHT*3 + UP*2)  )
		stuff.append(  Tex(r"\begin{bmatrix} 0.82 \\ 0.321 \end{bmatrix}").shift(RIGHT*1)  )
		stuff.append(  Tex(r"\begin{bmatrix} 0.498 \\ 0.755 \end{bmatrix}").shift(RIGHT*3)  )
		stuff.append(  Tex(r"\begin{bmatrix} 0.02 \\ 0.919 \end{bmatrix}").shift(RIGHT*5)  )
		stuff.append(  Tex(r"D = \{ \vec{x}_1,\vec{x}_2,\vec{x}_3, \cdots  \}").shift(RIGHT*3 + DOWN*2)  )


		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(12)
		self.play(FadeOut(Group(*stuff, *berries)))























		title3 = Text("Angle Embedding").shift(UP*3.5)
		self.play(Transform(title, title3))

		waiter(2)

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
		def gGate(pos,down, name, val):
			hx = pos
			h2 = Tex(name + "{:.3f}".format(float(val))).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=8, height=2.5, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def gGate2(pos,down, name):
			hx = pos
			h2 = Tex(name).scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=8, height=2.125, fill_color=PURPLE, fill_opacity=1, color=PURPLE).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		
		for i in range(0, 2):
			gates.append( hadamard(-4, i) )
			gates.append( gGate(-2 + 3*i, i, r"U_\theta = ", 0.82 - 0.499*i) )
		
		self.play(FadeIn(Group(*gates)))


		encoding = Tex(r"\vec{x}_1 = \begin{bmatrix} 0.82 \\ 0.321 \end{bmatrix}").shift(DOWN*1)
		self.play(FadeIn(encoding))
		waiter(10)
		for i in range(0, 2):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(encoding, *gates)))

















		title4 = Text("Basis Embedding").shift(UP*3.5)
		self.play(Transform(title, title4))

		stuff = []
		stuff.append( Text("Cost per mg of Gold?").shift(DOWN*3.5).scale(0.5) )
		berries = []
		gvals = []
		waiter(5)
		for i in stuff:
			self.play(FadeIn(i))
		for i in range(10):
			cval = random.randint(0, 7)
			thecol = [YELLOW, cval]
			gvals.append(cval)
			berries.append( createBerry(random.randint(-6, 6), random.randint(-1, 2), thecol[0], thecol[1]) )


		placeholder = Tex(r"").shift(DOWN*2.5)
		self.add(placeholder)
		for i in range(len(berries)):
			gcut = gvals[0:i+1]
			ketstring = r"\ket{\psi} = "
			for j in range(0, 8):
				amount = gcut.count(j)
				if amount != 0:
					ketstring += str(amount) + r"\ket{" +  str(bin(j)[2:] )  + r"} +"
			new = Tex(ketstring[:-1]).shift(DOWN*2.5)
			self.play(FadeIn( berries[i] ))
			self.play(Transform(placeholder, new), run_time=0.8)

		waiter(20)
		normpsi = Tex(r"Normalize(\ket{\psi}) \to QC").shift(DOWN*1.5)
		self.play(FadeIn(normpsi))
		waiter(15)

		self.play(FadeOut(Group(placeholder, normpsi, *berries, *stuff)))
		qubits = []
		for i in range(0, 3):
			qubits.append(qubit(i, str(i), ''))
			self.add(qubits[i].get())

		gates = []
		
		for i in range(0, 3):
			gates.append( gGate2(-2, i, r"U3(r, \theta, \phi)") )
		self.play(FadeIn(Group(*gates)))
		waiter(10)
		for i in range(0, 3):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*gates)))













		title5 = Text("Amplitude Embedding").shift(UP*3.5)
		self.play(Transform(title, title5))



		stuff = []
		stuff.append( Tex(r"\vec{x}_0 = \begin{bmatrix} 0.82 \\ 0.321 \end{bmatrix} = \begin{bmatrix} x_0^{(1)} \\ x_0^{(2)} \end{bmatrix}").shift(UP*2) )
		stuff.append( Tex(r"D = \{ x_0^{(1)}, \cdots , x_0^{(M)}, \cdots , x_N^{(1)}, \cdots , x_N^{(M)} \}").shift(UP*0.5) )
		stuff.append( Tex(r"D = \{ 0.82, 0.321, 0.498, 0.755 \}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\ket{\psi} = 0.82\ket{0} + 0.321\ket{1} + 0.498\ket{2} + 0.755\ket{3}").shift(DOWN*1.5) )
		stuff.append( Tex(r"Normalize(\ket{\psi}) \to QC").shift(DOWN*2.5) )


		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(20)








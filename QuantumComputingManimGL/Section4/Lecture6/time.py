from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Time Domain Photonic Circuits").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class time(Scene):
	def construct(self):
		text = Text("Time Domain Photonic Circuits")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Time Domain Photonic Circuits").shift(UP*3.5)
		self.play(FadeIn(title))

		corona = ImageMobject("./time.png").scale(1.2)
		self.play(FadeIn(corona))
		self.wait(15)


		self.play(FadeOut(corona))

		#make a 
		base = -2
		offset = 0.6
		x = -5
		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1, length=5, radius=1, color=RED):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				self.radius=radius
				self.length = length
				self.color = color
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([self.length, -offset*self.n + base, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=self.color).scale(self.radius))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*5.75).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)


		qubits = []
		for i in range(0, 1):
			if (i == 0):
				qubits.append(qubit(i, '0', '', length=5, radius=2))
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
		qubits[0].color = RED
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
		gates.append( beamsplitter(0, -1) )
		self.play(FadeIn(Group(*gates)))
		circle = Circle(color=WHITE).scale(2).shift(UP*0.5)
		self.play(FadeIn(circle))


		u = -np.pi
		dux = 2*np.sin(u)
		duy = 2*np.cos(u) + 0.5
		qubcol = RED
		qurad = 0.5
		def update_dot(self):
			self.become(Dot(np.array([2*np.sin(u),2*np.cos(u)+ 0.5,0]),fill_color=qubcol).scale(qurad))
		dotter = Dot(np.array([2*np.sin(u),2*np.cos(u)+ 0.5,0]), fill_color=BLUE).add_updater(update_dot)
		addeddot = False
		firstPhoton = False
		self.wait(10)
		for i in range(5):
			x = -5
			qubits[0].radius = 2
			crossed = False
			if (i == 1):
				qubits[0].color = BLUE
			if (i == 2):
				qubits[0].color = GREEN
			if (i == 3):
				qubits[0].color = YELLOW
			if (i == 4):
				qubits[0].color = WHITE
			while(x<5):
				x += 0.05
				if (x > 0 and crossed == False):
					qurad += 0.5
					if (i == 1):
						qubits[0].color = PURPLE
					if (i == 2):
						qubits[0].color = TEAL
					if (i == 3):
						qubits[0].color = GOLD
					if (i == 4):
						qubits[0].color = GREY
					crossed = True
				if (x > 0):
					u -= 2*np.pi/10 * 0.05
					if (addeddot==False):
						addeddot = True
						firstPhoton = True
						self.add(dotter)
						qubits[0].radius = 1
					if (i == 1):
						qubcol = PURPLE
					if (i == 2):
						qubcol = ORANGE
					if (i == 3):
						qubcol = GREEN_SCREEN
					if (i == 4):
						qubcol = GREY_BROWN
				if (x <= 0 and firstPhoton == True):
					u -= 2*np.pi/10 * 0.05
				self.wait(0.001)
		self.wait(30)





















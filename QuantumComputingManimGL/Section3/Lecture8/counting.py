from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Counting").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class counting(Scene):
	def construct(self):
		text = Text("Quantum Counting").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Grover Iterate").shift(UP*3.5)
		self.play(FadeIn(title))

		grov = Tex(r"\ket{\psi} = a\ket{x} + b\ket{\psi^\prime}").shift(UP*1)
		self.play(FadeIn(grov))
		self.wait(8)

		grov2 = Tex(r"\bra{x}\ket{\psi^\prime} = 0").shift(DOWN*1)
		self.play(FadeIn(grov2))
		self.wait(4)

		self.play(FadeOut(Group(grov, grov2)))

		#show grover iteration
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		r = 2.4
		x = 3.14159/4
		a = r * np.sin(x)
		b = r * np.cos(x)
		c = 2.4
		vector = Vector(direction=[a,b/10,0])
		vectorX = Vector(direction=[a, 0,0], fill_color=RED)
		vectorY = Vector(direction=[0,b,0], fill_color=GREEN)
		vectorZ = Vector(direction=[0,0,c], fill_color=YELLOW)
		self.play(ShowCreation(Group(axes, grid, vectorX, vectorY)))

		def update_vectorLabel(self):
			self.become( Tex(r"\ket{\psi}").move_to(vector.get_end() + [0.5, 0.5, 0] ) )
		labelY = Tex(r"\ket{x}").shift(UP*2.5)
		labelX = Tex(r"\ket{\psi^\prime}").shift(RIGHT*4)
		labelZ = Tex(r"\ket{y}").shift(OUT*2.5)
		self.play(FadeIn(Group(labelX, labelY)))

		labelPsi = Tex(r"\ket{\psi}").move_to(vector.get_end() + [0.5, 0.5, 0] )
		labelPsi.add_updater(update_vectorLabel)
		self.play(FadeIn(Group(vector, labelPsi)))
		vector2 = Vector(direction=[a,b/10,0])
		vector3 = Vector(direction=[a,b/10,c/10])
		self.add(vector2)


		s = 0
		t = 0
		b = b/10
		[j, k] = [a.copy(), b.copy()]

		def update_vector(self):
			self.become(Vector(direction=[a, b, 0]).rotate_about_origin(s, np.array([1, 0, 0])).rotate_about_origin(t, np.array([j, k, 0])) )
		vector.add_updater(update_vector)

		target = 3.14159
		for i in range(0, 11):
			while (s < target):
				s += 0.1
				self.wait(0.001)
			if (i == 0):
				self.wait(10)
			while (t < target):
				t += 0.1
				self.wait(0.001)
			if (i == 0 or i==6):
				self.wait(10)
			vector.remove_updater(update_vector)
			s = 0
			t = 0
			end = vector.get_end()
			a = end[0]
			b = end[1]
			vector.add_updater(update_vector)
		self.wait(5)
		self.play(FadeOut(Group(vector, vector2, labelX, labelY, labelPsi, vectorX, vectorY, axes, grid)))


		grov = Tex(r"\ket{\psi} = a\ket{x} + b\ket{y} + c\ket{\psi^\prime}").shift(UP*1)
		self.play(FadeIn(grov))
		self.wait(8)
		grov2 = Tex(r"\bra{x}\ket{\psi^\prime} = 0 \ \ \ \ \ \ \ \ \ \ \bra{y}\ket{\psi^\prime} = 0").shift(DOWN*1)
		self.play(FadeIn(grov2))
		self.wait(4)
		self.play(FadeOut(Group(grov, grov2)))






		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, 30 * DEGREES,
			run_time=2
		)
		frame.generate_target()
		frame.target.set_width(15)
		self.play(MoveToTarget(frame))
		def spin(m, dt):
			m.increment_theta(-0.1 * dt)
		frame.add_updater(spin)

		a = r * np.sin(x)
		b = r * np.cos(x)
		c = r * np.cos(x) * 0.8

		b = b/10
		c = c/10
		[l, m, o] = [a.copy(), b.copy(), c.copy()]
		def update_vectorp(self):
			self.become(Vector(direction=[a, b, c]).rotate_about_origin(s, np.array([1, 0, 0])).rotate_about_origin(t, np.array([l, m, o])) )
		vectorp = Vector(direction=[a,b,c])
		vectorp2 = vectorp.copy()
		vectorp.add_updater(update_vectorp)
		def update_vectorLabel(self):
			self.become( Tex(r"\ket{\psi}").move_to(vectorp.get_end() + [0.5, 0.5, 0.5] ) )
		labelPsi2 = Tex(r"\ket{\psi}").move_to(vectorp.get_end() + [0.5, 0.5, 0.5] )
		labelPsi2.add_updater(update_vectorLabel)
		self.play(FadeIn(Group(vectorX, vectorY, vectorZ, labelX, labelY, labelZ, labelPsi2, vectorp, vectorp2, axes, grid)))


		target = 3.14159
		for i in range(0, 10):
			while (s < target):
				s += 0.1
				frame.increment_theta(-0.1*0.015)
				self.wait(0.001)
			if (i == 0):
				self.wait(10)
			self.wait(0.2)
			while (t < target):
				t += 0.1
				frame.increment_theta(-0.1*0.015)
				self.wait(0.001)
			if (i == 0 or i==6):
				self.wait(10)
			self.wait(0.2)
			vectorp.remove_updater(update_vectorp)
			s = 0
			t = 0
			end = vectorp.get_end()
			a = end[0]
			b = end[1] 
			c = end[2]
			vectorp.add_updater(update_vectorp)
		self.wait(20)
		self.play(FadeOut(Group(Group(vectorX, vectorY, vectorZ, labelX, labelY, labelZ, labelPsi2, vectorp, vectorp2, axes, grid))))







		frame.remove_updater(spin)
		frame.generate_target()
		frame.target.set_euler_angles(
			theta=0 * DEGREES,
			phi=0 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		title2 = Text("Quantum Counting").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.wait(2)
		problem = Text("How many solutions to Grover's Algorithm?").shift(UP*0.5)
		self.play(FadeIn(problem))
		self.wait(7)
		self.play(FadeOut(problem))




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
		for i in range(0, 6):
			if (i == 0):
				qubits.append(qubit(i, 'A', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'B', ''))
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
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft

		gates = []
		
		for i in range(0, 6):
			gates.append( hadamard(-4.25, i) )
		for i in range(0, 1):
			gates.append( gCGate(-3.5, 0, 3, r'G', PURPLE, 3) )
		for i in range(0, 2):
			gates.append( gCGate(-2.75 + 3*i/4, 1, 3, r'G', PURPLE, 3) )
		for i in range(0, 4):
			gates.append( gCGate(-1.25 + 3*i/4, 2, 3, r'G', PURPLE, 3) )
		self.play(FadeIn(Group(*gates)))


		qft = qftdag(3, 2, 2.5)
		self.play(FadeIn(qft))

		gatesm = []
		for i in range(0, 3):
			gatesm.append( measure(4.5, i) )
		self.play(FadeIn(Group(*gatesm)))


		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		qubits[4].dq = r"\ket{1}"
		qubits[5].dq = r"\ket{1}"
		self.wait(15)



		while(x < -4.25):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{-}"
		qubits[4].dq = r"\ket{-}"
		qubits[5].dq = r"\ket{-}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^\theta}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*4):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+^{\theta}}"
		self.wait(0.5)


		while(x < -4.25 + 0.75*5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+^{2\theta}}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*6):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+^{3\theta}}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*7):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+^{4\theta}}"
		self.wait(0.5)


		while(x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{-}"
		qubits[1].dq = r"\ket{-}"
		qubits[2].dq = r"\ket{-}"
		self.wait(0.5)



		while(x < 4.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(10)

		result2 = Text("Max Probability to Measure: 0b101").shift(DOWN*2.5)
		result = Text("# of Solutions = 0b101 = 5").shift(DOWN*3.5)
		self.play(FadeIn(result2))
		self.wait(10)
		self.play(FadeIn(result))
		self.wait(30)










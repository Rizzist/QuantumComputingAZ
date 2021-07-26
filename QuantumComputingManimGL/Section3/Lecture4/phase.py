from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Phase Estimation").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class phase(Scene):
	def construct(self):
		text = Text("Quantum Phase Estimation").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Quantum Phase Estimation - Theory").shift(UP*3.5)
		self.play(FadeIn(title))

		problem = Text('Suppose we have quantum gate, what is the angle of its phaseshift?').shift(DOWN*3).scale(0.5)
		self.play(FadeIn(problem))
		self.wait(3)

		unitary0 = Tex(r"U\ket{\psi} = e^{2\pi i * \theta}\ket{\psi}").shift(UP*1)
		self.play(FadeIn(unitary0))
		self.wait(3)

		unitary = Tex(r"U(a_0\ket{0} + a_1\ket{1}) = a_0\ket{0} + e^{2\pi i * \theta}a_1\ket{1}")
		self.play(FadeIn(unitary))
		self.wait(3)

		unitary2 = Tex(r"U^{2^N}(a_0\ket{0} + a_1\ket{1}) = a_0\ket{0} + e^{2\pi i * \theta * 2^N}a_1\ket{1} ").shift(DOWN*1)
		self.play(FadeIn(unitary2))
		self.wait(3)

		#self.wait(3)

		self.play(FadeOut(Group(problem, unitary, unitary2, unitary0)))


		#explain truncation approximation
		title2 = Text("Quantum Phase Estimation - Circuit").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title2))





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
				qubits.append(qubit(i, 'A', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'B', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'C', ''))
			elif (i == 3):
				qubits.append(qubit(i, r'\psi', ''))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
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

		gates = []
		gates.append( xgate(-4.25, 3) )
		for i in range(0, 3):
			gates.append( hadamard(-4.25, i) )
		for i in range(0, 1):
			gates.append( gCGate(-3.5, 0, 3, r'U_c', PURPLE) )
		for i in range(0, 2):
			gates.append( gCGate(-2.75 + 3*i/4, 1, 3, r'U_c', PURPLE) )
		for i in range(0, 4):
			gates.append( gCGate(-1.25 + 3*i/4, 2, 3, r'U_c', PURPLE) )
		self.play(FadeIn(Group(*gates)))


		qft = qftdag(3, 2, 1.5)
		self.play(FadeIn(qft))

		gatesm = []
		for i in range(0, 3):
			gatesm.append( measure(4.5, i) )
		self.play(FadeIn(Group(*gatesm)))


		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(15)
		while(x < -4.25):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)

		#explain the kickback
		state = Tex(r"U_c\ket{1+} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & e^{2\pi i\theta} \end{bmatrix} \begin{bmatrix} 0 \\ \frac{1}{\sqrt{(2})} \\ 0 \\ \frac{1}{\sqrt{(2})} \end{bmatrix} = \begin{bmatrix} 0 \\ \frac{1}{\sqrt{(2})} \\ 0 \\ \frac{1}{\sqrt{(2})}e^{2\pi i\theta} \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \otimes \begin{bmatrix} \frac{1}{\sqrt{(2})} \\ \frac{1}{\sqrt{(2})}e^{2\pi i\theta} \end{bmatrix} = \ket{1+^\theta}").shift(DOWN*2).scale(0.8)
		self.play(FadeIn(state))
		self.wait(40)
		self.play(FadeOut(state))

		while(x < -4.25 + 0.75*2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^\theta}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)

		for i in range(4, 8):
			while(x < -4.25 + 0.75*i):
				x += 0.05
				self.wait(0.001)
			self.wait(0.5)
			qubits[0].dq = r"\ket{+^\theta}"
			qubits[1].dq = r"\ket{+^{2\theta}}"
			qubits[2].dq = r"\ket{+^{"+ str(i-3) + r"\theta}}"
			qubits[3].dq = r"\ket{1}"
			self.wait(0.5)
		while(x < -4.25 + 0.75*7.75):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^{2^0\theta}}"
		qubits[1].dq = r"\ket{+^{2^1\theta}}"
		qubits[2].dq = r"\ket{+^{2^2\theta}}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)

		self.wait(5)

		

		while(x < 3):
			x += 0.05
			self.wait(0.001)

		rewrite0 = Tex(r"\ket{ABC} = \frac{1}{2^{(N/2})}\bigotimes_{k=0}^{2} \Big( \ket{0} + \omega_{2^N}^{2^N2^k\theta} \ket{1} \Big)").shift(DOWN*2)
		self.play(FadeIn(rewrite0))
		self.wait(15)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(DOWN*1)
		self.play(MoveToTarget(frame, run_time=2.0))

		rewrite1 = Tex(r"\ket{ABC} = \frac{1}{2^{(N/2})}\sum_{k=0}^{2^3-1} \omega_{2^N}^{2^Nk\theta} \ket{k}").shift(DOWN*3.5)
		self.play(FadeIn(rewrite1))
		self.wait(15)

		frame.target.shift(DOWN*3.5)
		self.play(MoveToTarget(frame, run_time=2.0))
		

		qftinv = Tex(r"QFT^\dag(\ket{y}^N) = \frac{1}{2^{(N/2})}\sum_{x=0}^{2^N-1} \omega_{2^N}^{-xy} \ket{x}").shift(DOWN*5)
		self.play(FadeIn(qftinv))
		self.wait(15)

		qftinv2 = Tex(r"QFT^\dag(\ket{ABC}) = \frac{1}{2^N}\sum_{x=0}^{2^N-1}\sum_{k=0}^{2^N-1} \omega_{2^N}^{2^Nk\theta}\omega_{2^N}^{-xk} \ket{x}").shift(DOWN*7)
		self.play(FadeIn(qftinv2))
		self.wait(15)

		frame.target.shift(DOWN*3)
		self.play(MoveToTarget(frame, run_time=2.0))

		qftinv3 = Tex(r"Y = QFT^\dag(\ket{ABC}) = \frac{1}{2^N}\sum_{x=0}^{2^N-1}\sum_{k=0}^{2^N-1} \omega_{2^N}^{k(2^N\theta-x)} \ket{x}").shift(DOWN*9)
		self.play(FadeIn(qftinv3))
		self.wait(15)

		qftinv4 = Tex(r"Max(Y) \to x \pm \epsilon \approx 2^N\theta").shift(DOWN*11)
		self.play(FadeIn(qftinv4))
		self.wait(15)

		frame.target.shift(DOWN*3)
		self.play(MoveToTarget(frame, run_time=2.0))

		qftinv5 = Tex(r"Measure(Y) \to \theta \to \geq \frac{4}{\pi^2} \approx 0.405").shift(DOWN*13)
		self.play(FadeIn(qftinv5))
		self.wait(15)

		self.wait(5)

		frame.target.shift(UP*10.5)
		self.play(MoveToTarget(frame, run_time=2.0))
		thegood = Group(qftinv5, qftinv4, qftinv3, qftinv2, qftinv, rewrite0, rewrite1)
		self.play(FadeOut(thegood))

		title3 = Text("Quantum Phase Estimation - Example").shift(UP*3.5)
		self.play(Transform(title2, title3))

		qubits[0].dq = r"\ket{-}"
		qubits[1].dq = r"\ket{-}"
		qubits[2].dq = r"\ket{-}"
		while(x < 4.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)

		showx = Tex(r"x = 010 \text{ what is } \theta ?").shift(DOWN*0.5)
		self.play(FadeIn(showx))
		self.wait(5)

		showx2 = Tex(r"x = 2 = 2^3 \theta").shift(DOWN*1.5)
		self.play(FadeIn(showx2))
		self.wait(5)

		showx3 = Tex(r"\theta = \frac{1}{4} \to U_c\ket{\psi} = e^{2\pi i \theta}\ket{\psi} = e^{\pi i/2}\ket{\psi}").shift(DOWN*2.5)
		self.play(FadeIn(showx3))

		self.wait(15)

		for i in range(0, 4):
			self.remove(qubits[i].get())
		theobjects= Group(*gates, *gatesm, qft, showx, showx2, showx3)
		self.play(FadeOut(theobjects))




























		#3d example
		#3d visualization, 2 bit fourier transform
		#show 3d rep
		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)
		frame.generate_target()
		frame.target.set_width(20)
		self.play(MoveToTarget(frame))

		
		def qubit3d(xPos, yPos):
			sphere = Sphere(radius = 1, point=ORIGIN, color=RED)
			sphereMesh = SurfaceMesh(sphere, resolution=(7, 7), flat_stroke=True, color=GREY)

			labelpX = Tex(r'\ket{-}').shift(RIGHT*1.5)
			labelrX = Tex(r'\ket{+}').shift(LEFT*1.5)

			labelpY = Tex(r'\ket{-i}').shift(UP*1.5)
			labelrY = Tex(r'\ket{+i}').shift(DOWN*1.5)

			labelpZ = Tex(r'\ket{0}').rotate(PI/2, axis=RIGHT).shift(OUT*1.5)
			labelrZ = Tex(r'\ket{1}').rotate(PI/2, axis=RIGHT).shift(IN*1.5)

			x = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), fill_color=GREY_E, color=GREY_E)
			y = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), fill_color=GREY_E, color=GREY_E)
			z = Line(np.array([0, 0, -1]), np.array([0, 0, 1]), fill_color=GREY_E, color=GREY_E)
		#self.add_fixed_in_frame_mobjects(labelX, labelY, labelZ)
			vect = Vector(direction=[0, 0, 1])
			qubitG1 = Group(sphereMesh, x, y, z, labelpX, labelpY, labelpZ, labelrX, labelrY, labelrZ)
			qubitG1.shift(RIGHT*xPos + UP*yPos)
			return qubitG1
		def vect3d(x, y, direction):
			return Vector(direction=[0, 0, direction]).shift(RIGHT*x + UP*y)
		the3dqubs = []
		the3dqubs.append(qubit3d(-6, 0))
		the3dqubs.append(qubit3d(-2, 0))
		the3dqubs.append(qubit3d(2, 0))
		the3dqubs.append(qubit3d(6, 0))
		
		the3dvects = []
		the3dvects.append(vect3d(-6, 0, 1))
		the3dvects.append(vect3d(-2, 0, 1))
		the3dvects.append(vect3d(2, 0, 1))
		the3dvects.append(vect3d(6, 0, 1))

		self.add(*the3dqubs, *the3dvects)
		frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
		#add vectors
		r = [0, 0, 0, 0]
		s = [0, 0, 0, 0]
		t = [0, 0, 0, 0]
		def update_vect1(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r[0], np.array([1, 0, -1])).rotate_about_origin(s[0], np.array([0, 0, 1])).rotate_about_origin(t[0], np.array([0, -1, 0])).shift(LEFT*6))
		the3dvects[0].add_updater(update_vect1)
		def update_vect2(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r[1], np.array([1, 0, -1])).rotate_about_origin(s[1], np.array([0, 0, 1])).rotate_about_origin(t[1], np.array([1, 0, 0])).shift(LEFT*2))
		the3dvects[1].add_updater(update_vect2)
		def update_vect3(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r[2], np.array([1, 0, -1])).rotate_about_origin(s[2], np.array([0, 0, 1])).rotate_about_origin(t[2], np.array([0, 1, 0])).shift(RIGHT*2))
		the3dvects[2].add_updater(update_vect3)
		def update_vect4(self):
			self.become( Vector(direction=[0, 0, 1]).rotate_about_origin(r[3], np.array([1, 0, -1])).rotate_about_origin(s[3], np.array([0, 0, 1])).rotate_about_origin(t[3], np.array([1, 0, 0])).shift(RIGHT*6) )
		the3dvects[3].add_updater(update_vect4)
		
		def hadamard3d(pos):
			#big H 
			hadamardbro2 = Square(fill_color=YELLOW, fill_opacity=0.1, color=YELLOW).scale(1.5)
			hadamo2 = Text("H", fill_color=BLACK).scale(2.5)
			hadamard2 = Group(hadamardbro2, hadamo2).shift(RIGHT*pos + IN*20)
			hadamard2.generate_target()
			return hadamard2
		def xgate3d(pos):
			#big H 
			hadamardbro2 = Square(fill_color=GREEN, fill_opacity=0.1, color=GREEN).scale(1.5)
			hadamo2 = Text("X", fill_color=BLACK).scale(2.5)
			hadamard2 = Group(hadamardbro2, hadamo2).shift(RIGHT*pos + IN*20)
			hadamard2.generate_target()
			return hadamard2
		def rxGate3d(a,b,n):
			cnot4 = Dot(np.array([a,0,0]), fill_color=RED).scale(3)
			cnot5 = Tex(r"R_"+ str(n)).scale(4).set_color(RED).shift(RIGHT*b)
			cnot6 = Line(np.array([a, 0, 0]), np.array([b, 0, 0]), color=RED)
			hadamardbro2 = Square(fill_color=ORANGE, fill_opacity=0.1, color=ORANGE).scale(1.5).shift(RIGHT*b)
			cnot22 = Group(hadamardbro2, cnot4, cnot5, cnot6).shift(IN*20)
			cnot22.generate_target()
			return cnot22
		def uxGate3d(a,b):
			cnot4 = Dot(np.array([a,0,0]), fill_color=BLACK).scale(3)
			cnot5 = Tex(r"?").scale(4).set_color(BLACK).shift(RIGHT*b)
			cnot6 = Line(np.array([a, 0, 0]), np.array([b, 0, 0]), color=GREY)
			hadamardbro2 = Square(fill_color=GREY, fill_opacity=0.1, color=GREY).scale(1.5).shift(RIGHT*b)
			cnot22 = Group(hadamardbro2, cnot4, cnot5, cnot6).shift(IN*20)
			cnot22.generate_target()
			return cnot22
		def measure3d(pos):
			hadamardbro2 = Square(fill_color=BLUE, fill_opacity=0.1, color=BLUE).scale(1.5)
			hadamo2 = Text("M", fill_color=BLACK).scale(2.5)
			hadamard2 = Group(hadamardbro2, hadamo2).shift(RIGHT*pos + IN*20)
			hadamard2.generate_target()
			return hadamard2
		def qft3d(pos):
			hadamardbro2 = Rectangle(width=8, height=3, fill_color=ORANGE, fill_opacity=0.1, color=ORANGE).scale(1.5)
			hadamo2 = Tex(r"QFT^\dag", fill_color=BLACK).scale(2.5)
			hadamard2 = Group(hadamardbro2, hadamo2).shift(RIGHT*pos + IN*20)
			hadamard2.generate_target()
			return hadamard2
		def moveGate(gate, run=0.5):
			gate.target.shift(OUT*20)
			self.play(MoveToTarget(gate, run_time=run))
		def moveGates(gates, run=0.5):
			newG = Group(*gates)
			newG.generate_target()
			newG.target.shift(OUT*20)
			self.play(MoveToTarget(newG, run_time=run))

		gates3d = []
		gates3du = []
		gates3dm = []
		gateqft = qft3d(-2)

		gates3d.append( hadamard3d(-6) )
		gates3d.append( hadamard3d(-2) )
		gates3d.append( hadamard3d(2) )
		gates3d.append( xgate3d(6) )

		gates3du.append( uxGate3d(-6, 6) )
		gates3du.append( uxGate3d(-2, 6) )
		gates3du.append( uxGate3d(-2, 6) )
		gates3du.append( uxGate3d(2, 6) )
		gates3du.append( uxGate3d(2, 6) )
		gates3du.append( uxGate3d(2, 6) )
		gates3du.append( uxGate3d(2, 6) )

		gates3dm.append( measure3d(-6) )
		gates3dm.append( measure3d(-2) )
		gates3dm.append( measure3d(2) )

		self.add(*gates3d, *gates3du, *gates3dm)
		#APPLY ON QUBIT 1
		moveGates(gates3d, 4)
		while (r[0]<3.14159):
			r[0] += 0.05
			r[1] += 0.05
			r[2] += 0.05
			t[3] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGates(gates3d, 4)

		moveGate(gates3du[0])
		while (s[0]<3.14159/4):
			s[0] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(gates3du[0])

		for i in range(0, 2):
			moveGate(gates3du[i+1])
			while (s[1]<3.14159/4*(i+1)):
				s[1] += 0.05
				frame.increment_theta(0.1*0.015)
				self.wait(0.001)
			moveGate(gates3du[i+1])
		for i in range(0, 4):
			moveGate(gates3du[i+3])
			while (s[2]<3.14159/4*(i+1)):
				s[2] += 0.05
				frame.increment_theta(0.1*0.015)
				self.wait(0.001)
			moveGate(gates3du[i+3])


		moveGate(gateqft, 4)
		while (t[0]>-3.14159/2):
			t[0] -= 0.05
			t[1] -= 0.05
			t[2] += 0.05

			r[0]+=0.004
			r[1]+=0.009
			r[2]-=0.008
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(gateqft, 4)


		moveGates(gates3dm, 4)
		r[0] = 0
		r[1] = 0
		r[2] = 0

		s[0] = 0
		s[1] = 0
		s[2] = 0

		t[0] = 0
		t[1] = 0
		t[2] = 3.14159
		moveGates(gates3dm, 4)

		#show vals
		x0 = Tex(r"x = 001").rotate(PI).shift(DOWN*4)
		x1 = Tex(r"x = 2^3 \theta = 1").rotate(PI).shift(DOWN*3)
		x2 = Tex(r"\theta = \frac{1}{8}").rotate(PI).shift(DOWN*2)
		self.play(FadeIn(x0))
		self.wait(5)
		self.play(FadeIn(x1))
		self.wait(5)
		self.play(FadeIn(x2))
		self.wait(20)












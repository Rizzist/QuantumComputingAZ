from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Circuit: CNOT").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class cnot(Scene):
	def construct(self):
		text = Text("Quantum Circuit: CNOT")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		#qubit circuit

		title = Text("CNOT Gate").shift(UP*3.5)
		self.play(Write(title))

		
		offset = 2
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*1))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*1))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7).add_updater(update_q2)

		l1 = Line(np.array([-5, 0, 0]), np.array([5, 0, 0]))
		l2 = Line(np.array([-5, -offset, 0]), np.array([5, -offset, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,0,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset,0]),fill_color=BLUE))

		qubit1 = Dot(np.array([x,0,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)

		itsg = Group(q1, q2, qubit1, qubit2)
		self.play(FadeIn(itsg), FadeIn(l1), FadeIn(l2))
		#cnot gate
		def update_cnot1(self):
			self.become(Dot(np.array([cx,0,0]), fill_color=RED))
		def update_cnot2(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx).set_color(RED))
		def update_cnot3(self):
			self.become(Line(np.array([cx, 0, 0]), np.array([cx, -offset, 0]), fill_color=RED))
		cx = 0
		cnot1 = Dot(np.array([cx,0,0]), fill_color=RED)
		cnot1.add_updater(update_cnot1)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx)
		cnot2.add_updater(update_cnot2)
		cnot3 = Line(np.array([cx, 0, 0]), np.array([cx, -offset, 0]))
		cnot3.add_updater(update_cnot3)
		cnot = Group(cnot1, cnot2, cnot3)
		self.play(FadeIn(cnot))
		self.wait(3)
		while (x < 5):
			x += 0.025
			self.wait(0.001)

		x = -5
		dq2 = r"\ket{1}"

		while (x < 5):
			x += 0.025
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"

		while (x < 0):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.025
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"

		while (x < 0):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.025
			self.wait(0.001)

		itsmatrix = Tex(r"CNOT = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}").shift(UP*1.7)
		self.play(FadeIn(itsmatrix))
		self.wait(5)
		self.play(FadeOut(itsmatrix))





		#Bell States with Quantum Gates
		title2 = Text("Bell State").shift(UP*3.5)
		self.play(Transform(title, title2))

		while(cx < 1):
			cx += 0.1
			self.wait(0.001)

		hadamardbro = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5)
		hadamo = Text("H", fill_color=BLACK)
		hadamard = Group(hadamardbro, hadamo)
		hadamard.shift(LEFT*1)
		self.play(FadeIn(hadamard))
		self.wait(3)

		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"

		while (x < -1):
			x += 0.025
			self.wait(0.001)
		dq1 = r"\ket{+}"
		while (x < 1):
			x += 0.025
			self.wait(0.001)
		itsmatrix2 = Tex(r"\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} \ket{+0}").shift(UP*1.7).shift(LEFT*4)
		self.play(FadeIn(itsmatrix2))
		self.wait(3)

		itsmatrix3 = Tex(r"\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{(2})} \\ 0 \\ \frac{1}{\sqrt{(2})} \\ 0 \end{bmatrix}").shift(UP*1.7).shift(LEFT*4)
		self.play(Transform(itsmatrix2, itsmatrix3))
		self.wait(3)

		itsmatrix4 = Tex(r"\begin{bmatrix} \frac{1}{\sqrt{(2})} \\ 0 \\ 0 \\ \frac{1}{\sqrt{(2})} \end{bmatrix} = \frac{1}{\sqrt{(2})}\ket{00} + \frac{1}{\sqrt{(2})}\ket{11}").shift(UP*2).shift(LEFT*2)
		dq1 = ""
		dq2 = ""
		self.play(Transform(itsmatrix2, itsmatrix4))
		self.wait(3)
		#dq2 = ""

		measurebro = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.5)
		measa = Text("M", fill_color=BLACK)
		measure = Group(measurebro, measa)
		measure.shift(RIGHT*5)
		self.play(FadeIn(measure))
		while (x < 5):
			x += 0.025
			self.wait(0.001)

		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"

		boxer = SurroundingRectangle(q1).scale(2.2)
		boxer2 = SurroundingRectangle(q2).scale(2.2)
		for i in range(0, 10):
			val = random.randint(0, 1)
			self.play(ShowCreation(boxer), ShowCreation(boxer2))
			dq1 = r"\ket{" + str(val) + "}" 
			dq2 = r"\ket{" + str(val) + "}" 
			self.play(FadeOut(boxer), FadeOut(boxer2))
		self.wait(3)
		notb = Group(hadamard, itsg, cnot, l1, l2, measure, itsmatrix2)
		self.play(FadeOut(notb))
	







		#show entangled blochsphere

		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)

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

		qubitG1 = Group(sphere, sphereMesh, x, y, z, labelpX, labelpY, labelpZ, labelrX, labelrY, labelrZ)
		qubitG1.shift(LEFT*2)
		self.play(ShowCreation(sphereMesh), FadeIn(labelpX), FadeIn(labelpY), FadeIn(labelpZ), FadeIn(labelrX), FadeIn(labelrY), FadeIn(labelrZ), FadeIn(x), FadeIn(y), FadeIn(z))

		


		sphere2 = Sphere(radius = 1, point=ORIGIN, color=RED)
		sphereMesh2 = SurfaceMesh(sphere2, resolution=(7, 7), flat_stroke=True, color=GREY)

		labelpX2 = Tex(r'\ket{-}').shift(RIGHT*1.5)
		labelrX2 = Tex(r'\ket{+}').shift(LEFT*1.5)

		labelpY2 = Tex(r'\ket{-i}').shift(UP*1.5)
		labelrY2 = Tex(r'\ket{+i}').shift(DOWN*1.5)

		labelpZ2 = Tex(r'\ket{0}').rotate(PI/2, axis=RIGHT).shift(OUT*1.5)
		labelrZ2 = Tex(r'\ket{1}').rotate(PI/2, axis=RIGHT).shift(IN*1.5)

		x2 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), fill_color=GREY_E, color=GREY_E)
		y2 = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), fill_color=GREY_E, color=GREY_E)
		z2 = Line(np.array([0, 0, -1]), np.array([0, 0, 1]), fill_color=GREY_E, color=GREY_E)
		#self.add_fixed_in_frame_mobjects(labelX, labelY, labelZ)

		qubitG2 = Group(sphere2, sphereMesh2, x2, y2, z2, labelpX2, labelpY2, labelpZ2, labelrX2, labelrY2, labelrZ2)
		qubitG2.shift(RIGHT*2)
		self.play(ShowCreation(sphereMesh2), FadeIn(labelpX2), FadeIn(labelpY2), FadeIn(labelpZ2), FadeIn(labelrX2), FadeIn(labelrY2), FadeIn(labelrZ2), FadeIn(x2), FadeIn(y2), FadeIn(z2))

		frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
		#add vectors
		vectL = Vector(direction=[0, 0, 1]).shift(LEFT*2)
		vectR = Vector(direction=[0, 0, 1]).shift(RIGHT*2)
		self.play(FadeIn(vectL), FadeIn(vectR))

		#big H 
		hadamardbro2 = Square(fill_color=YELLOW, fill_opacity=0.1, color=YELLOW).scale(2)
		hadamo2 = Text("H", fill_color=BLACK).scale(2.5)
		hadamard2 = Group(hadamardbro2, hadamo2)
		hadamard2.shift(LEFT*2 + IN*10)
		self.add(hadamard2)

		hadamard2.generate_target()
		hadamard2.target.shift(OUT*10)
		r = 0
		def update_vectL(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r, np.array([1, 0, -1])).shift(LEFT*2))
		vectL.add_updater(update_vectL)

		self.play(MoveToTarget(hadamard2, run_time=3))

		while (r<3.14159):
			r += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		hadamard2.generate_target()
		hadamard2.target.shift(OUT*10)
		self.play(MoveToTarget(hadamard2, run_time=3))


		self.play(FadeOut(labelrX2), FadeOut(labelpX))
		#cnot gate
		offset = 2
		cx = 0
		cnot4 = Dot(np.array([-offset,0,0]), fill_color=RED).scale(3)
		cnot5 = Tex(r"\otimes").scale(4).set_color(RED).shift(RIGHT*offset)
		cnot6 = Line(np.array([-offset, 0, 0]), np.array([offset, 0, 0]), color=RED)
		cnot22 = Group(cnot4, cnot5, cnot6)
		cnot22.shift(IN*10)
		cnot22.generate_target()
		cnot22.target.shift(OUT*10)
		self.add(cnot22)
		self.play(MoveToTarget(cnot22, run_time=3))

		#apply connections
		def update_conn(self):
			self.become(Line(vectL.get_end(), vectR.get_end(), fill_color=RED_E, color=RED_E))
		conn = Line(vectL.get_end(), vectR.get_end(), fill_color=RED_E, color=RED_E)
		conn.add_updater(update_conn)
		self.play(ShowCreation(conn))
		r2 = 3.14159
		def update_vectR(self):
			self.become(Vector(direction=[0, 0, 1], fill_color=GREEN).scale(r2)).shift(RIGHT*2)
		vectR.add_updater(update_vectR)
		def update_vectL2(self):
			self.become(Vector(direction=[-1, 0, 0], fill_color=GREEN).shift(LEFT*2))
		vectL.remove_updater(update_vectL)
		vectL.add_updater(update_vectL2)
		while (r2>0):
			r2 -= 0.05
			frame.increment_theta(0.1*0.02)
			self.wait(0.001)
		vectL.remove_updater(update_vectL2)
		vectR.remove_updater(update_vectR)
		vectR = Dot(np.array([2,0,0]), fill_color=RED)
		cnot22.target.shift(OUT*10)
		self.add(cnot22)
		self.play(MoveToTarget(cnot22, run_time=3))

		measurebro2 = Square(fill_color=BLUE, fill_opacity=0.1, color=BLUE).scale(2)
		meas2 = Text("M", fill_color=BLACK).scale(2.5)
		measure2 = Group(measurebro2, meas2)
		z = -10
		measure2.shift(LEFT*2 + OUT*z)
		self.add(measure2)
		def update_measure(self):
			self.become(measure2.move_to(LEFT*2 + OUT*z))
		measure2.add_updater(update_measure)

		vectL.generate_target()
		vectR.generate_target()
		for i in range(0, 10):
			z = -10
			tested=False
			vectL.target = Vector(direction=[-1, 0, 0], fill_color=GREEN).shift(LEFT*2)
			vectR.target = Dot(np.array([2,0,0]), fill_color=RED)
			self.play(MoveToTarget(vectL, run_time=0.01))
			self.play(MoveToTarget(vectR, run_time=0.01))
			while(z < 10):
				z += 0.1
				frame.increment_theta(0.1*0.02)
				self.wait(0.001)
				if (z >= 0 and tested==False):
					q = 2*random.randint(0, 1) - 1
					vectL.target = Vector(direction=[0, 0, q], fill_color=GREEN).shift(LEFT*2)
					vectR.target = Vector(direction=[0, 0, q], fill_color=GREEN).shift(RIGHT*2)
					self.play(MoveToTarget(vectL, run_time=0.01))
					self.play(MoveToTarget(vectR, run_time=0.01))
					tested= True
			

		self.wait(12)





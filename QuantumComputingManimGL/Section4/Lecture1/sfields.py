from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Photonics & QuModes").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class sfields(Scene):
	def construct(self):
		text = Text("Quantum Photonics & QuModes").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("Qubits vs QuModes").shift(UP*3.5)
		self.play(FadeIn(title))


		stuff = []
		stuff.append( Tex(r"\ket{\psi} = a\ket{0} + b\ket{1} = \sum_{x=0}^n a_x\ket{x}").shift(UP*1) )
		stuff.append( Tex(r"\ket{\psi} = \int \psi (x)\ket{x}dx").shift(DOWN*1) )

		for i in stuff:
			self.play(FadeIn(i))
			self.wait(4)

		for i in stuff:
			self.play(FadeOut(i))



		#3d
		toanalyse = Tex(r"\ket{\psi} = \int \psi (x)\ket{x}dx").shift(DOWN*2)
		self.play(FadeIn(toanalyse))

		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(FadeIn(Group(axes, grid)))
		labelX = Tex(r"\ket{x}").shift(RIGHT*4.5)
		labelY = Tex(r"\ket{p}").shift(UP*2.75)
		self.play(FadeIn(Group(labelX, labelY)))

		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)
		#frame.generate_target()
		#frame.target.set_width(20)
		#self.play(MoveToTarget(frame))
	
		a = 0
		b = 0
		def update_dot(self):
			self.become( Dot(np.array([a,b,0]), fill_color=RED) )
		
		cval = Dot(np.array([a,b,0]), fill_color=RED)
		self.play(FadeIn(cval))
		cval.add_updater(update_dot)
		t = np.pi/2
		
		for i in range(500):
			t += 0.01
			a = 2*np.sin(t + np.pi/2)
			b = 2*np.sin(2*t)
			self.wait(0.0001)
		
		while(a > 1):
			a -= 0.1
			self.wait(0.0001)
		a = 1
		while (b > 0):
			b -= 0.1
			self.wait(0.0001)
		b = 0
		
	
		def spin(m, dt):
			m.increment_theta(0.1 * dt)
		frame.add_updater(spin)
	
		self.wait(4)

		toanalyse2 = Tex(r"1 = \int \psi (0)\ket{0}dx = \int \psi (0)\begin{bmatrix} 1 \\ 0 \end{bmatrix} dx").shift(DOWN*2)
		self.play(Transform(toanalyse, toanalyse2))
		self.wait(4)

		integralr = Line(np.array([1, 0, 0]), np.array([1, 0, 1.3]), color=GREEN)
		self.play(FadeIn(integralr))

		self.wait(2)
		toanalyse3 = Tex(r"\ket{\psi} = \int \psi (x)\ket{x}dx").shift(DOWN*3.5)
		self.play(Transform(toanalyse, toanalyse3))

		
		# Gauss surface
		op = np.matrix([[1, 0], [0, 1]])
		dispop = np.exp(op)
		gaussian = ParametricSurface(
			lambda u, v: [u, v, np.absolute(np.linalg.det(np.exp(    -1*np.matrix([u, v])*op*np.transpose(np.matrix([u, v]))     ) ))],#np.exp(-(u**2) - v**2)],
			u_range=(-5, 5),
			v_range=(-2.5, 2.5),
			resolution=(90, 90),
		)
		gaussian.set_color(GREEN, 1).shift(RIGHT*1)
		gaussian.stretch(2, 2)
		self.play(
			FadeIn(gaussian),
			frame.set_phi, 70 * DEGREES,
			frame.set_theta, 10 * DEGREES,
			run_time=3
		)
		self.wait(5)
		self.play(
			frame.increment_phi, -20 * DEGREES,
			frame.set_theta, -120 * DEGREES,
			run_time=2
		)
		title2 = Text("QuModes - Vacuum State").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.wait(15)
		


		gaussian.generate_target()
		gaussian.target.stretch(0.5, 0)
		gaussian.target.set_color(RED)
		self.play(MoveToTarget(gaussian))
		title3 = Text("QuModes - Squeezed State").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title3))
		self.wait(15)

		self.play(Rotating(gaussian, np.pi/2, run_time=2 ) ) 
		title4 = Text("QuModes - Rotation").shift(UP*3.5)
		self.play(Transform(title3, title4))
		self.wait(5)

		gaussian.target.shift(LEFT*3+ DOWN*1)
		self.play(MoveToTarget(gaussian))
		title5 = Text("QuModes - Displacement").shift(UP*3.5)
		self.play(Transform(title3, title5))
		self.wait(5)





		self.play(FadeOut(Group(gaussian)))#, cval, integralr)))
	
		# Gauss surface
		
		theta = 0.1*62.8
		op = np.matrix([[np.cos(theta), 1j*np.sin(theta)], [1j*np.sin(theta), -np.cos(theta)]])
		gaussianc = ParametricSurface(
			lambda u, v: [u, v, np.imag(np.linalg.det(np.exp(1j*np.matrix([u, v])*op*np.matrix([[u, 0], [0, v]])*np.transpose(np.matrix([u, v])) ) )) ],#np.exp(-1j*(u**3) -1j*(v**3) )],
			u_range=(-2, 2),
			v_range=(-2, 2),
			resolution=(50, 50),
		)
		gaussianc.set_color(GREEN, 1)#.shift(RIGHT*1)
		self.play(FadeIn(gaussianc))
		self.wait(0.0001)

		title6 = Text("QuModes - Cubic Phase").shift(UP*3.5)
		self.play(Transform(title3, title6))
		self.wait(30)
		"""
		self.play(FadeOut(Group(axes, grid, toanalyse, labelX, labelY, gaussianc)))
		frame.remove_updater(spin)
		frame.target.set_euler_angles(
			theta=0 * DEGREES,
			phi=0 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		self.wait(10)
		"""









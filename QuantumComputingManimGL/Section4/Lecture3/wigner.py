from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Wigner Function & Photonic Measurement").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class wigner(Scene):
	def construct(self):
		text = Text("Fock States, Wigner Function, Photonic Measurement").scale(0.7)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Fock States").shift(UP*3.5)
		self.play(FadeIn(title))
		
		stuff = []
		#stuff.append( Tex(r"").shift(UP*0) )
		stuff.append( Tex(r"F_k = \ket{n_1, n_2, n_3, ..., n_k} \to \text{Occupation Num. Representation}").shift(UP*3) )
		stuff.append( Tex(r"\ket{1, 0, ..., 0} \to \ket{0, 1, ..., 0} \text{Property of Bosons, Symmetric}").shift(UP*2.5) )
		stuff.append( Tex(r"N = \sum n_i").shift(UP*1.75 + LEFT*3) )
		stuff.append( Tex(r"F_1 = \ket{n_1} \to F_2 = \ket{n_1, n_2}").shift(UP*1.75 + RIGHT*3) )
		stuff.append( Tex(r"F = F_0 \bigoplus F_1 \bigoplus F_2 \bigoplus F_3 \bigoplus ...").shift(UP*1) )
		stuff.append( Tex(r"\text{Direct sum of Vector Spaces, Dimensions Add}").shift(UP*0.25) )
		stuff.append( Tex(r"\ket{0} + \ket{1} + \ket{2, 0} + \ket{1, 1}").shift(DOWN*0.5 + UP*0.25) )
		stuff.append( Tex(r"a_i^\dag\ket{n_1, ..., n_k} = \sqrt{n_i+1}\ket{n_1,..., (n_i+1),..., n_k}").shift(DOWN*1 + UP*0.25).scale(0.9) )
		stuff.append( Tex(r"a_i\ket{n_1, ..., n_k} = \sqrt{n_i}\ket{n_1,..., (n_i-1),..., n_k}").shift(DOWN*1.5 + UP*0.25).scale(0.9) )
		stuff.append( Tex(r"a_i^\dag a_i\ket{n_i} = a_i^\dag\sqrt{n_i}\ket{n_i-1} = \sqrt{n_i - 1 + 1}\sqrt{n_i}\ket{n_i-1 + 1} = n_i\ket{n_i}").shift(DOWN*2 + UP*0.125).scale(0.9) )
		stuff.append( Tex(r"\hat{n} = a_i^\dag a_i \to \text{Occupation Number Operator}").shift(DOWN*2.5).scale(0.9)  )
		stuff.append( Tex(r"\bar{n} = Tr(\hat{p}\hat{n}) \to \text{Mean Photon Number}").shift(DOWN*3).scale(0.9)  )
		stuff.append( Tex(r"\text{Fock States have no Information on Phase!}").shift(DOWN*3.5) )

		for i in stuff:
			self.play(FadeIn(i))
			self.wait(10)
		self.play(FadeOut(Group(*stuff)))
		



		#camera
		frame = self.camera.frame
		self.play(frame.increment_phi, 50 * DEGREES, frame.increment_theta, -30 * DEGREES, run_time=2 ) 
		def spin(m, dt):
			m.increment_theta(0.1 * dt)
		frame.add_updater(spin)
		#axes
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		labelX = Tex(r"\ket{x}").shift(RIGHT*4.5)
		labelY = Tex(r"\ket{p}").shift(UP*2.75)
		self.play(FadeIn(Group(axes, grid, labelX, labelY)))
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
		self.play(FadeIn(gaussian), frame.set_phi, 70 * DEGREES, frame.set_theta, 10 * DEGREES, run_time=3 ) 
		self.wait(5)
		self.play(frame.increment_phi, -20 * DEGREES, frame.set_theta, -120 * DEGREES, run_time=2 )


		quadop = np.matrix([[1, 0], [0, 1]])
		linop = np.matrix([[0, 0]])
		gaussian2 = ParametricSurface(
			lambda u, v: [u, v, (0 if (u**2 + v**2 - 5) > 0 else -1) * np.real(np.exp( -1j*np.matrix([u, v])*quadop*np.transpose(np.matrix([u, v])) - 1*np.matrix([u, v])*np.transpose(linop)))  ],#np.exp(-(u**2) - v**2)],
			u_range=(-5, 5),
			v_range=(-2.5, 2.5),
			resolution=(90, 90),
		)

		self.play(Transform(gaussian, gaussian2))
		self.wait(10)
		gaussian3 = ParametricSurface(
			lambda u, v: [u, v, (0 if (u**2 + v**2 - 15) > 0 else 1) * np.real(np.exp( -1j*np.matrix([u, v])*quadop*np.transpose(np.matrix([u, v])) - 1*np.matrix([u, v])*np.transpose(linop)))  ],#np.exp(-(u**2) - v**2)],
			u_range=(-5, 5),
			v_range=(-5, 5),
			resolution=(90, 90),
		)
		gaussian3.set_color(RED, 1)
		gaussian3.stretch(0.5, 0)
		gaussian3.stretch(0.5, 1)

		self.play(Transform(gaussian, gaussian3))
		self.wait(10)
		self.play(FadeOut(Group(gaussian, axes, grid, labelX, labelY)))
		frame.remove_updater(spin)
		frame.target.set_euler_angles(
			theta=-6 * DEGREES,
			phi=0 * DEGREES,
		)
		self.play(MoveToTarget(frame))


		title2 = Text("Constructing Wigner Function").shift(UP*3.5).scale(0.9)
		self.play(Transform(title, title2))
	
		stuffw = []
		stuffw.append( Tex(r"\vec{b} = \begin{bmatrix} \hat{a}_1 & \hat{a}_1^\dag & \hat{a}_2 & \hat{a}_2^\dag \end{bmatrix}^T").shift(UP*2.5 + UP*0.3) )
		stuffw.append( Tex(r"[b_i, b_j] = \Omega_{ij} \to \text{Photon is a Boson, Symplectic Matrix}").shift(UP*1.6 + UP*0.3) )
		stuffw.append( Tex(r"\Omega_{ij} = \bigoplus_{i=1}^n \omega = \begin{bmatrix} \omega & 0 \\ 0 & \omega \end{bmatrix}").shift(UP*0.5 + UP*0.3 + LEFT*3) )
		stuffw.append( Tex(r"\omega = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}").shift(UP*0.5 + UP*0.3 + RIGHT*3) )
		#stuff.append( Tex(r"[b_i, b_j] = \Omega_{ij}").shift(UP*3) )
		stuffw.append( Tex(r"D(x, q) = e^{i\hat{x}^T\Omega q} \to q \in \mathbb{R}^{2n} \to \text{Weyl Displacement Operator}").shift(DOWN*0.75 + UP*0.3) )
		stuffw.append( Tex(r"\chi (x, q) = Tr(\hat{p} D(x, q)) \to \text{Exp. Val of Weyl Op.}").shift(DOWN*1.5 + UP*0.3))
		stuffw.append( Tex(r"W(x) = \int D(x, q) \chi (x, q) dq \to \text{Wigner Function}").shift(DOWN*2.325 + UP*0.2) )
		stuffw.append( Text("Wigner Function is a Quasiprobability Distribution").shift(DOWN*3.25).scale(0.7) )

		for i in stuffw:
			self.play(FadeIn(i))
			self.wait(10)
		self.play(FadeOut(Group(*stuffw)))
	
		title2 = Text("Continuous Variable Measurements").shift(UP*3.5).scale(0.9)
		self.play(Transform(title, title2))
		stuff2 = []
		stuff2.append( Text("Homodyne Measurement").shift(UP*2.75).scale(0.8) )
		stuff2.append( Tex(r"E(t) = X(t)cos(\omega t) + Y(t)sin(\omega t)").shift(UP*2) )
		stuff2.append( Tex(r"\langle cos(\omega t) | E(t)\rangle = X").shift(UP*1.25) )
		stuff2.append( Tex(r"\langle sin(\omega t) | E(t)\rangle = Y").shift(UP*0.5) )
		stuff2.append( Text("Measure 1 Component with Certainty").shift(UP*0).scale(0.5) )
		stuff2.append( Text("Heterodyne Measurement").shift(DOWN*1) )
		stuff2.append( Text("Simultaneously Measure 2 Components, with Uncertainty").shift(DOWN*2).scale(0.7) )
		stuff2.append( Text("Heisenberg Uncertainty Principle").shift(DOWN*3).scale(0.7) )

		for i in stuff2:
			self.play(FadeIn(i))
			self.wait(5)
		self.play(FadeOut(Group(*stuff2)))

		stuff3 = []
		stuff3.append( Text("Photon Counting").shift(UP*2.5) )
		stuff3.append( Text("Count # of Photons").shift(UP*1.5) )
		stuff3.append( Text("Used to Implement Non-Gaussian States").shift(UP*0.5) )

		for i in stuff3:
			self.play(FadeIn(i))
			self.wait(3)
		self.wait(10)
		#self.play(FadeOut(Group(*stuff2)))









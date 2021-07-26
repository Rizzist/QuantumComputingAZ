from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Projection, Expectation Value, Singular Value Decomposition (SVD)").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class proj(Scene):
	def construct(self):
		text = Text("Projection, Expectation Value, Singular Value Decomposition (SVD)").scale(0.7)
		self.play(FadeIn(text))
		self.wait(6)
		self.play(FadeOut(text))

		title = Text("Projection").shift(UP*3.5)
		self.play(Write(title))
		
		#show projection
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(ShowCreation(axes))  
		self.play(ShowCreation(grid))   
		self.wait(1)
		x = 0
		a = np.sin(x)
		b = np.cos(x)
		vector = Vector(direction=[a,b,0])
		vectorX = Vector(direction=[a, 0,0], fill_color=RED)
		
		self.add(vectorX) 
		self.add(vector)
		def update_vector(self):
			self.become(Vector(direction=[a,b,0]))
		def update_vectorX(self):
			self.become(Vector(direction=[a, 0,0], fill_color=RED))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		#self.play(ShowCreation(sphere),ShowCreation(garis),ShowCreation(axes))
		self.wait(2)
		while(x<3.5*2):
			x+=0.03
			a = np.sin(x)
			b = np.cos(x)
			self.wait(0.0001)
		dline = DashedLine(vector.get_end(), vectorX.get_end(), color=YELLOW)
		self.play(ShowCreation(dline))

		vector.generate_target()
		vector.target = Vector(vectorX.get_end())
		vector.remove_updater(update_vector)
		self.remove(vector)
		self.add(vector)
		self.play(MoveToTarget(vector))
		self.wait(3)
		pmatrix = Tex(r"P_x\vec{v} = \vec{v_x}").shift(LEFT*3.5 + UP)
		self.play(FadeIn(pmatrix))
		self.wait(3)
		pmatrix2 = Tex(r"P_x(P_x\vec{v}) = P_x(\vec{v_x})").shift(LEFT*3.5 + UP)
		self.play(Transform(pmatrix, pmatrix2))
		self.wait(3)
		pmatrix3 = Tex(r"P_x(P_x\vec{v}) = P_x(\vec{v_x}) = \hat{\vec{v_x}}").shift(LEFT*3.5 + UP)
		self.play(Transform(pmatrix, pmatrix3))
		self.wait(3)
		pmatrix11 = Tex(r"P^2 = P").shift(RIGHT*3 + UP)
		self.play(FadeIn(pmatrix11))
		self.wait(3)
		pmatrix22 = Tex(r"P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}").shift(DOWN*2)
		self.play(FadeIn(pmatrix22))

		self.wait(5)
		axesG = Group(grid, vector, vectorX, dline, pmatrix, pmatrix11, pmatrix22)
		self.play(FadeOut(axesG))

		frame = self.camera.frame
		frame.generate_target()
		frame.target.set_euler_angles(
			theta=-40 * DEGREES,
			phi=40 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		def spin(m, dt):
			m.increment_theta(-0.1 * dt)
		frame.add_updater(spin)

		#show 3d projection
		curve1=ParametricCurve(
				lambda u : np.array([
				1*np.cos(u),
				1*np.sin(u),
				u/2
			]),color=RED,t_min=-TAU,t_max=TAU,
			)
		self.play(ShowCreation(curve1))
		self.wait(3)
		curveForm = Tex(r"G_v = \begin{bmatrix} \sin{t} \\ \cos{t} \\ t \end{bmatrix}").rotate(3*PI/2).shift(UP*2 + RIGHT*2)
		self.play(FadeIn(curveForm))
		self.wait(5)
		curve2 = ParametricCurve(
				lambda u : np.array([
				1*np.cos(u),
				1*np.sin(u),
				0
			]),color=RED,t_min=-TAU,t_max=TAU,
			)
		self.play(Transform(curve1, curve2))
		self.wait(3)
		curveForm2 = Tex(r"P_{xy}G_v = \begin{bmatrix} \sin{t} \\ \cos{t} \\ 0 \end{bmatrix}").rotate(3*PI/2).shift(DOWN*2 + RIGHT*2)
		self.play(FadeIn(curveForm2))
		self.wait(3)
		curveForm3 = Tex(r"P_{xy} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}").rotate(PI).shift(DOWN*2 + LEFT*2)
		self.play(FadeIn(curveForm3))
		self.wait(3)
		taxesG = Group(axes, curveForm, curveForm2, curveForm3, curve1)
		self.play(FadeOut(taxesG))

		frame.remove_updater(spin)
		frame.target.set_euler_angles(
			theta=0 * DEGREES,
			phi=0 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		
		#show math of projection + inner product in qubits
		itsareal = Tex(r"\vec{v} = a_0\ket{0} + a_1\ket{1}").shift(DOWN*3)
		self.play(FadeIn(itsareal))
		self.wait(3)
		poperator = Tex(r"P\vec{v} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\vec{v} = a_0\ket{0}").shift(LEFT*3)
		self.play(FadeIn(poperator))
		self.wait(3)
		itslength = Tex(r"Length = \sqrt{\sum_{i=1}^{n} a_i^2}").shift(RIGHT*4 + UP*1)
		self.play(FadeIn(itslength))
		self.wait(3)
		vectlength = Tex(r"\widehat{(\mid \vec{v} \mid)}^2 = Length^2 = \sum_{i=0}^{n}(a_i)^2").shift(LEFT*3 + DOWN*2)
		self.play(FadeIn(vectlength))

		self.wait(6)

		iitsareal2 = Tex(r"\ket{v} = a_0\ket{0} + a_1\ket{1}").shift(DOWN*3)
		self.play(Transform(itsareal, iitsareal2))
		self.wait(5)
		poperator2 = Tex(r"P\ket{v} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\ket{v} = a_0\ket{0}").shift(LEFT*3)
		self.play(Transform(poperator, poperator2))
		itslength2 = Tex(r"1 = Length^2 = \sum_{i=1}^{n} a_i^*a_i").shift(RIGHT*4+ UP*1)
		self.play(Transform(itslength, itslength2))
		vectlength2 = Tex(r"\widehat{(\mid \ket{v}\mid)}^2 = Length^2 = \sum_{i=0}^{n}(a_i)^2").shift(LEFT*3 + DOWN*1.5)
		self.play(Transform(vectlength, vectlength2))
		self.wait(3)
		#perform changes
		vectlength3 = Tex(r"\braket{v} = Length^2 = \sum_{i=0}^{n}a_i^*a_i = 1").shift(LEFT*2.5 + DOWN*1.5)
		self.play(Transform(vectlength, vectlength3))
		self.wait(7)
		poperator3 = Tex(r"\bra{v}P\ket{v} = \bra{v}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\ket{v} = (a_0\ket{0})^\dag a_0\ket{0}").shift(LEFT*2.5)
		self.play(Transform(poperator, poperator3))
		self.wait(7)
		poperator4 = Tex(r"\bra{v}P\ket{v} = \bra{v}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\ket{v} =  a_0^*a_0\braket{0}").shift(LEFT*2.5)
		self.play(FadeOut(poperator), FadeIn(poperator4))
		self.wait(3)
		poperator5 = Tex(r"\bra{v}P\ket{v} = \bra{v}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\ket{v} =  a_0^*a_0").shift(LEFT*2.5)
		self.play(Transform(poperator4, poperator5))

		self.wait(8)

		poperator8 = Tex(r"\bra{v}P\ket{v} = \bra{v} \ket{0}\bra{0} \ket{v} \in \mathbb{R}").shift(LEFT*3)
		self.play(FadeOut(poperator4), FadeIn(poperator8))
		self.wait(8)

		poperator42 = Tex(r"P = \ket{0}\bra{0}").shift(LEFT*3 + UP*2)
		self.play(FadeIn(poperator42))
		self.wait(5)

		poperator43 = Tex(r"P^2 = \ket{0} \bra{0} \ket{0} \bra{0}").shift(UP*2 + RIGHT*2)
		self.play(FadeIn(poperator43))
		self.wait(3)
		poperator44 = Tex(r"P^2 = \ket{0}(\bra{0}\ket{0})\bra{0}").shift(UP*2+ RIGHT*2)
		self.play(Transform(poperator43, poperator44))
		self.wait(3)
		poperator45 = Tex(r"P^2 = \ket{0}\bra{0} = P").shift(UP*2+ RIGHT*2)
		self.play(Transform(poperator43, poperator45))


		self.wait(8)
		poperator4k = Tex(r"\bra{v}x\ket{v} = \langle x \rangle").shift(LEFT*3)
		self.play(FadeOut(poperator8), FadeIn(poperator4k))
		self.wait(3)

		title2 = Text("Expectation Value").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.wait(2)

		projgroup = Group(poperator42, poperator4k, vectlength, itslength, itsareal, poperator43)
		self.play(FadeOut(projgroup))

		#explain expectation
		expect = Tex(r"E(A) = \sum_{i=0}^{n} a_ip(a_i)").shift(DOWN*3)
		self.play(FadeIn(expect))
		self.wait(8)

		itsfair = Text(r"Fair: 50% 0 or 1").scale(0.8).shift(UP*2)
		self.play(FadeIn(itsfair))
		self.wait(5)

		itse = Tex(r"E(C) = 0 * p(0) + 1 * p(1)")
		self.play(Write(itse))
		self.wait(3)

		itse2 = Tex(r"E(C) = 0 * 0.5+ 1 * 0.5")
		self.play(Transform(itse, itse2))
		self.wait(3)

		itse3 = Tex(r"E(C) = 0.5")
		self.play(Transform(itse, itse3))
		self.wait(3)

		exG = Group(expect, itsfair, itse)
		self.play(FadeOut(exG))
		self.wait(3)

		#SVD Matrix
		title2 = Text("Singular Value Decomposition").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.wait(3)

		spectral = Tex(r"A = PDP^{-1}").shift(UP*2)
		self.play(FadeIn(spectral))
		self.wait(3)

		itsnn = Text("n x n").shift(UP*1 + LEFT*1).scale(0.5)
		self.play(FadeIn(itsnn))
		itsnn2 = Text("n x m").shift(UP*1 + LEFT*1).scale(0.5)
		self.play(Transform(itsnn, itsnn2))
		self.wait(3)
		self.play(FadeOut(itsnn))

		spectral2 = Tex(r"A^TA = VDV^{-1}").shift(LEFT*3 + UP*2)
		self.play(Transform(spectral, spectral2))
		self.wait(5)

		spectral22 = Tex(r"AA^T = UDU^{-1}").shift(RIGHT*3 + UP*2)
		self.play(FadeIn(spectral22))
		self.wait(8)
		resultdesired = Tex(r"A\vec{v} = \sigma \vec{u}")
		self.play(FadeIn(resultdesired))
		self.wait(6)
		qdesired = Tex(r"AV = U \Sigma").shift(DOWN*1.5)
		self.play(Write(qdesired))
		self.wait(6)
		qtotal = Tex(r"A = U \Sigma V^{-1}").shift(DOWN*2.5)
		self.play(Write(qtotal))
		self.wait(6)
		qtotal2 = Tex(r"A = U \Sigma V^\dag").shift(DOWN*2.5)
		self.play(Transform(qtotal, qtotal2))

		self.wait(3)
		spectral3 = Tex(r"A^TA = (U \Sigma V^\dag)^T(U \Sigma V^\dag)").shift(LEFT*3 + UP*2)
		self.play(Transform(spectral, spectral3))
		self.wait(3)
		spectral4 = Tex(r"A^TA = (V \Sigma^T U^\dag)(U \Sigma V^\dag)").shift(LEFT*3 + UP*2)
		self.play(Transform(spectral, spectral4))
		self.wait(3)
		spectral5 = Tex(r"A^TA = V \Sigma^T (U^\dag U) \Sigma V^\dag").shift(LEFT*3 + UP*2)
		self.play(Transform(spectral, spectral5))
		self.wait(3)
		spectral6 = Tex(r"A^TA = V \Sigma^T \Sigma V^\dag").shift(LEFT*3 + UP*2)
		self.play(Transform(spectral, spectral6))
		self.wait(3)

		spectral23 = Tex(r"D = \Sigma^2").shift(RIGHT*3 + UP*2)
		self.play(Transform(spectral22, spectral23))
		self.wait(3)

		almostgroup = Group(spectral22, spectral, qdesired, resultdesired)
		self.play(FadeOut(almostgroup))

		self.play(FadeIn(axes), FadeIn(grid))
		newgeom = Square()
		self.play(FadeIn(newgeom))
		self.wait(6)
		self.play(Rotate(newgeom, PI/4))
		self.wait(6)
		mat = [[1.0, 0], [1.0, 1.5]]
		self.play(ApplyMatrix(mat, newgeom))
		self.wait(6)
		self.play(Rotate(newgeom, 3 * PI/16))
		self.wait(20)
















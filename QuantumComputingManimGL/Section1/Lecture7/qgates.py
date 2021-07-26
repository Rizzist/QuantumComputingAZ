from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Gates: Hadamard, Pauli Matrices, Phase Shifts").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class qbro(Scene):
	def construct(self):
		text = Text("Quantum Gates: Hadamard, Pauli Matrices, Phase Shifts").scale(0.8)
		self.play(FadeIn(text))
		self.wait(7)
		self.play(FadeOut(text))

		Title = Text("Hilbert Basis Vectors").shift(UP*3.5)
		self.play(FadeIn(Title))
		self.wait(1)

		tryit = Tex(r"\ket{\psi} = a_1\begin{bmatrix} 1 \\ 0  \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1  \end{bmatrix}")
		self.play(Write(tryit))
		self.wait(5)

		basis = Tex(r"\ket{0} = \begin{bmatrix} 1\\ 0 \end{bmatrix}  \quad  \ket{1} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(DOWN*2)
		self.play(Write(basis))
		self.wait(5)

		tryit2 = Tex(r"\ket{\psi} = a_1\ket{0} + a_2\ket{1}")
		self.play(Transform(tryit, tryit2))
		self.wait(6)

		basis2 = Tex(r"\ket{+} = \frac{1}{\sqrt{(2})}\begin{bmatrix} 1\\ 1 \end{bmatrix}  \quad  \ket{-} = \frac{1}{\sqrt{(2})}\begin{bmatrix} 1 \\ -1 \end{bmatrix}").shift(DOWN*2)
		self.play(Transform(basis, basis2))
		self.wait(4)

		tryit3 = Tex(r"\ket{\psi} = a_1\ket{0} + a_2\ket{1} = a_3\ket{+} + a_4\ket{-}")
		self.play(Transform(tryit, tryit3))
		self.wait(6)

		baka = Tex(r"\ket{1}\otimes\ket{0} = \ket{10} = \begin{bmatrix} 0\\ 0\\1\\0 \end{bmatrix}").shift(UP*1.75)
		self.play(FadeIn(baka))
		self.wait(15)

		self.play(FadeOut(tryit), FadeOut(basis), FadeOut(baka))
		
		#Show Hadamard Gate
		Title2 = Text("Hadamard Gate").shift(UP*3.5)
		self.play(Transform(Title, Title2))
		self.wait(2)
		qgate = Square(1, color=YELLOW)
		qgateT = Text("H")

		#setup qubit and hadamard gate
		x = -3
		def update_qubit(self):
			self.become(Dot(np.array([x,-3,0]),fill_color=BLUE))
		qubit = Dot(np.array([x,-3,0]), fill_color=BLUE)
		qubit.add_updater(update_qubit)
		qgroupH = Group(qgate, qgateT).shift(DOWN*3)
		line = Line(np.array([-15, -3, 0]), np.array([15, -3, 0]))
		self.add(line)
		self.play(FadeIn(qgroupH))
		self.play(FadeIn(qubit))
		#setup axes
		axes = ThreeDAxes(height=12,axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-10,y_max=10)
		
		axes2 = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1.5})
		grid2 = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.4},x_min=-5,x_max=5,y_min=-5,y_max=5)
		axes2XLabel = Tex(r"\begin{bmatrix} 1\\ 0 \end{bmatrix}").shift(RIGHT*5)
		axes2YLabel = Tex(r"\begin{bmatrix} 0\\ 1 \end{bmatrix}").shift(UP*2)
		reflectLine = DashedLine(np.array([-5, 5, 0]), np.array([5, -5, 0]))
		axg2 = Group(axes2, grid2, axes2XLabel, axes2YLabel, reflectLine)
		self.play(ShowCreation(axg2)) 

		#setup vectors
		a = 1
		b = 1
		v1 = [1, 0]
		v2 = [0, 1]
		vector = Vector(direction=[a,b,0])
		vectorX = Vector(direction=[a, 0,0], fill_color=RED)
		vectorY = Vector(direction=[0,b,0], fill_color=GREEN)
		axg = Group(axes, grid, vectorX, vectorY, vector)
		self.play(ShowCreation(axg))  
		def update_vector(self):
			self.become(Vector(direction=[1, 1,0]))
		def update_vectorX(self):
			self.become(Vector(direction=[v1[0], v1[1],0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[v2[0],v2[1],0], fill_color=GREEN))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)

		itsagate = Tex(r"\ket{\psi} = a_1\ket{0} + a_2\ket{1}")
		def update_ketvect(self):
			self.next_to(qubit, UP, buff=0.5)
		itsagate.add_updater(update_ketvect)
		self.play(Write(itsagate))

		self.wait(3)
		#make qubit move
		t = 0
		while(t < 300):
			x += 0.01
			t += 1
			self.wait(0.001)
		qgate2 = Square(1, fill_color=YELLOW, fill_opacity=1)
		qgateT2 = Text("H")
		qgroupH2 = Group(qgate2, qgateT2).shift(DOWN*3)
		self.play(Transform(qgroupH, qgroupH2))
		#apply rotation 135 degrees
		self.wait(5)
		optitle = Tex(r"Ops:").scale(0.7).shift(LEFT*5.5 + UP * 2)
		op1 = Tex(r"Rot: 135^{\circ} or \frac{3\pi}{4}").scale(0.7).shift(LEFT*4 + UP*1.5)
		self.play(Write(optitle))

		self.play(Rotate(axg, -3*PI/4), rate_func=smooth)
		axg3 = axg.copy()
		axg3.rotate(-3*PI/4)
		self.remove(axg)
		self.add(axg3)
		#apply reflection
		self.play(Write(op1))
		self.wait(6)
		self.play(Rotate(axg3, PI, axis=np.array([-5, 5, 0])), rate_func=smooth)
		op2 = Tex(r"Refl: y=-x}").scale(0.7).shift(LEFT*4 + UP*1)
		self.play(Write(op2))
		self.wait(6)

		#update ket vector
		itsagate2 = Tex(r"H\ket{\psi} = a_1(H\ket{0}) + a_2(H\ket{1})")
		self.play(Transform(itsagate, itsagate2))
		while(t < 600):
			x += 0.01
			t += 1
			self.wait(0.001)
		itsagate3 = Tex(r"H\ket{\psi} = a_1(\ket{+}) + a_2(H\ket{1})")
		self.play(Transform(itsagate, itsagate3))
		self.wait(6)
		itsagate4 = Tex(r"H\ket{\psi} = a_1\ket{+} + a_2\ket{-}")
		itsagate4.add_updater(update_ketvect)
		self.play(FadeOut(itsagate))
		self.play(FadeIn(itsagate4))
		self.wait(6)
		#go through gate again
		while(t > 300):
			x -= 0.01
			t -= 1
			self.wait(0.001)
		self.wait(6)
		#apply rotation 135 degrees
		op3 = Tex(r"Rot: 135^{\circ} or \frac{3\pi}{4}").scale(0.7).shift(LEFT*4 + UP*0.5)
		axg4 = axg3.copy()
		self.play(Rotate(axg3, -3*PI/4), rate_func=smooth)
		axg4.rotate(-3*PI/4)
		self.remove(axg3)
		self.add(axg4)
		#apply reflection
		self.play(Write(op3))
		self.wait(6)
		self.play(Rotate(axg4, PI, axis=np.array([-5, 5, 0])), rate_func=smooth)
		op4 = Tex(r"Refl: y=-x}").scale(0.7).shift(LEFT*4)
		self.play(Write(op4))
		self.wait(6)
		#update hadamard
		itsagate5 = Tex(r"H^2\ket{\psi} = a_1(H\ket{+}) + a_2(H\ket{-})")
		self.play(Transform(itsagate4, itsagate5))
		while(t > 0):
			x -= 0.01
			t -= 1
			self.wait(0.001)
		itsagate6 = Tex(r"H^2\ket{\psi} = a_1\ket{0} + a_2\ket{1}")
		self.play(Transform(itsagate4, itsagate6))
		self.wait(6)
		hproperty1 = Tex(r"H = \frac{1}{\sqrt{(2})}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}").shift(RIGHT*4 + UP*2.2)
		self.play(FadeIn(hproperty1))
		self.wait(6)
		hproperty2 = Tex(r"H^2 = \mathbb{I}").shift(RIGHT*4 + UP*1.1)
		self.play(FadeIn(hproperty2))
		self.wait(6)

		hproperty3 = Tex(r"H\ket{0} = \ket{+}").shift(RIGHT*4 + DOWN*1.2)
		self.play(FadeIn(hproperty3))
		self.wait(6)
		hproperty4 = Tex(r"H\ket{+} = \ket{0}").shift(RIGHT*4 + DOWN*1.8)
		self.play(FadeIn(hproperty4))
		self.wait(6)

		hproperty5 = Tex(r"H\ket{1} = \ket{-}").shift(RIGHT*4 + DOWN*2.4)
		self.play(FadeIn(hproperty5))
		self.wait(6)
		hproperty6 = Tex(r"H\ket{-} = \ket{1}").shift(RIGHT*4 + DOWN*3.0)
		self.play(FadeIn(hproperty6))
		self.wait(6)

		#remove everything
		self.play(FadeOut(axg4), FadeOut(axg2), FadeOut(itsagate4), FadeOut(qgroupH), FadeOut(qubit), FadeOut(line), FadeOut(optitle), FadeOut(op1), FadeOut(op2), FadeOut(op3), FadeOut(op4))
		self.play(FadeOut(hproperty1), FadeOut(hproperty2), FadeOut(hproperty3), FadeOut(hproperty4), FadeOut(hproperty5), FadeOut(hproperty6))

		#pauli matrices
		Title3 = Text("Pauli Matrices").shift(UP*3.5)
		self.play(Transform(Title, Title3))
		self.wait(4)
		px = Tex(r"\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}").shift(LEFT*4).shift(UP*2)
		py = Tex(r"\sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}").shift(LEFT*4)
		pz = Tex(r"\sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}").shift(LEFT*4).shift(DOWN*2)
		self.play(FadeIn(px), FadeIn(py), FadeIn(pz))
		self.wait(3)
		pxx = Tex(r"\sigma_x^2 = \mathbb{I}").shift(UP*2)
		pyy = Tex(r"\sigma_y^2 = \mathbb{I}")
		pzz = Tex(r"\sigma_z^2 = \mathbb{I}").shift(DOWN*2)
		self.play(FadeIn(pxx), FadeIn(pyy), FadeIn(pzz))
		self.wait(3)
		pp3 = Tex(r"\sigma_i^{\dag}\sigma_i = \mathbb{I}").shift(RIGHT*4 + UP*2)
		self.play(FadeIn(pp3))
		self.wait(5)
		pp2 = Tex(r"Tr(\sigma_i) = 0").shift(RIGHT*4 + UP*0.5)
		self.play(FadeIn(pp2))
		self.wait(6)

		pp = Tex(r"-i\sigma_x\sigma_y\sigma_z = \mathbb{I}").shift(RIGHT*4 + DOWN*1)
		self.play(FadeIn(pp))
		self.wait(6)

		pp4 = Tex(r"Exercise: \ket{\psi} = \frac{1}{\sqrt{(5})}\ket{0} + \frac{2}{\sqrt{(5})}\ket{1}").shift(RIGHT*2 + DOWN*3.2)
		self.play(FadeIn(pp4))
		self.wait(10)

		pg = Group(px, py, pz, pp, pp2, pp3, pp4, pxx, pyy, pzz)
		self.play(FadeOut(pg))

		#Rotation Matrix
		Title4 = Text("Phase Shift").shift(UP*3.5)
		self.play(Transform(Title, Title4))
		self.wait(3)
		rt = Tex(r"R_{\theta} = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}")
		self.play(Write(rt))
		self.wait(6)
		exercise = Text("Check if Unitary").shift(DOWN*2)
		self.play(Write(exercise))
		self.wait(6)
		self.play(FadeOut(exercise))

		rt2 = Tex(r"R_{\theta}\ket{0} = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \ket{0}")
		self.play(Transform(rt, rt2))
		self.wait(6)

		rt3 = Tex(r"R_{\theta}\ket{1} = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = e^{i\theta}\ket{1}")
		self.play(Transform(rt, rt3))
		self.wait(6)

		rt4 = Tex(r"R_{\theta}\ket{\psi} = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}(a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \end{bmatrix})")
		self.play(Transform(rt, rt4))
		self.wait(6)

		rt5 = Tex(r"R_{\theta}\ket{\psi} = a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2e^{i\theta}\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
		self.play(FadeOut(rt))
		self.play(FadeIn(rt5))
		self.wait(6)

		eulerfudge2 = Tex(r"\ket{\psi} = R_1e^{i\phi_1}\begin{bmatrix} 1 \\ 0  \end{bmatrix} + R_2e^{i\phi_2}\begin{bmatrix} 0 \\ 1  \end{bmatrix}").shift(DOWN*2.5)
		self.play(Write(eulerfudge2))
		self.wait(6)

		rt6 = Tex(r"R_{\theta}\ket{\psi} = R_1e^{i\phi_1}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + R_2e^{i\phi_2}e^{i\theta}\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
		self.play(Transform(rt5, rt6))
		self.wait(6)

		rt7 = Tex(r"R_{\theta}\ket{\psi} = R_1e^{i\phi_1}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + R_2e^{i(\phi_2 + \theta)}\begin{bmatrix} 0 \\ 1 \end{bmatrix}")
		self.play(Transform(rt5, rt7))
		self.wait(6)











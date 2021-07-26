from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Reduced Density Matrix, Partial Trace, Bloch Vector").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class trace(Scene):
	def construct(self):
		text = Text("Reduced Density Matrix, Partial Trace, Bloch Vector").scale(0.85)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		title = Text("Reduced Density Matrix").shift(UP*3.5)
		
		its2 = Tex(r"p_{AB} = \begin{bmatrix} c_0^*c_0 & c_1^*c_0 & c_2^*c_0 & c_3^*c_0 \\  c_0^*c_1 & c_1^*c_1 & c_2^*c_1 & c_3^*c_1  \\ c_0^*c_2 & c_1^*c_2 & c_2^*c_2 & c_3^*c_2 \\ c_0^*c_3 & c_1^*c_3 & c_2^*c_3 & c_3^*c_3 \end{bmatrix}").shift(UP*1.5 + LEFT*0.5)
		self.play(Write(title), Write(its2))
		self.wait(3)
		dpsi = Tex(r"p_{A} = \begin{bmatrix} a_0^*a_0 & a_1^*a_0 \\ a_0^*a_1 & a_1^*a_1  \end{bmatrix}").shift(DOWN*2 + LEFT*3)
		dphi = Tex(r"p_{B} = \begin{bmatrix} b_0^*b_0 & b_1^*b_0 \\ b_0^*b_1 & b_1^*b_1  \end{bmatrix}").shift(DOWN*2 + RIGHT*3)
		self.play(Write(dpsi), Write(dphi))
		self.wait(3)
		boundphi = SurroundingRectangle(dphi)
		boundpsi = SurroundingRectangle(dpsi)
		self.play(ShowCreation(boundphi), ShowCreation(boundpsi))
		self.wait(3)
		ag = Group(dpsi, dphi, boundpsi, boundphi)
		self.play(FadeOut(ag))

		title2 = Text("Partial Trace").shift(UP*3.5)
		self.play(Transform(title, title2))
	

		showwhyA = Tex(r"p_{A} = \begin{bmatrix}Tr\begin{pmatrix} c_0^*c_0 & c_1^*c_0 \\ c_0^*c_1 & c_1^*c_1\end{pmatrix} & Tr\begin{pmatrix} c_2^*c_0 & c_3^*c_0 \\ c_2^*c_1 & c_3^*c_1\end{pmatrix}  \\ Tr\begin{pmatrix} c_0^*c_2 & c_1^*c_2 \\ c_0^*c_3 & c_1^*c_3\end{pmatrix}  & Tr\begin{pmatrix} c_2^*c_2 & c_3^*c_2 \\ c_2^*c_3 & c_3^*c_3\end{pmatrix} \end{bmatrix}")
		showwhyA.shift(DOWN*1.5)
		showwhyA[0][9:31].set_color(BLUE)
		showwhyA[0][33:55].set_color(RED)
		showwhyA[0][57:79].set_color(GREEN)
		showwhyA[0][81:103].set_color(YELLOW)
		self.play(FadeIn(showwhyA))
		self.wait(6)


		its3 = Tex(r"p_{AB} = \begin{bmatrix} c_0^*c_0 & c_1^*c_0 & c_2^*c_0 & c_3^*c_0 \\  c_0^*c_1 & c_1^*c_1 & c_2^*c_1 & c_3^*c_1  \\ c_0^*c_2 & c_1^*c_2 & c_2^*c_2 & c_3^*c_2 \\ c_0^*c_3 & c_1^*c_3 & c_2^*c_3 & c_3^*c_3 \end{bmatrix}").shift(UP*1.5 + LEFT*0.5)
		its3[0][8:13].set_color(BLUE)
		its3[0][18:23].set_color(RED)
		its3[0][33:38].set_color(BLUE)
		its3[0][43:48].set_color(RED)

		its3[0][48:53].set_color(GREEN)
		its3[0][58:63].set_color(YELLOW)
		its3[0][73:78].set_color(GREEN)
		its3[0][83:88].set_color(YELLOW)
		self.play(Transform(its2, its3))
		self.wait(6)
		self.play(FadeOut(showwhyA))

		#show it
		showwhyB = Tex(r"p_{B} = \begin{bmatrix}Tr\begin{pmatrix} c_0^*c_0 & c_2^*c_0 \\ c_0^*c_2 & c_2^*c_2\end{pmatrix} & Tr\begin{pmatrix} c_1^*c_0 & c_3^*c_0 \\ c_1^*c_2 & c_3^*c_1\end{pmatrix}  \\ Tr\begin{pmatrix} c_0^*c_1 & c_2^*c_1 \\ c_0^*c_3 & c_2^*c_3\end{pmatrix}  & Tr\begin{pmatrix} c_1^*c_1 & c_3^*c_1 \\ c_1^*c_3 & c_3^*c_3\end{pmatrix} \end{bmatrix}")
		showwhyB.shift(DOWN*1.5)
		showwhyB[0][9:31].set_color(BLUE)
		showwhyB[0][33:55].set_color(RED)
		showwhyB[0][57:79].set_color(GREEN)
		showwhyB[0][81:103].set_color(YELLOW)
		self.play(FadeIn(showwhyB))
		self.wait(6)

		its4 = Tex(r"p_{AB} = \begin{bmatrix} c_0^*c_0 & c_1^*c_0 & c_2^*c_0 & c_3^*c_0 \\  c_0^*c_1 & c_1^*c_1 & c_2^*c_1 & c_3^*c_1  \\ c_0^*c_2 & c_1^*c_2 & c_2^*c_2 & c_3^*c_2 \\ c_0^*c_3 & c_1^*c_3 & c_2^*c_3 & c_3^*c_3 \end{bmatrix}").shift(UP*1.5 + LEFT*0.5)
		its4[0][8:13].set_color(BLUE)
		its4[0][18:23].set_color(BLUE)
		its4[0][48:53].set_color(BLUE)
		its4[0][58:63].set_color(BLUE)

		its4[0][13:18].set_color(RED)
		its4[0][23:28].set_color(RED)
		its4[0][53:58].set_color(RED)
		its4[0][63:68].set_color(RED)

		its4[0][28:33].set_color(GREEN)
		its4[0][38:43].set_color(GREEN)
		its4[0][68:73].set_color(GREEN)
		its4[0][78:83].set_color(GREEN)

		
		its4[0][33:38].set_color(YELLOW)
		its4[0][43:48].set_color(YELLOW)
		its4[0][73:78].set_color(YELLOW)
		its4[0][83:88].set_color(YELLOW)
		self.play(Transform(its2, its4))
		self.wait(7)
		self.play(FadeOut(its2), FadeOut(showwhyB))

		#formulas
		t1 = Tex(r"p_A = \sum_{i=1}^{n} (\mathbb{I}\otimes\bra{i})p_{AB}(\mathbb{I}\otimes\ket{i})").shift(UP*2)
		t2 = Tex(r"p_B = \sum_{j=1}^{m} (\bra{j}\otimes\mathbb{I})p_{AB}(\ket{j}\otimes\mathbb{I})")
		self.play(FadeIn(t1), FadeIn(t2))
		self.wait(6)
		self.play(FadeOut(t1), FadeOut(t2))


		#bloch vector
		title3 = Text("Bloch Vector").shift(UP*3.5)
		self.play(Transform(title, title3))

		dpure = Tex(r"p_{\psi} = \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix} \ \ \ \ \ \ \ket{\psi} = \ket{+}").shift(UP*2.4)
		self.play(FadeIn(dpure))
		self.wait(3)

		x = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix})  \ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix}\begin{bmatrix} 0 & -i \\ i & 0\end{bmatrix}) \ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & -1\end{bmatrix}) \ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg = Group(x, y, z)
		self.play(FadeIn(anotherg))
		self.wait(5)

		x2 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix})\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y2 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} \frac{i}{2} & \frac{-i}{2} \\ \frac{i}{2} & \frac{-i}{2}\end{bmatrix})\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z2 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} \frac{1}{2} & \frac{-1}{2} \\ \frac{1}{2} & \frac{-1}{2}\end{bmatrix})\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg2 = Group(x2, y2, z2)
		self.play(Transform(anotherg, anotherg2))
		self.wait(5)

		x3 = Tex(r"x = Tr(p_{\psi}\sigma_x) = 1\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y3 = Tex(r"y = Tr(p_{\psi}\sigma_y) = 0\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z3 = Tex(r"z = Tr(p_{\psi}\sigma_z) = 0\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg3 = Group(x3, y3, z3)
		self.play(Transform(anotherg, anotherg3))
		self.wait(8)



		dpure2 = Tex(r"p_{\psi} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \ \ \ \ \ \ \ket{\psi} = \ket{1}").shift(UP*2.4)
		self.play(Transform(dpure, dpure2))

		x4 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} 0 & 0 \\ 0 & 1\end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix})  \ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y4 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} 0 & 0 \\ 0 & 1\end{bmatrix}\begin{bmatrix} 0 & -i \\ i & 0\end{bmatrix}) \ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z4 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} 0 & 0 \\ 0 & 1\end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & -1\end{bmatrix}) \ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg4 = Group(x4, y4, z4)
		self.play(Transform(anotherg, anotherg4))
		self.wait(6)

		x5 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} 0 & 0 \\ 1 & 0\end{bmatrix})\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y5 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} 0 & 0 \\ -i & 0\end{bmatrix})\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z5 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} 0 & 0 \\ 0 & -1\end{bmatrix})\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg5 = Group(x5, y5, z5)
		self.play(Transform(anotherg, anotherg5))
		self.wait(3)

		x6 = Tex(r"x = Tr(p_{\psi}\sigma_x) = 0\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y6 = Tex(r"y = Tr(p_{\psi}\sigma_y) = 0\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z6 = Tex(r"z = Tr(p_{\psi}\sigma_z) = -1\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg6 = Group(x6, y6, z6)
		self.play(Transform(anotherg, anotherg6))
		self.wait(7)
















		#show 2 MIXED bloch spheres
		title3 = Text("Bloch Vector - Mixed State").shift(UP*3.5)
		self.play(Transform(title, title3))

		dpure3 = Tex(r"p_{\psi} = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix} \ \ \ \ \ \ \ket{\psi} = \ket{1} \ \ or \ \  \ket{0}").shift(UP*2.4)
		self.play(Transform(dpure, dpure3))
		self.wait(3)

		x7 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} 0.5 & 0 \\ 0 & 0.5\end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix})  \ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y7 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} 0.5 & 0 \\ 0 & 0.5\end{bmatrix}\begin{bmatrix} 0 & -i \\ i & 0\end{bmatrix}) \ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z7 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} 0.5 & 0 \\ 0 & 0.5\end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & -1\end{bmatrix}) \ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg7 = Group(x7, y7, z7)
		self.play(Transform(anotherg, anotherg7))
		self.wait(6)

		x8 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} 0 & 0.5 \\ 0.5 & 0\end{bmatrix})\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y8 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} 0 & i/2 \\ -i/2 & 0\end{bmatrix})\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z8 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} 0.5 & 0 \\ 0 & -0.5\end{bmatrix})\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg8 = Group(x8, y8, z8)
		self.play(Transform(anotherg, anotherg8))
		self.wait(3)

		x9 = Tex(r"x = Tr(p_{\psi}\sigma_x) = 0\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y9 = Tex(r"y = Tr(p_{\psi}\sigma_y) = 0\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z9 = Tex(r"z = Tr(p_{\psi}\sigma_z) = 0\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg9 = Group(x9, y9, z9)
		self.play(Transform(anotherg, anotherg9))
		self.wait(3)

		how = Tex(r"det(p_{\psi}) \neq 0 \ \ MIXED STATE! \ \ \ \ \ \ det(p_{\psi}) = 0 \ \  PURE STATE!").scale(0.8).shift(DOWN*3.5)
		self.play(FadeIn(how))
		self.wait(8)
		how2 = Text("Why is it 0???").shift(DOWN*3.5)
		self.play(Transform(how, how2))
		

		#show 2 mixed bloch spheres
		dpure4 = Tex(r"p_{\psi} = \begin{bmatrix} \frac{3}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{bmatrix} \ \ \ \ \ \ \ket{\psi} = \ket{+} \ \ or \ \  \ket{0}").shift(UP*2.4)
		self.play(Transform(dpure, dpure4))
		self.wait(3)
		x11 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} \frac{3}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix})  \ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y11 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} \frac{3}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{bmatrix}\begin{bmatrix} 0 & -i \\ i & 0\end{bmatrix}) \ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z11 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} \frac{3}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & -1\end{bmatrix}) \ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg11 = Group(x11, y11, z11)
		self.play(Transform(anotherg, anotherg11))
		self.wait(3)
		x22 = Tex(r"x = Tr(p_{\psi}\sigma_x) = Tr(\begin{bmatrix} \frac{1}{4} & \frac{1}{4} \\ \frac{3}{4} & \frac{1}{4} \end{bmatrix})\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y22 = Tex(r"y = Tr(p_{\psi}\sigma_y) = Tr(\begin{bmatrix} \frac{i}{4} & \frac{-i}{4} \\ \frac{3i}{4} & \frac{-i}{4} \end{bmatrix})\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z22 = Tex(r"z = Tr(p_{\psi}\sigma_z) = Tr(\begin{bmatrix} \frac{3}{4} & \frac{-1}{4} \\ \frac{1}{4} & \frac{-1}{4} \end{bmatrix})\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg22 = Group(x22, y22, z22)
		self.play(Transform(anotherg, anotherg22))
		self.wait(3)
		x33 = Tex(r"x = Tr(p_{\psi}\sigma_x) = \frac{1}{2}\ \ \ \ \ \ \ x \in \{\ket{+}, \ket{-}\}").shift(UP*0.8)
		y33 = Tex(r"y = Tr(p_{\psi}\sigma_y) = 0\ \ \ \ \ \ \ y \in \{\ket{i}, \ket{-i}\}").shift(DOWN*0.7)
		z33 = Tex(r"z = Tr(p_{\psi}\sigma_z) = \frac{1}{2}\ \ \ \ \ \ \ z \in \{\ket{0}, \ket{1}\}").shift(DOWN*2.2)
		anotherg33 = Group(x33, y33, z33)
		self.play(Transform(anotherg, anotherg33))
		self.wait(8)
		grouper = Group(anotherg, how)
		self.play(FadeOut(grouper))
		








		dpure.generate_target()
		dpure.target.shift(UP*2.5)
	

		#show 3d rep
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
		vectL = Vector(direction=[-1, 0, 0]).shift(LEFT*2)
		vectR = Vector(direction=[0, 0, 1]).shift(RIGHT*2)
		
		box = Rectangle(8, 6, color=BLUE)
		#
		self.play(FadeIn(vectL), MoveToTarget(dpure), FadeIn(vectR), FadeIn(box))

		#time for measuring
		box1 = SurroundingRectangle(qubitG1)
		box2 = SurroundingRectangle(qubitG2)

		vectL.generate_target()
		for i in range(0, 10):
			vectL.target = Vector(direction=[-1, 0, 0]).shift(LEFT*2)
			self.play(MoveToTarget(vectL))
			a = random.randint(0, 1)
			if (a == 1):
				b = random.randint(0, 1)
				vectL.target = Vector(direction=[0, 0, 2*b - 1]).shift(LEFT*2)
				self.play(ShowCreation(box1), MoveToTarget(vectL))
				self.play(FadeOut(box1))
			else:
				self.play(ShowCreation(box2))
				self.play(FadeOut(box2))
		vectL.target = Vector(direction=[-1, 0, 0]).shift(LEFT*2)
		self.play(MoveToTarget(vectL))

		self.wait(4)

		#the result is just add the vectors
		sphere3 = Sphere(radius = 1, point=ORIGIN, color=RED)
		sphereMesh3 = SurfaceMesh(sphere2, resolution=(7, 7), flat_stroke=True, color=GREY)

		labelpX3 = Tex(r'\ket{-}').shift(RIGHT*1.5)
		labelrX3 = Tex(r'\ket{+}').shift(LEFT*1.5)

		labelpY3 = Tex(r'\ket{-i}').shift(UP*1.5)
		labelrY3 = Tex(r'\ket{+i}').shift(DOWN*1.5)

		labelpZ3 = Tex(r'\ket{0}').rotate(PI/2, axis=RIGHT).shift(OUT*1.5)
		labelrZ3 = Tex(r'\ket{1}').rotate(PI/2, axis=RIGHT).shift(IN*1.5)

		x3 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), fill_color=GREY_E, color=GREY_E)
		y3 = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), fill_color=GREY_E, color=GREY_E)
		z3 = Line(np.array([0, 0, -1]), np.array([0, 0, 1]), fill_color=GREY_E, color=GREY_E)
		#self.add_fixed_in_frame_mobjects(labelX, labelY, labelZ)

		qubitG3 = Group(sphere3, sphereMesh3, x3, y3, z3, labelpX3, labelpY3, labelpZ3, labelrX3, labelrY3, labelrZ3)
		qubitG3.shift(RIGHT*7)
		sphereMesh3.shift(LEFT*2)
		frame.generate_target()
		frame.target.set_width(20)
		frame.target.shift(RIGHT*7)
		self.play(MoveToTarget(frame), ShowCreation(sphereMesh3), FadeIn(labelpX3), FadeIn(labelpY3), FadeIn(labelpZ3), FadeIn(labelrX3), FadeIn(labelrY3), FadeIn(labelrZ3), FadeIn(x3), FadeIn(y3), FadeIn(z3))
		
		vect2L = vectL.copy()
		vect2R = vectR.copy()
		vect2L.generate_target()
		vect2R.generate_target()

		vect2R.target.shift(RIGHT*5)
		self.play(MoveToTarget(vect2R))
		self.wait(2)
		vect2L.target.shift(RIGHT*9 + OUT*1)
		self.play(MoveToTarget(vect2L))
		self.wait(2)
		vect3 = Vector(direction=[-1, 0, 1]).shift(RIGHT*7)
		self.play(FadeIn(vect3), FadeOut(vect2L), FadeOut(vect2R))
		self.wait(2)
		vect3.generate_target() 
		vect3.target = Vector(direction=[-0.5, 0, 0.5]).shift(RIGHT*7)
		self.play(MoveToTarget(vect3))
		self.wait(6)
		frame.target.shift(LEFT*7)
		
		dpure3.shift(DOWN*6.5 + RIGHT*3).rotate(PI)
		self.play(MoveToTarget(frame), FadeOut(vect3), FadeIn(dpure3))
		self.wait(2)
		vectL.target = Vector(direction=[0, 0, -1]).shift(LEFT*2)
		self.play(MoveToTarget(vectL))
		self.wait(3)
		frame.target.shift(RIGHT*7)
		self.play(MoveToTarget(frame))
		self.wait(3)
		


		vect2L = vectL.copy()
		vect2R = vectR.copy()
		vect2L.generate_target()
		vect2R.generate_target()

		vect2R.target.shift(RIGHT*5)
		self.play(MoveToTarget(vect2R))

		vect2L.target.shift(RIGHT*8.9 + OUT*1)
		self.play(MoveToTarget(vect2L))
		self.wait(3)
		dotter = Dot(np.array([7,0,0]), fill_color=RED)
		self.play(FadeOut(vect2R), FadeOut(vect2L), FadeIn(dotter))


		result1 = Text("1. Mixed State represents average of Bloch Vectors").rotate(3*PI/2)
		result2 = Text("2. Mixed State Bloch Vectors are inside the Bloch Sphere").rotate(3*PI/2)

		result1.shift(RIGHT*11)
		result2.shift(RIGHT*10)
		self.wait(3)
		self.play(FadeIn(result1), FadeIn(result2))

		self.wait(15)















from manimlib import *
import numpy as np

class FirstScene(ThreeDScene):
	def construct(self):
		text = Text("Linear Independance, Span, Orthogonality")
		self.play(FadeIn(text))
		self.wait(3)

class LinearBro(Scene):
	def construct(self):
		text = Text("Linear Independance, Span, Orthogonality")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		dogood = Tex(r"\vec{x} = \begin{bmatrix} a \\ b \\ c \end{bmatrix} = a_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} + a_3\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}")
		self.play(ShowCreation(dogood))
		self.wait(3)
		self.play(FadeOut(dogood))
		self.remove(dogood)

		axes = ThreeDAxes()
		frame = self.camera.frame
		frame.set_euler_angles(
			theta=-30 * DEGREES,
			phi=70 * DEGREES,
		)

		self.play(ShowCreation(axes))
		self.wait(1)
		#self.move_camera(phi=45*DEGREES, theta=-30*DEGREES)

		#show 3 axes + basis
		r = 2
		phi = 0
		theta = 3.14159
		a = r*np.cos(phi)*np.sin(theta)
		b = r*np.sin(phi)*np.sin(theta)
		c = r*np.cos(theta)
		vector = Vector(direction=[a,b,c])
		vectorX = Vector(direction=[a, 0,0], fill_color=RED)
		vectorY = Vector(direction=[0,b,0], fill_color=GREEN)
		vectorZ = Vector(direction=[0,0,c], fill_color=BLUE)

		#self.set_camera_orientation()
		self.add(vectorX, vectorY, vectorZ) 
		self.add(vector)
		def update_vector(self):
			self.become(Vector(direction=[a,b,c]))
		def update_vectorX(self):
			self.become(Vector(direction=[a, 0,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,b,0], fill_color=GREEN))
		def update_vectorZ(self):
			self.become(Vector(direction=[0,0,c], fill_color=BLUE))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		vectorZ.add_updater(update_vectorZ)

		dogood2 = Tex(r"\vec{x} = \begin{bmatrix} "+str("{:.2f}".format(a))+" \\\\ "+str("{:.2f}".format(b))+" \\\\ "+str("{:.2f}".format(c))+" \\end{bmatrix}")
		dogood2.shift(DOWN*4)
		def vec(self):
			self.become(Tex(r"\vec{x} = \begin{bmatrix} "+str("{:.2f}".format(a))+" \\\\ "+str("{:.2f}".format(b))+" \\\\ "+str("{:.2f}".format(c))+" \\end{bmatrix}")).shift(DOWN*4)
		dogood2.add_updater(vec)
		
		self.play(ShowCreation(dogood2))

		ticker = 0
		while(phi<6.28):
			ticker += 1
			phi+=0.03
			theta -= 0.05
			a = r*np.cos(phi)*np.sin(theta)
			b = r*np.sin(phi)*np.sin(theta)
			c = r*np.cos(theta)
			frame.set_euler_angles(
				theta=-30 * DEGREES + ticker/2*DEGREES,
				phi=70 * DEGREES,
			)
			self.wait(0.001)
		self.wait(1)
		self.remove(axes,dogood2,vector, vectorX, vectorY, vectorZ)
		
		frame.set_euler_angles(
				theta=0,
				phi=0,
			)
		dogood3 = Tex(r"\vec{x} = \begin{bmatrix} a \\ b \\ c \end{bmatrix} = a_1\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \\ -1\end{bmatrix} + a_3\begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}")
		def vec(self):
			self.become(Tex(r"\vec{x} = \begin{bmatrix} "+str("{:.2f}".format(a))+" \\\\ "+str("{:.2f}".format(-a +b -c))+" \\\\ "+str("{:.2f}".format(-b + c))+" \\end{bmatrix}")).shift(DOWN*4)
		dogood2.add_updater(vec)
		self.play(ShowCreation(dogood3))
		self.wait(3)
		self.play(FadeOut(dogood3))
		self.remove(dogood3)

		frame.set_euler_angles(
				theta=-30 * DEGREES + ticker/2*DEGREES,
				phi=70 * DEGREES,
			)
		self.add(axes, dogood2,vector, vectorX, vectorY, vectorZ)
	



				#show with different basis: [1, -1, 0], [0, 1, -1], [0, -1, 1]
		def update_vector(self):
			self.become(Vector(direction=[a,b,c]))
		def update_vectorX(self):
			self.become(Vector(direction=[a, -a,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,b,-b], fill_color=GREEN))
		def update_vectorZ(self):
			self.become(Vector(direction=[0,-c,c], fill_color=BLUE))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		vectorZ.add_updater(update_vectorZ)
		ticker = 0
		while(phi>0):
			ticker += 1
			phi-=0.03
			theta -= 0.05
			a = r*np.cos(phi)*np.sin(theta)
			b = r*np.sin(phi)*np.sin(theta)
			c = r*np.cos(theta)
			frame.set_euler_angles(
				theta=-30 * DEGREES + ticker/2*DEGREES,
				phi=70 * DEGREES,
			)
			self.wait(0.001)
		self.wait(5)

		#What is span?
		self.play(FadeOut(axes), FadeOut(dogood2),FadeOut(vector), FadeOut(vectorX), FadeOut(vectorY), FadeOut(vectorZ))
		frame.set_euler_angles(
				theta=-0,
				phi=0,
			)
		thequestion=Text("What is Span?")
		thequestion.shift(UP*3)
		self.play(ShowCreation(thequestion))
		self.wait(2)
		dogood4 = Tex(r"a_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} + a_3\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} ? \\ ? \\ ? \end{bmatrix}")
		self.play(FadeIn(dogood4))
		self.wait(2)
		q = 30.23
		r = 86.23
		s = -100
		
		dogood5 = Tex(r" "+ str("{:.2f}".format(q)) + "\\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\end{bmatrix} + "+str("{:.2f}".format(r))+"\\begin{bmatrix} 0 \\\\ 1 \\\\ 0\\end{bmatrix} + " + str("{:.2f}".format(s)) + "\\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} "+str("{:.2f}".format(q+s))+ " \\\\ " +str("{:.2f}".format(r+s))+ " \\\\ "+str("{:.2f}".format(0))+" \\end{bmatrix}").shift(DOWN*3)
		self.play(Transform(dogood4, dogood5))
		def update_spanner(self):
			self.become(Tex(r" "+ str("{:.2f}".format(q)) + "\\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\end{bmatrix} + "+str("{:.2f}".format(r))+"\\begin{bmatrix} 0 \\\\ 1 \\\\ 0\\end{bmatrix} + " + str("{:.2f}".format(s)) + "\\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} "+str("{:.2f}".format(q+s))+ " \\\\ " +str("{:.2f}".format(r+s))+ " \\\\ "+str("{:.2f}".format(0))+" \\end{bmatrix}")).shift(DOWN*3)
		dogood5.add_updater(update_spanner)
		self.remove(dogood4)
		self.add(dogood5)
		def update_vector(self):
			self.become(Dot(np.array([(q+s)/50,(r+s)/50,0])))
		def update_vectorX(self):
			self.become(Vector(direction=[q/50, 0,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,r/50,0], fill_color=GREEN))
		def update_vectorZ(self):
			self.become(Vector(direction=[s/50,s/50,0], fill_color=BLUE))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		vectorZ.add_updater(update_vectorZ)
		self.add(axes,vector, vectorX, vectorY, vectorZ)
 
		aticker = 0
		while(aticker<100):
			aticker += 1
			q += 0.2
			r -= 0.3
			s += 0.5
			self.wait(0.01)


		self.wait(12)
		def update_spanner(self):
			self.become(Tex(r" "+ str("{:.2f}".format(q)) + "\\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\end{bmatrix} + "+str("{:.2f}".format(r))+"\\begin{bmatrix} 0 \\\\ 1 \\\\ 0\\end{bmatrix} + " + str("{:.2f}".format(s)) + "\\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} "+str("{:.2f}".format(q))+ " \\\\ " +str("{:.2f}".format(r))+ " \\\\ "+str("{:.2f}".format(s))+" \\end{bmatrix}")).shift(DOWN*3)
		dogood5.add_updater(update_spanner)
		def update_vector(self):
			self.become(Dot(np.array([(q)/50,(r)/50,s/50])))
		def update_vectorX(self):
			self.become(Vector(direction=[q/50, 0,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,r/50,0], fill_color=GREEN))
		def update_vectorZ(self):
			self.become(Vector(direction=[0,0,s/50], fill_color=BLUE))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		vectorZ.add_updater(update_vectorZ)

		s = 0
		while(aticker<200):
			aticker += 1
			q += 0.2
			r -= 0.3
			s += 0.8
			frame.set_euler_angles(
				theta=-30 * DEGREES + aticker/2*DEGREES,
				phi=70 * DEGREES,
			)
			self.wait(0.01)
		self.wait(12)
		self.play(FadeOut(axes), FadeOut(dogood5),FadeOut(vector), FadeOut(vectorX), FadeOut(vectorY), FadeOut(vectorZ))
		frame.set_euler_angles(
				theta=0,
				phi=0,
			)
		notgood = Tex(r"\left\{\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}\right\}").shift(UP*1)
		notgoodw = Tex(r"\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}").shift(DOWN*1)
		itslinindep = Text("Linear Independent").shift(UP*3)
		self.play(Transform(thequestion,itslinindep))
		self.play(FadeIn(notgood))
		self.wait(8)
		self.play(FadeIn(notgoodw))
		self.wait(3)
		notgood2 = Tex(r"\left\{\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}\right\}").shift(UP*1)
		self.play(Transform(notgood, notgood2))
		
		self.wait(5)
		self.play(FadeOut(thequestion))
		self.play(FadeOut(notgood), FadeOut(notgoodw))

		#Orthogonal
		itsortho = Text("Orthogonality").shift(UP*3)
		self.play(Write(itsortho))
		basis = Tex(r"B_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}  B_2=\begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(UP*1)
		self.play(ShowCreation(basis))
		self.wait(3)

		basis2 = Tex(r"B_1\cdot B_2").shift(DOWN*1)
		self.play(ShowCreation(basis2))
		self.wait(6)

		basis3 = Tex(r"\langle B_1\mid B_2\rangle = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(DOWN*1)
		self.play(Transform(basis2, basis3))
		self.wait(3)

		basis4 = Tex(r"\langle B_1\mid B_2\rangle = 0").shift(DOWN*1)
		self.play(Transform(basis2, basis4))
		self.wait(3)


		self.play(FadeOut(basis))
		self.remove(basis)
		basis5 = Tex(r"\langle B_i\mid B_j\rangle = \delta_{ij} = \begin{cases} 1, & \text{if } i=j,\\0, & \text{if } i\neq j.\end{cases}")
		self.play(Transform(basis2, basis5))
		self.wait(8)
		gramshmith = Text("Gram–Schmidt process").shift(DOWN*2)
		self.play(Write(gramshmith))
		self.wait(8)











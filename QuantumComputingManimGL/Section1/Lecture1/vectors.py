from manimlib import *
import numpy as np
#〈 〉
class FirstScene(Scene):
	def construct(self):
		text = Text("Vectors, R & C, Basis")
		self.play(FadeIn(text))
		self.wait(3)

class VectorDecomposition(ThreeDScene):
	def construct(self):
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
		vectorY = Vector(direction=[0,b,0], fill_color=GREEN)
		
		self.add(vectorX, vectorY) 
		self.add(vector)
		def update_vector(self):
			self.become(Vector(direction=[a,b,0]))
		def update_vectorX(self):
			self.become(Vector(direction=[a, 0,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,b,0], fill_color=GREEN))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		#self.play(ShowCreation(sphere),ShowCreation(garis),ShowCreation(axes))
		self.wait(2)
		while(x<6.3*2):
			x+=0.03
			a = np.sin(x)
			b = np.cos(x)
			self.wait(0.0001)
class VectorEquation(Scene):
	def construct(self):
		text = Text("Vectors, R & C, Basis")
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))
		self.remove(text)

		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(ShowCreation(axes))  
		self.play(ShowCreation(grid))  
		self.wait(1)
		x = 0
		a = 2.2 * np.sin(x)
		b = 2.2 * np.cos(x)
		vector = Vector(direction=[a,b,0])
		vectorX = Vector(direction=[a, 0,0], fill_color=RED)
		vectorY = Vector(direction=[0,b,0], fill_color=GREEN)
		
		self.add(vectorX, vectorY) 
		self.add(vector)
		def update_vector(self):
			self.become(Vector(direction=[a,b,0]))
		def update_vectorX(self):
			self.become(Vector(direction=[a, 0,0], fill_color=RED))
		def update_vectorY(self):
			self.become(Vector(direction=[0,b,0], fill_color=GREEN))
		vector.add_updater(update_vector)
		vectorX.add_updater(update_vectorX)
		vectorY.add_updater(update_vectorY)
		#self.play(ShowCreation(sphere),ShowCreation(garis),ShowCreation(axes))
		self.wait(2)
		while(x<6.28*2):
			x+=0.03
			a = 2.2 * np.sin(x)
			b = 2.2 * np.cos(x)
			self.wait(0.0001)
		self.remove(vectorX, vectorY)
		self.play(FadeOut(vector))
		self.wait(1)
		self.remove(vector)
		self.play(FadeOut(axes)) 
		self.play(FadeOut(grid)) 
		self.wait(1)








		regvec = Tex(r"\vec{x} = \begin{bmatrix} a \\ b \end{bmatrix}")
		self.add(regvec)
		self.wait(3)
		decompvec = (Tex(r"\vec{x} = \begin{bmatrix} a \\ b \end{bmatrix} = a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \end{bmatrix}"))
		self.play(Transform(regvec, decompvec))
		self.wait(3)
		
		#show basis coefficients
		line = Arrow(DOWN*0.75, UP*0.75, fill_color=RED)
		line.move_to(LEFT*0.1 + DOWN * 1.35)
		self.play(FadeIn(line))
		line.generate_target()
		line.target.shift(RIGHT*1.9)

		itsareal = Tex(r"a_1, a_2 \in \mathbb{R}")
		itsareal.move_to(UP*1.25)
		self.play(MoveToTarget(line))
		self.play(FadeIn(itsareal))
		self.play(FadeOut(line))
		self.remove(line)
		itsanr2 = Tex(r"\vec{x} \in \mathbb{R}^2")
		itsanr2.move_to(DOWN*1.25)
		self.play(FadeIn(itsanr2))

		self.wait(3)
		#euclidean norm
		doubledecompvec = (Tex(r"\vec{x} = \begin{bmatrix} a \\ b \end{bmatrix} = a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = \sqrt{\sum_{i=1}^{n} a_i^2}"))
		self.play(Transform(regvec, doubledecompvec))

		self.wait(6)
		#Name rule 1: all qubits in C^2
		complexlaw = Tex(r"\textrm{1. All qubits are in } \mathbb{C}^2")
		complexlaw.move_to(UP * 3.5)
		self.play(FadeIn(complexlaw))
		self.wait(6)

		#Apply rule 1
		itsanc2 = Tex(r"\ket{x} \in \mathbb{C}^2")
		itsanc2.move_to(DOWN*1.25)
		self.play(Transform(itsanr2, itsanc2))

		self.wait(2)
		itsacomplex = Tex(r"a_1, a_2 \in \mathbb{C}")
		itsacomplex.move_to(UP*1.25)
		self.play(Transform(itsareal, itsacomplex))

		self.wait(3)
		complexdecompvec = (Tex(r"\ket{x} = \begin{bmatrix} a \\ b \end{bmatrix} = a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = \sqrt{\sum_{i=1}^{n} ??}"))
		self.play(Transform(regvec, complexdecompvec))
		
		self.wait(6)
		#Complex Conjugate
		complexconjugate1 = Tex(r"p = a + bi")
		spacer = Tex(r"\textrm{   }")
		complexconjugate2 = Tex(r"p^* = a - bi")
		conjugategroup = VGroup(complexconjugate1, spacer, complexconjugate2).arrange(RIGHT)
		conjugategroup.move_to(DOWN * 2.5)
		self.play(FadeIn(conjugategroup))
		self.wait(5)

		complexconjugate3 = Tex(r"p^*p = (a + bi)(a - bi)")
		complexconjugate3.move_to(DOWN * 2.5)
		self.play(Transform(conjugategroup, complexconjugate3))

		self.wait(3)
		complexconjugate6 = Tex(r"p^*p = a^2 + b^2 = d^2 \in \mathbb{R}")
		complexconjugate6.move_to(DOWN * 2.5)
		self.play(Transform(conjugategroup, complexconjugate6))
		
		self.wait(3)
		complexdecompveclength = (Tex(r"\ket{x} = \begin{bmatrix} a \\ b \end{bmatrix} = a_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = \sqrt{\sum_{i=1}^{n} a_i^*a_i}"))
		self.play(Transform(regvec, complexdecompveclength))
		self.play(FadeOut(conjugategroup))
		self.wait(5)

		#choose a_1 = 1+i, a_2 = 1-i
		complexdecompveclength2 = (Tex(r"\ket{x} = \begin{bmatrix} a \\ b \end{bmatrix} = (1 + i)\begin{bmatrix} 1 \\ 0 \end{bmatrix} + (1 - i)\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = \sqrt{\sum_{i=1}^{n} {a_i^*a_i}}"))
		self.play(Transform(regvec, complexdecompveclength2))

		self.wait(3)
		complexdecompveclength3 = (Tex(r"\ket{x} = \begin{bmatrix} a \\ b \end{bmatrix} = (1 + i)\begin{bmatrix} 1 \\ 0 \end{bmatrix} + (1 - i)\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = 2"))
		self.play(Transform(regvec, complexdecompveclength3))

		self.wait(5)
		#Name Rule 2: The Euclidean Norm of Qubits is 1
		complexlaw2 = Tex(r"\textrm{2. The Euclidean Norm of all Qubits is 1 }")
		complexlaw2.move_to(UP * 2.85)
		self.play(FadeIn(complexlaw2))

		complexdecompveclength4 = (Tex(r"Normalize(\ket{x}) = \frac{(1 + i)}{(2)}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + \frac{(1 - i)}{(2)}\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = 1"))
		self.play(Transform(regvec, complexdecompveclength4))
		self.wait(12)

		#
		complexdecompveclength44 = (Tex(r"Length = \sqrt{\sum_{i=1}^{n} {a_i^*a_i}} = 1"))
		self.play(Transform(regvec, complexdecompveclength44))
		self.wait(12)
		complexdecompveclength45 = (Tex(r"Length^2 = \sum_{i=1}^{n} {a_i^*a_i} = 1"))
		self.play(Transform(regvec, complexdecompveclength45))
		self.wait(12)

		#Problem 1: x = [[2+i], [3+4i]]
		complexdecompveclength5 = (Tex(r"\ket{x} = \begin{bmatrix} 2+i \\ 3+4i \end{bmatrix}"))
		self.play(Transform(regvec, complexdecompveclength5))
		self.wait(14)

		complexdecompveclength6 = (Tex(r"\ket{x} = \begin{bmatrix} 2+i \\ 3+4i \end{bmatrix} = 2 + i\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 3+4i\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = \sqrt{(30)"))
		self.play(Transform(regvec, complexdecompveclength6))
		self.wait(6)

		complexdecompveclength7 = (Tex(r"Normalize(\ket{x}) = \frac{2+i}{\sqrt{(30})}\begin{bmatrix} 1 \\ 0 \end{bmatrix} + \frac{3+4i}{\sqrt{(30})}\begin{bmatrix} 0 \\ 1 \end{bmatrix} \textrm{   } Length = 1"))
		self.play(Transform(regvec, complexdecompveclength7))
		self.wait(12)






































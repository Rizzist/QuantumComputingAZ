from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Inner Product, Outer Product, Adjoint")
		self.play(FadeIn(text))
		self.wait(3)

class InnerScene(Scene):
	def construct(self):
		text = Text("Inner Product, Outer Product, Adjoint")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		self.remove(text)
		thequestion = Text("What is an Inner Product?")
		self.play(FadeIn(thequestion))
		self.wait(1)
		thequestion.generate_target()
		thequestion.target.shift(UP*3.5)
		self.play(MoveToTarget(thequestion))

		starterkit = Tex(r"\vec{A}, \vec{B} \in \mathbb{R}^2")
		starterkit.shift(DOWN*3)
		self.play(FadeIn(starterkit))

		#show the dot product
		thedot = Tex(r"\vec{A}\cdot\vec{B}")
		self.play(FadeIn(thedot))
		self.wait(2)

		thedot2 = Tex(r"\vec{A}\cdot\vec{B} = \sum_{i=1}^{n} a_i*b_i")
		self.play(Transform(thedot, thedot2))
		self.wait(3)

		thedot3 = Tex(r"\vec{A}\cdot\vec{B} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}\cdot\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \sum_{i=1}^{n} a_i*b_i")
		self.play(Transform(thedot, thedot3))
		self.wait(3)

		line = Arrow(DOWN*0.75, UP*0.75, fill_color=RED)
		line.shift(DOWN*1.3 + LEFT * 1)
		self.play(FadeIn(line))

		line.generate_target()
		line.target.shift(RIGHT*1.3)
		self.play(MoveToTarget(line))

		self.play(FadeOut(line))
		self.remove(line)

		thedot4 = Tex(r"\vec{A}\cdot\vec{B} = \begin{bmatrix} a_1 & a_2 \end{bmatrix}\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = a_1*b_1 + a_2*b_2")
		self.play(Transform(thedot, thedot4))
		self.wait(6)
		self.play(FadeOut(thedot))



		#geometric
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(ShowCreation(axes))  
		self.play(ShowCreation(grid))  
		#self.wait(1)
		x = 0
		a = 1 * np.sin(x)
		b = 1 * np.cos(x)
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
		#setup vectors above

		#setup dotproduct
		#Text("a^{", i, "}")
		thexdot = Tex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}\cdot\vec{A} = \sum_{i=1}^{n} x_i*a_i")
		thexdot.shift(UP*2)
		self.play(FadeIn(thexdot))


	

	
		# ValueTrackers definition
		x_value = ValueTracker(0)
		# DecimalNumber definition
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		# TeX labels definition
		x_label = Text("Dot Product = ")
		# Grouping of labels and numbers
		# Align labels and numbers
		x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
		group = VGroup(x_tex,x_label).scale(1)
		self.add(group.shift(RIGHT * 2.5 + DOWN*1.5))
		
		self.wait(3)




		
		#self.wait(2)
		while(x<6.28*2):
			x+=0.03
			a = 1 * np.sin(x)
			b = 1 * np.cos(x)
			self.play(
				x_value.set_value,float("{:.2f}".format(a)),
				rate_func=linear,
				run_time=0.0001
			)
			self.wait(0.0001)
		self.remove(vectorX)
		self.play(FadeOut(vector))
		self.wait(1)
		self.remove(vector)
		self.play(FadeOut(axes)) 
		self.play(FadeOut(grid)) 
		self.play(FadeOut(thexdot))
		self.play(FadeOut(group))
		self.play(FadeOut(thequestion))
		self.remove(thexdot, group, thequestion)
		self.wait(1)



		#the equation,, general dot product
		thedot5 = Tex(r"\langle \vec{A},\vec{A} \rangle = \begin{bmatrix} a_1 & a_2 \end{bmatrix}\cdot\begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = a_1*a_1 + a_2*a_2")
		self.play(FadeIn(thedot))
		self.wait(3)
		self.play(Transform(thedot, thedot5))
		self.wait(8)


		#thecomplexlaws
		complexlaw = Tex(r"\textrm{1. All qubits are in } \mathbb{C}^2")
		complexlaw.move_to(UP * 3.5)
		self.play(FadeIn(complexlaw))
		complexlaw2 = Tex(r"\textrm{2. The Euclidean Norm of all Qubits is 1 }")
		complexlaw2.move_to(UP * 2.85)
		self.play(FadeIn(complexlaw2))

		self.wait(5)
		#the equation,, general dot product
		thedot6 = Tex(r"\langle\vec{A},\vec{A}\rangle = \begin{bmatrix} a_1 & a_2 \end{bmatrix}\cdot\begin{bmatrix} a_1 \\ a_2 \end{bmatrix} ?= a_1*a_1 + a_2*a_2 ?= 1")
		self.play(FadeOut(thedot))
		self.play(Write(thedot6))

		self.wait(10)
		thedot7 = Tex(r"\langle\vec{A}\mid\vec{A}\rangle = \begin{bmatrix} a_1 & a_2 \end{bmatrix}\cdot\begin{bmatrix} a_1 \\ a_2 \end{bmatrix} ?= a_1*a_1 + a_2*a_2 ?= 1")
		self.play(Transform(thedot6, thedot7))


		self.wait(3)
		starterkitcomplex = Tex(r"\ket{A}, \ket{B} \in \mathbb{C}^2")
		starterkitcomplex.shift(DOWN*3)
		self.play(Transform(starterkit, starterkitcomplex))

		self.wait(10)
		thedot8 = Tex(r"\langle\vec{A}\mid\vec{A}\rangle = \begin{bmatrix} a_1^* & a_2^* \end{bmatrix}\begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = a_1^*a_1 + a_2^*a_2 = 1")
		thedot8.shift(UP*1.6)
		self.play(Transform(thedot6, thedot8))

		self.wait(5)
		thedot91 = Tex(r"\mid\vec{A}\rangle = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} ")
		self.play(Write(thedot91))

		self.wait(4)
		thedot92 = Tex(r"\langle\vec{A}\mid = ? ")
		thedot92.shift(DOWN*1.6)
		self.play(Write(thedot92))

		self.wait(5)
		thedot921 = Tex(r"\langle\vec{A}\mid = \begin{bmatrix} a_1^* & a_2^* \end{bmatrix} ")
		thedot921.shift(DOWN*1.6)
		self.play(Transform(thedot92, thedot921))
		self.wait(5)
		self.play(FadeOut(thedot6))
		self.play(FadeOut(thedot91))
		self.play(FadeOut(thedot92))
		self.remove(thedot6, thedot92, thedot91)

		self.wait(2)
		thehermitian = Tex(r"(\mid\vec{A}\rangle)^\dag = (\begin{bmatrix} a_1 \\ a_2 \end{bmatrix})^\dag ")
		self.play(Write(thehermitian))

		self.wait(6)
		thehermitian2 = Tex(r"(\mid\vec{A}\rangle)^\dag = (\begin{bmatrix} a_1 & a_2 \end{bmatrix})^* ")
		self.play(Transform(thehermitian, thehermitian2))

		self.wait(4)
		thehermitian3 = Tex(r"(\mid\vec{A}\rangle)^\dag = (\begin{bmatrix} a_1^* & a_2^* \end{bmatrix}) ")
		self.play(Transform(thehermitian, thehermitian3))

		self.wait(4)
		thehermitian3 = Tex(r"\langle\vec{A}\mid = \begin{bmatrix} a_1^* & a_2^* \end{bmatrix} ")
		self.play(Transform(thehermitian, thehermitian3))

		self.wait(3)
		self.play(FadeOut(thehermitian))
		self.remove(thehermitian)

		thefinalproduct = Tex(r"\langle\vec{A}\mid\vec{B}\rangle = \begin{bmatrix} a_1^* & a_2^* \end{bmatrix}\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = a_1^*b_1 + a_2^*b_2")
		self.play(FadeIn(thefinalproduct))

		self.wait(4)
		thefinalproduct2 = Tex(r"\langle\vec{A}\mid\vec{B}\rangle = \begin{bmatrix} a_1^* & a_2^* \end{bmatrix}\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \sum_{i=1}^{n} a_i*b_i")
		self.play(Transform(thefinalproduct, thefinalproduct2))
		self.wait(8)
		self.play(FadeOut(thefinalproduct))

		#talk about outer product
		theouterproduct = Tex(r"(\langle\vec{A}\mid\vec{A}\rangle)(\langle\vec{B}\mid\vec{B}\rangle) = 1")
		self.play(FadeIn(theouterproduct))

		self.wait(15)
		theouterproduct2 = Tex(r"\langle\vec{A} \textrm{   } (\mid\vec{A}\rangle\langle\vec{B}\mid) \textrm{   } \vec{B}\rangle = 1")
		self.play(Transform(theouterproduct, theouterproduct2))

		self.wait(5)
		theouterproduct3 = Tex(r"(\mid\vec{A}\rangle\langle\vec{B}\mid) = ?")
		self.play(Transform(theouterproduct, theouterproduct3))
		theouterproduct3.shift(UP*2)
		self.play(Transform(theouterproduct, theouterproduct3))
		self.wait(3)
		#matrix analysis
		theouterproduct4 = Tex(r"\langle\vec{A} \textrm{   } (\mid\vec{A}\rangle\langle\vec{B}\mid) \textrm{   } \vec{B}\rangle = 1")
		theouterproduct4.shift(UP*2)
		self.play(FadeOut(theouterproduct))
		self.play(FadeIn(theouterproduct4))

		leftside = Text(r"1 x n")
		leftside.shift(LEFT*2).scale(0.5)
		midside = Text(" ? ")
		midside.shift(LEFT*0.5).scale(0.5)
		rightside = Text(r"n x 1")
		rightside.shift(RIGHT*1).scale(0.5)
		result = Text(r"1x1")
		result.shift(RIGHT*2).scale(0.5)

		self.play(Write(leftside))
		self.play(Write(midside))
		self.play(Write(rightside))
		self.play(Write(result))

		self.wait(3)
		self.play(Transform(midside, Text(" n x n ").shift(LEFT*0.5).scale(0.5)))
		self.wait(2)
		self.remove(leftside, midside, rightside, result)

		theouterproduct10 = Tex(r"(\mid\vec{A}\rangle\langle\vec{B}\mid) = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}\begin{bmatrix} b_1^* & b_2^* \end{bmatrix} ")
		self.play(Transform(theouterproduct4, theouterproduct10))

		self.wait(4)
		theouterproduct11 = Tex(r"(\mid\vec{A}\rangle\langle\vec{B}\mid) = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}\begin{bmatrix} b_1^* & b_2^* \end{bmatrix} = \begin{bmatrix} a_1b_1^* & a_1b_2^* \\ a_2b_1^* & a_2b_2^* \end{bmatrix}")
		self.play(Transform(theouterproduct4, theouterproduct11))
		self.wait(5)
























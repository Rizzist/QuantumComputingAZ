from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Bell Space, Schmidt Decomposition, Entanglement").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class bell(Scene):
	def construct(self):
		text = Text("Schmidt Decomposition, Bell States, Entanglement").scale(0.8)
		self.play(FadeIn(text))
		self.wait(6)
		self.play(FadeOut(text))




		#its psi
		title = Text("State Space").shift(UP*3.5)
		itsphi = Tex(r"\ket{\phi} = a_0 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_1  \begin{bmatrix} 0 \\ 1 \end{bmatrix}")
		self.play(FadeIn(title), FadeIn(itsphi))
		self.wait(3)
		itsphi.generate_target()
		itsphi.target = Tex(r"\ket{\phi} = a_0 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_1  \begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(LEFT*3)

		itsphiq = Tex(r"\ket{\psi} = b_0 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + b_1  \begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(RIGHT*3)
		self.play(FadeIn(itsphiq), MoveToTarget(itsphi))
		self.wait(3)

		howcombine = Tex(r"\ket{\phi\psi} = ?").shift(DOWN*2)
		self.play(FadeIn(howcombine))
		self.wait(6)
		itgroup = Group(howcombine, itsphi, itsphiq)
		self.play(FadeOut(itgroup))




		#its schmidt
		title2 = Text("Schmidt Decomposition").shift(UP*3.5)
		self.play(Transform(title, title2))

		whatitsin = Tex(r"\ket{\psi} \in \mathbb{H}_1 \ \ \ \ket{\phi} \in \mathbb{H}_2 \ \ \ \ \ket{\psi\phi}, \ket{w} \in \mathbb{H}_1 \otimes \mathbb{H}_2").shift(DOWN*3.3)
		self.play(Write(whatitsin))
		self.wait(4)

		itsbasis = Tex(r"\{ A_0, A_1, ...\} \ \ \ A_i \in \mathbb{H}_1 \ \ \ \ \ \ \{ B_0, B_1, ...\} \ \ \ B_i \in \mathbb{H}_2").shift(DOWN*2)
		self.play(FadeIn(itsbasis))
		self.wait(4)

		representit = Tex(r"\ket{\psi} = \sum_{i=0}^{n} a_iA_i \ \ \ \ \ \ \ket{\phi} = \sum_{j=0}^{m} b_jB_j").shift(DOWN*0.7)
		self.play(Write(representit))
		self.wait(4)

		its = Tex(r"\ket{w} = \sum_{0 \leq i \leq n, 1 \leq j \leq m}^{} c_{ij} A_i \otimes B_j").shift(UP*1)
		self.play(FadeIn(its))
		self.wait(4)

		its2 = Tex(r"\ket{\psi\phi} = \sum_{0 \leq i \leq n, 1 \leq j \leq m}^{} (a_ib_j) A_i \otimes B_j").shift(UP*1)
		self.play(Transform(its, its2))
		self.wait(6)



		#example
		itsbasis2 = Tex(r"\{ \ket{0}, \ket{1}  \} \ \ \ \ket{i} \in \mathbb{H}_1 \ \ \ \ \ \ \{ \ket{0}, \ket{1} \} \ \ \ \ket{j} \in \mathbb{H}_2").shift(DOWN*2)
		self.play(Transform(itsbasis, itsbasis2))
		self.wait(4)

		representit2 = Tex(r"\ket{\psi} = \sum_{i=0}^{n} a_i\ket{i} \ \ \ \ \ \ \ket{\phi} = \sum_{j=0}^{m} b_j\ket{j}").shift(DOWN*0.7)
		self.play(Transform(representit, representit2))
		self.wait(4)

		its2 = Tex(r"\ket{\psi\phi} = \sum_{0 \leq i \leq n, 1 \leq j \leq m}^{} (a_ib_j) \ket{i} \otimes \ket{j}").shift(UP*1)
		self.play(FadeOut(its), FadeIn(its2))
		self.wait(4)

		#the up shot
		its3 = Tex(r"\ket{\psi\phi} = \sum_{0 \leq i \leq n, 1 \leq j \leq m}^{} (a_ib_j) \ket{i} \otimes \ket{j} = \sum_{0 \leq i \leq n, 1 \leq j \leq m}^{} (a_ib_j) \ket{ij}").shift(UP*1)
		self.play(FadeOut(its2), FadeIn(its3))
		self.wait(4)

		groupitUp = Group(itsbasis, representit, its3)
		self.play(FadeOut(groupitUp))





		#REAL EXAMPLE
		letstry = Tex(r"\ket{\psi\phi} = a_0b_0 \ket{0}\otimes\ket{0} + a_0b_1 \ket{0}\otimes\ket{1} + a_1b_0 \ket{1}\otimes\ket{0} + a_1b_1 \ket{1}\otimes\ket{1}").scale(0.9).shift(UP*2.5)
		self.play(FadeIn(letstry))
		self.wait(3)

		dotensorproduct = Tex(r"\ket{\psi\phi} = a_0b_0 \begin{bmatrix} 1 \\ 0 \end{bmatrix}\otimes\begin{bmatrix} 1 \\ 0 \end{bmatrix}+ a_0b_1 \begin{bmatrix} 1 \\ 0 \end{bmatrix}\otimes\begin{bmatrix} 0 \\ 1 \end{bmatrix} + a_1b_0 \begin{bmatrix} 0 \\ 1 \end{bmatrix}\otimes\begin{bmatrix} 1 \\ 0 \end{bmatrix} + a_1b_1 \begin{bmatrix} 0 \\ 1 \end{bmatrix}\otimes\begin{bmatrix} 0 \\ 1 \end{bmatrix}").scale(0.9).shift(UP*1.5)
		self.play(FadeIn(dotensorproduct))
		self.wait(3)

		dotensorproduct2 = Tex(r"\ket{\psi\phi} = a_0b_0 \begin{bmatrix} 1\begin{bmatrix} 1 \\ 0 \end{bmatrix} \\ 0\begin{bmatrix} 1 \\ 0 \end{bmatrix} \end{bmatrix}+ a_0b_1 \begin{bmatrix} 1\begin{bmatrix} 0 \\ 1 \end{bmatrix} \\ 0\begin{bmatrix} 0 \\ 1 \end{bmatrix} \end{bmatrix} + a_1b_0 \begin{bmatrix} 0\begin{bmatrix} 1 \\ 0 \end{bmatrix} \\ 1\begin{bmatrix} 1 \\ 0 \end{bmatrix} \end{bmatrix} + a_1b_1 \begin{bmatrix} 0\begin{bmatrix} 0 \\ 1 \end{bmatrix} \\ 1\begin{bmatrix} 0 \\ 1 \end{bmatrix} \end{bmatrix}").scale(0.9).shift(DOWN*0.5)
		self.play(FadeIn(dotensorproduct2))
		self.wait(3)

		dotensorproduct3 = Tex(r"\ket{\psi\phi} = a_0b_0 \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}+ a_0b_1 \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix} + a_1b_0 \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} + a_1b_1\begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}").shift(DOWN*0.5)
		self.play(Transform(dotensorproduct2, dotensorproduct3))
		self.wait(3)

		letstry2 = Tex(r"\ket{\psi\phi} = a_0b_0 \ket{00} + a_0b_1 \ket{01}+ a_1b_0 \ket{10} + a_1b_1 \ket{11}").shift(DOWN*2.5)
		self.play(FadeIn(letstry2))
		self.wait(3)

		putitallG = Group(letstry, dotensorproduct, dotensorproduct2)
		self.play(FadeOut(putitallG))

		therealbasis = Tex(r"\ket{001011}")
		self.play(Write(therealbasis))

		therealbasis2 = Tex(r"\ket{101011}")
		self.play(Transform(therealbasis, therealbasis2))

		therealbasis3 = Tex(r"\ket{101111}")
		self.play(Transform(therealbasis, therealbasis3))

		therealbasis4 = Tex(r"\ket{111100}")
		self.play(Transform(therealbasis, therealbasis4))

		therealbasis5 = Tex(r"\ket{110110}")
		self.play(Transform(therealbasis, therealbasis5))

		therealbasis5 = Tex(r"\ket{111111}")
		self.play(Transform(therealbasis, therealbasis5))

		therealbasis6 = Tex(r"\ket{000000}")
		self.play(Transform(therealbasis, therealbasis6))

		self.play(FadeOut(therealbasis))


		#NOW DO ONE FOR THE PUBLIC EXAMPLE
		q1 = Tex(r"\ket{\psi} = \ket{0}").shift(LEFT*4)
		q2 = Tex(r"\ket{\phi} = \frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}").shift(RIGHT*3)
		q3 = Tex(r"\ket{\psi\phi} = ?").shift(UP*2)
		self.play(FadeIn(q1), FadeIn(q2), FadeIn(q3))
		self.wait(13)

		q32 = Tex(r"\ket{\psi\phi} = a_0b_0 \ket{00} + a_0b_1 \ket{01}+ a_1b_0 \ket{10} + a_1b_1 \ket{11}").shift(UP*2)
		self.play(Transform(q3, q32))
		self.wait(5)

		q33 = Tex(r"\ket{\psi\phi} = (1)(\frac{1}{\sqrt{(2})}) \ket{00} + (1)(\frac{1}{\sqrt{(2})}) \ket{01}+ (0)(\frac{1}{\sqrt{(2})}) \ket{10} + (0)(\frac{1}{\sqrt{(2})}) \ket{11}").scale(0.8).shift(UP*2)
		self.play(Transform(q3, q33))
		self.wait(5)

		q34 = Tex(r"\ket{\psi\phi} = \frac{1}{\sqrt{(2})} \ket{00} + \frac{1}{\sqrt{(2})} \ket{01}").shift(UP*2)
		self.play(Transform(q3, q34))
		self.wait(6)

		anotherg = Group(q1, q2, q3)
		self.play(FadeOut(anotherg), FadeOut(whatitsin), FadeOut(letstry2))

		#is schmidt always possible?
		title3 = Text("Schmidt Decomposition?").shift(UP*3.5)
		self.play(Transform(title, title3))
		bell1 = Tex(r"\ket{w} = \frac{1}{\sqrt{(2})} \ket{00} + \frac{1}{\sqrt{(2})} \ket{11}").shift(UP*2)
		self.play(FadeIn(bell1))
		self.wait(3)

		title4 = Text("Bell States").shift(UP*3.5)
		self.play(Transform(title, title4))

		bell11 = Tex(r"\ket{B_0} = \frac{1}{\sqrt{(2})} \ket{00} + \frac{1}{\sqrt{(2})} \ket{11}").shift(UP*2)
		self.play(Transform(bell1, bell11))
		self.wait(3)

		bell2 = Tex(r"\ket{B_1} = \frac{1}{\sqrt{(2})} \ket{01} + \frac{1}{\sqrt{(2})} \ket{10}").shift(UP*0.5)
		self.play(FadeIn(bell2))
		self.wait(3)

		bell3 = Tex(r"\ket{B_2} = \frac{1}{\sqrt{(2})} \ket{01} - \frac{1}{\sqrt{(2})} \ket{10}").shift(DOWN*1)
		self.play(FadeIn(bell3))
		self.wait(3)

		bell4 = Tex(r"\ket{B_3} = \frac{1}{\sqrt{(2})} \ket{00} - \frac{1}{\sqrt{(2})} \ket{11}").shift(DOWN*2.5)
		self.play(FadeIn(bell4))
		self.wait(3)

		self.play(FadeOut(bell2), FadeOut(bell3), FadeOut(bell4))

		exB = Tex(r"\ket{\psi\phi} = \ket{B_0}")
		self.play(Write(exB))
		self.wait(3)

		#show it
		psi = Tex(r"\ket{\psi}")
		psic = Circle(color=YELLOW)
		psG = Group(psi, psic)
		psG.shift(DOWN*2 + LEFT*1)
		self.play(FadeIn(psG))

		phi = Tex(r"\ket{\phi}")
		phic = Circle(color=YELLOW)
		phG = Group(phi, phic)
		phG.shift(DOWN*2 + RIGHT*1)
		self.play(FadeIn(phG))

		psG.generate_target()
		psG.target.shift(LEFT*3)
		phG.generate_target()
		phG.target.shift(RIGHT*3)
		self.play(MoveToTarget(psG), MoveToTarget(phG))

		psi.generate_target()
		psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)

		phi.generate_target()
		phi.target = Tex(r"\ket{?}").shift(DOWN*2 + RIGHT*4)

		self.play(MoveToTarget(psi), MoveToTarget(phi))
		self.wait(6)

		psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)
		phi.target = Tex(r"\ket{0}").shift(DOWN*2 + RIGHT*4)
		self.play(MoveToTarget(psi), MoveToTarget(phi))

		psi.target = Tex(r"\ket{1}").shift(DOWN*2 + LEFT*4)
		phi.target = Tex(r"\ket{1}").shift(DOWN*2 + RIGHT*4)
		self.play(MoveToTarget(psi), MoveToTarget(phi))

		title5 = Text("Entanglement").shift(UP*3.5)
		self.play(Transform(title, title5))
		for i in range(0, 7):
			psi.target = Tex(r"\ket{0}").shift(DOWN*2 + LEFT*4)
			phi.target = Tex(r"\ket{0}").shift(DOWN*2 + RIGHT*4)
			self.play(MoveToTarget(psi), MoveToTarget(phi))

			psi.target = Tex(r"\ket{1}").shift(DOWN*2 + LEFT*4)
			phi.target = Tex(r"\ket{1}").shift(DOWN*2 + RIGHT*4)
			self.play(MoveToTarget(psi), MoveToTarget(phi))
		self.wait(12)







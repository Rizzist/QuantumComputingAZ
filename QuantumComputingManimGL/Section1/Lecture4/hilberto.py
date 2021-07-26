from manimlib import *
import numpy as np

class FirstScene(ThreeDScene):
	def construct(self):
		text = Text("Postulate of Quantum Mechanics I, Hilbert Space")
		self.play(FadeIn(text))
		self.wait(3)

class Hilbi(ThreeDScene):
	def construct(self):
		text = Text("Postulate of Quantum Mechanics I, Hilbert Space").scale(0.8)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		ithasbasis = Text("Basis Decomposition").shift(UP*3)
		bro = Tex(r"\ket{\psi}")
		itsanc2 = Tex(r"\ket{\psi} \in \mathbb{C}^2").shift(DOWN*3)
		self.play(FadeIn(ithasbasis))
		self.play(Write(itsanc2))
		self.play(Write(bro))
		self.wait(1)
		bro2 = Tex(r"\ket{\psi} = \sum_{i=1}^{n} a_i\ket{B_i}").shift(UP*1.8)
		basisors = Tex(r"\left\{B_1, B_2, ... \right\}").shift(DOWN*0.5)
		conditions = Text("Linearly Independent, Span Covers Space, Mutually Orthogonal").shift(DOWN*1.75).scale(0.6)
		itsacomplex = Tex(r"a_i \in \mathbb{C}")
		itsacomplex.move_to(UP*0.5)
		self.play(Transform(bro, bro2))
		self.play(Write(itsacomplex))
		self.wait(6)
		self.play(Write(basisors))
		self.wait(3)
		self.play(Write(conditions))
		self.wait(6)

		bro3 = Tex(r"\ket{\psi} = \sum_{i=1}^{n} a_i\ket{B_i}").shift(UP*1.8)

		self.play(Transform(bro, bro3))
		self.wait(6)

		itsanc23 = Tex(r"\ket{\psi} \in \mathbb{C}^2 + \langle , \rangle").shift(DOWN*3)
		self.play(Transform(itsanc2, itsanc23))
		self.wait(4)

		itsanc24 = Tex(r"\ket{\psi} \in \mathbb{C}^2 + \langle , \rangle = \mathbb{H}^2").shift(DOWN*3)
		self.play(Transform(itsanc2, itsanc24))

		self.wait(5)
		ithasbasis2 = Text("Postulate of Quantum Mechanics I").shift(UP*3)
		self.play(Transform(ithasbasis, ithasbasis2))
		self.wait(10)
















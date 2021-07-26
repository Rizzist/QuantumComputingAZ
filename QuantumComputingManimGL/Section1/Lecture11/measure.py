from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("3rd Postulate of QM, Measurement, Born Rule").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class m(Scene):
	def construct(self):
		text = Text("3rd Postulate of QM, Measurement, Born Rule")
		self.play(FadeIn(text))
		self.wait(6)
		self.play(FadeOut(text))
		title = Text("3rd Postulate of QM: Observables").shift(UP*3.5)
		self.play(Write(title))

		content = Text("All observables are associated with eigenvalues when measured").scale(0.6).shift(DOWN*3.5)
		self.play(Write(content))
		self.wait(4)
		item = Tex(r"B\ket{\psi} = \lambda\ket{\psi}")
		self.play(Write(item))
		self.wait(8)
		item2 = Tex(r"\bra{\psi}B^\dag B\ket{\psi} = \lambda^\dag\lambda")
		self.play(Transform(item, item2))
		self.wait(8)
		self.play(FadeOut(item))


		#write down math
		title2 = Text("Measurement").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		poperator = Tex(r"\bra{v}P\ket{v} = \bra{v}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\ket{v} =  a_i^*a_i")
		self.play(FadeIn(poperator))
		self.wait(5)
		poperator2 = Tex(r"\bra{v}P\ket{v} = \bra{v}\ket{0}\bra{0}\ket{v} =  a_0^*a_0")
		self.play(Transform(poperator, poperator2))
		self.wait(3)
		poperator3 = Tex(r"\bra{v}M_0\ket{v} = \bra{v}\ket{0}\bra{0}\ket{v} =  a_0^*a_0").shift(DOWN*0.3)
		self.play(Transform(poperator, poperator3))
		self.wait(3)
		itsap = Tex(r"M_0 = \ket{0}\bra{0}").shift(DOWN*2 + LEFT*3.5)
		itsapd = Tex(r"M_1 = \ket{1}\bra{1}").shift(DOWN*2 + RIGHT*3.5)
		self.play(Write(itsap), Write(itsapd))
		self.wait(6)
		itsapq = Tex(r"M = \sum_{i=0}^{n} c_i\ket{i}\bra{i}").shift(UP*1)
		

		#born rule
		title3 = Text("Born Rule").shift(UP*3.5)
		self.play(Transform(title, title3))
		expM = Tex(r"E(M) = \sum_{i=0}^{n}c_ia_i^*a_i").shift(UP*2.4)
		self.play(Write(expM))
		self.wait(5)

		expM1 = Tex(r"E(M_0) = a_0^*a_0").shift(UP*2)
		self.play(Transform(expM, expM1))
		self.wait(5)

		testsample = Tex(r"\{ a_0^*a_0 - 0.6, a_0^*a_0 + 3, a_0^*a_0 + 0.002, a_0^*a_0 - 2.01, a_0^*a_0 - 0.388 \}").shift(UP*0.7)
		self.play(Write(testsample))
		self.wait(5)
		expM1 = Tex(r"E(M) = \sum_{i=0}^{n}c_ia_i^*a_i").shift(UP*2.4)

		self.play(FadeOut(testsample), FadeOut(expM), FadeOut(itsap), FadeOut(itsapd), FadeOut(poperator), FadeIn(expM1))

		#example
		expMW = Tex(r"E(M) = c_0a_0^*a_0 + c_1a_1^*a_1").shift(UP*1)
		self.play(Write(expMW))
		self.wait(5)

		expMWW = Tex(r"E(M) = c_0 \bra{v}\ket{0}\bra{0}\ket{v} + c_1 \bra{v}\ket{1}\bra{1}\ket{v}")
		self.play(Write(expMWW))
		self.wait(5)

		expMWWW = Tex(r"E(M) = \bra{v} \sum_{i=0}^{n}c_i\ket{i}\bra{i} \ket{v} ").shift(DOWN*1)
		self.play(Write(expMWWW))
		self.wait(5)

		#poperatorw2 = Tex(r"\bra{v}M\ket{v} = \bra{v} \sum_{i=0}^{n} c_i\ket{i}\bra{i} \ket{v} =  E(M)").shift(DOWN*0.3)
		#self.play(Transform(poperator, poperatorw2))

		poperatorw3 = Tex(r"\bra{v}M\ket{v} = E(M)").shift(DOWN*1)
		self.play(Transform(expMWWW, poperatorw3))
		self.wait(5)

		self.play(FadeOut(expMW), FadeIn(itsapq))
		itsapq2 = Tex(r"M = \sum_{i=0}^{n} \lambda_i\ket{\lambda_i}\bra{\lambda_i}").shift(DOWN*2)
		self.play(Transform(itsapq, itsapq2))
		self.wait(5)
		itsbounding = SurroundingRectangle(itsapq)
		self.play(ShowCreation(itsbounding))
		self.wait(5)
		itsGrouper = Group(itsapq, expMWW, expMWWW, itsbounding)
		self.play(FadeOut(itsGrouper))


		#go back to postulate
		title6 = Text("3rd Postulate of QM: Observables").shift(UP*3.5)
		self.play(Transform(title, title6))

		poperatorw4 = Tex(r"B\ket{v} = \lambda\ket{v}").shift(DOWN*0.3)
		self.play(FadeIn(poperatorw4))
		self.wait(5)

		poperatorw5 = Tex(r"B\ket{v} = \sum_{i=0}^{n} \lambda_i\ket{i}\bra{i} \ket{v}")
		self.play(Transform(poperatorw4, poperatorw5))
		self.wait(5)

		poperatorw5 = Tex(r"B\ket{v} = \sum_{i=0}^{n} \lambda_ia_i\ket{i}")
		self.play(Transform(poperatorw4, poperatorw5), FadeOut(expM1))
		self.wait(5)

		poperatorw6 = Tex(r"B\ket{v} = \sum_{i=0}^{n} \lambda_ia_i\ket{i} = \lambda\ket{v}")
		self.play(Transform(poperatorw4, poperatorw6))
		self.wait(5)

		#what measurement actually means, example
		self.play(FadeOut(poperatorw4), FadeOut(content))
		title7 = Text(r"Measure").shift(UP*3.5)
		self.play(FadeOut(title),FadeIn(title7))

		item = Tex(r"\ket{\psi} = \frac{i}{\sqrt{(5})} \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \frac{2}{\sqrt{(5})} \begin{bmatrix} 0 \\ 1 \end{bmatrix}").shift(UP*2.5)
		self.play(Write(item))
		self.wait(5)

		problem = Tex(r"Calculate \bra{\psi}M_0\ket{\psi}").shift(DOWN*3)
		self.play(Write(problem))


		self.wait(14)

		sol1 = Tex(r"\bra{\psi} M_0 \ket{\psi} = (\frac{-i}{\sqrt{(5})} \bra{0} + \frac{2}{\sqrt{(5})} \bra{1}) \ \ (\ket{0}\bra{0}) \ \ (\frac{i}{\sqrt{(5})} \ket{0} + \frac{2}{\sqrt{(5})} \ket{1})").scale(0.95).shift(UP*1)
		self.play(Write(sol1))
		self.wait(5)

		sol2 = Tex(r"\bra{\psi} M_0 \ket{\psi} = (\frac{-i}{\sqrt{(5})} \bra{0}\ket{0})(\frac{i}{\sqrt{(5})} \bra{0}\ket{0})").shift(DOWN*0.3)
		self.play(Write(sol2))
		self.wait(5)

		sol3 = Tex(r"\bra{\psi} M_0 \ket{\psi} = \frac{1}{5}").shift(DOWN*1.7)
		self.play(Write(sol3))
		self.wait(5)

		sol4 = Tex(r"\bra{\psi} M_0 \ket{\psi} = \frac{1}{5} = (\frac{i}{\sqrt{(5})})^*\frac{i}{\sqrt{(5})} ").shift(DOWN*1.7)
		self.play(Transform(sol3, sol4))
		self.wait(5)












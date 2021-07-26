from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Eigenvector, Eigenvalue, Diagonalization").scale(0.8)
		self.play(FadeIn(text))
		self.wait(3)


class eigo(Scene):
	def construct(self):
		text = Text("Eigenvector, Eigenvalue, Diagonalization").scale(0.9)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		#show matrix
		title = Text("Eigenvalue").shift(UP*3.5)
		self.play(Write(title))
		self.wait(3)
		ematrix = Tex(r"A\vec{v} = a_1\vec{v}")
		self.play(FadeIn(ematrix))
		self.wait(4)		
		ematrix2 = Tex(r"A\vec{v} = \lambda\vec{v}")
		self.play(Transform(ematrix, ematrix2))
		self.wait(7)

		ematrix3 = Tex(r"A\vec{v} = \lambda\mathbb{I}\vec{v}")
		self.play(Transform(ematrix, ematrix3))
		self.wait(3)

		ematrix4 = Tex(r"A\vec{v} - \lambda\mathbb{I}\vec{v} = 0")
		self.play(Transform(ematrix, ematrix4))
		self.wait(3)

		ematrix5 = Tex(r"(A - \lambda\mathbb{I})\vec{v} = 0")
		self.play(Transform(ematrix, ematrix5))
		self.wait(3)

		detem = Tex(r"det(A - \lambda\mathbb{I}) = 0").shift(DOWN*1)
		self.play(Write(detem))
		self.wait(5)

		ematrix.generate_target()
		detem.generate_target()
		detem.target.shift(LEFT*3)
		ematrix.target.shift(LEFT*3)
		self.play(MoveToTarget(detem), MoveToTarget(ematrix))

		exmatrix = Tex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}").shift(RIGHT*3)
		self.play(Write(exmatrix))
		self.wait(3)

		exmatrix2 = Tex(r"A - \lambda\mathbb{I} = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}").shift(RIGHT*3)
		self.play(Transform(exmatrix, exmatrix2))
		self.wait(3)

		exmatrix3 = Tex(r"A - \lambda\mathbb{I} = \begin{bmatrix} 1-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix}").shift(RIGHT*3)
		self.play(Transform(exmatrix, exmatrix3))
		self.wait(3)

		exdetem = Tex(r"det(A - \lambda\mathbb{I}) = (1-\lambda)(2-\lambda) = 0").shift(RIGHT*3 + DOWN*1)
		self.play(Write(exdetem))
		self.wait(3)


		upperlupper = Tex(r"\lambda_1 = 1 \quad \lambda_2 = 2").shift(DOWN*2)
		self.play(Write(upperlupper))
		self.wait(3)

		eigenvectorG = Group(upperlupper, exdetem, detem, exmatrix, ematrix)
		eigenvectorG.generate_target()
		eigenvectorG.target.shift(UP*2.6)
		self.play(MoveToTarget(eigenvectorG))

		title2 = Text("Eigenvector").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.wait(3)

		surrounder = SurroundingRectangle(ematrix)
		self.play(Write(surrounder))

		e2matrix = Tex(r"(A - \lambda_1\mathbb{I})\vec{v} = 0").shift(LEFT*3)
		e3matrix = Tex(r"(A - \lambda_2\mathbb{I})\vec{v} = 0").shift(RIGHT*3)
		self.play(Write(e2matrix), Write(e3matrix))
		self.wait(3)

		smatrix = Tex(r"\begin{bmatrix} 1-\lambda_1 & 1 \\ 0 & 2-\lambda_1 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(LEFT*3 + DOWN*2)
		s2matrix = Tex(r"\begin{bmatrix} 1-\lambda_2 & 1 \\ 0 & 2-\lambda_2 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(RIGHT*3 + DOWN*2)
		self.play(Write(smatrix), Write(s2matrix))
		self.wait(3)

		smatrix2 = Tex(r"\begin{bmatrix} 1-1 & 1 \\ 0 & 2-1 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(LEFT*3 + DOWN*2)
		s2matrix2 = Tex(r"\begin{bmatrix} 1-2 & 1 \\ 0 & 2-2 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(smatrix, smatrix2), Transform(s2matrix, s2matrix2))
		self.wait(3)

		smatrix3 = Tex(r"\begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(LEFT*3 + DOWN*2)
		s2matrix3 = Tex(r"\begin{bmatrix} -1 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \vec{0}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(smatrix, smatrix3), Transform(s2matrix, s2matrix3))
		self.wait(3)

		smatrix4 = Tex(r"\begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \vec{0}").shift(LEFT*3 + DOWN*2)
		s2matrix4 = Tex(r"\begin{bmatrix} -1 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \vec{0}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(smatrix, smatrix4), Transform(s2matrix, s2matrix4))
		self.wait(3)

		smatrix5 = Tex(r"\begin{bmatrix} 1 \\ 0 \end{bmatrix}").shift(LEFT*3 + DOWN*2)
		s2matrix5 = Tex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(smatrix, smatrix5), Transform(s2matrix, s2matrix5))
		self.wait(6)

		oggroup = Group(eigenvectorG, surrounder, e2matrix, e3matrix, smatrix, s2matrix)
		self.play(FadeOut(oggroup))

		#diagonalization
		title3 = Text("Diagonalization").shift(UP*3.5)
		self.play(Transform(title, title3))
		self.wait(3)


		wmatrix = Tex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}").shift(LEFT*4 + UP*2)
		self.play(Write(wmatrix))
		dupper = Tex(r"\lambda_1 = 1 \quad \lambda_2 = 2").shift(LEFT*4)
		self.play(Write(dupper))
		evectors = Tex(r"\vec{v_1} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}").shift(LEFT*5 + DOWN*2)
		e2vectors = Tex(r"\vec{v_2} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}").shift(LEFT*3 + DOWN*2)
		self.play(Write(evectors), Write(e2vectors))
		self.wait(6)
		diagonal = Tex(r"A = PDP^{-1}").shift(RIGHT*4 + UP*2)
		self.play(Write(diagonal))
		self.wait(5)
		resulter = Tex(r"A = \begin{bmatrix} \vec{v_1} & \vec{v_2} \end{bmatrix}DP^{-1}").shift(RIGHT*4)
		self.play(Write(resulter))
		self.wait(6)
		resulter2 = Tex(r"A = \begin{bmatrix} \vec{v_1} & \vec{v_2} \end{bmatrix}\begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}P^{-1}").shift(RIGHT*4)
		self.play(Transform(resulter, resulter2))
		self.wait(4)
		resulter3 = Tex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}P^{-1}").shift(RIGHT*3)
		self.play(Transform(resulter, resulter3))
		self.wait(7)

		#inverse matrix
		augmented90 = Tex(r"\begin{bmatrix} P & \mid & \mathbb{I} \end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Write(augmented90))
		self.wait(3)
		augmented = Tex(r"\begin{bmatrix} 1 & 1 & \mid & 1 & 0\\0 & 1 & \mid & 0 & 1\end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(augmented90, augmented))
		self.wait(3)
		augmented2 = Tex(r"\begin{bmatrix} 1 & 0 & \mid & 1 & -1\\0 & 1 & \mid & 0 & 1\end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(augmented90, augmented2))
		self.wait(3)
		augmented3 = Tex(r"\begin{bmatrix} 1 & 0 & \mid & 1 & -1\\0 & 1 & \mid & 0 & 1\end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(augmented90, augmented3))
		self.wait(3)
		augmented4 = Tex(r"\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(augmented90, augmented4))
		self.wait(3)

		resulter4 = Tex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}").shift(RIGHT*4)
		self.play(Transform(resulter, resulter4), FadeOut(augmented90))
		self.wait(3)

		powerit = Tex(r"A^2 = (PDP^{-1})^2").shift(RIGHT*3 + DOWN*2)
		self.play(Write(powerit))
		self.wait(3)
		powerit2 = Tex(r"A^2 = PDP^{-1}PDP^{-1}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(powerit, powerit2))
		self.wait(3)
		powerit3 = Tex(r"A^2 = PD(P^{-1}P)DP^{-1}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(powerit, powerit3))
		self.wait(3)
		powerit3 = Tex(r"A^2 = PD^2P^{-1}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(powerit, powerit3))
		self.wait(3)
		powerit4 = Tex(r"A^n = PD^nP^{-1}").shift(RIGHT*3 + DOWN*2)
		self.play(Transform(powerit, powerit4))
		self.wait(3)

		triplegroup = Group(wmatrix, dupper, evectors, e2vectors, powerit)
		self.wait(15)
		#you can think about it at home






from manimlib import *
import numpy as np

class FirstScene(ThreeDScene):
	def construct(self):
		text = Text("Tensor Product, Unitary Matrices, Quantum Gates").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class TensorBro(ThreeDScene):
	def construct(self):
		text = Text("Tensor Product, Unitary Matrices, Quantum Gates").scale(0.9)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		combiningqubits = Text("Representing Multiple Qubits").shift(UP*3)
		itsaqubits = Tex(r"\ket{\psi}, \ket{\varphi} \in \mathbb{H}^2").shift(DOWN*3)
		self.play(Write(combiningqubits))
		self.play(Write(itsaqubits))
		self.wait(2)
		qubits2 = Tex(r"\ket{\psi}\ket{\varphi}")
		self.play(Write(qubits2))
		self.wait(5)

		itsaqubitsw = Tex(r"\ket{\psi}\ket{\varphi} \in \mathbb{H}^4").shift(DOWN*2)
		self.play(Write(itsaqubitsw))
		self.wait(3)

		qubits3 = Tex(r"\ket{\psi}\ket{\varphi} = \begin{bmatrix} \psi_1 \\ \psi_2  \end{bmatrix} \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix}")
		self.play(Transform(qubits2, qubits3))
		self.wait(3)

		qubits4 = Tex(r"\ket{\psi}\ket{\varphi} = \begin{bmatrix} \psi_1 \\ \psi_2  \end{bmatrix} \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} = \begin{bmatrix}\psi_1\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \\ \psi_2\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \end{bmatrix} ")
		self.play(Transform(qubits2, qubits4))
		self.wait(3)

		qubits5 = Tex(r"\ket{\psi}\ket{\varphi} = \begin{bmatrix} \psi_1 \\ \psi_2  \end{bmatrix} \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} = \begin{bmatrix}\psi_1\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \\ \psi_2\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \psi_1\varphi_1 \\ \psi_1\varphi_2 \\ \psi_2\varphi_1 \\ \psi_2\varphi_2 \end{bmatrix}")
		self.play(Transform(qubits2, qubits5))
		self.wait(6)

		combiningqubits2 = Text("Tensor Product").shift(UP*3)
		self.play(Transform(combiningqubits, combiningqubits2))

		qubits6 = Tex(r"\ket{\psi}\otimes\ket{\varphi} = \begin{bmatrix} \psi_1 \\ \psi_2  \end{bmatrix}\otimes \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} = \begin{bmatrix}\psi_1\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \\ \psi_2\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \psi_1\varphi_1 \\ \psi_1\varphi_2 \\ \psi_2\varphi_1 \\ \psi_2\varphi_2 \end{bmatrix}")
		self.play(Transform(qubits2, qubits6))
		self.wait(3)

		qubits7 = Tex(r"\ket{\psi\varphi} = \begin{bmatrix} \psi_1 \\ \psi_2  \end{bmatrix}\otimes \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} = \begin{bmatrix}\psi_1\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \\ \psi_2\begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \psi_1\varphi_1 \\ \psi_1\varphi_2 \\ \psi_2\varphi_1 \\ \psi_2\varphi_2 \end{bmatrix}")
		self.play(Transform(qubits2, qubits7))
		self.wait(3)

		itsaqubitsw2 = Tex(r"\ket{\psi\varphi} \in \mathbb{H}^4").shift(DOWN*2)
		self.play(Transform(itsaqubitsw, itsaqubitsw))
		self.wait(3)

		self.wait(2)
		qubits8 = Tex(r"\ket{\psi\varphi} = \begin{bmatrix} 1 \\ 0  \end{bmatrix}\otimes \begin{bmatrix} 0 \\ 1  \end{bmatrix} = \begin{bmatrix}1\begin{bmatrix} 0 \\ 1 \end{bmatrix} \\ 0\begin{bmatrix} 0 \\ 1  \end{bmatrix} \end{bmatrix}")
		self.play(Transform(qubits2, qubits8))
		self.wait(3)

		#
		self.play(FadeOut(qubits2))
		self.remove(qubits2)
		qubits9 = Tex(r"\ket{\psi\varphi} = \begin{bmatrix} 1 \\ 0  \end{bmatrix}\otimes \begin{bmatrix} 0 \\ 1  \end{bmatrix} = \begin{bmatrix}1\begin{bmatrix} 0 \\ 1 \end{bmatrix} \\ 0\begin{bmatrix} 0 \\ 1  \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}")
		self.play(FadeIn(qubits9))
		self.wait(6)
		self.play(FadeOut(qubits9))

		qubits10 = Tex(r"\begin{bmatrix} 0 \\ 1  \end{bmatrix}\otimes \begin{bmatrix} 1 \\ 0  \end{bmatrix}")
		self.play(FadeIn(qubits10))
		self.wait(14)
		self.play(FadeOut(qubits10))

		qubits11 = Tex(r"\begin{bmatrix}0\begin{bmatrix} 1 \\ 0 \end{bmatrix} \\ 1\begin{bmatrix} 1 \\ 0  \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}")
		self.play(Write(qubits11))
		self.wait(4)

		self.play(FadeOut(qubits11), FadeOut(combiningqubits), FadeOut(itsaqubitsw), FadeOut(itsaqubits))

		#now do unitary matrices
		unitary = Text("Unitary Matrices").shift(UP*3)
		self.play(Write(unitary))

		itsunitary = Tex(r"U")
		self.play(Write(itsunitary))
		self.wait(4)

		itsunitary2 = Tex(r"U^\dag U = \mathbb{I}")
		self.play(Transform(itsunitary, itsunitary2))
		self.wait(4)

		#property 1: Determinant is 1
		itsunitary21 = Tex(r"det(U^\dag U) = det(\mathbb{I})").shift(DOWN*2)
		self.play(Write(itsunitary21))
		self.wait(3)

		itsunitary22 = Tex(r"det(U^\dag)det(U) = det(\mathbb{I})").shift(DOWN*2)
		self.play(Transform(itsunitary21, itsunitary22))
		self.wait(3)

		itsunitary23 = Tex(r"det(U) = 1").shift(DOWN*2)
		self.play(Transform(itsunitary21, itsunitary23))
		self.wait(8)

		self.play(FadeOut(unitary), FadeOut(itsunitary), FadeOut(itsunitary23))

		#Quantum Gates
		qgate = Tex(r"\textrm{1. All Quantum Gates are Unitary Matrices}").shift(UP*3.5)
		self.play(Write(qgate))

		itsagate = Tex(r"G")
		self.play(Write(itsagate))

		itsunitary24 = Tex(r"det(G) = 1").shift(DOWN*2)
		self.play(Transform(itsunitary21, itsunitary24))

		self.wait(5)

		itsagate2 = Tex(r"\ket{\psi_2} = G\ket{\psi_1}").shift(UP*1.25)
		self.play(Transform(itsagate, itsagate2))
		
		self.wait(5)
		#Name Rule 2: The Euclidean Norm of Qubits is 1
		complexlaw2 = Tex(r"\textrm{2. The Euclidean Norm of all Qubits is 1 }")
		complexlaw2.move_to(UP * 2.85)
		self.play(FadeIn(complexlaw2))

		self.wait(8)
		itsagate21 = Tex(r"\mid{(\ket{\psi_2})}\mid = det(G)*\mid{(\ket{\psi_1})}\mid")
		self.play(FadeIn(itsagate21))

		self.wait(3)
		itsagate22 = Tex(r"\mid{(\ket{\psi_2})}\mid  = 1*\mid{(\ket{\psi_1})}\mid")
		self.play(Transform(itsagate21, itsagate22))

		self.wait(3)
		itsagate23 = Tex(r"\mid{(\ket{\psi_2})}\mid = \mid{(\ket{\psi_1})}\mid = 1")
		self.play(Transform(itsagate21, itsagate23))
		self.wait(8)





















from manimlib import *
import numpy as np

class FirstScene(ThreeDScene):
	def construct(self):
		text = Text("Postulate II of Quantum Mechanics, Super Operators, Euler Formula").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class euler(ThreeDScene):
	def construct(self):
		text = Text("Postulate II of Quantum Mechanics, Super Operators, Euler Formula").scale(0.7)
		self.play(FadeIn(text))
		self.wait(6)
		self.play(FadeOut(text))
		combiningqubits = Text("The 2nd Postulate").shift(UP*3)
		itsaqubits = Tex(r"\ket{\psi}, \ket{\varphi} \in \mathbb{H}^2").shift(DOWN*3.5)
		self.play(Write(combiningqubits))
		self.play(Write(itsaqubits))
		self.wait(2)

		itsagate = Tex(r"G\ket{\psi_1} = \ket{\psi_2}")
		self.play(Write(itsagate))
		self.wait(8)

		itsagate2 = Tex(r"U\ket{\psi_0} = \ket{\psi_t}").shift(UP*1)
		self.play(Transform(itsagate, itsagate2))
		self.wait(8)

		thepostulate = Tex(r"\textrm{A qubit at any state in time after can be represented with a unitary matrix}").shift(DOWN*2.2).scale(0.8)
		self.play(Write(thepostulate))
		self.wait(8)

		itsagate3 = Tex(r"\ket{\psi_0}").shift(UP*1)
		self.play(Transform(itsagate, itsagate3))


		x = -5
		def update_qubit(self):
			self.become(Dot(np.array([x,-1,0]),fill_color=BLUE))
		qubit = Dot(np.array([x,-1,0]), fill_color=BLUE)
		qubit.add_updater(update_qubit)
		qgate = Square(1, color=YELLOW).shift(DOWN*1 + LEFT*3)
		qgate2 = Square(1, color=YELLOW).shift(DOWN*1 + LEFT*1)
		qgate3 = Square(1, color=YELLOW).shift(DOWN*1 + RIGHT*1)
		qgate4 = Square(1, color=YELLOW).shift(DOWN*1 + RIGHT*3)
		line = Line(np.array([-15, -1, 0]), np.array([15, -1, 0]))
		self.add(line)
		self.play(ShowCreation(qubit))
		self.play(ShowCreation(qgate))
		self.play(ShowCreation(qgate2))
		self.play(ShowCreation(qgate3))
		self.play(ShowCreation(qgate4))
		self.wait(5)
		

		g1 = False
		g2 = False
		g3 = False
		g4 = False
		def update_vector(self):
			self.next_to(qubit, UP, buff=1.5)
		itsagate.add_updater(update_vector)

		t = 0
		while(t < 1000):
			x += 0.01
			t += 1
			if (t>200 and g1 == False):
				qgate11 = Square(1, fill_color=YELLOW, fill_opacity=1).shift(DOWN*1 + LEFT*3)
				itsagate4 = Tex(r"U_1\ket{\psi_0}")
				self.play(Transform(qgate, qgate11))
				self.play(Transform(itsagate, itsagate4))
				g1 = True
			if (t>400 and g2 == False):
				qgate22 = Square(1, fill_color=YELLOW, fill_opacity=1).shift(DOWN*1 + LEFT*1)
				itsagate5 = Tex(r"U_2U_1\ket{\psi_0}")
				self.play(Transform(qgate2, qgate22))
				self.play(Transform(itsagate, itsagate5))
				g2 = True
			if (t>600 and g3 == False):
				qgate33 = Square(1, fill_color=YELLOW, fill_opacity=1).shift(DOWN*1 + RIGHT*1)
				itsagate6 = Tex(r"U_3U_2U_1\ket{\psi_0}")
				self.play(Transform(qgate3, qgate33))
				self.play(Transform(itsagate, itsagate6))
				g3 = True
			if (t>800 and g4 == False):
				qgate44 = Square(1, fill_color=YELLOW, fill_opacity=1).shift(DOWN*1 + RIGHT*3)
				itsagate7 = Tex(r"U_4U_3U_2U_1\ket{\psi_0}")
				self.play(Transform(qgate4, qgate44))
				self.play(Transform(itsagate, itsagate7))
				g4 = True
			self.wait(0.001)

		self.wait(5)
		itsagate.remove_updater(update_vector)
		itsagate8 = Tex(r"\varepsilon\ket{\psi_0}=U_4U_3U_2U_1\ket{\psi_0} = \ket{\psi_t}").shift(UP*0.5)
		self.play(Transform(itsagate, itsagate8))
		self.wait(6)

		itsagate9 = Tex(r"\varepsilon = U_4U_3U_2U_1").shift(UP*0.5)
		self.play(Transform(itsagate, itsagate9))
		self.wait(3)

		self.play(FadeOut(qubit), FadeOut(line), FadeOut(qgate), FadeOut(qgate2), FadeOut(qgate3), FadeOut(qgate4))

		itsagate100 = Tex(r"(\varepsilon)^\dag = (U_4U_3U_2U_1)^\dag").shift(DOWN*0.5)
		self.play(ShowCreation(itsagate100))
		self.wait(5)
		itsagate101 = Tex(r"(\varepsilon)^\dag = (U_1^T U_2^T U_3 ^T U_4^T)^*").shift(DOWN*0.5)
		self.play(Transform(itsagate100, itsagate101))
		self.wait(3)
		itsagate102 = Tex(r"(\varepsilon)^\dag = (U_1^\dag U_2^\dag U_3^\dag U_4^\dag)").shift(DOWN*0.5)
		self.play(Transform(itsagate100, itsagate102))

		self.wait(3)
		self.play(FadeOut(itsagate))
		itsagate110 = Tex(r"(\varepsilon)^\dag \varepsilon= (U_1^\dag U_2^\dag U_3^\dag U_4^\dag)(U_4U_3U_2U_1)")
		self.play(Transform(itsagate100, itsagate110))
		self.wait(3)
		itsagate111 = Tex(r"(\varepsilon)^\dag \varepsilon= U_1^\dag U_2^\dag U_3^\dag (U_4^\dag U_4)U_3U_2U_1")
		self.play(Transform(itsagate100, itsagate111))
		self.wait(8)
		itsagate112 = Tex(r"(\varepsilon)^\dag \varepsilon= U_1^\dag U_2^\dag U_3^\dag U_3U_2U_1")
		self.play(Transform(itsagate100, itsagate112))
		itsagate113 = Tex(r"(\varepsilon)^\dag \varepsilon= U_1^\dag U_2^\dag U_2U_1")
		self.play(Transform(itsagate100, itsagate113))
		itsagate114 = Tex(r"(\varepsilon)^\dag \varepsilon= U_1^\dag U_1")
		self.play(Transform(itsagate100, itsagate114))
		itsagate115 = Tex(r"(\varepsilon)^\dag \varepsilon= \mathbb{I}")
		self.play(Transform(itsagate100, itsagate115))

		combiningqubits2 = Text("Super Operator").shift(UP*3)
		self.play(Transform(combiningqubits, combiningqubits2))
		self.wait(6)
		self.play(FadeOut(itsagate100), FadeOut(thepostulate), FadeOut(itsaqubits))


		#Euler Formula
		combiningqubits3 = Text("Euler Formula").shift(UP*3)
		self.play(Transform(combiningqubits, combiningqubits3))
		self.wait(5)
		eulernation = Tex(r"a + bi = Re^{i\theta} = R*(\cos{\theta} + i\sin{\theta})").shift(UP*1.8)
		self.play(ShowCreation(eulernation))
		self.wait(10)
		eulerfudge = Tex(r"\ket{\psi} = a_1\begin{bmatrix} 1 \\ 0  \end{bmatrix} + a_2\begin{bmatrix} 0 \\ 1  \end{bmatrix}")
		self.play(ShowCreation(eulerfudge))
		self.wait(5)
		eulerfudge2 = Tex(r"\ket{\psi} = R_1e^{i\theta}\begin{bmatrix} 1 \\ 0  \end{bmatrix} + R_2e^{i\phi}\begin{bmatrix} 0 \\ 1  \end{bmatrix}")
		self.play(Transform(eulerfudge, eulerfudge2))
		self.wait(12)










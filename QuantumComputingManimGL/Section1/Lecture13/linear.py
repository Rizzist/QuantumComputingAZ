from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Linear Operators, Density Operator, Mixed States").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class linear(Scene):
	def construct(self):
		text = Text("Linear Operators, Density Operator, Mixed States").scale(0.8)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		title = Text("Linear Operator").shift(UP*3.5)
		itslinear = Tex(r"\hat{A} \in \mathbb{L} : \mathbb{H} \to \mathbb{H}").shift(DOWN*3)
		self.play(FadeIn(title), Write(itslinear))
		self.wait(6)
		prop1 = Tex(r"\hat{A}(a f(x)) = a\hat{A} f(x) ")
		prop2 = Tex(r"\hat{A}(f(x) + g(x)) = \hat{A} f(x) + \hat{A} g(x) ").shift(DOWN*1)
		self.play(FadeIn(prop1), FadeIn(prop2))
		self.wait(3)
		itstrue = Tex(r"\hat{A}\ket{\psi} = a\ket{\psi}").shift(UP*1)
		self.play(FadeIn(itstrue))
		self.wait(3)

		yupyup = Text("All quantum gates are linear operators represented by a matrix").scale(0.7).shift(DOWN*2)
		self.play(FadeIn(yupyup))
		self.wait(6)

		groupIt = Group(yupyup, prop1, prop2, itstrue, itslinear)
		self.play(FadeOut(groupIt))

		#its a density operator
		title2 = Text("Density Operator").shift(UP*3.5)
		self.play(Transform(title, title2))

		itsp = Tex(r"\ket{\psi} = a_0 \ket{0} + a_1 \ket{1}").shift(UP*2.5)
		self.play(Write(itsp))


		dpure = Tex(r"p_{\psi} = \ket{\psi}\bra{\psi}").shift(UP*1.5)
		self.play(Write(dpure))
		self.wait(6)

		dpurec = Tex(r"p_{\psi} = \begin{bmatrix} a_0^*a_0 & a_1^*a_0 \\ a_0^*a_1 & a_1^*a_1\end{bmatrix}")
		self.play(Write(dpurec))
		self.wait(3)

		diag = Tex(r"Tr(p_{\psi})  = 1").shift(LEFT*4 + UP*1.5)
		self.play(FadeIn(diag))
		self.wait(2)

		projector = Tex(r"p_{\psi}^2  = p_{\psi}").shift(RIGHT*4 + UP*1.5)
		self.play(FadeIn(projector))
		self.wait(2)

		hermiticity = Tex(r"p_{\psi}^\dag  = p_{\psi}").shift(RIGHT*4 + DOWN*1.5)
		self.play(FadeIn(hermiticity))
		self.wait(2)

		positivity = Tex(r"p_{\psi} > 0").shift(LEFT*4 + DOWN*1.5)
		self.play(FadeIn(positivity))
		self.wait(2)

		expected = Tex(r"\langle A \rangle = Tr(Ap_{\psi})").shift(DOWN*1.5)
		self.play(FadeIn(expected))
		self.wait(2)

		expected2 = Tex(r"\langle M_0 \rangle = Tr(M_0p_{\psi})").shift(DOWN*2.5)
		self.play(FadeIn(expected2))
		self.wait(8)

		itspure = Text("Density Matrix of Pure State in Superposition").scale(0.8).shift(DOWN*3.5)
		self.play(Write(itspure))
		self.wait(6)

		
		#replace some stuff
		itsp2 = Tex(r"\ket{\psi} = \frac{1}{\sqrt{(2})} \ket{0} + \frac{1}{\sqrt{(2})} \ket{1}").shift(UP*2.5)
		self.play(Transform(itsp, itsp2))
		self.wait(3)

		dpurec2 = Tex(r"p_{\psi} = \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2}\end{bmatrix}")
		self.play(Transform(dpurec, dpurec2))
		self.wait(6)

		qG = Group(diag, projector, hermiticity, positivity, dpurec, dpure, itsp, expected, expected2)
		self.play(FadeOut(qG))







		#lets look at the quad vector
		itsquad = Tex(r"\ket{\psi\phi} = c_0 \ket{00} + c_1 \ket{01} + c_2 \ket{10} + c_2 \ket{11}").shift(UP*2.5)
		self.play(Write(itsquad))

		notsopure = Tex(r"p_{\psi\phi} = \ket{\psi\phi}\bra{\psi\phi}").shift(UP*1.5)
		self.play(Write(notsopure))
		self.wait(3)
		
		notsopurec = Tex(r"p_{\psi\phi} = \begin{bmatrix} c_0^*c_0 & c_1^*c_0 & c_2^*c_0 & c_3^*c_0 \\  c_0^*c_1 & c_1^*c_1 & c_2^*c_1 & c_3^*c_1  \\ c_0^*c_2 & c_1^*c_2 & c_2^*c_2 & c_3^*c_2 \\ c_0^*c_3 & c_1^*c_3 & c_2^*c_3 & c_3^*c_3 \end{bmatrix}").shift(DOWN*1)
		self.play(Write(notsopurec))
		self.wait(3)

		notsopurec99 = Tex(r"p_{\psi\phi} = \begin{bmatrix} c_0^*c_0 & c_1^*c_0 & c_2^*c_0 & c_3^*c_0 \\  c_0^*c_1 & c_1^*c_1 & c_2^*c_1 & c_3^*c_1  \\ c_0^*c_2 & c_1^*c_2 & c_2^*c_2 & c_3^*c_2 \\ c_0^*c_3 & c_1^*c_3 & c_2^*c_3 & c_3^*c_3 \end{bmatrix} = p_{\psi} \otimes p_{\phi}").shift(DOWN*1)
		self.play(Transform(notsopurec, notsopurec99))
		self.wait(3)


		#bell
		itsquad2 = Tex(r"\ket{B_0} =  \frac{1}{\sqrt{(2})}  \ket{00} +  \frac{1}{\sqrt{(2})}  \ket{11}").shift(UP*2.5)
		self.play(Transform(itsquad, itsquad2))

		notsopure2 = Tex(r"p_{B_0} = \ket{B_0}\bra{B_0}").shift(UP*1.5)
		self.play(Transform(notsopure, notsopure2))
		self.wait(3)
		
		notsopurec2 = Tex(r"p_{B_0} = \begin{bmatrix} \frac{1}{2} & 0 & 0 & \frac{1}{2} \\  0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \frac{1}{2} & 0 & 0  & \frac{1}{2} \end{bmatrix}").shift(DOWN*1)
		self.play(Transform(notsopurec, notsopurec2))
		self.wait(6)

		itspure2 = Text("Density Matrix of Pure State in Entanglement").scale(0.8).shift(DOWN*3.5)
		self.play(Transform(itspure, itspure2))
		self.wait(5)


		#bell2
		itsquad3 = Tex(r"\ket{B_1} =  \frac{1}{\sqrt{(2})}  \ket{01} +  \frac{1}{\sqrt{(2})}  \ket{10}").shift(UP*2.5)
		self.play(Transform(itsquad, itsquad3))

		notsopure3 = Tex(r"p_{B_1} = \ket{B_1}\bra{B_1}").shift(UP*1.5)
		self.play(Transform(notsopure, notsopure3))
		self.wait(3)
		
		notsopurec3 = Tex(r"p_{B_1} = \begin{bmatrix} 0 & 0 & 0 & 0 \\  0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}").shift(DOWN*1)
		self.play(Transform(notsopurec, notsopurec3))
		self.wait(6)

		gagain = Group(itsquad, notsopure, notsopurec, itspure)
		self.play(FadeOut(gagain))







		#its a mixed state
		title3 = Text("Mixed State").shift(UP*3.5)
		self.play(Transform(title, title3))

		box = Square(color=YELLOW).scale(2.5)
		aphi = [] 
		for i in range(0, 10):
			aphi.append(Tex(r"\ket{\psi_0}").shift(random.randint(-10, 10)/5 * LEFT + random.randint(-10, 10)/5 * DOWN))

		ensemble = Group(box, *aphi)
		self.play(ShowCreation(ensemble))
		ensemble.generate_target()
		ensemble.target.shift(LEFT*4)
		whatisphi = Tex(r"\ket{\psi_0} = \ket{0} \ \ \ 50\%").shift(RIGHT*1 + UP*2)
		whatisphi2 = Tex(r"\ket{\psi_0} = \ket{1} \ \ \ 50\%").shift(RIGHT*1 + UP*1)
		whatisphi3 = Tex(r"\ket{\psi} = \frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}").shift(RIGHT*2)
		itsnotsup = Text("Not Superposition").scale(0.7).shift(RIGHT*2)

		self.play(MoveToTarget(ensemble), Write(whatisphi), Write(whatisphi2), Write(itsnotsup))
		self.wait(6)

		defn = Tex(r"p_{o} = \sum_{i=0}^{n} q p_{\psi_0}").shift(RIGHT*1.5 + DOWN*1)
		defer = Tex(r"\sum_{i=0}^{n} q = 1").shift(RIGHT*1 + DOWN*2.5)
		self.play(Write(defn), Write(defer))
		self.wait(12)

		defn2 = Tex(r"p_{o} = \sum_{i=0}^{10} 0.1 \ket{\psi_0}\bra{\psi_0}").shift(RIGHT*1.5 + DOWN*1.3)
		defer2 = Tex(r"\ket{0}\bra{0} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \ \ \ \ket{1}\bra{1} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}").shift(RIGHT*2.5 + DOWN*3)
		self.play(Transform(defn, defn2), Transform(defer, defer2))
		self.wait(5)

		defn3 = Tex(r"p_{o} =  \begin{bmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{2} \end{bmatrix}").shift(RIGHT*1.5 + DOWN*1.3)
		self.play(Transform(defn, defn3))
		self.wait(6)

		gtriple = Group(defer, itsnotsup)
		self.play(FadeOut(gtriple))

		defn3 = Tex(r"p_{o} =  \begin{bmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{2} \end{bmatrix} \ \ \ p_{\psi} =  \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} \end{bmatrix}").shift(RIGHT*2.5 + DOWN*1.5)
		whatisphi22 = Tex(r"\ket{\psi_0} = \ket{1}").shift(RIGHT*0 + UP*1.5)
		lolitssame = Text("<<< Same Qubit").scale(0.8).shift(UP*1.55 + RIGHT*3.5)
		whyitsmixed = Tex(r"Tr(p_{o}^2) < 1").shift(RIGHT*4 + UP*1.55)
		self.play(Transform(defn, defn3), Write(whatisphi3), FadeOut(whatisphi), Transform(whatisphi2, whatisphi22), FadeIn(whyitsmixed))
		
		itspure3 = Text("Density Matrix of Mixed State").scale(0.8).shift(DOWN*3.5)
		
		self.play(FadeIn(itspure3))
		self.wait(6)

		itsuknow = []
		whatisphi32 = Tex(r"\ket{\psi} = \ket{1}")
		whatisphi33 = Tex(r"\ket{\psi} = \ket{0}")
		itsuknow.append(whatisphi32)
		itsuknow.append(whatisphi33)

		self.play(Transform(whatisphi3, whatisphi32), FadeOut(whyitsmixed), FadeIn(lolitssame))
		self.wait(12)
		boxer = SurroundingRectangle(whatisphi3)
		boxer2 = SurroundingRectangle(whatisphi2)
		for i in range(0, 10):
			self.play(ShowCreation(boxer), ShowCreation(boxer2), Transform(whatisphi3, itsuknow[random.randint(0, 1)]))
			self.play(FadeOut(boxer), FadeOut(boxer2))
		self.wait(12)

















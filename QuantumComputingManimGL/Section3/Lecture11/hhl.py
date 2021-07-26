from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("HHL Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class hhl(Scene):
	def construct(self):
		text = Text("HHL Algorithm").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Linear Systems").shift(UP*3.5)
		self.play(FadeIn(title))

		system = []
		system.append( Tex(r"A\vec{x} = \vec{b}").shift(UP*3 + LEFT*4) )
		system.append( Tex(r"\vec{x} = A^{-1}\vec{b}").shift(UP*2 + LEFT*4) )
		system.append( Tex(r"A\ket{x} = \ket{b}").shift(UP*3 + RIGHT*4) )
		system.append( Tex(r"\ket{x} = A^{-1}\ket{b}").shift(UP*2 + RIGHT*4) )
		system.append( Tex(r"A \to \{ \ket{u_j}\} & \{ \lambda_j\}").shift(UP*2.5) )
		system.append( Tex(r"A = P^{-1}DP").shift(UP*1.5) )
		system.append( Tex(r"A^{-1} = P^{-1}\frac{1}{D}P \to \{ \frac{1}{\lambda_j}\}").shift(UP*0.5) )
		system.append( Tex(r"\ket{b} = \sum_{j=0}^{n}c_j\ket{u_j}").shift(DOWN*0 + LEFT*5) )
		system.append( Tex(r"\ket{x} = \sum_{j=0}^{n}c_j\frac{1}{\lambda_j}\ket{u_j}").shift(DOWN*0 + RIGHT*5) )
		system.append( Text(r"Hamiltonian Simulation").shift(DOWN*1).scale(0.7) )
		system.append( Text(r"Quantum Phase Estimation").shift(DOWN*2).scale(0.7) )
		system.append( Text(r"General Born Rule").shift(DOWN*3).scale(0.7) )

		for i in system:
			self.play(FadeIn(i))
			self.wait(10)
		self.play(FadeOut(Group(*system)))

		title2 = Text("HHL Algorithm").shift(UP*3.5)
		self.play(Transform(title, title2))
		steps = []
		steps.append( Tex(r"\text{Step 0: Prepare 1 bit Ancilla, n bit register to store eigenvalues, n bit to store } \ket{b} ").shift(UP*3).scale(0.7) )
		steps.append( Tex(r"\ket{0}_a \ket{0}_r \ket{b}_m \to \sum_{j=0}c_j\ket{0}_a \ket{0}_r\ket{u_j}").shift(UP*2.25).scale(0.7) )
		steps.append( Tex(r"\text{Step 1: Implement Hamiltonian Simulation of } A \to e^{iA} ").shift(UP*1.5).scale(0.7) )
		steps.append( Tex(r"\text{Step 2: Perform Quantum Phase Estimation on } e^{iA} \to \lambda_j \to Eigenvalues \to Register").shift(UP*0.75).scale(0.7) )
		steps.append( Tex(r"\sum_j c_j \ket{0}_a \ket{0}_r \ket{u_j} \to \sum_j c_j \ket{0}_a \ket{\lambda_j}_r \ket{u_j}").shift(UP*0).scale(0.7) )
		steps.append( Tex(r"\text{Step 3: Perform Controlled Rotation on Ancilla} ").shift(DOWN*0.75).scale(0.7) )
		steps.append( Tex(r"\ket{0}_a \to ((1-\frac{C^2}{\lambda_j^2})^{0.5}\ket{0}_a + \frac{C}{\lambda_j}\ket{1}_a \to \sum_{j=0} c_j ((1-\frac{C^2}{\lambda_j^2})^{0.5}\ket{0}_a + \frac{C}{\lambda_j}\ket{1}_a)\ket{\lambda_j}_r\ket{u_j}").shift(DOWN*1.5).scale(0.7) )
		steps.append( Tex(r"\text{Step 4: Perform REVERSE Quantum Phase Estimation on } e^{iA} \to \ket{\lambda_j}_r \to \ket{0}_r").shift(DOWN*2.25).scale(0.7) )
		steps.append( Tex(r"\sum_{j=0} c_j ((1-\frac{C^2}{\lambda_j^2})^{0.5}\ket{0}_a + \frac{C}{\lambda_j}\ket{1}_a)\ket{\lambda_j}_r\ket{u_j} \to \sum_{j=0} c_j ((1-\frac{C^2}{\lambda_j^2})^{0.5}\ket{0}_a + \frac{C}{\lambda_j}\ket{1}_a)\ket{0}_r\ket{u_j}").shift(DOWN*3).scale(0.7) )
		steps.append( Tex(r"\text{Step 5: Measure Ancilla (Apply General Born Rule), if its 1, we have Inverse }").shift(DOWN*3.75).scale(0.7) )
		steps.append( Tex(r"\sum_{j=0} c_j ((1-\frac{C^2}{\lambda_j^2})^{0.5}\ket{0}_a + \frac{C}{\lambda_j}\ket{1}_a)\ket{0}_r\ket{u_j} \to \sum_{j=0} c_j (\frac{C}{\lambda_j}\ket{1}_a)\ket{0}_r\ket{u_j}").shift(DOWN*4.5).scale(0.7) )
		steps.append( Tex(r"\ket{x} = \sum_{j=0} c_j \frac{C}{\lambda_j}\ket{u_j}").shift(DOWN*5.85) )
	
		frame = self.camera.frame
		frame.generate_target()
		for i in range(0, len(steps)):
			self.play(FadeIn(steps[i]))
			if (i == 8):
				frame.target.shift(DOWN*3)
				self.play(MoveToTarget(frame, run_time=2.0))
			self.wait(10)
		frame.target.shift(UP*3)
		self.play(MoveToTarget(frame, run_time=2.0))
		self.play(FadeOut(Group(*steps)))

		applyit = Tex(r"\begin{bmatrix} \frac{3}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} \end{bmatrix}\begin{bmatrix} x_0 \\ x_1 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}").shift(UP*0).scale(2.5)
		self.play(FadeIn(applyit))
		self.wait(15)







from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Parallel & Serial Gates").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class serial(Scene):
	def construct(self):
		text = Text("Parallel & Serial Gates").scale(1.1)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		title = Text("Serial Gates").shift(UP*3.5)
		self.play(Write(title))

		offset = 2
		x = -5
		dq1 = r"\ket{\psi}"
		dq2 = r"\ket{\phi}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*1))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*1))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7).add_updater(update_q2)

		l1 = Line(np.array([-5, 0, 0]), np.array([5, 0, 0]))
		l2 = Line(np.array([-5, -offset, 0]), np.array([5, -offset, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,0,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset,0]),fill_color=BLUE))

		qubit1 = Dot(np.array([x,0,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)

		itsg = Group(q1, q2, qubit1, qubit2)
		self.play(FadeIn(itsg), FadeIn(l1), FadeIn(l2))
		hadamardbro = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5)
		hadamo = Text("H", fill_color=BLACK)
		hadamard1 = Group(hadamardbro, hadamo)
		hadamard1.shift(LEFT*1)
		self.play(FadeIn(hadamard1))

		phasebro = Square(fill_color=GREEN, fill_opacity=1, color=GREEN).scale(0.5)
		phaser = Tex(r"R_\theta", fill_color=BLACK).scale(1.2)
		phase = Group(phasebro, phaser)
		phase.shift(RIGHT*1)
		self.play(FadeIn(phase))
		
		whyitstrue = Text("Superoperator can represent serial gates").shift(UP*2)
		self.play(FadeIn(whyitstrue))

		combiner = Rectangle(fill_color=YELLOW_D, fill_opacity=1, color=GREEN).scale(0.5)
		combino = Tex(r"R_\theta \cdot H", fill_color=BLACK).scale(1.2)
		combine = Group(combiner, combino)
		self.play(FadeOut(hadamard1), FadeOut(phase), FadeIn(combine))
		self.wait(8)

		self.play(FadeOut(whyitstrue), FadeOut(combine))

		title2 = Text("Parallel Gates").shift(UP*3.5)
		self.play(Transform(title, title2))


		hadamardbro2 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5)
		hadamo2 = Text("H", fill_color=BLACK)
		hadamard2 = Group(hadamardbro2, hadamo2)
		hadamard2.shift(LEFT*1 + DOWN*offset)
		self.play(FadeIn(hadamard1), FadeIn(hadamard2))
		self.wait(3)
		texer = Tex(r"(H \otimes H) \ket{\psi \otimes \phi} = H\ket{\psi} \otimes H\ket{\phi}").shift(UP*2)
		self.play(FadeIn(texer))

		hadamardbro3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(1.8)
		hadamo3 = Tex(r"H \otimes H", fill_color=BLACK).scale(2)
		hadamard3 = Group(hadamardbro3, hadamo3)
		hadamard3.shift(DOWN*1)
		self.play(FadeOut(hadamard1), FadeOut(hadamard2), FadeIn(hadamard3))
		self.wait(3)

		hadamardbro4 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(1.8)
		hadamo4 = Tex(r"H^{\otimes 2}", fill_color=BLACK).scale(2)
		hadamard4 = Group(hadamardbro4, hadamo4)
		hadamard4.shift(DOWN*1)
		self.play(Transform(hadamard3, hadamard4))
		self.wait(12)














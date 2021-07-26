from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Instantaneous Quantum Polynomial").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class iqp(Scene):
	def construct(self):
		text = Text("Instantaneous Quantum Polynomial")
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("Instantaneous Quantum Polynomial").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		stuff.append(    Tex(r"\text{IQP Protocol: } H^{\otimes N}UH^{\otimes N}\ket{0}^{\otimes N}").shift(UP*2.75)    )
		stuff.append(    Tex(r"S^{\otimes N}U + \text{Homodyne Measure } \hat{p} \to \text{Run Multiple Times}").shift(UP*2)    )
		stuff.append(    Tex(r"1. \text{ Squeezed States} \to \text{Momentum in 'Superposition'}").shift(UP*1.25)    )
		stuff.append(    Tex(r"2. \ \ U = \{ Z(p), CZ(s), V(\gamma) \}").shift(UP*0.5)    )
		stuff.append(    Tex(r"3. \text{ Homodyne Measure of Momentum}").shift(DOWN*0.25)    )
		stuff.append(    	ImageMobject("./iqp").shift(DOWN*2.25).scale(0.75)    )
		for i in stuff:
			self.play(FadeIn(i))
			self.wait(10)
		self.wait(20)

















		
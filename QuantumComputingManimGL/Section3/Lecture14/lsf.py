from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Least Square Fitting").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)



class lsf(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Least Square Fitting").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Least Square Fitting").shift(UP*3.5)
		self.play(FadeIn(title))

		linreg = Text("Type of Linear Regression").shift(DOWN*3.5).scale(0.7)
		self.play(FadeIn(linreg))

		corona = ImageMobject("./stat.png").scale(1.5)
		self.play(FadeIn(corona))
		waiter(10)
		self.play(FadeOut(corona))


		eq = Tex(r"\hat{x} = (A^TA)^{-1}A^T\vec{b} = A^+\vec{b}").shift(UP*2.75)
		self.play(FadeIn(eq))
		waiter(10)

		stuff = []
		stuff.append( Text("1. Perform PseudoInverse").shift(UP*1.125).scale(0.7) )
		stuff.append( Text("2. Use HHL to get Coefficients").shift(UP*0).scale(0.7) )
		stuff.append( Text("3. Calculate Fit Parameter").shift(DOWN*1.125).scale(0.7) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)




















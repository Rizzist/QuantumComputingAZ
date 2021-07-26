from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Relevance of Quantum Machine Learning").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class tden(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
			
		title = Text("Density Matrix and Quantum Gates").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		stuff.append( Tex(r"\text{Density Matrix: } \rho \quad \quad \text{Quantum Gate: } U").shift(UP*2.5) )
		stuff.append( Tex(r"\rho = \ket{\psi}\bra{\psi}").shift(UP*1.5) )
		stuff.append( Tex(r"U \rho U^\dag = U\ket{\psi}\bra{\psi}U^\dag = \big( U\ket{\psi} \big) \big( U\ket{\psi} \big)^\dag").shift(DOWN*0.5) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(14)








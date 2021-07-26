from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Optical Neural Network (QONN)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class qonn(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Optical Neural Network (QONN)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Quantum Optical Neural Network (QONN)").shift(UP*3.5)
		self.play(FadeIn(title))



		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Similar to regular Quantum Machine Learning}").shift(UP*2) )
		stuff.append( Tex(r"\text{Quantum Functions} \to \text{Quantum Optical Functions}").shift(UP*1) )
		stuff.append( Tex(r"\text{Look at an example!}").shift(UP*0) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))
		

		











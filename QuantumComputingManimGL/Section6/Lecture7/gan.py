from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Generative Adversarial Networks (GAN)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class gan(Scene):
	def construct(self):
		wait = False
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Generative Adversarial Networks (GAN)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Generative Adversarial Networks (GAN)").shift(UP*3.5)
		self.play(FadeIn(title))


		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Convolution (Filter)} \to \text{Feature Map}").shift(UP*2) )
		stuff.append( SurroundingRectangle(stuff[0]) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(2)
		self.play(FadeOut(Group(*stuff)))
		

		









from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Relevance of Quantum Machine Learning").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class relevant(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Relevance of Quantum Machine Learning").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Relevance of Quantum Machine Learning").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		stuff.append( Tex(r"\text{- Refresher on older material (ie: algorithms)}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{- Apply new material learned (ie: Quantum Embedding)}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{- Learn Something New (ie: Fisher Information Matrix)}").shift(DOWN*0.5) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)










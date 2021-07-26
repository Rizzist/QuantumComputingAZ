from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Convolutional Neural Network (CNN)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class cnn(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Convolutional Neural Network (CNN)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Convolutional Neural Network (CNN)").shift(UP*3.5)
		self.play(FadeIn(title))

		cool = ImageMobject("./cnn.jpeg").scale(1.5)
		self.play(FadeIn(cool))
		waiter(2)
		self.play(FadeOut(cool))


		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Convolution (Filter)} \to \text{Feature Map}").shift(UP*2) )
		stuff.append( Tex(r"\text{2. Activation Function} \to \{ ReLU, Linear, Sigmoid, Tanh \}").shift(UP*1) )
		stuff.append( Tex(r"\text{3. Max Pooling} \to \text{Largest Value in Feature Map}").shift(UP*0) )
		stuff.append( Tex(r"\text{4. Input Result Into Neural Network}").shift(DOWN*1) )
		stuff.append( SurroundingRectangle(stuff[0]) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(15)
		waiter(14)
		#self.play(FadeOut(Group(*stuff)))
		







		
from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("QML w/ Qiskit & Pytorch").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class time(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("QML w/ Qiskit & Pytorch")
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		


















			
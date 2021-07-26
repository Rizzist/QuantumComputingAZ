from manimlib import *
import numpy as np

class FirstScene(ThreeDScene):
	def construct(self):
		text = Text("Tensor Product, Unitary Matrices, Quantum Gates")
		self.play(FadeIn(text))
		self.wait(3)
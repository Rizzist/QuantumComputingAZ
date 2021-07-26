from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("QML - Pennylane").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class plane(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Machine Learning - Pennylane")
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Machine Learning").shift(UP*3.25)
		self.play(FadeIn(title))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Supervised Learning}").shift(LEFT*3.5 + UP*2).scale(1.2) )
		stuff.append( Tex(r"\text{2. Unsupervised Learning}").shift(LEFT*3.5 + DOWN*0.5).scale(1.2) )
		stuff.append( Tex(r"\text{- Regression (Linear Regression, Decision Tree, Neural Network)}").shift(UP*1.3).scale(0.8) )
		stuff.append( Tex(r"\text{- Classification (Logistic Regression, SVM, Naive Bayes)}").shift(UP*0.6) )
		stuff.append( Tex(r"\text{- Clustering (K-Means, Density Based)}").shift(DOWN*1.2) )
		stuff.append( Tex(r"\text{- Dimensionality Reduction (PCA)}").shift(DOWN*1.9) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(3)
		self.play(FadeOut(Group(*stuff)))






		title2 = Text("Quantum Machine Learning").shift(UP*3.25)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Classical Machine Learning w/ Quantum Functions}").shift(UP*2) )
		stuff.append( Tex(r"\text{2. Quantum Algorithms for Quantum Machine Learning}").shift(DOWN*0.5) )
		stuff.append( SurroundingRectangle(stuff[0]) )
		for i in stuff:
			self.play(ShowCreation(i))
			waiter(5)
		waiter(15)
		#self.play(FadeOut(Group(*stuff)))
















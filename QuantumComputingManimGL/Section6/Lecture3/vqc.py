from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Variational Quantum Classifiers (VQC)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class vqc(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Variational Quantum Classifiers (VQC)").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Variational Quantum Classifiers (VQC)").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Data} \to \text{\# Features, \# Classes }").shift(UP*2) )
		stuff.append( Tex(r"\text{2. Classical \& Quantum Nodes (Python Functions)}").shift(UP*1.2) )
		stuff.append( Tex(r"\text{- \# Features} \to \text{Throughput}").shift(UP*0.6).scale(0.8) )
		stuff.append( Tex(r"\text{- \# Classes} \to \text{\# Nodes}").shift(UP*0).scale(0.8) )
		stuff.append( Tex(r"\text{3. Cost Function} \propto \text{Correct Predictions} ").shift(UP*-0.6) )
		stuff.append( Tex(r"\text{4. Optimization} \to \text{Pre-Built Functions} ").shift(UP*-1.4) )
		stuff.append( Tex(r"\text{Example: Iris Data Set}").shift(UP*-3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))
		

















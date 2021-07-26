from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("DiVincenzo's Criteria for a Quantum Computer").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class div(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("DiVincenzo's Criteria for a Quantum Computer").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("DiVincenzo's Criteria for a Quantum Computer").shift(UP*3.5)
		self.play(FadeIn(title))

		ty = Tex(r"\text{What is a quantum computer? What is needed?}")
		self.play(FadeIn(ty))
		waiter(10)
		self.play(FadeOut(ty))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Scalable Physical System w/ Logical Qubits}").shift(UP*2) )
		stuff.append( Tex(r"\text{2. Arbituary State Initialization}").shift(UP*1) )
		stuff.append( Tex(r"\text{3. Long Relevant Decoherence Time}").shift(UP*0) )
		stuff.append( Tex(r"\text{4. Universal Set of Quantum Gates}").shift(DOWN*1) )
		stuff.append( Tex(r"\text{5. Ability to Measure Qubits}").shift(DOWN*2) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(15)
		waiter(15)
		#self.play(FadeOut(Group(*stuff)))














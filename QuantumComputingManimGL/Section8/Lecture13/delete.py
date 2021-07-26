from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("No-Teleportation Theorem, No-Deleting Theorem").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class delete(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("No-Teleportation Theorem, No-Deleting Theorem").scale(0.9)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("No-Teleportation Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Classical Bits} \to \text{Quantum Bits} \to \text{Classical Bits}").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Quantum Bits} \to \text{Classical Bits} \to \text{Quantum Bits?}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{According to Theorem, NO!}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{Quantum State cannot be determined from 1 Measurement}").shift(UP*-0.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))

















		title2 = Text("No-Deleting Theorem").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"U\ket{\psi}_A\ket{\psi}_B = \ket{\psi}_A\ket{0}_B?").shift(UP*2.5) )
		stuff.append( Tex(r"\text{According to No-Deleting Theorem, No!}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{Corrollary of No-Hiding Theorem and Duel of No-Cloning Theorem}").shift(UP*0.5).scale(0.9) )
		stuff.append( Tex(r"U\ket{\psi}_A\ket{\psi}_B\ket{A}_C = \ket{\psi}_A\ket{0}_B\ket{A^\prime}_C").shift(UP*-0.5))
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))



















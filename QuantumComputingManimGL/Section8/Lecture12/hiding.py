from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("No-Hiding Theorem, No-Communication Theorem").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class hiding(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("No-Hiding Theorem, No-Communication Theorem").scale(0.9)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("No-Hiding Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\ket{\psi} \otimes \ket{A} \to \ket{\psi^\prime} \otimes \ket{A^\prime(\psi)}").shift(UP*2.5) )
		stuff.append( Tex(r"\text{If less information in } \psi \text{ then more information in A (Environment)}").shift(UP*1.5).scale(0.9) )
		stuff.append( Tex(r"\text{Conservation of Quantum Information}").shift(UP*0.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))













		title2 = Text("No-Communication Theorem").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Given 2 people each with only an ebit, }").shift(UP*2.5) )
		stuff.append( Tex(r"\text{they cannot communicate useful information.}").shift(UP*2.0) )
		stuff.append( Tex(r"\text{Entanglement is 50/50} \to \text{Means of Connection not Communication}").shift(UP*0.5).scale(0.9) )
		stuff.append( Tex(r"\text{Superdense Coding uses Bits and Qubits}").shift(DOWN*0.5) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))




















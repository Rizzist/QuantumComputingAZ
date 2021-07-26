from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("No-Broadcast Theorem, Superbroadcasting").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class broadcast(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("No-Broadcasting Theorem, Superbroadcasting").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("No-Broadcasting Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"U\ket{0...0}\ket{\psi} = \ket{\psi}^n").shift(UP*1) )
		stuff.append( Tex(r"\text{Not Possible - No-Cloning Theorem}").shift(UP*0) )
		stuff.append( Tex(r"\text{Cannot Copy Pure States}").shift(UP*-1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))





		title2 = Text("Superbroadcasting").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Can copy non-commuting mixed states}").shift(UP*-3.2) )
		stuff.append( Tex(r"\rho = \rho_A \otimes \rho_B \to \text{multiple qubits s.t}").shift(UP*2.5) )
		stuff.append( Tex(r"\rho_A = \ket{\psi^n}\bra{\psi^n} \quad \quad \rho_B = \ket{0^m}\bra{0^m}").shift(UP*1.25) )
		stuff.append( Tex(r"U \rho U^\dag = U \rho_A \otimes \rho_B U^\dag = U \rho_A \otimes \rho_A U^\dag ").shift(UP*0) )
		stuff.append( Tex(r"n = 4 \quad \quad m = 2 ").shift(UP*-1) )
		stuff.append( Tex(r"\text{Different Qubits Can Produce The Same Mixed State}").shift(UP*-2.2).scale(1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))























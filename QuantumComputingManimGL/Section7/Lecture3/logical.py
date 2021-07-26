from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Stabilizer Code & Quantum Noise Models").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class logical(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Stabilizer Code & Quantum Noise Models").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Stabilizer Code").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{How to map all Error Syndromes?}").shift(UP*2.75) )
		stuff.append( Tex(r"\begin{tabular}{ c c c c c c c c c c } $M_1$ & Z & Z & - & - & - & - & - & - & -  \\ $M_2$ & - & Z & Z & - & - & - & - & - & - \\ $M_3$ & - & - & - & Z & Z & - & - & - & -  \\ $M_4$ & - & - & - & - & Z & Z & - & - & -  \\ $M_5$ & - & - & - & - & - & - & Z & Z & - \\ $M_6$ & - & - & - & - & - & - & - & Z & Z \\ $M_7$ & X & X & X & X & X & X & - & - & - \\ $M_8$ & - & - & - & X & X & X & X & X & X \end{tabular}").shift(DOWN*0) ) 
		stuff.append( Line(np.array([-3.5, -2.25, 0]), np.array([-3.5, 2.25, 0])) )
		stuff.append( Tex(r"\text{Shor Code Error Syndromes}").shift(DOWN*3) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))










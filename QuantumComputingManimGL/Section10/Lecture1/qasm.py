from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("OpenQASM: Quantum Assembly").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class qasm(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("OpenQASM: Quantum Assembly").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("OpenQASM: Quantum Assembly").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{General Code for Quantum Computers}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{Quantum Algorithms}").shift(UP*1.5) )
		stuff.append( Tex(r"\downarrow").shift(UP*0.9) )
		stuff.append( Tex(r"\text{Quantum Coding Languages}").shift(UP*0.3) )
		stuff.append( Tex(r"\downarrow").shift(DOWN*0.3) )
		stuff.append( Tex(r"\text{Quantum Assembly}").shift(DOWN*0.9) )
		stuff.append( Tex(r"\downarrow").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{Quantum Instruction Set Architecture} \to \{H, P, CX, CCX \} \ \ \{D, S, K, V, BS \}").shift(DOWN*2.1).scale(0.8) )
		stuff.append( Tex(r"\downarrow").shift(DOWN*2.7) )
		stuff.append( Tex(r"\text{Quantum Chip} \to \text{Photons/Ions/SQUID}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i.shift(UP*0.2)))
			waiter(5)
		sss = SurroundingRectangle(stuff[5]).scale(1.2)
		self.play(ShowCreation(sss))
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))

















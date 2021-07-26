from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Distance Measures for Quantum Information").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class distance(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Distance Measures for Quantum Information").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Trace Distance").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{How Different are 2 Quantum States}").shift(DOWN*3.3) )
		stuff.append( Tex(r"0 \leq T(\rho, \sigma) = \frac{1}{2}Tr(\mid \rho - \sigma \mid) \leq \frac{1}{2}").shift(UP*2.6) )
		stuff.append( Tex(r"\rho = \sum_i r_i \ket{i}\bra{i}").shift(UP*1.4 + LEFT*2.5) )
		stuff.append( Tex(r"\sigma = \sum_i s_i \ket{i}\bra{i}").shift(UP*1.4 + RIGHT*2.5) )
		stuff.append( Tex(r"\rho = \frac{3}{4} \ket{0}\bra{0} + \frac{1}{4}\ket{1}\bra{1}").shift(UP*0.2 + LEFT*3) )
		stuff.append( Tex(r"\sigma = \frac{2}{3} \ket{0}\bra{0} + \frac{1}{3}\ket{1}\bra{1}").shift(UP*0.2 + RIGHT*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"T(\rho, \sigma) = \frac{1}{2}Tr(\mid \frac{1}{12}\ket{0}\bra{0} - \frac{1}{12}\ket{1}\bra{1}  \mid) = \frac{1}{2}Tr(\frac{1}{12}\ket{0}\bra{0} + \frac{1}{12}\ket{1}\bra{1})").shift(DOWN*1).scale(0.9) )
		stuff2.append( Tex(r"T(\rho, \sigma) = \frac{1}{2}(\frac{1}{24}) = \frac{1}{48}").shift(DOWN*2.2) )
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)
		self.play(FadeOut(Group(*stuff, *stuff2)))

		





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"T(\rho, \sigma) = \frac{1}{2}Tr(\mid \rho - \sigma \mid)").shift(UP*2.5) )
		stuff.append( Tex(r"\vec{r} \to \text{Bloch Vector for } \rho").shift(UP*1.5 + LEFT*4) )
		stuff.append( Tex(r"\vec{s} \to \text{Bloch Vector for } \sigma").shift(UP*1.5 + RIGHT*4) )
		stuff.append( Tex(r"\rho = \frac{\mathbb{I} + \vec{r} \cdot \{X,Y,Z\} }{2}").shift(UP*0.2 + LEFT*3) )
		stuff.append( Tex(r"\sigma = \frac{\mathbb{I} + \vec{s} \cdot \{X,Y,Z\} }{2}").shift(UP*0.2 + RIGHT*3) )
		stuff.append( Tex(r"T(\rho, \sigma) = \frac{1}{4} \mid (\vec{r} - \vec{s}) \cdot \{X,Y,Z\} \mid").shift(DOWN*1) )
		stuff.append( Tex(r"T(\rho, \sigma) = \frac{1}{2} \mid \vec{r} - \vec{s} \mid").shift(DOWN*2.2) )
		stuff.append( Tex(r"\text{Trace Distance is half distance on Bloch Sphere!}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))

		





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"T(\rho, \sigma) = \frac{1}{2}Tr(\mid \rho - \sigma \mid)").shift(UP*2.5) )
		stuff.append( Tex(r"\rho^{AB} = \frac{1}{2} \ket{\psi_A}\bra{\psi_A} + \frac{1}{2} \ket{\psi_B}\bra{\psi_B}").shift(UP*1.5) )
		stuff.append( Tex(r"\sigma^{AB} = \frac{1}{2} \ket{\phi_A}\bra{\phi_A} + \frac{1}{2} \ket{\phi_B}\bra{\phi_B}").shift(UP*0.3) )
		stuff.append( Tex(r"T(\rho^A, \sigma^A) \leq T(\rho^{AB}, \sigma^{AB})").shift(DOWN*0.9) )
		stuff.append( Tex(r"T(\rho^B, \sigma^B) \leq T(\rho^{AB}, \sigma^{AB})").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Partial Info. of System is more similar than full info. of System}").shift(DOWN*3.3).scale(0.8) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))

		#Trace Distance Measure as half substract trace + example
		#partial 1,2 a distance less than full 1,2 a,b distance
		


		title2 = Text("Fidelity").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"F(\rho, \sigma) = Tr\big( \rho^{0.5}\sigma^{0.5} \big)").shift(UP*2.5) )
		stuff.append( Tex(r"F(\rho, \sigma) = \max_{\ket{\phi}} \mid \bra{\psi}\ket{\phi} \mid").shift(UP*1.5) )
		stuff.append( Tex(r"A(\rho, \sigma) = arccos(F(\rho, \sigma))").shift(UP*0.5) )
		stuff.append( Tex(r"\text{Angle b/w Bloch Vectors}").shift(DOWN*3.3).scale(0.8) )
		stuff.append( Tex(r"A(\rho, \tau) \leq A(\rho, \sigma) + A(\sigma, \tau) \to \text{Triangle Inequality}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{How similar two different Quantum States}").shift(DOWN*1.5) )
		stuff.append( Tex(r"1 - F(\rho, \sigma) \leq T(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)^2}").shift(DOWN*2.5) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(15)
		#Fidelity Measure












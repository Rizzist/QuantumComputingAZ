from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Uncertainty Principle").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class principle(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Uncertainty Principle").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Uncertainty Principle").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\langle A \rangle = \bra{\psi}A\ket{\psi}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{Classical: }\sigma_A^2 = (A - \langle A \rangle)^2").shift(UP*1.6) )
		stuff.append( Tex(r"\text{Quantum: }\sigma_A^2 =  \langle (A - \langle A \rangle)^2 \rangle").shift(UP*0.6) )
		stuff.append( Tex(r"\sigma_A^2 =  \bra{\psi} (A - \langle A \rangle)^2 \ket{\psi}").shift(DOWN*0.4) )
		stuff.append( Tex(r"\sigma_A^2 =  \braket{(A - \langle A \rangle)\psi}").shift(DOWN*1.4) )
		stuff.append( Tex(r"\sigma_A^2 =  \braket{f}").shift(DOWN*2.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff)))


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\sigma_A^2 \sigma_B^2 =  \braket{f}\braket{g}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{Schwarz Inequality: } \braket{f}\braket{g} \geq \mid \bra{f}\ket{g} \mid^2").shift(UP*1.6) )
		stuff.append( Tex(r"\sigma_A^2 \sigma_B^2 \geq \mid \bra{f}\ket{g} \mid^2").shift(UP*0.6) )
		stuff.append( Tex(r"\mid z\mid^2 = Re(z)^2 + Im(z)^2 \geq Im(z)^2 = \bigg(\frac{(z-z^*)}{2i}\bigg)^2").shift(DOWN*0.4) )
		stuff.append( Tex(r"\sigma_A^2 \sigma_B^2 \geq \bigg(\frac{1}{2i} (\bra{f}\ket{g} - \bra{g}\ket{f})\bigg)^2").shift(DOWN*1.4) )
		stuff.append( Tex(r"\bra{f}\ket{g} - \bra{g}\ket{f} \to ?").shift(DOWN*2.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff)))





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\bra{f}\ket{g} = \bra{(A - \langle A \rangle)\psi}  \ket{(B - \langle B \rangle)\psi}").shift(UP*2.6) )
		stuff.append( Tex(r"\bra{f}\ket{g} = \bra{\psi} AB - A\langle B \rangle - \langle A \rangle B + \langle A \rangle \langle B \rangle \ket{\psi}").shift(UP*1.6) )
		stuff.append( Tex(r"\bra{f}\ket{g} = \langle AB \rangle - \langle A \rangle \langle B \rangle - \langle A \rangle \langle B \rangle + \langle A \rangle \langle B \rangle").shift(UP*0.6) )
		stuff.append( Tex(r"\bra{f}\ket{g} = \langle AB \rangle - \langle A \rangle \langle B \rangle ").shift(DOWN*0.4) )
		stuff.append( Tex(r"\bra{g}\ket{f} = \langle BA \rangle - \langle A \rangle \langle B \rangle ").shift(DOWN*1.4) )
		stuff.append( Tex(r"\bra{f}\ket{g} - \bra{g}\ket{f} = \langle AB \rangle - \langle BA \rangle").shift(DOWN*2.4) )
		stuff.append( Tex(r"\bra{f}\ket{g} - \bra{g}\ket{f} = \langle [A, B] \rangle").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff)))

		


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\sigma_A^2 \sigma_B^2 \geq (\frac{1}{2i} (\bra{f}\ket{g} - \bra{g}\ket{f}))^2").shift(UP*2.5) )
		stuff.append( Tex(r"\bra{f}\ket{g} - \bra{g}\ket{f} = \langle [A, B] \rangle").shift(UP*1.5) )
	
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		result = Tex(r"\sigma_A^2 \sigma_B^2 \geq \bigg(\frac{\langle [A, B] \rangle}{2i} \bigg)^2").shift(DOWN*2.5).scale(1.5) 
		self.play(FadeIn(result))

		self.play(FadeOut(Group(*stuff)))


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"[x, p] = ih").shift(UP*2.5 + LEFT*2) )
		stuff.append( Tex(r"\sigma_x^2 \sigma_p^2 \geq \bigg(\frac{ih}{2i} \bigg)^2").shift(UP*2.5 + RIGHT*2) )
		stuff.append( Tex(r"\sigma_x^2 \sigma_p^2 \geq \frac{h^2}{4}").shift(UP*1) )
		stuff.append( Tex(r"\text{Heisenberg Uncertainty Principle: } \sigma_x \sigma_p \geq \frac{h}{2}").shift(DOWN*0.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		result2 = Tex(r"\sigma_A^2 \sigma_B^2 \geq \bigg(\frac{Tr(\rho [A, B]}{2i} \bigg)^2").shift(DOWN*2.5).scale(1.5) 
		self.play(Transform(result, result2))
		waiter(15)






















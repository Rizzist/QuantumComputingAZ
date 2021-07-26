from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Bennet's Laws, Partial Transpose, Entanglement Measures").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class bennet(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Bennet's Laws, Partial Transpose, Entanglement Measures").scale(0.8)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Bennet's Laws").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Bennet's Laws of Quantum Information: }").shift(UP*2 + LEFT*2) )
		stuff.append( Tex(r"\text{1 qubit } \geq \text{ 1 bit} \quad \quad \quad \to \text{Classical}").shift(UP*1) )
		stuff.append( Tex(r"\text{1 qubit } \geq \text{ 1  ebit} \quad \quad \quad \to \text{Entanglement Bit}").shift(UP*0 + RIGHT*0.9) )
		stuff.append( Tex(r"\text{1 ebit + 1 qubit } \geq \text{ 2 bits} \quad \quad \quad \to \text{Superdense Coding}").shift(DOWN*1 + RIGHT*0.1) )
		stuff.append( Tex(r"\text{1 ebit + 2 bits } \geq \text{ 1 qubit} \quad \quad \quad \to \text{Quantum Teleportation}").shift(DOWN*2 + RIGHT*0.6) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(3)
		self.play(FadeOut(Group(*stuff)))














		title2 = Text("Partial Transpose").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\rho \to \mathbb{H}_A \otimes \mathbb{H}_B").shift(UP*2.5) )
		stuff.append( Tex(r"\rho = \sum_{ijkl} a_{ij}^{kl} \ket{i}\bra{j} \otimes \ket{k}\bra{l}").shift(UP*1.25) )
		stuff.append( Tex(r"\rho^{T_B} = (\mathbb{I} \otimes T)\rho = \sum_{ijkl} a_{ij}^{kl} \ket{i}\bra{j} \otimes (\ket{k}\bra{l})^T = \sum_{ijkl} a_{ij}^{kl} \ket{i}\bra{j} \otimes \ket{l}\bra{k}").shift(UP*0) )
		stuff.append( Tex(r"\text{Peres–Horodecki or PPT Criterion: }").shift(DOWN*2 + LEFT*1).scale(1.2) )
		stuff.append( Tex(r"\text{If all the eigenvalues of } \rho^{T_B} \text{ are positive, }").shift(DOWN*2.75) )
		stuff.append( Tex(r"\text{the state is seperable, otherwise it is entangled}").shift(DOWN*3.25) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))



















		title2 = Text("Types of Entanglement Measures").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Relative Entropy Entanglement (REE)}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{2. Logarithmic Negativity}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{3. Distillation Entanglement}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{4. Squashed Entanglement}").shift(DOWN*1.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))








		title2 = Text("Logarithmic Negativity").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\mathbb{N}(\rho) = \frac{\mid\mid\rho^{T_B}\mid\mid-1}{2}").shift(UP*2.5) )
		stuff.append( Tex(r"\mid\mid\rho^{T_B}\mid\mid = Tr  \sqrt{(\rho^{T_B})^\dag \rho^{T_B}}").shift(UP*1.25) )
		stuff.append( Tex(r"\mathbb{N}(\rho) = \Bigg(   Tr \bigg(  (\rho^{T_B})^\dag \rho^{T_B})^{0.5} \bigg)   -1    \Bigg)/2").shift(DOWN*0) )
		stuff.append( Tex(r"\mathbb{N}(\rho) = \right| \sum_{\lambda_i < 0} \lambda_i \right| ").shift(DOWN*1.5) )
		stuff.append( Tex(r"E_N = \log \bigg( 2*\mathbb{N}(\rho) - 1 \bigg)").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(20)
		#self.play(FadeOut(Group(*stuff)))






















from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Channels, Channel Capacity").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class channel(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Channels, Channel Capacity").scale(0.9)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Quantum Channels").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Group(Tex(r"\text{Any processing of quantum info (storage or transfer)}").shift(UP*2.7), Tex(r"\text{can be represented by quantum channel}").shift(UP*2)) )
		stuff.append( Tex(r"\text{Memoryless: Output depends only on immediate input}").shift(UP*1) )
		stuff.append( Tex(r"\text{Density Matrix: } \rho").shift(UP*0.4) )
		stuff.append( Tex(r"\text{Krauss Operators: } \sum_k B_k^*B_k = \mathbb{I}").shift(DOWN*0.7) )
		stuff.append( Tex(r"\text{Quantum Operation: } \Phi(\rho) =  \sum_k B_k^* \rho B_k").shift(DOWN*1.8) )
		stuff.append( Tex(r"\text{Quantum Channel only transmits Quantum Information: } \Phi").shift(DOWN*2.7) )
		stuff.append( Tex(r"\text{(Schrödinger picture) Does not send classical info, only quantum }").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))












		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Group(Tex(r"\text{Let } H_A \text{ and } H_B \text{ be state spaces where}").shift(UP*2.7), Tex(r"\text{information can be transmitted and recieved: } H_A \to H_B").shift(UP*2.1)) )
		stuff.append( Tex(r"\text{Properties of } \Phi").shift(UP*1.2 + LEFT*1.5) )
		stuff.append( Tex(r"\text{1. } \Phi \text{ is linear}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{2. } \Phi \text{ is a positive map}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{3. } \Phi \text{ preserves trace} \to Tr(\Phi(\rho)) = Tr(\rho)").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{4. When } dim(H_A) < dim(H_B): \mathbb{I}_n \otimes \Phi \text{ is a positive map}").shift(DOWN*2.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))



		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Let } L(H_A) \text{ be a family of linear maps on } H_A").shift(UP*2.5) )
		stuff.append( Tex(r"\Psi : L(H_A) \to L(H_B)").shift(UP*1.5) )
		stuff.append( Tex(r"\text{Now we Include Classical Information}").shift(UP*0) )
		stuff.append( Tex(r"\Psi : L(H_A) \otimes C(X) \to L(H_B)").shift(DOWN*1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))




		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Time Evolution: } \rho \to \Phi(\rho) = U_t\rho U_t^*").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Error Correction: } \Phi_{BF} = \{ \Phi_1, \Phi_2  \}").shift(UP*1.5) )
		stuff.append( Group(Tex(r"\Phi_1 = \sqrt{p} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} ").shift(UP*0 + LEFT*2), Tex(r"\Phi_2 = \sqrt{1-p} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} ").shift(UP*0 + RIGHT*2)) )
		stuff.append( Tex(r"\Phi(\rho) = \Phi_1(\rho) + \Phi_2(\rho) = \sqrt{p} \ \  \mathbb{I}\rho\mathbb{I}^* + \sqrt{1-p} \ \ X\rho X^*").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{Quantum Teleportation}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))










		
		title2 = Text("Channel Capacity").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{How many (Qu)bits can be sent through 1 use of the channel?}").shift(UP*2.5) )
		stuff.append( Tex(r"Alice \stackrel{N}{\to} Bob").shift(UP*1).scale(2) )
		stuff.append( Tex(r"\text{Capacity: } C(N) = \max_{p(X)} I(A:B)").shift(DOWN*1) )
		stuff.append( Tex(r"\text{Just a classical channel}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))







		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Group(Tex(r"\text{Clasical Channel } N").shift(UP*2 + LEFT*3.75).scale(1.5), Tex(r"\text{Classical Capacity}").shift(UP*0.5 + LEFT*4), Tex(r"C(N)").shift(UP*1 + LEFT*4)  ) )
		stuff.append( Tex(r"\text{Quantum Channel } \mathbb{N}").shift(UP*2 + RIGHT*3.5).scale(1.5) )
		stuff.append( Tex(r"\text{Classical Capacity } C(\mathbb{N})").shift(DOWN*-0.5 + RIGHT*4) )
		stuff.append( Tex(r"\text{Quantum Capacity } Q(\mathbb{N})").shift(DOWN*0.5 + RIGHT*4) )
		stuff.append( Tex(r"\text{Private Classical Capacity } P(\mathbb{N})").shift(DOWN*1.5 + RIGHT*3.25) )
		stuff.append( Tex(r"\text{Entanglement Assisted Classical Capacity } C_E(\mathbb{N})").shift(DOWN*2.5 + RIGHT*1.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))















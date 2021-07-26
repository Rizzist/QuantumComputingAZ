from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("LOCC, Entanglement Swapping").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class locc(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("LOCC, Entanglement Swapping").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("LOCC").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Local Operations and Classical Communication }").shift(UP*2.5) )
		stuff.append( Tex(r"\stackrel{Local}{Quantum} \ \ \stackrel{Classical}{\to} \ \ \stackrel{Local}{Quantum}").shift(DOWN*0).scale(2) )
		stuff.append( Tex(r"\text{Quantum Teleportation }").shift(DOWN*2.5) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Alice and Bob share a bell state, 1 qubit each}").shift(UP*2.5) )
		stuff.append( Group(Tex(r"\ket{\Psi_0} = \frac{1}{\sqrt{(2})} \bigg(  \ket{00} + \ket{11} \bigg)  ").shift(DOWN*-1.5 + LEFT*3.5), Tex(r"\ket{\Psi_1} = \frac{1}{\sqrt{(2})} \bigg(  \ket{01} + \ket{10} \bigg)  ").shift(DOWN*-1.5 + RIGHT*3.5)) )
		stuff.append( Tex(r"\text{Alice measures 0: Could be either} \to \text{Classical Channel}").shift(DOWN*0) )
		stuff.append( Tex(r"\text{Bob measures 1: } \ket{\Psi_1} \to \text{Success from LOCC}").shift(DOWN*0.8) )
		stuff.append( Tex(r"\text{Entire Process: LOCC Operation } LOCC_1").shift(DOWN*1.6) )
		stuff.append( Tex(r"LOCC_1 \subset LOCC_r \subset LOCC_{r+1} \subset LOCC_{\mathbb{N}}").shift(DOWN*2.3) )
		stuff.append( Tex(r"\text{What can you do with LOCC? - LOCC Protocols}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))

		




	
		title2 = Text("LOCC Protocols").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. State Preparation}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{2. State Discrimination}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{3. Entanglement Conversion}").shift(UP*-0.5) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))











		
		title2 = Text("Entanglement Swapping").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"Alice").shift(UP*1.5 + LEFT*4) )
		stuff.append( Tex(r"Bob").shift(UP*1.5 + RIGHT*4) )


		stuff.append( Dot().shift(LEFT*2 + UP*2).scale(3).set_color(RED) )
		stuff.append( Dot().shift(RIGHT*2 + UP*2).scale(3).set_color(RED) )
		stuff.append( Dot().shift(LEFT*2 + UP*1).scale(3).set_color(BLUE) )
		stuff.append( Dot().shift(RIGHT*2 + UP*1).scale(3).set_color(BLUE) )

		stuff.append( Tex(r"1").shift(LEFT*2.5 + UP*2.2) )
		stuff.append( Tex(r"2").shift(RIGHT*2.5 + UP*2.2) )
		stuff.append( Tex(r"3").shift(RIGHT*2.5 + UP*1.2) )
		stuff.append( Tex(r"4").shift(LEFT*2.5 + UP*1.2) )

		stuff.append( Line(np.array([-2, 2, 0]), np.array([2, 2, 0])) )
		stuff.append( Line(np.array([-2, 1, 0]), np.array([2, 1, 0])) )
		for i in stuff:
			self.play(FadeIn(i))


		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"1. \ \ \ \ CNOT_{\{2, 3\} }").shift(DOWN*0.4).scale(1.3) )
		stuff2.append( Tex(r"2. \ \ \ \ CNOT_{\{3, 2\} }").shift(DOWN*1.2).scale(1.3) )
		stuff2.append( Tex(r"3. \ \ \ \ CNOT_{\{1, 4\} }").shift(DOWN*2).scale(1.3) )
		
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(5)
		self.play(FadeOut(stuff[-1]), FadeOut(stuff[-2]))



		stuff3 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff3.append( Line(np.array([-2, 2, 0]), np.array([2, 1, 0])).set_color(YELLOW) )
		stuff3.append( Line(np.array([-2, 1, 0]), np.array([2, 2, 0])).set_color(YELLOW) )
		stuff3.append( Tex(r"\text{Completely LOCC!! No Qubits Transfered, Only Bits!}").shift(DOWN*3.3) )
		for i in stuff3:
			self.play(FadeIn(i))
		waiter(15)
		#self.play(FadeOut(Group(*stuff)))







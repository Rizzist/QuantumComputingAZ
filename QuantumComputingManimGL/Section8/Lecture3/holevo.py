from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Holevo's Theorem").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class holevo(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Holevo's Theorem").scale(1.2)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		#print(YELLOW)
		title = Text("Holevo's Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{How many bits can be transmitted in a Qubit?}").shift(UP*2.7) )
		stuff.append( Tex(r"Z \to 3n \quad \quad Y \in Z \to 2n \quad \quad X \in Y \to n").shift(UP*1.8) )
		stuff.append( Tex(r"I(Y, Z) = H(Y) + H(Z) - H(Y, Z)").shift(UP*0.9) )
		stuff.append( Tex(r"I(Y, Z) = 2n + 3n - 3n = 2n").shift(DOWN*0) )
		stuff.append( Tex(r"I(X, Z) = n + 3n - 3n = n").shift(DOWN*0.9) )
		stuff.append( Tex(r"Z \to Y \to X").shift(DOWN*1.8) )
		stuff.append( Tex(r"I_{acc}(\sigma, \rho) \to \text{What can be accessed?}").shift(DOWN*2.7) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"I_{acc}(\sigma, \rho) = \max_{\sigma_z} I(X, Y)").shift(UP*2.7) )
		stuff.append( Tex(r"\text{Density Matrix: } \rho").shift(UP*1.8) )
		stuff.append( Tex(r"\rho = \frac{1}{2^n} \sum^{2^n} \ket{i}\bra{i} \otimes \ket{i}\bra{i}").shift(UP*0.8) )
		stuff.append( Tex(r"\rho_a = Tr_b(\rho) = \frac{1}{2^n} \sum^{2^n} \ket{i}\bra{i} Tr(\ket{i}\bra{i})").shift(DOWN*0.3) )
		stuff.append( Tex(r"\rho_a = \rho_b = \frac{1}{2^n} \sum^{2^n} \ket{i}\bra{i}").shift(DOWN*1.5) )
		stuff.append( Tex(r"H(\rho_a) = H(\rho_b) = \log 2^n").shift(DOWN*2.4) )
		stuff.append( Tex(r"I(\rho_a, \rho_b) = \log 2^n").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))



		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"I_{acc}(\sigma, \rho) = \max_{\sigma_z} I(\rho_a, \rho_b) = \log 2^n").shift(UP*2.7) )
		stuff.append( Tex(r"\text{Max. Entanglement -> Max. Transmission}").shift(UP*1.8) )
		stuff.append( Tex(r"\text{if seperable: } \rho = \rho_a \otimes \rho_b \to I(\rho_a, \rho_b) = 0").shift(UP*0.9) )
		stuff.append( Tex(r"\text{Holevo Information: } \chi = S(\rho) - \sum_i p_i S(\rho_i)").shift(UP*0) )
		stuff.append( Tex(r"\text{Holevo's Theorem: } I(\rho_a, \rho_b) \leq \chi").shift(DOWN*1.3) )
		stuff.append( Tex(r"I(\rho_a, \rho_b) \leq S(\rho) - \sum_i p_i S(\rho_i) \leq \log 2^n = n bits").shift(DOWN*3.2) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))

		
		title2 = Text("Holevo's Theorem - Superdense Coding").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{4 Qubits: } I_{acc}(\sigma, \rho) = \log (2^4) = \text{4 bits} \to 0-15").shift(DOWN*3.4) )
		stuff.append( Tex(r"\text{Maximally Entangle}").shift(DOWN*2.8) )
		stuff.append( Tex(r"\text{Alice}").shift(UP*1 + LEFT*4.5) )
		stuff.append( Tex(r"\text{Bob}").shift(DOWN*1 + LEFT*4.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(4)
		
		qubCoords = []
		qubs = []
		qubs2 = []
		def superdenseQubit():
			c = Circle(color=YELLOW).scale(0.5)
			d = Tex(r"\psi")
			return Group(c, d)
		def underlayQubit(col):
			c = Circle(color=col, fill_color=col, fill_opacity=0.2).scale(0.5)
			return c

		for i in range(4):
			qubs.append(superdenseQubit())
			qubCoords.append( [-3 + 2*i, 1, 0] )
		for i in range(4):
			qubs[i].generate_target()
			qubs[i].target.move_to(qubCoords[i])
			self.play(MoveToTarget(qubs[i]))

		qubCoords[3] = [3, -1, 0]
		qubs[3].target.move_to(qubCoords[3])
		self.play(MoveToTarget(qubs[3]))

		for i in range(3):
			col = RED
			if (i == 1):
				col = GREEN
			if (i == 2):
				col = GREEN
			qubs2.append(underlayQubit(col))
			qubCoords.append( [-3 + 2*i, 1, 0] )
		for i in range(3):
			qubs2[i].move_to(qubCoords[i])
			qubs2[i].generate_target()
			self.play(MoveToTarget(qubs2[i]))
		waiter(10)
		for i in range(3):
			qubCoords[i] = [-3 + 2*i, -1, 0]
			qubs[i].target.move_to(qubCoords[i])
			qubs2[i].target.move_to(qubCoords[i])
			self.play(MoveToTarget(qubs[i]), MoveToTarget(qubs2[i]))


		waiter(30)
		#self.play(FadeOut(Group(*stuff)))





















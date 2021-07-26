from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Landauer Principle").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class heat(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Landauer Principle, Margolus-Levitin Theorem").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		#print(YELLOW)
		title = Text("Landauer Principle").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Where does heat come from in a computer?}").shift(UP*2.5) )
		stuff.append( Tex(r"\text{- Electric Resistance of Current Carrier}").shift(UP*1.5 + RIGHT*1.2) )
		stuff.append( Tex(r"\text{- Information Loss}").shift(UP*0.5 + LEFT*1) )
		stuff.append( Tex(r"\text{Principle: Irreversible Computing Processes Increases Entropy}").shift(DOWN*3).scale(1) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Quantum Gates are Reversible}").shift(UP*2) )
		stuff.append( Tex(r"\text{Landauer Principle does not apply to Quantum Computers}").shift(UP*1).scale(1) )
		stuff.append( Tex(r"\text{Benefit of Quantum Computers}").shift(UP*0).scale(1) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))







		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Lower theoretical limit of energy consumption of computation}").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Boltzmann Entropy Formula: } S = k_B \ln(W)").shift(UP*1.5) )
		stuff.append( Tex(r"W \to \text{\# of Possible States}").shift(UP*0.5) )
		stuff.append( Tex(r"E = ST").shift(DOWN*0.5) )
		stuff.append( Tex(r"E = k_B T \ln(W)").shift(DOWN*1.5) )
		stuff.append( Tex(r"W_{bit} = 2 \to \{ 0, 1\}").shift(DOWN*2.5) )
		#

		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Group(Tex(r"E = k_B T \ln(W)").shift(UP*2.5), Tex(r"E_{bit} = k_B T \ln(2) =  2.856 * 10^{-21} \text{ Joules}").shift(UP*1.5)) )
		stuff.append( Tex(r"E_{terabyte} = 2.2848 * 10^{-12} \text{ Joules}").shift(UP*0.5) )
		stuff.append( Tex(r"\text{Koomey's Law: Computation per Joule doubles every 1.57 Years}").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{Performance per Watt: } 10^3 \text{ MegaFlops} \to 10^6 \text{ FLOPS}").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{Max Operations per Joule per Second?}").shift(DOWN*2.5) )
		#

		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))












		title2 = Text("Margolus-Levitin Theorem").shift(UP*3.5)
		self.play(Transform(title, title2))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Koomey's Law: Computation per Joule doubles every 1.57 Years}").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Performance per Watt: } 10^6 \text{ FLOPS} \to 10^{11}-10^{19} \text{ OPS}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{Theorem: A maximum of } 6*10^{33} \text{ Operations can be done with 1 joule in 1 second}").shift(DOWN*3.2).scale(0.8) )
		
		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"\text{Quantum Limit: System w/ Avg. Energy E}").shift(UP*0.5) )
		stuff2.append( Tex(r"\text{Time to Orthogonal State = } \frac{h}{4E} \to \text{Flip }\ket{0} \text{ to } \ket{1}  ").shift(DOWN*0.5) )
		stuff2.append( Tex(r"\text{Bremermann's limit, Bekenstein bound, Limits of computation}").shift(DOWN*2).scale(0.9).set_color(YELLOW) )
		#

		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(10)
		waiter(20)
		#self.play(FadeOut(Group(*stuff, *stuff2)))










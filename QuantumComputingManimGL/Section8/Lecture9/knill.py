from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Gottesman–Knill theorem, Eastin–Knill theorem").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class knill(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Gottesman–Knill theorem, Eastin–Knill theorem").scale(0.9)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Gottesman–Knill theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Theorem: The following components can be effectively simulated on a classical computer: }").shift(UP*2.5).scale(0.7) )
		stuff.append( Tex(r"\text{1. State Preparation of Qubits}").shift(UP*1.5) )
		stuff.append( Tex(r"\text{2. Clifford Gates: } \{ H, S, CNOT\}").shift(UP*0.75) )
		stuff.append( Tex(r"\text{3. Measurement}").shift(UP*0) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))












		title2 = Text("Eastin–Knill theorem").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Theorem: No Quantum Error Correction code can have a continuous}").shift(UP*2.7).scale(0.9) )
		stuff.append( Tex(r"\text{symmetry acting transversely on physical qubits}").shift(UP*2.2).scale(0.9) )
		stuff.append( Tex(r"\text{Transversal: Affecting 2 different Logical Qubits}").shift(UP*1.3) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		
		stuff2 = []
		for i in range(3):
			for j in range(3):
				stuff2.append( Dot().set_color(YELLOW).shift(LEFT*0.75 + RIGHT*i + DOWN*j + UP*0) )
			stuff2.append( Rectangle(height=3, width=0.8).shift(LEFT*0.75 + RIGHT*i + DOWN*1).set_color(GREEN) )
		
		for i in stuff2:
			self.play(FadeIn(i, run_time=0.1))

		stuff2[2].generate_target()
		stuff2[2].target.set_color(RED)
		self.play(MoveToTarget(stuff2[2]))
		stuff2[2].target.set_color(YELLOW)
		self.play(MoveToTarget(stuff2[2]))


		stuff2[5].generate_target()
		stuff2[5].target.set_color(RED)
		self.play(MoveToTarget(stuff2[5]))
		stuff2[5].target.set_color(YELLOW)
		self.play(MoveToTarget(stuff2[5]))



		stuff2[8].generate_target()
		stuff2[8].target.set_color(RED)
		self.play(MoveToTarget(stuff2[8]))
		stuff2[8].target.set_color(YELLOW)
		self.play(MoveToTarget(stuff2[8]))

		ellipse= Ellipse(width=3, height=1, color=BLUE).shift(RIGHT*0.25 + UP*0)
		self.play(FadeIn(ellipse))


		stuff2[4].generate_target()
		stuff2[4].target.set_color(RED)
		self.play(MoveToTarget(stuff2[4]))
		waiter(5)
		stuff2[0].generate_target()
		stuff2[0].target.set_color(RED)
		stuff2[8].target.set_color(RED)
		self.play(MoveToTarget(stuff2[0]), MoveToTarget(stuff2[8]))
		finale = Tex(r"\text{Any Universal Set of Quantum Gates cannot be Implemented Fault-Tolerantly}").shift(DOWN*3.3).scale(0.8)
		self.play(FadeIn(finale))
		waiter(20)
		#self.play(FadeOut(Group(*stuff)))






































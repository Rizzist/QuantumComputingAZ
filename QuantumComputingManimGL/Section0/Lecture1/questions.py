from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Computing A-Z").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class questions(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Computing A-Z").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Why did you make this course?}").shift(UP*0).scale(2) )
		stuff.append( Tex(r"\text{Why is this course unique?}").shift(UP*0).scale(2) )
		stuff.append( Tex(r"\text{Some Tips on taking the course?}").shift(UP*0).scale(2) )
		stuff.append( Tex(r"\text{Who is this course for?}").shift(UP*0).scale(2) )
		stuff.append( Tex(r"\text{Are you grateful for this opportunity?}").shift(UP*0).scale(1.5) )
		stuff.append( Tex(r"\text{Anything else you would like to say?}").shift(UP*0).scale(1.5) )
		self.play(ShowCreation(stuff[0]))
		for i in range(1, len(stuff)):
			waiter(10)
			self.play(FadeOut(stuff[i-1]), Write(stuff[i]))
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))
		












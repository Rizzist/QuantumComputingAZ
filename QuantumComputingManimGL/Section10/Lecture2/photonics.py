from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Photonics Hardware").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class photonics(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Photonics Hardware").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Photonics Hardware").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{China Quantum Supremacy December 2020}").shift(UP*2.6) )
		stuff.append( ImageMobject("./chinaphotonics.png").shift(DOWN*1).scale(1.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))







		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( ImageMobject("./chinaphotonics2.png").shift(DOWN*0.5).scale(1.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))






		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( ImageMobject("./polarize.png").shift(DOWN*0.5).scale(1.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))






		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Xanadu Silicone Photonics}").shift(UP*2.7) )
		stuff.append( ImageMobject("./siliconep.jpeg").shift(DOWN*0.5).scale(1.4) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))









		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( ImageMobject("./small.png").shift(DOWN*0).scale(1.4) )
		stuff.append( Tex(r"\text{Hong-Ou-Mandel Effect w/ N photons}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))

















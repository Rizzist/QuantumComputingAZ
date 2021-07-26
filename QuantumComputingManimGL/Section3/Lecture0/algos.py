from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Algorithms").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class algo(Scene):
	def construct(self):
		text = Text("Quantum Algorithms").scale(1.3)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))	

		title = Text("What its all about").shift(UP*3.5)
		self.play(FadeIn(title))

		items = []
		items.append( Text("1. Amplitude Amplification").shift(LEFT*3.5 + UP*2).scale(0.8) )
		items.append( Text("2. Period Finding - QFT").shift(LEFT*3.5 + UP*1).scale(0.8) )
		items.append( Text("3. Quantum Walks").shift(LEFT*3.65 + DOWN*0).scale(0.8) )
		items.append( Text("4. Classical/Quantum Hybrids").shift(LEFT*1.5 + DOWN*1).scale(0.8) )

		self.play(FadeIn(items[0]))
		self.wait(5)
		stuff1 = []
		stuff1.append( Tex(r"a\ket{0} + ").shift(UP*2 + RIGHT*1) )
		stuff1.append( Tex(r"b\ket{1} + ").shift(UP*2 + RIGHT*1.5 + RIGHT*1) )
		stuff1.append( Tex(r"c\ket{2}").shift(UP*2 + RIGHT*2.75 + RIGHT*1) )
		self.play(FadeIn(Group(*stuff1)))
		self.wait(10)
		self.play(ScaleInPlace(stuff1[0], 0.5, run_time=3.0), ScaleInPlace(stuff1[1], 1.5, run_time=3.0), ScaleInPlace(stuff1[2], 0.5, run_time=3.0))
		self.wait(5)

		self.play(FadeIn(items[1]))
		self.wait(5)
		stuff2 = []
		stuff2.append( Tex(r"a\ket{0} + ").shift(UP*1 + RIGHT*1) )
		stuff2.append( Tex(r"b\ket{1} + ").shift(UP*1 + RIGHT*1.5 + RIGHT*1) )
		stuff2.append( Tex(r"a\ket{2} + ").shift(UP*1 + RIGHT*3 + RIGHT*1) )
		stuff2.append( Tex(r"b\ket{3}").shift(UP*1 + RIGHT*4.25 + RIGHT*1) )
		self.play(FadeIn(Group(*stuff2)))
		self.wait(10)
		stuff21 = []
		stuff21.append( Tex(r"p\ket{0} + ").shift(UP*1 + RIGHT*1).scale(0.5) )
		stuff21.append( Tex(r"q\ket{1} + ").shift(UP*1 + RIGHT*1.5 + RIGHT*1).scale(0.5) )
		stuff21.append( Tex(r"r\ket{2} + ").shift(UP*1 + RIGHT*3 + RIGHT*1).scale(1.5) )
		stuff21.append( Tex(r"s\ket{3}").shift(UP*1 + RIGHT*4.5 + RIGHT*1).scale(0.5) )
		self.play(Transform(Group(*stuff2), Group(*stuff21), run_time=3.0))
		self.wait(5)

		self.play(FadeIn(items[2]))
		self.wait(10)
		self.play(FadeIn(items[3]))
		self.wait(30)













from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("No Cloning Theorem, Forking").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class clone(Scene):
	def construct(self):
		text = Text("No Cloning Theorem, Forking").scale(1.1)
		self.play(FadeIn(text))
		self.wait(3)
		self.play(FadeOut(text))


		title = Text("No Cloning Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		theorem = Tex(r"\text{There is no Unitary Operator U s.t } U\ket{a}\ket{b} = \ket{a}\ket{a}").shift(DOWN*3.5)
		self.play(FadeIn(theorem))
		self.wait(3)
		assumption = Tex(r"\text{Assume arbituary } \ket{\psi} \text { and } \ket{\phi}").scale(0.9).shift(UP*2.75)
		self.play(FadeIn(assumption))
		self.wait(3)
		truth = Tex(r"U\ket{\phi}\ket{0} = \ket{\phi}\ket{\phi}").shift(UP*2)
		truth2 = Tex(r"U\ket{\psi}\ket{0} = \ket{\psi}\ket{\psi}").shift(UP*1.25)
		self.play(FadeIn(truth), FadeIn(truth2))
		self.wait(3)
		itsun = Tex(r"\bra{\phi}\ket{\psi} = (\bra{\phi}\bra{0})(\ket{\psi}\ket{0})").shift(UP*0.5)
		self.play(FadeIn(itsun))
		self.wait(3)
		itsun2 = Tex(r"\bra{\phi}\ket{\psi} = (\bra{\phi}\bra{0})U^\dag U(\ket{\psi}\ket{0})").shift(DOWN*0.25)
		self.play(FadeIn(itsun2))
		self.wait(3)
		itsun3 = Tex(r"\bra{\phi}\ket{\psi} = (\bra{\phi}\bra{\phi})(\ket{\psi}\ket{\psi})").shift(DOWN*1)
		self.play(FadeIn(itsun3))
		self.wait(3)
		itsun4 = Tex(r"\bra{\phi}\ket{\psi} = (\bra{\phi}\ket{\psi})^2").shift(DOWN*1.75)
		self.play(FadeIn(itsun4))
		self.wait(3)
		itsun5 = Tex(r"\ket{\psi} = \ket{\phi} \ \ \ \ \ \bra{\phi}\ket{\psi} = 0").shift(DOWN*2.5)
		self.play(FadeIn(itsun5))
		self.wait(3)
		itsnay = SurroundingRectangle(assumption)
		self.play(ShowCreation(itsnay))
		grouper = Group(theorem, assumption, truth2, truth, itsun, itsun2, itsun3, itsun4, itsun5, itsnay)
		self.play(FadeOut(grouper))

		reality = Text("You can only clone orthogonal states").shift(UP*0.5)
		re2 = Tex(r"\ket{10} \to \ket{11} ").shift(DOWN*0.5)
		tg = Group(reality, re2)
		self.play(FadeIn(tg))
		self.wait(8)
		self.play(FadeOut(tg))

		#forking
		title2 = Text("Forking").shift(UP*3.5)
		self.play(Transform(title, title2))

		x = -5
		y = 0
		def update_dot1(self):
			self.become(Dot(np.array([x,y,0]),fill_color=BLUE))
		def update_dot2(self):
			self.become(Dot(np.array([x,-y,0]),fill_color=BLUE))
		electron1 = Dot(np.array([x,y,0]),fill_color=BLUE).add_updater(update_dot1)
		electron2 = Dot(np.array([x,-y,0]),fill_color=BLUE).add_updater(update_dot2)
		l1 = Line(np.array([-5, 0, 0]), np.array([0, 0, 0]))
		l2 = Line(np.array([0, 0, 0]), np.array([5, 2.5, 0]))
		l3 = Line(np.array([0, 0, 0]), np.array([5, -2.5, 0]))


		registers = Rectangle(height=1.5, fill_color=YELLOW, color=YELLOW, fill_opacity=1)
		registert = Text("Register").set_color(BLACK)
		register = Group(registers, registert)
		register.shift(RIGHT*4.5 + UP*2.5)

		ALUs = Rectangle(height=1.5, fill_color=YELLOW, color=YELLOW, fill_opacity=1)
		ALUt = Text("ALU").set_color(BLACK)
		ALU = Group(ALUs, ALUt)
		ALU.shift(RIGHT*4.5 + DOWN*2.5)


		itsallthesame = Group(l1, l2, l3, register, ALU, electron1, electron2)
		self.play(FadeIn(itsallthesame))
		self.wait(2)

		while (x < 0):
			x += 0.05
			self.wait(0.001)

		while (x < 5):
			x += 0.05
			y += 0.025
			self.wait(0.001)
		x = -5
		y = 0
		while (x < 0):
			x += 0.05
			self.wait(0.001)

		while (x < 5):
			x += 0.05
			y += 0.025
			self.wait(0.001)


		x = -5
		y = 0
		while (x < 0):
			x += 0.05
			self.wait(0.001)

		while (x < 2):
			x += 0.05
			y += 0.025
			self.wait(0.001)
		electron2.remove_updater(update_dot2)
		xmark = Text("X").set_color(RED).shift(RIGHT*2 + DOWN*1)
		self.add(xmark)
		while (x < 5):
			x += 0.05
			y += 0.025
			self.wait(0.001)
		self.wait(10)


























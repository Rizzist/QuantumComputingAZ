from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Superconducting Quantum Interference Device (SQUID)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class squid(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Superconducting Quantum Interference Device (SQUID)").scale(0.8)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("SQUID").shift(UP*3.5)
		self.play(FadeIn(title))
		

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Superconductivity}").shift(UP*1.5).scale(1.5) )
		stuff.append( Tex(r"\text{2. Cooper Pairs}").shift(UP*0.25).scale(1.5) )
		stuff.append( Tex(r"\text{3. Josephson Junction}").shift(DOWN*1).scale(1.5) )
		stuff.append( Tex(r"\text{Quantized Magnetic Flux through Loop}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))














		title2 = Text("Superconductivity").shift(UP*3.5)
		self.play(Transform(title, title2))


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( ImageMobject("./supergraph.jpeg").shift(DOWN*0.5).scale(1.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))





		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		circle1 = Circle().scale(2).set_color(WHITE)
		circle2 = Circle().scale(2.5).set_color(WHITE)
		circle = Group(circle1, circle2)

		phi = 0
		elects = []
		def electronMaker(i):
			d = Dot().shift(RIGHT*np.sin(i*np.pi/10)*2.25 + UP*np.cos(i*np.pi/10)*2.25).set_color(YELLOW)
			def becomeE(self, i=i):
				self.become( Dot().shift(RIGHT*np.sin(i*np.pi/10 + phi)*2.25 + UP*np.cos(i*np.pi/10 + phi)*2.25).set_color(YELLOW) )
			d.add_updater(becomeE)
			return d
		for i in range(20):
			elects.append(electronMaker(i))
			

		stuff.append( circle )
		stuff.append( Text("E").shift(DOWN*2 + LEFT*4).scale(2) )
		stuff.append( Text("T").shift(DOWN*2 + RIGHT*4).set_color(RED).scale(3) )
		stuff.append( Group(*elects) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(1)
		
		square = Square(fill_opacity=1, fill_color=RED).shift(DOWN*2 + LEFT*4).set_color(GREEN)
		self.play(FadeOut(square))
		vphi = 1.4
		while(vphi > 0.01):
			phi = phi + vphi/10
			vphi = vphi*0.992
			self.wait(0.001)
		stuff.append( Text("T").shift(DOWN*2 + RIGHT*4).set_color(BLUE).scale(3) )
		self.play(FadeIn(stuff[-1], run_time=5.0))
		square = Square(fill_opacity=1, fill_color=RED).shift(DOWN*2 + LEFT*4).set_color(GREEN)
		self.play(FadeOut(square))
		vphi = 1.4
		while(phi < 50):
			phi = phi + vphi/10
			vphi = vphi*1
			self.wait(0.001)
		waiter(2)
		self.play(FadeOut(Group(*stuff)))







		
		title2 = Text("Cooper Pairs").shift(UP*3.5)
		self.play(Transform(title, title2))

		wire1 = Line([-5, 0.75, 0], [5, 0.75, 0])
		wire2 = Line([-5, -0.75, 0], [5, -0.75, 0])
		wire = Group(wire1, wire2)

		x1 = -5
		x2 = -5
		def electroner(i, j, col, m):
			e = Dot().scale(2).shift(UP*j + RIGHT*i)
			def becomer(self, i=i, j=j, col=col, m=m):
				if (m == 0):
					self.become( Dot().scale(2).shift(UP*j + RIGHT*i + RIGHT*x1) ).set_color(col)
				else:
					self.become( Dot().scale(2).shift(UP*j + RIGHT*i + RIGHT*x2) ).set_color(col)
			e.add_updater(becomer)
			return e
		electrons1 = []
		electrons2 = []
		for i in range(10):
			electrons1.append(electroner(i, 0.25, GREEN, 0))
			electrons2.append(electroner(i, -0.25, PURPLE, 1))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( wire )
		stuff.append( Group(*electrons1, *electrons2) )
		stuff.append( Text("T").shift(DOWN*2 + RIGHT*4).set_color(RED).scale(3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		for i in range(20):
			x1 = -5
			x2 = -5
			while (x1 < -4.1):
				x1 += 0.1
				x2 += 0.05
				self.wait(0.001)
			x1 = -5
			while (x1 < -4.1):
				x1 += 0.1
				x2 += 0.05
				self.wait(0.001)
		x1 = -5
		x2 = -5
		waiter(2)
		stuff.append( Text("T").shift(DOWN*2 + RIGHT*4).set_color(BLUE).scale(3) )
		self.play(FadeIn(stuff[-1], run_time=5.0))
		
		electrons3 = []
		electrons4 = []
		for i in range(10):
			electrons3.append(electroner(i, 0.25, YELLOW, 0))
			electrons4.append(electroner(i, -0.25, YELLOW, 1))
		ww = Group(*electrons3, *electrons4)
		self.play(ReplacementTransform(stuff[1], ww))
		for i in range(20):
			x1 = -5
			x2 = -5
			while (x1 < -4.1):
				x1 += 0.1
				x2 += 0.1
				self.wait(0.001)
		self.play(FadeOut(Group(*stuff, ww)))
		













		title2 = Text("Josephson Junction").shift(UP*3.5)
		self.play(Transform(title, title2))


		wire1 = Line([-5, 0.75, 0], [5, 0.75, 0])
		wire2 = Line([-5, -0.75, 0], [5, -0.75, 0])
		wire = Group(wire1, wire2)

		x1 = -5
		x2 = -5
		def electroner(i, j, col, m, o):
			e = Dot().scale(2).shift(UP*j + RIGHT*i)
			additional = 0
			if (o < 0.9):
				additional = 3
			def becomer(self, i=i, j=j, col=col, m=m):
				if (m == 0):
					self.become( Dot(fill_opacity=o).scale(2).shift(UP*j + RIGHT*i + RIGHT*x1 + RIGHT*additional) ).set_color(col)
				else:
					self.become( Dot(fill_opacity=o).scale(2).shift(UP*j + RIGHT*i + RIGHT*x2 + RIGHT*additional) ).set_color(col)
			e.add_updater(becomer)
			return e
		electrons3 = []
		electrons4 = []
		for i in range(4):
			electrons3.append(electroner(i, 0.25, YELLOW, 0, 1))
			electrons4.append(electroner(i, -0.25, YELLOW, 0, 1))
		ww = Group(*electrons3, *electrons4)

		electrons1 = []
		electrons2 = []
		for i in range(4):
			electrons1.append(electroner(i+3, 0.25, YELLOW, 1, 0.5))
			electrons2.append(electroner(i+3, -0.25, YELLOW, 1, 0.5))
		yy = Group(*electrons1, *electrons2)


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( wire )
		stuff.append( Group(ww, yy) )
		stuff.append( Rectangle(width=1, height=2, fill_opacity=1, fill_color=WHITE) )
		stuff.append( Tex(r"\text{Quantum Tunneling}").shift(DOWN*2) )
		stuff.append( Tex(r"E_{before} > E_{after}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		x1 = -5
		x2 = -5
		for i in range(20):
			x1 = -5
			x2 = -5
			while (x1 < -4.1):
				x1 += 0.1
				x2 += 0.1
				self.wait(0.001)
		waiter(10)
		self.play(FadeOut(Group(*stuff, ww)))






		title2 = Text("Superconducting Quantum Interference Device ").shift(UP*3.5)
		self.play(Transform(title, title2))
		corona = ImageMobject("./squider.jpeg").scale(1.5)
		self.play(FadeIn(corona))
		waiter(30)










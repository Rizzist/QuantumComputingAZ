from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Repeaters & Entanglement Distillation").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class repeater(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Repeaters & Entanglement Distillation").scale(0.9)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Quantum Repeaters").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Quantum Channel connecting long distances}").shift(UP*2.5) )
		stuff.append( Tex(r"Alice").shift(UP*1 + LEFT*6) )
		stuff.append( Tex(r"Bob").shift(UP*1 + RIGHT*6) )
		stuff.append( Dot().shift(LEFT*4.5 + UP*1).scale(1) )
		stuff.append( Dot().shift(RIGHT*4.5 + UP*1).scale(1) )
		stuff.append( Line(np.array([-4.5, 1, 0]), np.array([4.5, 1, 0])) )
		for i in stuff:
			self.play(FadeIn(i))

		x = 0
		def animUpdater(self):
			self.become( Dot().shift(LEFT*4.5 + RIGHT*x + UP*1).scale(1*(30-x)/10).set_color(RED) )
		animDot = Dot().shift(LEFT*4.5 + UP*1).scale(3).set_color(RED)
		animDot.add_updater(animUpdater)
		self.play(FadeIn(animDot))
		while (x < 9-0.05):
			x += 0.05
			self.wait(0.001)
		self.play(FadeOut(animDot))
		self.wait(0.5)
		x = 0
		def animUpdater(self):
			self.become( Dot().shift(LEFT*4.5 + RIGHT*x + UP*1).scale(2.5*(12-x)/10).set_color(RED) )
		animDot = Dot().shift(LEFT*4.5 + UP*1).scale(3).set_color(RED)
		animDot.add_updater(animUpdater)
		self.play(FadeIn(animDot))
		while (x < 9-0.05):
			x += 0.05
			self.wait(0.001)
		self.remove(animDot)
		waiter(5)
		#self.play(FadeOut(Group(*stuff)))







		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"Alice").shift(DOWN*1 + LEFT*6) )
		stuff2.append( Tex(r"Bob").shift(DOWN*1 + RIGHT*6) )
		stuff2.append( Dot().shift(LEFT*4.5 + DOWN*1).scale(1) )
		stuff2.append( Dot().shift(RIGHT*4.5 + DOWN*1).scale(1) )
		stuff2.append( Dot().shift(LEFT*0.25 + DOWN*1).scale(1) )
		stuff2.append( Dot().shift(RIGHT*0.25 + DOWN*1).scale(1) )
		stuff2.append( Line(np.array([-4.5, -1, 0]), np.array([-0.25, -1, 0])) )
		stuff2.append( Line(np.array([0.25, -1, 0]), np.array([4.5, -1, 0])) )
		
		stuff2.append( Dot().shift(LEFT*0.25 + DOWN*1).scale(3).set_color(BLUE) )
		stuff2.append( Dot().shift(RIGHT*0.25 + DOWN*1).scale(3).set_color(BLUE) )
		for i in stuff2:
			self.play(FadeIn(i))

		x = 0
		def animUpdater(self):
			self.become( Dot().shift(LEFT*4.5 + RIGHT*x + DOWN*1).scale(2.5*(12-x)/10).set_color(RED) )
		animDot = Dot().shift(LEFT*4.5 + DOWN*1).scale(3).set_color(RED)
		animDot.add_updater(animUpdater)
		self.play(FadeIn(animDot))
		while (x < 4.25-0.05):
			x += 0.05
			self.wait(0.001)
		self.remove(animDot, stuff2[-2], stuff2[-1])
		x = 4.75
		def animUpdater(self):
			self.become( Dot().shift(LEFT*4.5 + RIGHT*x + DOWN*1).scale(2.5*(12-(x-4.5))/10).set_color(RED) )
		animDot = Dot().shift(LEFT*4.5 + DOWN*1).scale(3).set_color(RED)
		animDot.add_updater(animUpdater)
		self.add(animDot)
		while (x < 9-0.05):
			x += 0.05
			self.wait(0.001)
		#self.remove(animDot)
		waiter(10)
		self.play(FadeIn(Group(stuff2[-1], stuff2[-2])))
		waiter(5)
		self.play(FadeOut(Group(*stuff, *stuff2, animDot)))






















		

		title2 = Text("Entanglement Distillation").shift(UP*3.5)
		self.play(Transform(title, title2))
		
		thesetter = Group(Tex(r"Alice").shift(LEFT*6), Tex(r"Bob").shift(RIGHT*6), Dot().shift(LEFT*4.5).scale(1), Dot().shift(RIGHT*4.5).scale(1), Dot().shift(LEFT*0.25).scale(1), Dot().shift(RIGHT*0.25).scale(1), Line(np.array([0.25, 0, 0]), np.array([4.5, 0, 0])), Line(np.array([-4.5, 0, 0]), np.array([-0.25, 0, 0])) )

		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"\text{Tranferring Entanglement to increase Entanglement Quality}").shift(UP*2.5) )
		stuff2.append( thesetter.shift(UP*1)  )
		stuff2.append( Group(Dot().shift(LEFT*0.25 + UP*1).scale(3).set_color(BLUE), Dot().shift(RIGHT*0.25 + UP*1).scale(3).set_color(BLUE)) )

		for i in stuff2:
			self.play(FadeIn(i))

		class createEntangleSet():
			def __init__(self, color):
				self.x = 0.1
				self.y = -1
				self.y2 = 0
				self.r = 3
				def update_dot1(self2):
					self2.become(Dot().shift(LEFT*4.5 + DOWN*self.y).scale(3).set_color(color))
				def update_dot2(self2):
					self2.become(Dot().shift(LEFT*4.5 + RIGHT*self.x + DOWN*self.y).scale(self.r).set_color(color))
				def update_etgl(self2):
					self2.become(CurvedArrow(np.array([-4.5, -self.y-self.y2, 0]), np.array([-4.5 + self.x, -self.y-self.y2, 0]), angle=np.pi/8, color=GREY))
				self.dot1 = Dot().shift(LEFT*4.5).scale(3).set_color(color).add_updater(update_dot1)
				self.dot2 = Dot().shift(LEFT*4.5 + RIGHT*self.x).scale(3).set_color(color).add_updater(update_dot2)
				self.etgl = CurvedArrow(np.array([-4.5, 0, 0]), np.array([-4.5 + self.x, 0, 0]), angle=np.pi/8, color=GREY).add_updater(update_etgl)
			def get(self):
				return Group(self.dot1, self.dot2, self.etgl)
			def getPos(self):
				return [self.x, self.y]
			def getArrow(self):
				return self.y2


		ebits = []
		for i in range(0, 3):
			ebits.append( createEntangleSet(ORANGE) )
		ebits.append( createEntangleSet(RED) )
		self.add(ebits[3].get())
		self.add(ebits[0].get())
		self.add(ebits[1].get())
		self.add(ebits[2].get())
		
		#self.play(FadeOut(Group(*stuff2)))

		for i in range(4):
			while(ebits[i].getPos()[0] < 4.25-0.05):
				ebits[i].x += 0.05
				ebits[i].r -= 0.015
				self.wait(0.001)
			self.remove(stuff2[-1])
			ebits[i].x += 0.5
			ebits[i].r = 3
			while(ebits[i].getPos()[0] < 9-0.05):
				ebits[i].x += 0.05
				ebits[i].r -= 0.01
				self.wait(0.001)
			while(ebits[i].getPos()[1] < i/1.5):
				ebits[i].y += 0.05
				self.wait(0.001)
			self.add(stuff2[-1])
		waiter(5)
		for i in range(4):
			while(ebits[i].getArrow() + ebits[i].getPos()[1] < 2-0.05):
				ebits[i].y2 += 0.05
				self.wait(0.001)
			ebits[3].r += 0.1
				

		newetgl = CurvedArrow(np.array([-4.5, -2, 0]), np.array([4.5, -2, 0]), angle=np.pi/8, color=WHITE)
		self.play(FadeIn(newetgl))
		finale = Tex(r"\text{From 40\% to 95\% Entanglement!}").shift(DOWN*3.3)
		self.play(FadeIn(finale))
		waiter(15)




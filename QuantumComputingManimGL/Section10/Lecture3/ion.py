from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Ion Trapping Technique").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class ion(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Ion Trapping Technique").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Ion Trapping Technique").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		axes = Axes(x_range=(-1, 10, 1), y_range=(-1, 10, 1), height=6, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } )
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(LEFT*0)

		func = lambda t : (t-4.5)**2
		graph = axes.get_graph(func, color=BLUE, step_size=0.001, ) 
		ball = Dot(color=RED).scale(2).move_to(axes.c2p(2.5, 4+1))
		x = 2.5
		y = 5
		t = 1000
		def ballUpdater(self):
			x = t/400 * np.cos(t*np.pi/100) + 4.5
			y = (x-4.5)**2 
			self.become( Dot(color=RED).scale(2).move_to(axes.c2p(x, y)) )
		ball.add_updater(ballUpdater)



		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Step 1: Create Potential Well via EM}").shift(UP*1) )
		stuff.append( Tex(r"\text{Step 2: Put Object w/ Low KE in Well}").shift(UP*0) )
		stuff.append( Tex(r"\text{Step 3: Its now Trapped}").shift(DOWN*1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(3)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))




		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( axes )
		stuff.append( graph )
		stuff.append( ball )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(2)
		waiter(5)
		while (t > 50):
			t -= 1
			self.wait(0.001)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))




		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Step 1: Create 3D Potential Well via EM}").shift(UP*1).set_color(BLACK) )
		stuff.append( Tex(r"\text{Step 1: Create \& Spin 3D Potential Well via EM}").shift(UP*0) )
		stuff.append( Tex(r"\text{Step 2: Put Object w/ Low KE in Well}").shift(DOWN*1) )
		stuff.append( Tex(r"\text{Step 3: Its now Trapped}").shift(DOWN*2) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(3)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))


		corona = ImageMobject("./iontrap.jpeg").shift(DOWN*0.5).scale(1.5)
		self.play(FadeIn(corona))
		waiter(10)




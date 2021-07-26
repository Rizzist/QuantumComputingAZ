from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("XZZX Surface Code").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class xzzx(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("XZZX Suface Code").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("XZZX Code").shift(UP*3.5)
		self.play(FadeIn(title))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\ket{\psi}").shift(UP*0) )
		stuff.append( Tex(r"\ket{0_z}").shift(UP*0 + LEFT*3) )
		stuff.append( Tex(r"\ket{0_z}").shift(UP*0 + RIGHT*3) )
		stuff.append( Tex(r"\ket{0_x}").shift(UP*2) )
		stuff.append( Tex(r"\ket{0_x}").shift(DOWN*2) )

		for i in stuff:
			self.play(FadeIn(i))
		waiter(2)
		self.remove(stuff[0])
		stuff[0] = Tex(r"a_0\ket{0} + a_1\ket{1}").shift(UP*0)
		self.add(stuff[0])
		waiter(4)
		self.remove(Group(stuff[0], stuff[1], stuff[2]))
		stuff[0] = Tex(r"a_0\ket{0} - a_1\ket{1}").shift(UP*0)
		stuff[1] = Tex(r"\ket{1_z}").shift(UP*0 + LEFT*3).set_color(RED)
		stuff[2] = Tex(r"\ket{1_z}").shift(UP*0 + RIGHT*3).set_color(RED)

		stuff[1].generate_target()
		stuff[2].generate_target()
		stuff[1].target = Tex(r"\ket{1_z}").shift(UP*0 + LEFT*3)
		stuff[2].target = Tex(r"\ket{1_z}").shift(UP*0 + RIGHT*3)
		self.add(Group(stuff[0], stuff[1], stuff[2]))
		self.play(MoveToTarget(stuff[1], run_time=2), MoveToTarget(stuff[2], run_time=2))
		waiter(2)

		waiter(2)
		self.remove(Group(stuff[0], stuff[1], stuff[2]))
		stuff[0] = Tex(r"a_0\ket{0} + a_1\ket{1}").shift(UP*0)
		stuff[1] = Tex(r"\ket{0_z}").shift(UP*0 + LEFT*3).set_color(RED)
		stuff[2] = Tex(r"\ket{0_z}").shift(UP*0 + RIGHT*3).set_color(RED)

		stuff[1].target = Tex(r"\ket{0_z}").shift(UP*0 + LEFT*3)
		stuff[2].target = Tex(r"\ket{0_z}").shift(UP*0 + RIGHT*3)
		self.add(Group(stuff[0], stuff[1], stuff[2]))
		self.play(MoveToTarget(stuff[1], run_time=2), MoveToTarget(stuff[2], run_time=2))
		waiter(2)

		waiter(2)
		self.remove(Group(stuff[0], stuff[3], stuff[4]))
		stuff[0] = Tex(r"a_1\ket{0} + a_0\ket{1}").shift(UP*0)
		stuff[3] = Tex(r"\ket{1_x}").shift(UP*2).set_color(BLUE)
		stuff[4] = Tex(r"\ket{1_x}").shift(DOWN*2).set_color(BLUE)

		stuff[3].generate_target()
		stuff[4].generate_target()
		stuff[3].target = Tex(r"\ket{1_x}").shift(UP*2)
		stuff[4].target = Tex(r"\ket{1_x}").shift(DOWN*2)
		self.add(Group(stuff[0], stuff[3], stuff[4]))
		self.play(MoveToTarget(stuff[3], run_time=2), MoveToTarget(stuff[4], run_time=2))
		waiter(2)

		waiter(2)
		self.remove(Group(stuff[0], stuff[3], stuff[4]))
		stuff[0] = Tex(r"a_0\ket{0} + a_1\ket{1}").shift(UP*0)
		stuff[3] = Tex(r"\ket{0_x}").shift(UP*2).set_color(BLUE)
		stuff[4] = Tex(r"\ket{0_x}").shift(DOWN*2).set_color(BLUE)

		stuff[3].generate_target()
		stuff[4].generate_target()
		stuff[3].target = Tex(r"\ket{0_x}").shift(UP*2)
		stuff[4].target = Tex(r"\ket{0_x}").shift(DOWN*2)
		self.add(Group(stuff[0], stuff[3], stuff[4]))
		self.play(MoveToTarget(stuff[3], run_time=2), MoveToTarget(stuff[4], run_time=2))
		waiter(2)
		self.play(FadeOut(Group(*stuff)))



		title2 = Text("Stabilizer of XZZX").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\begin{tabular}{ c c c c c c } $g_1$ & X & Z & Z & X & I   \\ $g_2$ & I & X & Z & Z & X   \\ $g_3$ & X & I & X & Z & Z \\ $g_4$ & Z & X & I & X & Z \end{tabular}").shift(DOWN*0) ) 
		stuff.append( Line(np.array([-2, -1, 0]), np.array([-2, 1, 0])) )
		stuff.append( Tex(r"\text{XZZX Code Error Syndromes}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
		waiter(20)
		self.play(FadeOut(Group(*stuff)))


		title2 = Text("Surface Code").shift(UP*3.5)
		self.play(Transform(title, title2))

		def codeSurface(x, y):
			scaler = 1
			shifter = 0.5
			c = Dot(np.array([x, y, 0]), color=WHITE).scale(scaler)
			cz = Dot(np.array([x+shifter, y, 0]), color=RED).scale(scaler)
			cz2 = Dot(np.array([x-shifter, y, 0]), color=RED).scale(scaler)
			cx = Dot(np.array([x, y+shifter, 0]), color=BLUE).scale(scaler)
			cx2 = Dot(np.array([x, y-shifter, 0]), color=BLUE).scale(scaler)
			return Group(c, cz, cz2, cx, cx2)

		surfaces = []
		
		surfaces.append( codeSurface(0, 0) )
		surfaces[0].generate_target()
		surfaces[0].target.rotate(np.pi/4)
		self.play(FadeIn(surfaces[0]))
		self.play(MoveToTarget(surfaces[0]))
		surfaces.append( codeSurface(2, 0) )
		surfaces[1].generate_target()
		surfaces[1].target.rotate(-np.pi/4)
		self.play(FadeIn(surfaces[1]))
		self.play(MoveToTarget(surfaces[1]))
		surfaces[1].target.shift(LEFT*1.3)
		self.play(MoveToTarget(surfaces[1]))

		surfaces.append( codeSurface(0, 0.7).rotate(-np.pi/4) )
		surfaces.append( codeSurface(0, -0.7).rotate(-np.pi/4) )
		surfaces.append( codeSurface(-0.7, 0).rotate(-np.pi/4) )
		self.play(FadeIn(surfaces[2]))
		self.play(FadeIn(surfaces[3]))
		self.play(FadeIn(surfaces[4]))

		surfaces.append( codeSurface(0.7, 0.7).rotate(np.pi/4) )
		surfaces.append( codeSurface(1.4, 0).rotate(np.pi/4) )
		surfaces.append( codeSurface(0.7, -0.7).rotate(np.pi/4) )
		surfaces.append( codeSurface(-1.4, 0).rotate(np.pi/4) )
		surfaces.append( codeSurface(-0.7, 0.7).rotate(np.pi/4) )
		surfaces.append( codeSurface(0, 1.4).rotate(np.pi/4) )
		surfaces.append( codeSurface(-0.7, -0.7).rotate(np.pi/4) )
		surfaces.append( codeSurface(0, -1.4).rotate(np.pi/4) )

		self.play(FadeIn(surfaces[5]))
		self.play(FadeIn(surfaces[6]))
		self.play(FadeIn(surfaces[7]))

		self.play(FadeIn(surfaces[8]))
		self.play(FadeIn(surfaces[9]))
		self.play(FadeIn(surfaces[10]))

		self.play(FadeIn(surfaces[11]))
		self.play(FadeIn(surfaces[12]))


		surfaces.append( codeSurface(0.7, 1.4).rotate(-np.pi/4) )
		surfaces.append( codeSurface(1.4, 0.7).rotate(-np.pi/4) )
		self.play(FadeIn(surfaces[13]))
		self.play(FadeIn(surfaces[14]))
		surfaces.append( codeSurface(-0.7, 1.4).rotate(-np.pi/4) )
		surfaces.append( codeSurface(-1.4, 0.7).rotate(-np.pi/4) )
		self.play(FadeIn(surfaces[15]))
		self.play(FadeIn(surfaces[16]))
		surfaces.append( codeSurface(0.7, -1.4).rotate(-np.pi/4) )
		surfaces.append( codeSurface(1.4, -0.7).rotate(-np.pi/4) )
		self.play(FadeIn(surfaces[17]))
		self.play(FadeIn(surfaces[18]))
		surfaces.append( codeSurface(-0.7, -1.4).rotate(-np.pi/4) )
		surfaces.append( codeSurface(-1.4, -0.7).rotate(-np.pi/4) )
		self.play(FadeIn(surfaces[19]))
		self.play(FadeIn(surfaces[20]))
		waiter(6)
		self.play(FadeOut(Group(*surfaces)))
		
		

		def codeSurface2(x, y, direc):
			scaler = 1
			shifter = 0.5
			c = Dot(np.array([x, y, 0]), color=BLACK).scale(scaler)
			cz = Dot(np.array([x+shifter, y, 0]), color=GREY).scale(scaler)
			cz2 = Dot(np.array([x-shifter, y, 0]), color=GREY).scale(scaler)
			cx = Dot(np.array([x, y+shifter, 0]), color=GREY).scale(scaler)
			cx2 = Dot(np.array([x, y-shifter, 0]), color=GREY).scale(scaler)
			return Group(c, cz, cz2, cx, cx2).rotate(direc * np.pi/4)

		def codeSurfaceZ(x, y, direc):
			scaler = 1.2
			shifter = 0.5
			c = Dot(np.array([x, y, 0]), color=WHITE).scale(scaler)
			cz = Dot(np.array([x+shifter, y, 0]), color=RED).scale(scaler)
			cz2 = Dot(np.array([x-shifter, y, 0]), color=RED).scale(scaler)
			return Group(c, cz, cz2).rotate(direc * np.pi/4)
		def codeSurfaceX(x, y, direc):
			scaler = 1.2
			shifter = 0.5
			c = Dot(np.array([x, y, 0]), color=WHITE).scale(scaler)
			cx = Dot(np.array([x, y+shifter, 0]), color=BLUE).scale(scaler)
			cx2 = Dot(np.array([x, y-shifter, 0]), color=BLUE).scale(scaler)
			return Group(c, cx, cx2).rotate(direc * np.pi/4)
		surfaces = []
		split = 0.7
		for i in range(-4, 4):
			for j in range(-4, 4):
				surfaces.append( codeSurface2(split*i, split*j, 1) )
		self.play(FadeIn(Group(*surfaces)))

		surfacesTemp = []
		surfacesTemp.append( codeSurfaceZ(split*1, split*1, 1) )
		surfacesTemp.append( codeSurfaceX(split*2, split*1, -1) )
		surfacesTemp.append( codeSurfaceX(split*-3, split*-2, 1) )
		surfacesTemp.append( codeSurfaceX(split*2, split*-1, -1) )
		surfacesTemp.append( codeSurfaceZ(split*2, split*-2, 1) )
		surfacesTemp.append( codeSurfaceZ(split*0, split*-3, -1) )
		surfacesTemp.append( codeSurfaceZ(split*-3, split*2, 1) )
		surfacesTemp.append( codeSurfaceZ(split*-1, split*3, -1) )
		self.play(FadeIn(Group(*surfacesTemp)))
		waiter(5)
		for i in surfacesTemp:
			self.play(FadeOut(i))
		#self.play(FadeOut(Group(*surfacesTemp)))
		surfacesTemp = []
		surfacesTemp.append( codeSurfaceZ(split*-1, split*-3, 1) )
		surfacesTemp.append( codeSurfaceX(split*-2, split*3, 1) )
		surfacesTemp.append( codeSurfaceX(split*3, split*-3, 1) )
		surfacesTemp.append( codeSurfaceX(split*0, split*0, 1) )
		surfacesTemp.append( codeSurfaceZ(split*2, split*2, 1) )
		surfacesTemp.append( codeSurfaceZ(split*3, split*-4, -1) )
		surfacesTemp.append( codeSurfaceZ(split*-4, split*3, 1) )
		surfacesTemp.append( codeSurfaceZ(split*-4, split*-3, -1) )
		self.play(FadeIn(Group(*surfacesTemp)))
		waiter(5)
		for i in surfacesTemp:
			self.play(FadeOut(i))
		waiter(20)



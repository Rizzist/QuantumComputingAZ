from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Feature Maps").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class feature(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Feature Maps").scale(1.1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Quantum Feature Maps").shift(UP*3.5)
		self.play(FadeIn(title))

		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(FadeIn(Group(axes, grid)))


		dots = []
		for i in range(0, 20):
			r = random.randint(100, 150)/100
			t = random.randint(1, 360)
			ang = t * 3.14159/180
			x = r*np.cos(ang)
			y = r*np.sin(ang)
			dots.append( Dot(np.array([x, y, 1]), color=RED).scale(1) )
		for i in range(0, 20):
			r = random.randint(250, 300)/100
			t = random.randint(1, 360)
			ang = t * 3.14159/180
			x = r*np.cos(ang)
			y = r*np.sin(ang)
			dots.append( Dot(np.array([x, y, -2]), color=BLUE).scale(1.2) )

		
		self.play(FadeIn(Group(*dots)))
		waiter(10)


		frame = self.camera.frame
		frame.generate_target()
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)
		def spin(m, dt):
			m.increment_theta(0.1 * dt)
		frame.add_updater(spin)
		waiter(5)
		sq = Square(7, fill_color=YELLOW, fill_opacity=0.2)
		self.play(FadeIn(sq))
		waiter(10)
		self.play(FadeOut(Group(sq, *dots)))







		def qubit3d(xPos, yPos):
			sphere = Sphere(radius = 1, point=ORIGIN, color=RED)
			sphereMesh = SurfaceMesh(sphere, resolution=(7, 7), flat_stroke=True, color=GREY)

			labelpX = Tex(r'\ket{-}').shift(RIGHT*1.5)
			labelrX = Tex(r'\ket{+}').shift(LEFT*1.5)

			labelpY = Tex(r'\ket{-i}').shift(UP*1.5)
			labelrY = Tex(r'\ket{+i}').shift(DOWN*1.5)

			labelpZ = Tex(r'\ket{0}').rotate(PI/2, axis=RIGHT).shift(OUT*1.5)
			labelrZ = Tex(r'\ket{1}').rotate(PI/2, axis=RIGHT).shift(IN*1.5)

			x = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), fill_color=GREY_E, color=GREY_E)
			y = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), fill_color=GREY_E, color=GREY_E)
			z = Line(np.array([0, 0, -1]), np.array([0, 0, 1]), fill_color=GREY_E, color=GREY_E)
		#self.add_fixed_in_frame_mobjects(labelX, labelY, labelZ)
			vect = Vector(direction=[0, 0, 1])
			qubitG1 = Group(sphereMesh, x, y, z, labelpX, labelpY, labelpZ, labelrX, labelrY, labelrZ)
			qubitG1.shift(RIGHT*xPos + UP*yPos)
			return qubitG1
		def vect3d(x, y, direction):
			return Vector(direction=[0, 0, direction]).shift(RIGHT*x + UP*y)
		the3dqubs = []
		the3dqubs.append(qubit3d(0, 0))
		self.add(*the3dqubs)
		frame.target.set_width(7)
		self.play(MoveToTarget(frame))

		dots3d = []
		cols3d = []
		pos3d = []
		totalDots = 30
		for i in range(0, totalDots):
			col = BLUE
			if (random.randint(0, 1) == 0):
				col = RED
			r = random.randint(1, 100)/100
			phi = random.randint(0, 180) * 3.14159/180
			theta = random.randint(0, 360) * 3.14159/180

			x = r * np.cos(phi) * np.sin(theta)
			y = r * np.sin(phi) * np.sin(theta)
			z = r * np.cos(theta)
			dots3d.append( Sphere(radius = 0.1, fill_color=col, fill_opacity=1, color=col).shift(LEFT*x + UP*y + OUT*z) )
			cols3d.append( col )
			pos3d.append( [r, phi, theta] )
		self.play(FadeIn(Group(*dots3d)))
		waiter(10)
		number = Text("0").shift(UP*2 + RIGHT*2)
		self.play(FadeIn(number))
		for j in range(8):
			for i in range(0, totalDots):
				pos3d[i][0] = pos3d[i][0] + (1 - pos3d[i][0])*0.2
				if cols3d[i] == RED:
					pos3d[i][1] = (pos3d[i][1]*180/3.14159 + (180 - pos3d[i][1]*180/3.14159)*0.2) * 3.14159/180
				else: 
					pos3d[i][1] = (pos3d[i][1]*180/3.14159)* 0.8 * 3.14159/180
				x = pos3d[i][0] * np.cos(pos3d[i][2]) * np.sin(pos3d[i][1])
				y = pos3d[i][0] * np.sin(pos3d[i][2]) * np.sin(pos3d[i][1])
				z = pos3d[i][0] * np.cos(pos3d[i][1])
				dots3d[i].generate_target()
				dots3d[i].target.move_to(LEFT*x + UP*y + OUT*z)
				self.play(MoveToTarget(dots3d[i]), run_time=0.1)
			if (j < 4):
				number2 = Text(str(j)).shift(UP*2 + LEFT*2)
			else:
				number2 = Text(str(j)).shift(DOWN*2 + LEFT*2)
			self.play(Transform(number, number2))
			waiter(0.2)
		waiter(20)
		"""
		self.play(FadeOut(Group(axes, grid, sq, *dots)))
		frame.remove_updater(spin)
		frame.target.set_euler_angles(
			theta=0 * DEGREES,
			phi=0 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		self.wait(10)
		"""
		












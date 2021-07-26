from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Barren Plateus, Narrow Gorge Phenomenon").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class barren(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Barren Plateus, Narrow Gorge Phenomenon").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
			
		title = Text("Barren Plateus").shift(UP*3.5)
		self.play(FadeIn(title))



		axes = Axes((-3, 10), (-1, 8))
		axes.add_coordinate_labels()

		self.play(Write(axes, lag_ratio=0.01, run_time=1))

		parabola = axes.get_graph(lambda x: 0.25 * x**2)
		parabola.set_stroke(BLUE)
		self.play(ShowCreation(parabola) ) 
		self.wait()

		# You can use axes.input_to_graph_point, abbreviated
		# to axes.i2gp, to find a particular point on a graph
		dot = Dot(color=RED)
		dot.move_to(axes.i2gp(2, parabola))
		self.play(FadeIn(dot, scale=0.5))

		# A value tracker lets us animate a parameter, usually
		# with the intent of having other mobjects update based
		# on the parameter
		x_tracker = ValueTracker(2)
		f_always(
			dot.move_to,
			lambda: axes.i2gp(x_tracker.get_value(), parabola)
		)

		#add more here
		self.play(x_tracker.animate.set_value(1.6), run_time=0.2)
		self.play(x_tracker.animate.set_value(1.2), run_time=0.4)
		self.play(x_tracker.animate.set_value(0.8), run_time=0.8)
		self.play(x_tracker.animate.set_value(0.4), run_time=1.2)
		self.play(x_tracker.animate.set_value(0.2), run_time=1.2)
		self.play(x_tracker.animate.set_value(0.1), run_time=1.2)
		self.play(x_tracker.animate.set_value(0), run_time=1.2)
		self.wait()



		step_graph = axes.get_graph(
			lambda x: 2.0 if x > 3 else 1.0,
			discontinuities=[3],
			color=GREEN,
		)
		step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)
		self.play(
			ReplacementTransform(parabola, step_graph),
			FadeIn(step_label),
			FadeOut(x_tracker)
		)

		x2_tracker = ValueTracker(5)
		f_always(dot.move_to, lambda: axes.i2gp(x2_tracker.get_value(), step_graph) )
		self.play(x2_tracker.animate.set_value(5.1), run_time=1)
		waiter(1)
		x2_tracker = ValueTracker(8)
		f_always(dot.move_to, lambda: axes.i2gp(x2_tracker.get_value(), step_graph) )
		waiter(1)
		x2_tracker = ValueTracker(6)
		f_always(dot.move_to, lambda: axes.i2gp(x2_tracker.get_value(), step_graph) )
		waiter(1)
		x2_tracker = ValueTracker(7)
		f_always(dot.move_to, lambda: axes.i2gp(x2_tracker.get_value(), step_graph) )
		waiter(5)


		self.play(FadeOut(Group(axes, dot, step_graph, step_label)))




		
		stuff = []
		#stuff.append( Tex(r"") )
		stuff.append( Tex(r"\ket{\psi (\theta)} \to \ket{0_n}").shift(DOWN*2.5) )
		stuff.append( Tex(r"C_g = \bra{\psi (\theta)} (\mathbb{I} - \ket{0_n}\bra{0_n}) \ket{\psi (\theta)}").shift(DOWN*3.25) )
		#stuff.append( Tex(r"").shift(DOWN*0) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(FadeIn(Group(axes, grid)))
		labelX = Tex(r"\ket{x}").shift(RIGHT*4.5)
		#labelY = Tex(r"\ket{p}").shift(UP*2.75)
		#self.play(FadeIn(Group(labelX)))

		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)
		def spin(m, dt):
			m.increment_theta(0.1 * dt)
		frame.add_updater(spin)
		# Gauss surface
		op = np.matrix([[1, 0], [0, 1]])
		dispop = np.exp(op)
		gaussian = ParametricSurface(
			lambda u, v: [u, v, -3*np.absolute(np.linalg.det(np.exp(    -1*np.matrix([6*u, 6*v])*op*np.transpose(np.matrix([u, v]))     ) )) - 2],#np.exp(-(u**2) - v**2)],
			u_range=(-2.5, 2.5),
			v_range=(-2.5, 2.5),
			resolution=(90, 90),
		)
		gaussian.set_color(GREEN, 1)
		gaussian.stretch(2, 2)
		self.play(
			FadeIn(gaussian),
			frame.set_phi, 70 * DEGREES,
			frame.set_theta, 10 * DEGREES,
			run_time=3
		)

		title2 = Text("Narrow Gorge Phenomenon").shift(UP*3.5)
		self.play(Transform(title, title2))


		self.wait(5)
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.set_theta, -100 * DEGREES,
			run_time=2
		)
		self.play(FadeOut(stuff[1]))
		stuff[1] = Tex(r"C_l = \bra{\psi (\theta)} (\mathbb{I} - \sum_{j=1}^n \ket{0}\bra{0}_j \otimes \mathbb{I}) \ket{\psi (\theta)}").shift(DOWN*3.25) 
		


		gaussianc = ParametricSurface(
			lambda u, v: [u, v, -2*np.absolute(np.linalg.det(np.exp(    -1*np.matrix([u*0.25, v*0.25])*op*np.transpose(np.matrix([u, v]))     ) )) - 1],#np.exp(-(u**2) - v**2)],
			u_range=(-2.5, 2.5),
			v_range=(-2.5, 2.5),
			resolution=(90, 90),
		)
		gaussianc.set_color(GREEN, 1)
		gaussianc.stretch(2, 2)
		self.play(
			FadeTransform(gaussian, gaussianc),
			frame.set_phi, 50 * DEGREES,
			frame.set_theta, 10 * DEGREES,
			run_time=3
		)
		self.play(FadeIn(stuff[1]))
		self.wait(5)
		self.play(
			frame.increment_phi, 20 * DEGREES,
			frame.set_theta, -120 * DEGREES,
			run_time=2
		)
		waiter(30)










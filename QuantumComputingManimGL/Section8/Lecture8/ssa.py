from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Wehrl entropy, Strong Subadditivity of Quantum Entropy (SSA)").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class ssa(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Wehrl entropy, SSA, Lieb's Theorem").scale(1.1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Wehrl Entropy").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"Q_\rho(x, p) = \int \phi(x, p \mid y)^* \rho(y, y^\prime) \phi(x, p \mid y^\prime) dy dy^\prime").shift(UP*2.6) )
		stuff.append( Tex(r"\phi(x, p \mid y) = \pi^{-0.25} e^{-\mid y-x \mid^2 /2 + ipx }").shift(UP*1.6) )
		stuff.append( Tex(r"S_W(\rho) = -\int Q_\rho(x, p) \log(Q_\rho(x, p)) dx dp").shift(UP*0.6) )
		stuff.append( Tex(r"\text{1. } S_W(\rho) \geq 1 \to \text{Wehrl Conjecture (Proven) }").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{2. } S_W(\rho) > S(\rho) \to \text{Von Neumann Quantum Entropy} }").shift(DOWN*2.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))



		title2 = Text("Strong Subadditivity of Quantum Entropy (SSA)").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Given Von Neumann Quantum Entropy } S(\rho)=-Tr(\rho \log(\rho))").shift(UP*2.5) )
		stuff.append( Tex(r"\text{and Tripartite Quantum State } \rho^{ABC}:").shift(UP*1.9 + LEFT*2) )
		stuff.append( Tex(r"S(\rho^{ABC}) + S(\rho^B) \leq S(\rho^{AB}) + S(\rho^{BC})").shift(UP*0) )
		stuff.append( Tex(r"\text{Where: } S(\rho^{AB}) = -Tr(\rho^{AB} \log(\rho^{AB}))").shift(DOWN*1) )
		stuff.append( Tex(r"\text{Quantum Entropy is a Concave Function}").shift(DOWN*3) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))


		axes = Axes((-5, 7), (-1, 5))
		axes.add_coordinate_labels()

		self.play(Write(axes, lag_ratio=0.01, run_time=1))

		parabola = axes.get_graph(lambda x: -0.25 * x**2+3, step_size=0.001)
		parabola.set_stroke(BLUE)
		self.play(ShowCreation(parabola) ) 
		self.wait()

		# You can use axes.input_to_graph_point, abbreviated
		# to axes.i2gp, to find a particular point on a graph
		dot = Dot(color=RED)
		dot.move_to(axes.i2gp(2, parabola))
		self.play(FadeIn(dot, scale=0.5))

		linedots = []
		dot2 = Dot(color=WHITE)
		dot2.move_to(axes.i2gp(3, parabola))
		x2_tracker = ValueTracker(3)
		f_always(dot2.move_to, lambda: axes.i2gp(x2_tracker.get_value(), parabola) )
		linedots.append(dot2)

		dot3 = Dot(color=WHITE)
		dot3.move_to(axes.i2gp(1, parabola))
		x3_tracker = ValueTracker(1)
		f_always(dot3.move_to, lambda: axes.i2gp(x3_tracker.get_value(), parabola) )
		linedots.append(dot3)



		def lupdater(self):
			self.become( Line(linedots[0], linedots[1]) )
		line = Line(linedots[0], linedots[1]).set_color(WHITE)
		line.add_updater(lupdater)

		self.play(FadeIn(linedots[0], scale=0.5))
		self.play(FadeIn(linedots[1], scale=0.5))
		self.play(FadeIn(line))
		# A value tracker lets us animate a parameter, usually
		# with the intent of having other mobjects update based
		# on the parameter
		x_tracker = ValueTracker(2)
		f_always(dot.move_to, lambda: axes.i2gp(x_tracker.get_value(), parabola) )
		self.play(x_tracker.animate.set_value(4), x2_tracker.animate.set_value(5), x3_tracker.animate.set_value(3),run_time=3)
		self.play(x_tracker.animate.set_value(-2), x2_tracker.animate.set_value(-1), x3_tracker.animate.set_value(-3), run_time=3)
		self.wait()
		waiter(5)

		self.play(FadeOut(Group(*linedots, line, axes, parabola, dot)))


		title2 = Text("Lieb's Theorem").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Given Concave Function f and } 0 \leq \lambda \leq 1").shift(UP*2.5 + LEFT*2) )
		stuff.append( Tex(r"f(\lambda x_1 + (1-\lambda)x_2) \geq \lambda f(x_1) + (1-\lambda)f(x_2)").shift(UP*1.5) )
		stuff.append( Tex(r"\text{Can we do the same w/ Matrices?}").shift(DOWN*1) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))
		

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Given Positive Matrices } R_1, R_2, Q_1, Q_2, T_1, T_2,").shift(UP*2.5 ) )
		stuff.append( Tex(r"0 = [ R_1, R_2 ] = [ Q_1, Q_2 ] = [ T_1, T_2 ]").shift(UP*1.7) )
		stuff.append( Tex(r"R_1 \geq Q_1 + T_1").shift(UP*0.5) )
		stuff.append( Tex(r"R_2 \geq Q_2 + T_2").shift(DOWN*0.5) )
		stuff.append( Tex(r"R_1^t * R_2^{1-t} \geq Q_1^1 Q_2^{1-t} + T_1^{t} T_2^{1-t}").shift(DOWN*1.5) )
		stuff.append( Tex(r"f(A,B) = Tr(X^\dag A^t X B^{1-t}) \to \text{is Concave}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeOut(Group(*stuff)))


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"Q_1(X) = \lambda A_1 X").shift(UP*2.7) )
		stuff.append( Tex(r"Q_2(X) = \lambda X B_1").shift(UP*2.1) )
		stuff.append( Tex(r"T_1(X) = (1-\lambda) A_2 X").shift(UP*1.5) )
		stuff.append( Tex(r"T_2(X) = (1-\lambda) X B_2").shift(UP*0.9) )
		stuff.append( Tex(r"R_1(X) = Q_1 + T_1").shift(UP*0.3) )
		stuff.append( Tex(r"R_2(X) = Q_2 + T_2").shift(DOWN*0.3) )
		stuff.append( Tex(r"R_1^t * R_2^{1-t} \geq Q_1^1 Q_2^{1-t} + T_1^{t} T_2^{1-t}").shift(DOWN*1.5) )
		stuff.append( Tex(r"f(A,B) = Tr(X^\dag A^t X B^{1-t}) \to \text{let f be Trace Function").shift(DOWN*2.3) )
		stuff.append( Tex(r"S(\rho^{ABC}) + S(\rho^B) \leq S(\rho^{AB}) + S(\rho^{BC})").shift(DOWN*3.2) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		waiter(15)
		#self.play(FadeOut(Group(*stuff)))







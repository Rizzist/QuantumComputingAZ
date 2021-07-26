from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Continuous Variable Quantum Information Theory").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class cvqit(Scene):
	def construct(self):
		text = Text("Continuous Variable Quantum Information Theory").scale(0.9)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("Operators").shift(UP*3.5).scale(0.9)
		self.play(FadeIn(title))
		
		stuff = []
		stuff.append( Tex(r"\hat{a} \to \text{Annihilation Operator}").shift(UP*3) )
		stuff.append( Tex(r"\hat{a}^\dag \to \text{Creation Operator}").shift(UP*2.5) )
		stuff.append( Tex(r"\hat{x} = c(\hat{a} + \hat{a}^\dag) \to \text{Position Operator}").shift(UP*2) )
		stuff.append( Tex(r"\hat{p} = -ic(\hat{a} - \hat{a}^\dag) \to \text{Momentum Operator}").shift(UP*1.5) )
		stuff.append( Tex(r"[\hat{x}, \hat{p}] = xp - px = 2ic^2 \to \text{Commutator}").shift(UP*1) )
		stuff.append( Tex(r"[\hat{a}_i, \hat{a}_j^\dag] = \mathbb{I}").shift(UP*0.5) )
		stuff.append( Tex(r"\hat{H}(\hat{x}, \hat{p}) \to U=e^{-iHt} \to \text{Hamiltonian Simulation}").shift(DOWN*0.125) )
		stuff.append( Tex(r"\hat{H} \to \hat{x}^2 \text{ or } \hat{p}^2 \to \text{Gaussian States}").shift(DOWN*0.75) )
		stuff.append( Tex(r"D(\alpha) = {e^{\alpha \hat{a}^\dag + \alpha^* \hat{a}}} \to \text{Displacement Operator}").shift(DOWN*1.5) )
		stuff.append( Tex(r"S(z) = {e^{z^* \hat{a}^2 - z \hat{a}^{\dag 2}}} \to \text{Squeeze Operator}").shift(DOWN*2.125) )
		stuff.append( Tex(r"R(\theta) = {e^{i\theta n}} \to \text{Rotation Operator}").shift(DOWN*2.75) )
		stuff.append( Tex(r"V(\gamma) = e^{i\gamma x^3} \to \text{Cubic Phase Operator}").shift(DOWN*3.375) )

		for i in stuff:
			self.play(FadeIn(i))
			self.wait(7)
		self.play(FadeOut(Group(*stuff)))
	

		stuff2 = []
		stuff2.append( Tex(r"X(x) = D(x), x \in \mathbb{R} \to \text{Analogous: Pauli X}").shift(UP*2.9) )
		stuff2.append( Tex(r"Z(p) = D(ip), p \in \mathbb{R} \to \text{Analogous: Pauli Z}").shift(UP*2.25) )
		stuff2.append( Tex(r"\hat{a}\ket{0} = 0 \to \hat{a}\ket{n} = \sqrt{n}\ket{n-1}").shift(UP*1.5) )
		stuff2.append( Tex(r"\hat{a}^\dag \ket{n} = \sqrt{n+1}\ket{n+1}").shift(UP*0.75) )
		stuff2.append( Tex(r"Beamsplitter").shift(DOWN*0.75).scale(1.25) )
		stuff2.append( Tex(r"BS_{ij}(\theta, \phi) = e^{\theta(e^{i\phi}\hat{a}_i^\dag \hat{a}_j - e^{-i\phi}\hat{a}_i \hat{a}_j^\dag )}").shift(DOWN*1.75).scale(2) )
		stuff2.append( Text(r"Annihilation Operators for Specific QuModes").shift(DOWN*3).scale(0.9) )
		for i in stuff2:
			self.play(FadeIn(i))
			self.wait(7)
		self.wait(15)
		self.play(FadeOut(Group(*stuff2)))
		

		#create graph w/ qumodes
		title2 = Text("QuModes & Operators").shift(UP*3.5).scale(0.9)
		self.play(Transform(title, title2))
		axes = Axes(x_range=(0, 1), y_range=(-3, 3, 0.5), height=5, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(DOWN*1.2).scale(0.8)

		self.play(FadeIn(axes))
		func = lambda t : math.sin(t*1*np.pi)
		time = 0
		sin_graph = axes.get_graph(func, color=RED, step_size=0.01, ) 
		def update_graph(self):
			func = lambda t : math.cos(time) * math.sin(t*1*np.pi)
			self.become(  axes.get_graph(func, color=RED, step_size=0.01, )    )
		sin_graph.add_updater(update_graph)
		self.play(ShowCreation(sin_graph))

		stuff = Tex(r"\ket{1, 0, 0, 0}").shift(UP*2.5)
		self.play(FadeIn(stuff))
		time = 0
		rotates = 4
		self.wait(5)
		while(time < np.pi*rotates):
			time += 0.1
			self.wait(0.001)

		
		def update_graph2(self):
			func = lambda t : math.cos(time) * math.sin(t*2*np.pi)
			self.become(  axes.get_graph(func, color=YELLOW, step_size=0.01, )    )
		sin_graph.remove_updater(update_graph)
		sin_graph.add_updater(update_graph2)
		stuff2 = Tex(r"a_0a_1^\dag\ket{1, 0, 0, 0} = \ket{0, 1, 0, 0}").shift(UP*2.5)
		self.play(Transform(stuff, stuff2))
		time = 0
		self.wait(5)
		while(time < np.pi*rotates):
			time += 0.1
			self.wait(0.001)


		
		def update_graph3(self):
			func = lambda t : math.cos(time) * math.sin(t*3*np.pi)
			self.become(  axes.get_graph(func, color=GREEN, step_size=0.01, )    )
		sin_graph.remove_updater(update_graph2)
		sin_graph.add_updater(update_graph3)
		stuff2 = Tex(r"a_1a_2^\dag\ket{0, 1, 0, 0} = \ket{0, 0, 1, 0}").shift(UP*2.5)
		self.play(Transform(stuff, stuff2))
		time = 0
		self.wait(5)
		while(time < np.pi*rotates):
			time += 0.1
			self.wait(0.001)


		
		def update_graph4(self):
			func = lambda t : math.cos(time) * math.sin(t*4*np.pi)
			self.become(  axes.get_graph(func, color=BLUE, step_size=0.01, )    )
		sin_graph.remove_updater(update_graph3)
		sin_graph.add_updater(update_graph4)
		stuff2 = Tex(r"a_2a_3^\dag\ket{0, 0, 1, 0} = \ket{0, 0, 0, 1}").shift(UP*2.5)
		self.play(Transform(stuff, stuff2))
		time = 0
		self.wait(5)
		while(time < np.pi*rotates):
			time += 0.1
			self.wait(0.001)

		
		height = 1
		def update_graph5(self):
			func = lambda t : math.cos(time) * math.sin(t*1*np.pi) * height
			self.become(  axes.get_graph(func, color=RED, step_size=0.01, )    )
		sin_graph.remove_updater(update_graph4)
		sin_graph.add_updater(update_graph5)
		stuff2 = Tex(r"a_3a_0^\dag a_0^\dag\ket{0, 0, 0, 1} = \ket{2, 0, 0, 0}").shift(UP*2.5)
		self.play(FadeOut(stuff), FadeIn(stuff2))
		self.wait(0.5)
		height += 1
		self.wait(0.5)
		time = 0
		self.wait(5)
		while(time < np.pi*rotates):
			time += 0.1
			self.wait(0.001)

		
		height1 = 2
		height2 = 1
		height3 = 2
		height4 = 1
		def update_graph5(self):
			func = lambda t :  (math.cos(time) * math.sin(t*1*np.pi) * height1 + math.cos(time*0.1 + 1.1) * math.sin(t*2*np.pi) * height2 + math.cos(time*2 + 2.4) *math.sin(t*3*np.pi) * height3 + math.cos(time*0.5 - 1) *math.sin(t*4*np.pi) * height4)
			self.become(  axes.get_graph(func, color=PURPLE, step_size=0.01, )    )
		sin_graph.remove_updater(update_graph4)
		sin_graph.add_updater(update_graph5)
		stuff4 = Tex(r"a_1^\dag a_2^\dag a_2^\dag a_3^\dag\ket{2, 0, 0, 0} = \ket{2, 1, 2, 1}").shift(UP*2.5)
		stuff3 = Text("Different Time Evolution!").shift(UP*2).scale(0.5)
		self.play(FadeOut(stuff2), FadeIn(stuff4), FadeIn(stuff3))
		
		time = 0
		self.wait(5)
		while(time < np.pi*(rotates + 8)):
			time += 0.1
			self.wait(0.001)


		self.wait(10)




















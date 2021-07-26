from manimlib import *
import numpy as np
import random

from sklearn.decomposition import PCA

class FirstScene(Scene):
	def construct(self):
		text = Text("Principle Component Analysis (PCA))").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class pca(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Principle Component Analysis (PCA)").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))

		title = Text("Principle Component Analysis").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		axes = Axes(x_range=(-2, 2, 0.5), y_range=(-1, 1, 0.5), height=6, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } )
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(LEFT*3.5).scale(0.5)

		dots = []
		csps = []
		points = []
		points.append([1.4, 0.9])
		points.append([1.7, 0.25])
		points.append([0.8, 0.3])
		points.append([-1, -0.25])
		points.append([-1.5, -0.8])
		points.append([-1.8, -0.5])

		def centerUpdater(self):
			[cx, cy] = [sum(x)/len(x) for x in zip(*points)]
			self.become( Dot(color=ORANGE).move_to(axes.c2p(cx, cy)) )
		centerDot = Dot().add_updater(centerUpdater)
		for i in range(len(points)):
			points[i][0] += 0.4
			points[i][1] -= 0.8
			csps.append(axes.c2p(points[i][0], points[i][1]))
			def dotUpdater(self, i=i):
				[cx, cy] = points[i]
				self.become( Dot(color=GREEN_SCREEN).move_to(axes.c2p(cx, cy)) )
			dots.append( Dot(color=GREEN_SCREEN).move_to(csps[i]).add_updater(dotUpdater) )
			
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( axes )
		stuff.append( Tex(r"\text{1. Data Set: } X").shift(RIGHT*3.5 + UP*2.5) )
		stuff.append( Group(*dots) )
		stuff.append( Tex(r"\text{2. Subtract Mean: } B = X - \bar{X} = U\Sigma V^T").shift(RIGHT*3.25 + UP*2).scale(0.9) )
		stuff.append(centerDot)
		for i in stuff:
			self.play(FadeIn(i))
		waiter(2)
		[cx, cy] = [sum(x)/len(x) for x in zip(*points)]
		for j in range(10):
			for i in range(len(points)):
				points[i][0] -= cx/10
				points[i][1] -= cy/10
				self.wait(0.01)
				
		#self.play(FadeOut(Group(*stuff)))
		stuff2 = []
		stuff2.append( Tex(r"\text{3. Covar. Matrix: } C = B^T B").shift(RIGHT*3.5 + UP*1.5) )
		stuff2.append( Tex(r"\text{4. Diagonalize C: } C = VDV^{-1}").shift(RIGHT*3.5 + UP*0.8) )
		stuff2.append( Tex(r"\text{5. Get PC's: } T = BV = U\Sigma").shift(RIGHT*3.5 + UP*0.2) )
		stuff2.append( Tex(r"\text{Sum of Squres SS: PCA 1} ").shift(RIGHT*3.5 + DOWN*1) )
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(5)
		pca=PCA(2)
		pca.fit(points)

		thelines = []
		thelines.append(Line([3*pca.components_[0][0], 3*pca.components_[0][1]], [-3*pca.components_[0][0], -3*pca.components_[0][1]]).set_color(RED))
		thelines.append(Line([pca.components_[1][0], pca.components_[1][1]], [-pca.components_[1][0], -pca.components_[1][1]]).set_color(RED))

		stuff3 = []
		stuff3.append( thelines[0].shift(LEFT*3.57) )
		stuff3.append( Tex(r"\text{Perp. (Sum of Squres SS): PCA 2} ").shift(RIGHT*3 + DOWN*1.6) )
		stuff3.append( thelines[1].shift(LEFT*3.57) )
		stuff3.append( Tex(r"\text{Variance Explained by PCA 1: } \sigma^2_1 = " + "{:.3f}".format(pca.explained_variance_ratio_[0])).shift(DOWN*2.5) )
		stuff3.append( Tex(r"\text{Variance Explained by PCA 2: } \sigma^2_2 = " + "{:.3f}".format(pca.explained_variance_ratio_[1])).shift(DOWN*3.3) )
		
		#pca.explained_variance_
		for i in stuff3:
			self.play(FadeIn(i))
			waiter(3)
		waiter(3)
		self.play(FadeOut(stuff[0]))
		def rotateAroundOrigin(point, angle):
			pointX = point[0]*np.cos(angle) - point[1]*np.sin(angle)
			pointY = point[0]*np.sin(angle) + point[1]*np.cos(angle)
			return [pointX, pointY]
		for i in range(45):
			for j in range(len(points)):
				points[j] = rotateAroundOrigin(points[j], -np.pi/400)
			for k in range(2):
				thelines[k].rotate(-np.pi/400)
			self.wait(0.01)
		self.play(FadeIn(stuff[0]))
		waiter(10)
		self.play(FadeOut(Group(*stuff, *stuff2, *stuff3)))
		





















		axes = Axes(x_range=(0, 4, 1), y_range=(0, 1, 0.1), height=6, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } )
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.scale(0.8).shift(UP*0.5)
		stuff = []
		#1.825
		boxes = []
		boxes.append(Rectangle(width=1, height=4.5, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + UP*1.25 + LEFT*2.4))
		boxes.append(Rectangle(width=1, height=0.5, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + DOWN*0.75))

		#stuff.append( Tex(r"") )
		stuff.append( axes )
		stuff.append( Group(Tex(r"PC_i").shift(LEFT*4 + DOWN*2.4), Tex(r"\sigma^2_i").shift(LEFT*6 + UP*0.5)) )
		stuff.append( Group(*boxes) )
		stuff.append( Tex(r"\text{Scree Plot}").shift(DOWN*3.3).scale(1.2) )
		for i in stuff:
			self.play(FadeIn(i))
		waiter(5)
		self.play(FadeOut(stuff[2]))


		#1.825
		boxes = []
		boxes.append(Rectangle(width=1, height=4, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + UP*1 + LEFT*2.4))
		boxes.append(Rectangle(width=1, height=1, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + DOWN*0.5))
		boxes.append(Rectangle(width=1, height=0.25, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + DOWN*0.875 + RIGHT*2.4))
		stuff[2] = Group(*boxes)
		self.play(FadeIn(stuff[2]))
		waiter(10)
		self.play(FadeOut(stuff[2]))
		#1.825
		boxes = []
		boxes.append(Rectangle(width=1, height=2, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + LEFT*2.4))
		boxes.append(Rectangle(width=1, height=2, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825))
		boxes.append(Rectangle(width=1, height=2, fill_opacity=1, color=BLUE, fill_color=BLUE).shift(DOWN*0.825 + RIGHT*2.4))
		stuff[2] = Group(*boxes)
		self.play(FadeIn(stuff[2]))
		waiter(10)
		self.play(FadeOut(Group(*stuff)))






		

		title2 = Text("Quantum Principle Component Analysis").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{1. Calculate Covariant Matrix: } \Sigma").shift(UP*2.5) )
		stuff.append( Tex(r"\text{2. Encode Cov. Matrix into Density Matrix: } \Sigma \to \rho").shift(UP*1.8) )
		stuff.append( Tex(r"\text{3. Make Multiple Copies of } \rho \to (\rho)*10").shift(UP*1.1) )
		stuff.append( Tex(r"\text{4. Quantum Walk w/ Hadamard Coin \& SWAP Shift Operator}").shift(UP*0.4) )
		stuff.append( Tex(r"\text{5. Perform Phase Estimation to get Eigenvalues}").shift(DOWN*0.3) )

		for i in stuff:
			self.play(FadeIn(i.shift(DOWN*1)))
			waiter(7)
		vvv = ImageMobject("./qpca.png").scale(1.5)
		self.play(FadeIn(vvv))
		waiter(15)




















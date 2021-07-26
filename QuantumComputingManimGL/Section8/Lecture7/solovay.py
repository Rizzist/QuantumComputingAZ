from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Solovay–Kitaev Theorem").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
eps = 0
class solovay(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Solovay–Kitaev Theorem").scale(1)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Solovay–Kitaev Theorem").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		result0 = Tex(r"\text{Approximate any Quantum Gate with Universal Set of Quantum Gates}").shift(DOWN*3.3).scale(0.9)
		stuff.append( Tex(r"\text{Unitary Groups, Special Unitary Groups}").shift(UP*2.6) )
		stuff.append( Tex(r"\text{SU(1): } U = [x] \to U^\dag = U^{-1} \quad \quad det(U) = 1 \to U = [1] ").shift(UP*1.6) )
		stuff.append( Tex(r"\text{SU(2): } U = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \quad \quad det(U) = 1 \to ad-bc = 1").shift(UP*0.3) )
		stuff.append( Tex(r"U^\dag = U^{-1} \to a^* = d \quad \quad c = -b^*").shift(DOWN*0.5 + RIGHT*3.5) )
		result1 = Tex(r"\text{SU(2): } U = \begin{bmatrix} a_0 + ia_1 & b_0 + ib_1 \\ -b_0 + ib_1 & a_0 - ia_1 \end{bmatrix}").shift(DOWN*2.3)
		self.play(FadeIn(result0))
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)
		self.play(FadeIn(result1))
		self.play(FadeOut(Group(*stuff)))









		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"U = \begin{bmatrix} a & b \\ c & d \end{bmatrix} = a_0 \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + ia_1 \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} + ib_0 \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix} +  ib_1 \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}").shift(UP*2) )
		stuff.append( Tex(r"U = \begin{bmatrix} a & b \\ c & d \end{bmatrix} = a_0 \mathbb{I} + ia_1 \mathbb{Z} + ib_0 \mathbb{Y} +  ib_1\mathbb{X}").shift(UP*0.3) )
		stuff.append( Tex(r"U \in SU(2)").shift(DOWN*1) )
		
		for i in stuff:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff, result0, result1)))



		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Generate SU(2) from few gates = Approximate Any SU(2) Matrix?}").shift(UP*2.5) )
		stuff.append( Tex(r"\Gamma = \{ X(\theta), Y(\theta), Z(\theta), P(\theta), CNOT \} \to \text{Universal Set}").shift(UP*1.25) )
		stuff.append( Tex(r"\Gamma = \{ H, S=P(\pi/2), T=P(\pi/4), CNOT \} \to \text{Universal Set}").shift(UP*0) )
		stuff.append( Tex(r"\text{Dense Subset of SU(2)} \to U \approx HSTSHTHSHSTSH").shift(DOWN*1.25) )
		stuff.append( Tex(r"\text{Requires Infinite Gates to be Exact, Approx is Good Enough}").shift(DOWN*2.3) )
		stuff.append( Tex(r"\text{Epsilon-Nets (Read Full Proof)}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(7)

		self.play(FadeOut(Group(*stuff)))











		

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Theorem: Let } \epsilon > 0 \text{ All Unitary U Gates can be approximated by a}").shift(DOWN*1.4).scale(0.9) )
		stuff.append( Tex(r"\text{product of length l of matrices } \{ H, S, T \} \text{ where } l \in O(\log^4 (\frac{1}{\epsilon})) \text{ and}").shift(DOWN*2).scale(0.9) )
		stuff.append( Tex(r"\mid \mid \prod_i U_i - U \mid \mid \leq \epsilon \to U_n = \prod_i^n U_i \to \lim_{n \to \infty} U_n = U").shift(DOWN*3).scale(0.9) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)

		#self.play(FadeOut(Group(*stuff)))










		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"D(U_n, U) = 2*T(U_n, U) = Tr(\mid U_n-U \mid ) < \epsilon(n)").shift(UP*2.5) )
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(5)

		self.play(FadeOut(Group(*stuff, *stuff2)))
		
		
		def generateEpsilon(x, y, r, col):
			global eps
			circs = []
			for i in range(1,30):
				circs.append( DashedVMobject(Circle(radius=r, color=col), num_dashes=30, fill_opacity=0.5, opacity=0.5).rotate(np.pi/20 * i) )
			circs.append( Tex(r"\epsilon_" + str(eps)).shift(UP*r + RIGHT*0.75*r) )
			eps += 1
			return Group(*circs).shift(RIGHT*x + UP*y)

		ls = 0.3
		us = 0.1
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Group(Circle(color=YELLOW).scale(3), Tex(r"SU(2)").shift(UP*2.5 + LEFT*3) ) )
		stuff.append( Group(Dot(color=WHITE), Tex(r"U_0").shift(LEFT*ls + UP*us).scale(0.5)) )
		stuff.append( Group(Tex(r"\times").shift(RIGHT*2.5).set_color(RED), Tex(r"U").shift(LEFT*ls + UP*us + RIGHT*2.5).scale(0.5)) )
		stuff.append( Group(Dot(color=BLUE).shift(UP*0.5 + RIGHT*0.5), Tex(r"X(\theta)").shift(LEFT*ls + UP*us + UP*0.5 + RIGHT*0.5).scale(0.5)) )
		stuff.append( Group(Dot(color=BLUE).shift(DOWN*0.5 + RIGHT*0.5), Tex(r"Y(\theta)").shift(LEFT*ls + UP*us + DOWN*0.5 + RIGHT*0.5).scale(0.5)) )
		stuff.append( Group(Dot(color=BLUE).shift(DOWN*0.5 + LEFT*0.5), Tex(r"Z(\theta)").shift(LEFT*ls + UP*us + DOWN*0.5 + LEFT*0.5).scale(0.5)) )
		stuff.append( Group(Dot(color=BLUE).shift(UP*0.5 + LEFT*0.5), Tex(r"P(\theta)").shift(LEFT*ls + UP*us + UP*0.5 + LEFT*0.5).scale(0.5)) )

		for i in stuff:
			self.play(FadeIn(i))
		eppers = generateEpsilon(2.5, 0, 2.3, ORANGE) 
		self.play(FadeIn(eppers))

		def coorder(x, y, z):
			return np.array([x, y, z])

		def linetexdotter(x1, y1, x2, y2, n):
			liner = Line(coorder(x1, y1, 0), coorder(x2, y2, 0), fill_opacity=0.5, opacity=0.5) 
			texer = Tex(r"U_" + str(n)).shift(RIGHT*ls + DOWN*us + RIGHT*x2 + UP*y2).scale(0.5)
			dotter = Dot(color=GREEN).shift(RIGHT*x2 + UP*y2)
			return Group(liner, texer, dotter)

		currentVal = Tex(r"U_0 = \mathbb{I}").shift(DOWN*3.5)
		self.play(FadeIn(currentVal))
		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )

		stuff2.append( linetexdotter(0, 0, 0.5, -0.5, 1) )
		stuff2.append( linetexdotter(0.5, -0.5, 1, 0.5, 2) )
		stuff2.append( linetexdotter(1, 0.5, 1.5, -0.5, 2) )
		stuff2.append( linetexdotter(1.5, -0.5, 2, 0.5, 2) )
		stuff2.append( linetexdotter(2, 0.5, 2.5, -0.2, 2) )
		kita = 2.3
		for i in stuff2:
			eppers2 = generateEpsilon(2.5, 0, kita, ORANGE) 
			self.play(Transform(eppers, eppers2))
			if (eps==2):
				currentVal2 = Tex(r"U_1 = Y(\theta_0)").shift(DOWN*3.5)
			elif (eps==3):
				currentVal2 = Tex(r"U_2 = Y(\theta_0)X(\theta_1)").shift(DOWN*3.5)
			elif (eps==4):
				currentVal2 = Tex(r"U_3 = Y(\theta_0)X(\theta_1)Y(\theta_2)").shift(DOWN*3.5)
			elif (eps==5):
				currentVal2 = Tex(r"U_4 =Y(\theta_0)X(\theta_1)Y(\theta_2)X(\theta_3)").shift(DOWN*3.5)
			elif (eps==6):
				currentVal2 = Tex(r"U_5 =Y(\theta_0)X(\theta_1)Y(\theta_2)X(\theta_3)Y(\theta_4)P(\theta_5)").shift(DOWN*3.5)
			self.play(FadeIn(i), Transform(currentVal, currentVal2))
			kita -= 0.5
			
	

		#self.play(FadeOut(Group(*stuff, *stuff2)))
		waiter(20)











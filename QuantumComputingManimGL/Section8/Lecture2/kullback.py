from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Kullback Leibler Divergence, Quantum Relative Entropy").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class kullback(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Kullback Leibler Divergence, Quantum Relative Entropy").scale(0.8)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		#print(YELLOW)
		title = Text("Kullback Leibler Divergence (Relative Entropy)").shift(UP*3.5)
		self.play(FadeIn(title))

		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Measure how different two probability distributions are}").shift(UP*2.7) )
		stuff.append( Tex(r"D_{KL}(P \mid \mid Q) = \sum_{x \in X} P(x) \log \frac{P(x)}{Q(x)}").shift(UP*1.7) )
		stuff.append( Tex(r"D_{KL}(P \mid \mid Q) =  \sum_{x \in X} P(x) (\log P(x) - \log Q(x))").shift(UP*0.3) )
		stuff.append( Tex(r"D_{KL}(P \mid \mid Q) = H(P, Q) - H(P)").shift(DOWN*0.8) )
		stuff.append( Tex(r"D_{KL} \geq 0").shift(DOWN*1.7) )
		stuff.append( Tex(r"\lim_{x \to -\infty} D_{KL}(P_n \mid \mid Q) = 0").shift(DOWN*2.6) )
		stuff.append( Tex(r"\lim_{x \to -\infty} P_n \to Q").shift(DOWN*3.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))



		#GRAPH OF x * ln(x)
		axes = Axes(x_range=(-3, 3, 0.5), y_range=(-0.1, 1, 0.2), height=2, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(UP*2).scale(0.7)

		self.play(FadeIn(axes))
		func = lambda t : np.exp(-t*t)
		sin_graph = axes.get_graph(func, color='#FFFF00', step_size=0.01, ) 
		self.play(ShowCreation(sin_graph))
		obj = Tex(r"y = e^{-x^2}").shift(UP*0.5)
		self.play(FadeIn(obj))
		#self.play(FadeOut(Group(obj, axes, sin_graph)))


		#GRAPH OF x * ln(x)
		axes2 = Axes(x_range=(-3, 3, 0.5), y_range=(-0.1, 1, 0.2), height=2, width=12, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes2.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes2.shift(DOWN*0.9).scale(0.7)

		self.play(FadeIn(axes2))
		k = 10
		func2 = lambda t : np.exp(-t*t*k)
		sin_graph2 = axes2.get_graph(func2, color='#FFFF00', step_size=0.01, ) 
		self.play(ShowCreation(sin_graph2))
		obj2 = Tex(r"y = e^{-k*x^2}").shift(DOWN*2.3)
		self.play(FadeIn(obj2))
		#self.play(FadeOut(Group(obj2, axes2, sin_graph2)))

		def KL(a, b):
			a = np.asarray(a, dtype=np.float)
			b = np.asarray(b, dtype=np.float)
			return np.sum(np.where(a != 0, a * np.log(a / b), 0))


		values1 = np.arange(-3, 3, 0.01)#[1.346112,1.337432,1.246655]
		values2 = np.arange(-3, 3, 0.01)#[1.033836,1.082015,1.117323]
		for i in range(0, len(values1)):
			values1[i] = np.exp(-values1[i]*values1[i])
		for i in range(0, len(values2)):
			values2[i] = np.exp(-k*values2[i]*values2[i])
		objKL = Tex(r"D_{KL} = \ " + str(KL(values1, values2))).shift(DOWN*3.25)
		self.play(FadeIn(objKL))

		
		k = 10
		mlp = 0
		for i in range(0, 100):
			mlp += 1
			k -= 0.097
			func3 = lambda t : np.exp(-t*t*k)
			self.remove(sin_graph2)
			sin_graph2 = axes2.get_graph(func3, color='#FF' + hex(int(k * 17))[2:] + 'AA', step_size=0.01, ) 
			self.add(sin_graph2)
			values1 = np.arange(-3, 3, 0.01)#[1.346112,1.337432,1.246655]
			values2 = np.arange(-3, 3, 0.01)#[1.033836,1.082015,1.117323]
			for i in range(0, len(values1)):
				values1[i] = np.exp(-values1[i]*values1[i])
			for i in range(0, len(values2)):
				values2[i] = np.exp(-k*values2[i]*values2[i])
			self.remove(objKL)
			objKL = Tex(r"D_{KL} = \ " + str(np.abs(KL(values1, values2)))).shift(DOWN*3.25)
			self.add(objKL)
			self.wait(0.01)
			if (mlp > 92):
				self.wait(0.5)
				
		waiter(10)
		self.play(FadeOut(Group(axes, axes2, obj, obj2, sin_graph, sin_graph2, objKL)))

		

		title2 = Text("Quantum Relative Entropy").shift(UP*3.5)
		self.play(Transform(title, title2))


		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Measure distinguishability of two diff. quantum states}").shift(UP*2.7) )
		stuff.append( Tex(r"S(\rho) = -Tr(\rho \log (\rho))").shift(UP*1.7) )
		stuff.append( Tex(r"S(\rho \mid \mid \sigma) = -Tr(\rho \log (\sigma)) - S(\rho)").shift(UP*0.7) )
		stuff.append( Tex(r"S(\rho \mid \mid \sigma) = -Tr(\rho \log (\sigma)) + Tr(\rho \log (\rho))").shift(DOWN*0.3) )
		stuff.append( Tex(r"S(\rho \mid \mid \sigma) = Tr(\rho \log (\rho)) - Tr(\rho \log (\sigma))").shift(DOWN*1.3) )
		stuff.append( Tex(r"S(\rho \mid \mid \sigma) = Tr(\rho (\log (\rho) - \log (\sigma)))").shift(DOWN*2.3) )
		stuff.append( Tex(r"\rho = \sum_j p_j \ket{\psi_j} \bra{\psi_j}").shift(DOWN*3.3) )



		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))


		
		title2 = Text("Relative Entropy of Entanglement (REE)").shift(UP*3.5)
		self.play(Transform(title, title2))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{Measure how entangled a system is}").shift(UP*2.7) )
		stuff.append( Tex(r"\text{State Space (Hilbert): } H = \bigotimes_k H_k").shift(UP*1.7) )
		stuff.append( Tex(r"D_{REE}(\rho) = \min_\sigma S(\rho \mid \mid \sigma)").shift(UP*0.7) )
		#entagability
		stuff.append( ImageMobject("./entangability.png").shift(DOWN*1.4).scale(0.7) )
		stuff.append( Tex(r"D_{REE}(\rho) = 0 \to \text{Not Entangled}").shift(DOWN*3.3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))











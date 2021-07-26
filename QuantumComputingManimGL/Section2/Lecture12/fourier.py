from manimlib import *
import scipy.integrate
import numpy as np
import random
import copy

USE_ALMOST_FOURIER_BY_DEFAULT = True
NUM_SAMPLES_FOR_FFT = 1000
DEFAULT_COMPLEX_TO_REAL_FUNC = lambda z : z.real

def get_fourier_transform(
	func, t_min, t_max, 
	complex_to_real_func = DEFAULT_COMPLEX_TO_REAL_FUNC,
	use_almost_fourier = USE_ALMOST_FOURIER_BY_DEFAULT,
	**kwargs ##Just eats these
	):
	scalar = 1.0#1./(t_max - t_min) if use_almost_fourier else 1.0
	def fourier_transform(f):
		z = scalar*scipy.integrate.quad(
			lambda t : func(t)*np.exp(complex(0, -TAU*f*t)),
			t_min, t_max
		)[0]
		return complex_to_real_func(z)
	return fourier_transform

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Fourier Transform").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class fourier1(Scene):
	def construct(self):
		text = Text("Quantum Fourier Transform").scale(1.3)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))	

		title = Text("Fourier Transform").shift(UP*3.5)
		self.play(FadeIn(title))


		axes = Axes(x_range=(-1, 3), y_range=(-2.5, 1.5, 0.5), height=6, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.scale(0.8)

		self.play(FadeIn(axes))
		func = lambda t : 0.6 * (math.cos(1*t*2*scipy.pi) + math.sin(2*t*2*scipy.pi) + math.sin(4*t*2*scipy.pi) + math.cos(6*t*2*scipy.pi))
		
		sin_graph = axes.get_graph(func, color=BLUE, step_size=0.001, ) 
		sin_label = axes.get_graph_label(sin_graph, r"{cos(2\pi*1) + sin(2\pi*2) + sin(2\pi*4) + cos(2\pi*6)}")
		sin_label.set_color(RED).shift(DOWN*5.3+ RIGHT*1.5)

		self.play(
			ShowCreation(sin_graph),
			
		)
		self.wait(3)

		fouriertheorem = Text("A reasonably continuous periodic function can be")
		fouriertheorem2 = Text("expressed as a sum of sin and cos terms").shift(DOWN*1)

		ft = Group(fouriertheorem, fouriertheorem2).scale(0.6)
		ft.shift(DOWN*2.7)
		self.play(FadeIn(ft))
		self.wait(6)
		self.play(FadeOut(ft), FadeIn(sin_label),)

		together = Group(axes, sin_graph, sin_label)
		together.generate_target()
		together.target.scale(0.5).shift(UP*2 + RIGHT*3)
		self.play(MoveToTarget(together))

		self.wait(8)
		


		axes2 = Axes(x_range=(0, 8), y_range=(-2, 2, 0.5), height=6, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes2.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes2.scale(0.8).shift(DOWN*1.2 + LEFT*2)
		self.play(FadeIn(axes2))

		#fourier_graph = axes.get_graph(get_fourier_transform(func, -1, 5), color=YELLOW, step_size=0.01)
		fourier_graph = axes2.get_graph(get_fourier_transform(func, 0, 5), color=YELLOW, step_size=0.01 ) 
		self.play(ShowCreation(fourier_graph) )
		self.wait(3)

		cos1 = Tex(r"cos, f=1").scale(0.5).shift(LEFT*5 + UP*1)
		sin1 = Tex(r"sin, f=2").scale(0.5).shift(LEFT*4 + DOWN*3)

		sin2 = Tex(r"sin, f=4").scale(0.5).shift(LEFT*2 + UP*1)
		cos2 = Tex(r"cos, f=6").scale(0.5).shift(LEFT*0 + DOWN*3)

		terms = Group(cos1, sin1, cos2, sin2)
		self.play(FadeIn(terms))
		self.wait(10)

		anotherg = Group(terms, fourier_graph, axes2, together)
		self.play(FadeOut(anotherg))


		#formula
		formula = Tex(r"\hat{f}(w) = \int_{a}^{b} f(x)*e^{iwx}dx ")
		self.play(FadeIn(formula))
		self.wait(8)
		self.play(FadeOut(formula))















		#DISCRETE FOURIER TRANSFORM
		title2 = Text("Discrete Fourier Transform").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title2))

		#formula
		formula2 = Tex(r"\hat{f}(k) = \sum_{i=0}^{N-1} f(x)*e^{\frac{i2\pi kx}{N}} ").scale(2)
		self.play(FadeIn(formula2))
		self.wait(8)
		self.play(FadeOut(formula2))


		axes = Axes(x_range=(0, 1), y_range=(-0.5, 0.5, 0.25), height=6, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.scale(0.8)

		self.play(FadeIn(axes))
		func = lambda t : 0.5 * (math.cos(2*t*2*scipy.pi))
		
		sin_graph = axes.get_graph(func, color=BLUE, step_size=0.0005, ) 
		sin_label = axes.get_graph_label(sin_graph, r"{0.5*cos(2\pi*2),\ \ 2Hz}")
		sin_label.set_color(RED).shift(DOWN*2 + LEFT*5)

		self.play(ShowCreation(sin_graph), FadeIn(sin_label),)
		self.wait(3)
#range
		dots = []
		for i in range(0, 10):
			dot = Dot(color=RED)
			dot.move_to(axes.i2gp(i/10, sin_graph))
			dots.append(dot)
		for i in range(0, 10):
			self.play(FadeIn(dots[i], scale=0.5, run_time=0.3))

		together = Group(axes, sin_graph, sin_label, *dots)
		together.generate_target()
		together.target.scale(0.5).shift(UP*2 + RIGHT*3)
		self.play(MoveToTarget(together))
		self.wait(3)

		t = np.linspace(0, 1, 10)
		s = 0.5*np.cos(2 * 2 * np.pi * t)
		fft = np.fft.fft(s)
		theft = []
		for i in range(0, 10):
			additional = ' < 1'
			if (i == 2 or i==8):
				additional = ' = 2.5'
			theftp = Text("f(" + str(i) + ") = " + str(format(fft[i], 'g')) + additional).scale(0.5).shift(LEFT*4 + UP*(2.4-i*(3/5)))
			theft.append(theftp)
		


		axes2 = Axes(x_range=(0, 10), y_range=(-5, 5, 2), height=6, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes2.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes2.scale(0.8)

		axes3 = Axes(x_range=(0, 10), y_range=(-3, 2.5, 2), height=6, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes3.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes3.scale(0.8)
		fftdots = []
		for i in range(0, 10):
			dot = Dot(color=RED)
			dot.move_to(axes2.c2p(i, np.absolute(fft[i])))
			fftdots.append(dot)
		thestuff = Group(axes2, *fftdots)
		thestuff.scale(0.8).shift(DOWN*1.5 + RIGHT*3)
		axes3.scale(0.8).shift(DOWN*1.5 + RIGHT*3)
		self.play(FadeIn(axes2))
		self.wait(3)
		#for i in range(0, 10):
		#		self.play(FadeIn(fftdots[i], scale=0.5, run_time=0.3))
		for i in range(0, 10):
			self.play(FadeIn(theft[i], run_time=0.3))
		dots2 = copy.deepcopy(dots)
		self.add(*dots2)
		for i in range(0, 10):
			self.play(Transform(dots2[i], fftdots[i], run_time=0.3))

		fourier_graph = axes3.get_graph(get_fourier_transform(func, 0, 5), color=YELLOW, step_size=0.01 ) 
		self.play(ShowCreation(fourier_graph))
		self.wait(3)

		sampRate = Text("Sampling Rate = 10 Hz").scale(0.5).shift(DOWN*2.5 + RIGHT*2.5)
		self.play(Write(sampRate))
		samp = Text("Nyquist Ferq = 10 Hz / 2 = 5 Hz").scale(0.5).shift(DOWN*3 + RIGHT*3)
		self.play(Write(samp))
		self.wait(15)

		

		theft2 = []
		for i in range(0, 5):
			additional = ' < 2'
			if (i == 2 or i==8):
				additional = ' = 5'
			theftp = Text("f(" + str(i) + ") = " + str(format(1.7 * fft[i], 'g')) + additional).scale(0.5).shift(LEFT*4 + UP*(2.4-i*(3/3)))
			theft2.append(theftp)
		fftdots2 = []
		for i in range(0, 5):
			dot = Dot(color=RED)
			dot.move_to(axes2.c2p(i, 2 * np.absolute(fft[i])))
			fftdots2.append(dot)
		g1 = Group(*theft)
		g2 = Group(*theft2)
		g3 = Group(*fftdots2)
		orig = Group(*fftdots)
		qq = Group(*dots2)
		self.play(FadeOut(g1), FadeIn(g2))
		self.play(Transform(orig, g3), FadeOut(qq))
		self.wait(6)


		sampRate2 = Text("Sampling Number = 10").scale(0.5).shift(DOWN*2.5 + LEFT*4)
		self.play(Write(sampRate2))
		samp2 = Text("Amplitude = f(2) / 10 = 0.5").scale(0.5).shift(DOWN*3 + LEFT*4)
		self.play(Write(samp2))
		self.wait(12)

		for i in range(0, 5):
			if (i != 2):
				self.play(FadeOut(theft2[i], run_time=0.5))
		#theft[1]
		surroundit = SurroundingRectangle(theft2[2])
		self.play(ShowCreation(surroundit))

		theta = Text("Angle approx. 45deg").scale(0.5).shift(LEFT*4 + DOWN*0.5)
		self.play(FadeIn(theta))
		result = Tex(r"f(x) = A*sin(b(x-\theta))").shift(LEFT*4 + DOWN*1.5)
		self.play(FadeIn(result))
		self.wait(7)

		allthestuff = Group(theta, result, surroundit, theft2[2], orig, samp, sampRate, samp2, sampRate2, together, axes2, fourier_graph)
		self.play(FadeOut(allthestuff))

		





















		#apps fo ft
		title3 = Text("Applications of Fourier Transform").shift(UP*3.5)
		self.play(Transform(title2, title3))
		corona = ImageMobject("./heat.jpeg").scale(0.6).shift(UP*1.8 + LEFT*5)
		self.play(FadeIn(corona))
		self.wait(4)

		corona2 = ImageMobject("./compress.jpeg").scale(0.6).shift(DOWN*1.5 + LEFT*4.5)
		self.play(FadeIn(corona2))
		self.wait(4)

		corona3 = ImageMobject("./pcb.jpeg").scale(0.6).shift(UP*2)
		self.play(FadeIn(corona3))
		self.wait(4)

		corona4 = ImageMobject("./quantum.jpeg").scale(0.6).shift(DOWN*2.5 + RIGHT*1)
		self.play(FadeIn(corona4))
		self.wait(4)

		corona5 = ImageMobject("./dsp.jpeg").scale(0.6).shift(RIGHT*5 + UP*0.5)
		self.play(FadeIn(corona5))
		self.wait(6)

		coronas = Group(corona, corona2, corona3, corona4, corona5)
		self.play(FadeOut(coronas))
		self.wait(2)



		#Quantum Computing Fourier Transform
		title4 = Text("Quantum Computing QFT").shift(UP*3.5)
		self.play(Transform(title2, title4))

		self.wait(5)













class fourier2(Scene):
	def construct(self):
		title = Text("Quantum Computing QFT").shift(UP*3.5)
		self.add(title)
		
		self.wait(6)
		stuffers = []
		for i in range(0, 8):
			temp = Tex(r"\ket{" + bin(i)[2:] + r"} = \ket{"+str(i)+"}_3").shift(UP*2.3 + DOWN*(i/1.3))
			stuffers.append(temp)
		toadd = Group(*stuffers)
		self.play(FadeIn(toadd))
		self.wait(15)
		youKNowwhat = Group(*stuffers)
		self.play(FadeOut(youKNowwhat))

		#formula
		formula = Tex(r"\hat{f}(y) = \sum_{k=0}^{N-1} f(x)*e^{\frac{i2\pi kx}{N}} ").scale(2)
		self.play(FadeIn(formula))
		self.wait(8)

		#formula
		formula2 = Tex(r"QFT(\ket{x}) =\frac{1}{\sqrt{(2^N})} \sum_{k=0}^{2^N-1} e^{{\frac{i2\pi kx}{2^N}}} \ket{k} ").shift(UP*1.5).scale(1.5)
		self.play(Transform(formula, formula2))
		self.wait(8)

		omega = Tex(r"\omega_{2^N} = e^{{\frac{i2\pi}{2^N}}}").shift(DOWN*1.5).scale(2)
		self.play(FadeIn(omega))
		self.wait(8)

		rootofu = Text("2^N'th Root of Unity").shift(DOWN*3)
		self.play(FadeIn(rootofu))
		self.wait(4)

		formula3 = Tex(r"QFT(\ket{x}) =\frac{1}{\sqrt{(2^N})} \sum_{k=0}^{2^N-1} \omega_{2^N}^{kx} \ket{k} ").shift(UP*1.5).scale(1.5)
		self.play(Transform(formula, formula3))
		self.wait(8)

		nowremove = Group(formula, rootofu, omega)
		self.play(FadeOut(nowremove))


		#explain roots of unity
		axes = ThreeDAxes(axis_config={"include_tip": False,"include_ticks":False,"stroke_width":1})
		grid = NumberPlane(axis_config={"stroke_opacity":0},background_line_style={"stroke_opacity":0.2},x_min=-5,x_max=5,y_min=-5,y_max=5)
		self.play(ShowCreation(axes))  
		self.play(ShowCreation(grid))   
		self.wait(1)
		circle = Circle(radius=2).set_color(GREY)
		self.play(ShowCreation(circle))

		def complexLine(t, p=0.6, show=True):
			rad = t * np.pi/180
			x = np.cos(rad)*2
			y = np.sin(rad)*2
			line = Line(np.array([0, 0, 0]), np.array([x, y, 0])).set_color(BLUE)
			point = Dot(np.array([x, y, 0])).set_color(RED)
			arcer = Arc(0, rad, radius=p)
			return Group(line, point, arcer)
		c1 = complexLine(50, 0.4)
		c2 = complexLine(70, 0.8)
		self.play(ShowCreation(c1), ShowCreation(c2))
		self.add(c1, c2)
		x = 70
		c = complexLine(x)
		self.add(c)
		while(x < 120):
			x += 0.3
			self.remove(c)
			c = complexLine(x)
			self.add(c)
			self.wait(0.04)
		thecs = Group(c1, c2, c)
		self.play(FadeOut(thecs))

		c = complexLine(0)
		self.play(FadeIn(c))
		cs = []
		for i in range(0, 4):
			y = 90*i
			while(y < 90*(i+1)):
				y += 0.6
				self.remove(c)
				c = complexLine(y)
				self.add(c)
				self.wait(0.04)
			cs.append(complexLine(y))
			self.add(cs[i])
			self.wait(1)

		whatitis = Text("Complex Vector raised to the N'th power is equal to 1").shift(DOWN*3).scale(0.7)
		self.play(Write(whatitis))
		self.wait(5)


		thets = []
		for i in range(0, 4):
			val = ''
			if (i == 0):
				val = '1'
			if (i == 1):
				val = 'i'
			if (i == 2):
				val = '-1'
			if (i == 3):
				val = '-i'
			theo = Tex(r"\omega_4^"+ str(i) + r" = e^{i\pi/2*"+str(i)+r"} = " + val).shift(LEFT*4.5 + UP*2.5 + DOWN*(i*1.2)).scale(1.1)
			thets.append(theo)
		g = Group(*thets)
		self.play(FadeIn(g))
		self.wait(7)
		unitynowgo = Group(g, whatitis, circle, axes, grid, *cs, c)
		self.play(FadeOut(unitynowgo))


		#USE FORMULA FOR QFT1, QFT2, QFT3

		title2 = Text("QFT - N = 2 qubits {0-3}").shift(UP*3.5)
		self.play(Transform(title, title2))
		formulas1 = Tex(r"QFT(\ket{0}_2 or \ket{00}) =\frac{1}{\sqrt{(2^N})} \sum_{k=0}^{2^N-1} \omega_{2^N}^{kx} \ket{k} ").shift(UP*2)
		self.play(FadeIn(formulas1))
		self.wait(3)

		formulas11 = Tex(r"QFT(\ket{0}_2 or \ket{00}) =\frac{1}{2} \sum_{k=0}^{2^2-1} \omega_{2^2}^{kx} \ket{k} ").shift(UP*2)
		formulas2 = Tex(r"QFT(\ket{1}_2 or \ket{01}) =\frac{1}{2} \sum_{k=0}^{2^2-1} \omega_4^{kx} \ket{k} ").shift(UP*0.5)
		self.play(Transform(formulas1, formulas11), FadeIn(formulas2))
		self.wait(3)

		formulas111 = Tex(r"QFT(\ket{0}_2 or \ket{00}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{0k} \ket{k} ").shift(UP*2)
		formulas22 = Tex(r"QFT(\ket{1}_2 or \ket{01}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{1k} \ket{k} ").shift(UP*0.5)
		formulas3 = Tex(r"QFT(\ket{2}_2 or \ket{10}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{2k} \ket{k} ").shift(DOWN*1)
		self.play(Transform(formulas1, formulas111), Transform(formulas2, formulas22), FadeIn(formulas3))

		formulas4 = Tex(r"QFT(\ket{3}_2 or \ket{11}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{3k} \ket{k} ").shift(DOWN*2.5)
		self.play(FadeIn(formulas4))
		self.wait(3)

		formulas1111 = Tex(r"QFT(\ket{0}_2 or \ket{00}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{0k} \ket{k} = 0.5\ket{0} + 0.5\ket{1} + 0.5\ket{2} + 0.5\ket{3}").shift(UP*2).scale(0.7)
		formulas222 = Tex(r"QFT(\ket{1}_2 or \ket{01}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{1k} \ket{k} = 0.5\ket{0} + 0.5i\ket{1} - 0.5\ket{2} - 0.5i\ket{3}").shift(UP*0.5).scale(0.7)
		formulas33 = Tex(r"QFT(\ket{2}_2 or \ket{10}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{2k} \ket{k} = 0.5\ket{0} - 0.5\ket{1} + 0.5\ket{2} - 0.5\ket{3}").shift(DOWN*1).scale(0.7)
		formulas44 = Tex(r"QFT(\ket{3}_2 or \ket{11}) =\frac{1}{2} \sum_{k=0}^{3} \omega_4^{3k} \ket{k} = 0.5\ket{0} - 0.5i\ket{1} - 0.5\ket{2} + 0.5i\ket{3}").shift(DOWN*2.5).scale(0.7)
		self.play(Transform(formulas1, formulas1111), Transform(formulas2, formulas222), Transform(formulas3, formulas33), Transform(formulas4, formulas44))
		self.wait(10)
		forms = Group(formulas1, formulas2, formulas3, formulas4)
		self.play(FadeOut(forms))

		thematrix = Tex(r"QFT_2 =  \begin{bmatrix} 1 & 1 & 1 & 1\\ 1  & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix} ").shift(RIGHT*4 + UP*1.8)
		self.play(FadeIn(thematrix))

		whichColumn = Arrow(DOWN*0.75, UP*0.75, fill_color=RED)
		whichColumn.shift(RIGHT*3.4+ UP * 0.2)
		self.play(FadeIn(whichColumn))

		#explain roots of unity
		self.play(ShowCreation(axes))  
		self.play(ShowCreation(grid))   
		self.play(ShowCreation(circle))
		def complexLinew(t, p=0.6, show=True):
			rad = t * np.pi/180
			x = np.cos(rad)*2
			y = np.sin(rad)*2
			point = Dot(np.array([x, y, 0])).set_color(RED)
			return Group(point)

		def complexLineCol(t, color):
			rad = t * np.pi/180
			x = np.cos(rad)*2
			y = np.sin(rad)*2
			line = Line(np.array([0, 0, 0]), np.array([x, y, 0])).set_color(color)
			point = Dot(np.array([x, y, 0])).set_color(GREEN).scale(0.5)
			return Group(line, point)
		c = complexLinew(0)
		self.play(FadeIn(c))
		cs = []
		for i in range(0, 4):
			y = 90*i
			while(y < 90*(i+1)):
				y += 1.2
				self.remove(c)
				c = complexLinew(y)
				self.add(c)
				self.wait(0.04)
			cs.append(complexLinew(y))
			self.add(cs[i])
			self.wait(1)

		psi = Tex(r"\ket{\psi} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}").shift(LEFT*5.5 + DOWN*2.5)
		fpsi = Tex(r"QFT(\ket{\psi}) = \begin{bmatrix} 0.5 \\ 0.5 \\ 0.5 \\ 0.5 \end{bmatrix}").shift(LEFT*4.5 + UP*2)
		self.play(FadeIn(psi), FadeIn(fpsi))

		user = complexLineCol(0, GREEN)
		self.play(FadeIn(user))
		click = Text("").shift(RIGHT*3)
		cps = []
		z = 0
		for j in range(0, 4):
			while(z > 0):
				z -= 8
				self.remove(user)
				user = complexLineCol(z, GREEN)
				self.add(user)
				self.wait(0.04)
			z = 0
			self.remove(user)
			user = complexLineCol(z, GREEN)
			self.add(user)
			self.wait(0.01)
			if (j == 1):
				psi2 = Tex(r"\ket{\psi} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}").shift(LEFT*5.5 + DOWN*2.5)
				fpsi2 = Tex(r"QFT(\ket{\psi}) = \begin{bmatrix} 0.5 \\ 0.5i \\ -0.5 \\ -0.5i \end{bmatrix}").shift(LEFT*4.5 + UP*2)
				self.play(Transform(psi, psi2), Transform(fpsi, fpsi2))
			if (j == 2):
				psi2 = Tex(r"\ket{\psi} = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}").shift(LEFT*5.5 + DOWN*2.5)
				fpsi2 = Tex(r"QFT(\ket{\psi}) = \begin{bmatrix} 0.5 \\ -0.5 \\ 0.5 \\ -0.5 \end{bmatrix}").shift(LEFT*4.5 + UP*2)
				self.play(Transform(psi, psi2), Transform(fpsi, fpsi2))
			if (j == 3):
				psi2 = Tex(r"\ket{\psi} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}").shift(LEFT*5.5 + DOWN*2.5)
				fpsi2 = Tex(r"QFT(\ket{\psi}) = \begin{bmatrix} 0.5 \\ -0.5i \\ -0.5 \\ 0.5i \end{bmatrix}").shift(LEFT*4.5 + UP*2)
				self.play(Transform(psi, psi2), Transform(fpsi, fpsi2))
			for i in range(0, 4):
				self.play(FadeOut(click))
				while(z < 90*j*i):
					z += 2.0
					self.remove(user)
					user = complexLineCol(z, GREEN)
					self.add(user)
					self.wait(0.04)
				z = 90*j*i
				self.remove(user)
				user = complexLineCol(z, GREEN)
				self.add(user)
				self.wait(0.04)
				click = Text("" + str(i+1)).shift(RIGHT*3)
				self.wait(1)
				self.add(click)
			whichColumn.generate_target()
			whichColumn.target.shift(RIGHT*1)
			self.play(MoveToTarget(whichColumn))
			self.wait(2)

		self.wait(8)
		allofIt = Group(whichColumn, click, psi, fpsi, *cs, thematrix, axes, grid, circle, c, user)
		self.play(FadeOut(allofIt))
		
		#qft omega matrices
		qftmatrix1 = Tex(r"QFT_1 =  \begin{bmatrix} 1 & 1\\ 1  & \omega_2^1 \end{bmatrix} ").shift(UP*2.5 + LEFT*4)
		self.play(FadeIn(qftmatrix1))

		qftmatrix2 = Tex(r"QFT_2 =  \begin{bmatrix} 1 & 1 & 1 & 1\\ 1  & \omega_4^1 & \omega_4^2 & \omega_4^3 \\ 1 & \omega_4^2 & \omega_4^4 & \omega_4^6 \\ 1 & \omega_4^3 & \omega_4^6 & \omega_4^8 \end{bmatrix} ").shift(RIGHT*4 + UP*2.25)
		self.play(FadeIn(qftmatrix2))

		qftmatrix3 = Tex(r"QFT_3 =  \begin{bmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\ 1  & \omega_8^1 & \omega_8^2 & \omega_8^3 & \omega_8^4  & \omega_8^5 & \omega_8^6 & \omega_8^7 \\ 1  & \omega_8^2 & \omega_8^4 & \omega_8^6 & \omega_8^8  & \omega_8^{10} & \omega_8^{12} & \omega_8^{14} \\ 1  & \omega_8^3 & \omega_8^6 & \omega_8^9 & \omega_8^{12}  & \omega_8^{14} & \omega_8^{16} & \omega_8^{18} \\ 1  & \omega_8^4 & \omega_8^8 & \omega_8^{12} & \omega_8^{16}  & \omega_8^{20} & \omega_8^{24} & \omega_8^{28} \\ 1  & \omega_8^5 & \omega_8^{10} & \omega_8^{15} & \omega_8^{20}  & \omega_8^{25} & \omega_8^{30} & \omega_8^{35} \\ 1  & \omega_8^6 & \omega_8^{12} & \omega_8^{18} & \omega_8^{24}  & \omega_8^{30} & \omega_8^{36} & \omega_8^{42} \\ 1  & \omega_8^7 & \omega_8^{14} & \omega_8^{21} & \omega_8^{28}  & \omega_8^{35} & \omega_8^{42} & \omega_8^{49}\end{bmatrix} ").shift(LEFT*1 + DOWN*1.5)
		self.play(FadeIn(qftmatrix3))
		self.wait(8)
		qftmatrices = Group(qftmatrix1, qftmatrix2, qftmatrix3)
		self.play(FadeOut(qftmatrices))
		#schmidt factorization
		title3 = Text("QFT - Schmidt Decomposition").shift(UP*3.5)
		self.play(Transform(title, title3))

		formulaq = Tex(r"QFT(\ket{x}) =\frac{1}{\sqrt{(2^N})} \sum_{k=0}^{2^N-1} \omega_{2^N}^{kx} \ket{k} ").shift(UP*2)
		self.play(FadeIn(formulaq))
		self.wait(3)

		formulawhy = Text("No Entanglement, No Mixed States - Schmidt Decomposition!").shift(DOWN*3).scale(0.5)
		self.play(Write(formulawhy))

		thesmidth = Tex(r"QFT(\ket{x}) = \frac{1}{\sqrt{(2^N})}\bigotimes_{k=0}^{N-1} \Big( \ket{0} + \omega_{2^N}^{(N-k)x} \ket{1} \Big)").shift(DOWN)
		self.play(FadeIn(thesmidth))
		self.wait(8)

		schmidtbros = Group(formulaq, formulawhy, thesmidth)
		self.play(FadeOut(schmidtbros))



		title4 = Text("QFT - N = 1 qubits {0-1}").shift(UP*3.5)
		self.play(Transform(title, title4))

		todo = Text("Calculate QFT each basis of 1 qubit").shift(DOWN*3).scale(0.5)
		self.play(Write(todo))

		self.wait(15)
		solve1 = Tex(r"QFT(\ket{0}_1 or \ket{0}) =\frac{1}{2} \sum_{k=0}^{1} \omega_2^{0k} \ket{k} = \frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}").shift(UP*2).scale(0.7)
		solve2 = Tex(r"QFT(\ket{1}_1 or \ket{1}) =\frac{1}{2} \sum_{k=0}^{1} \omega_2^{1k} \ket{k} = \frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}").shift(UP*0).scale(0.7)
		solve3 = Tex(r"QFT(\ket{x}) = H").shift(DOWN*1.5).scale(0.7)

		self.play(FadeIn(solve1))
		self.wait(3)
		self.play(FadeIn(solve2))
		self.wait(3)
		self.play(FadeIn(solve3))


		self.wait(8)
		solves = Group(solve1, solve2, solve3, todo)
		self.play(FadeOut(solves))

		#show its unitary
		itsunitary = Text("QFT is Unitary")
		itsunitary2 = Text("QFT has InverseQFT").shift(DOWN*3)
		self.play(FadeIn(itsunitary), FadeIn(itsunitary2))
		self.wait(6)
		self.play(FadeOut(itsunitary), FadeOut(itsunitary2))
		

		title5 = Text("QFT - Circuit").shift(UP*3.5)
		self.play(Transform(title, title5))

		self.wait(5)


























class fourier3(Scene):
	def construct(self):
		title = Text("QFT - Circuit").shift(UP*3.5)
		self.add(title)
		self.wait(2)
		
		#make a 
		base = 1.5
		offset = 1.5
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.45, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq) + "_" + str(self.n)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([5, -offset*self.n + base, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=BLUE))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*5.75).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)


		qubits = []
		for i in range(0, 2):
			if (i == 0):
				qubits.append(qubit(i, '2^1', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2^0', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'X_1', 'X_2'))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())

		def hadamard(pos,down):
			hx = pos
			h2 = Text("H").shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def rtgate(pos, up, down, val):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"R_" + str(val)).scale(1.5).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=ORANGE, fill_opacity=1, color=ORANGE).scale(0.5).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot3, vnot4, vnot1, vnot2)
			return vnot

		h1 = hadamard(-2, 0)
		r1 = rtgate(0, 1, 0, 2)
		h2 = hadamard(2, 1)
		gates = Group(h1, r1, h2)
		self.wait(4)
		self.play(FadeIn(gates))

		thergate = Tex(r"R_N = \begin{bmatrix} 1 & 0 \\ 0 & \omega_{2^N} \end{bmatrix}").shift(DOWN*2.75)
		self.play(FadeIn(thergate))

		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(3)

		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}*i*\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}*i*\ket{1}"
		qubits[1].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(3)

		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{0}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\ket{0}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\frac{1}{\sqrt{(2})}\ket{0} + \frac{1}{\sqrt{(2})}\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)


		self.wait(3)


		x = -5
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(5)
		while(x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}*i*\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)
		while(x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}*i*\ket{1}"
		qubits[1].dq = r"\frac{1}{\sqrt{(2})}\ket{0} - \frac{1}{\sqrt{(2})}\ket{1}"
		self.wait(0.5)
		while(x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(3)

		self.play(FadeOut(gates))
		for i in range(0, 2):
			self.remove(qubits[i].get())









		qubits = []
		for i in range(0, 3):
			if (i == 0):
				qubits.append(qubit(i, '2^2', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2^1', ''))
			elif (i == 2):
				qubits.append(qubit(i, '2^0', ''))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())




		h1 = hadamard(-3, 0)
		r1 = rtgate(-2, 1, 0, 2)
		r2 = rtgate(-1, 2, 0, 3)
		h2 = hadamard(0, 1)
		r3 = rtgate(1, 2, 1, 2)
		h3 = hadamard(2, 2)
		gates = Group(h1, r1, h2, r2, r3, h3)
		self.play(FadeIn(gates))
		self.wait(4)



		self.play(FadeOut(gates))
		for i in range(0, 3):
			self.remove(qubits[i].get())

		self.play(FadeOut(thergate))



		qubits = []
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, '2^3', ''))
			elif (i == 1):
				qubits.append(qubit(i, '2^2', ''))
			elif (i == 2):
				qubits.append(qubit(i, '2^1', ''))
			elif (i == 3):
				qubits.append(qubit(i, '2^0', ''))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())


		h1 = hadamard(-4.5, 0)
		r1 = rtgate(-3.5, 1, 0, 2)
		r2 = rtgate(-2.5, 2, 0, 3)
		r3 = rtgate(-1.5, 3, 0, 4)
		h2 = hadamard(-0.5, 1)
		r4 = rtgate(0.5, 2, 1, 2)
		r5 = rtgate(1.5, 3, 1, 3)
		h3 = hadamard(2.5, 2)
		r6 = rtgate(3.5, 3, 2, 2)
		h4 = hadamard(4.5, 3)
		gates = Group(h1, r1, h2, r2, r3, h3, r4, r5, r6, h4)
		self.play(FadeIn(gates))
		self.wait(4)

		self.play(FadeOut(gates))


		qft1 = Rectangle(width=3, height=5.5, color=BLUE, fill_color=BLUE, fill_opacity=1)
		qft2 = Text("QFT").set_color(BLACK)
		qft = Group(qft1, qft2).shift(DOWN*0.75)
		self.play(FadeIn(qft))

		self.wait(5)
		for i in range(0, 4):
			self.remove(qubits[i].get())
		self.play(FadeOut(qft))
	




		#3d visualization, 2 bit fourier transform
		#show 3d rep
		frame = self.camera.frame
		self.play(
			frame.increment_phi, 50 * DEGREES,
			frame.increment_theta, -30 * DEGREES,
			run_time=2
		)
		frame.generate_target()
		frame.target.set_width(20)
		self.play(MoveToTarget(frame))

		
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
		the3dqubs.append(qubit3d(-6, 0))
		the3dqubs.append(qubit3d(-2, 0))
		the3dqubs.append(qubit3d(2, 0))
		the3dqubs.append(qubit3d(6, 0))
		
		the3dvects = []
		the3dvects.append(vect3d(-6, 0, 1))
		the3dvects.append(vect3d(-2, 0, -1))
		the3dvects.append(vect3d(2, 0, 1))
		the3dvects.append(vect3d(6, 0, -1))

		self.add(*the3dqubs, *the3dvects)
		frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
		#add vectors
		
		def hadamard3d(pos):
			#big H 
			hadamardbro2 = Square(fill_color=YELLOW, fill_opacity=0.1, color=YELLOW).scale(1.5)
			hadamo2 = Text("H", fill_color=BLACK).scale(2.5)
			hadamard2 = Group(hadamardbro2, hadamo2).shift(RIGHT*pos + IN*20)
			hadamard2.generate_target()
			return hadamard2
		def rxGate(a,b,n):
			cnot4 = Dot(np.array([a,0,0]), fill_color=RED).scale(3)
			cnot5 = Tex(r"R_"+ str(n)).scale(4).set_color(RED).shift(RIGHT*b)
			cnot6 = Line(np.array([a, 0, 0]), np.array([b, 0, 0]), color=RED)
			hadamardbro2 = Square(fill_color=ORANGE, fill_opacity=0.1, color=ORANGE).scale(1.5).shift(RIGHT*b)
			cnot22 = Group(hadamardbro2, cnot4, cnot5, cnot6).shift(IN*20)
			cnot22.generate_target()
			return cnot22
		def moveGate(gate):
			gate.target.shift(OUT*20)
			self.play(MoveToTarget(gate, run_time=4))
		hgates = []
		rgates = []
		hgates.append(hadamard3d(-6))
		rgates.append(rxGate(-2, -6, 2))
		rgates.append(rxGate(2, -6, 3))
		rgates.append(rxGate(6, -6, 4))

		hgates.append(hadamard3d(-2))
		rgates.append(rxGate(2, -2, 2))
		rgates.append(rxGate(6, -2, 3))

		hgates.append(hadamard3d(2))
		rgates.append(rxGate(6, 2, 2))

		hgates.append(hadamard3d(6))

		self.add(*hgates)
		self.add(*rgates)

		
		r = [0, 0, 0, 0]
		s = [0, 0, 0, 0]
		def update_vect1(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r[0], np.array([1, 0, -1])).rotate_about_origin(s[0], np.array([0, 0, 1])).shift(LEFT*6))
		the3dvects[0].add_updater(update_vect1)
		def update_vect2(self):
			self.become(Vector(direction=[0, 0, -1]).rotate_about_origin(r[1], np.array([1, 0, -1])).rotate_about_origin(s[1], np.array([0, 0, 1])).shift(LEFT*2))
		the3dvects[1].add_updater(update_vect2)
		def update_vect3(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r[2], np.array([1, 0, -1])).rotate_about_origin(s[2], np.array([0, 0, 1])).shift(RIGHT*2))
		the3dvects[2].add_updater(update_vect3)
		def update_vect4(self):
			self.become(Vector(direction=[0, 0, -1]).rotate_about_origin(r[3], np.array([1, 0, -1])).rotate_about_origin(s[3], np.array([0, 0, 1])).shift(RIGHT*6))
		the3dvects[3].add_updater(update_vect4)








		#APPLY ON QUBIT 1
		moveGate(hgates[0])
		while (r[0]<3.14159):
			r[0] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(hgates[0])
		moveGate(rgates[0])
		while (s[0]<3.14159/2):
			s[0] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(rgates[0])

		moveGate(rgates[1])
		moveGate(rgates[1])

		moveGate(rgates[2])
		while (s[0]<3.14159/2 + 3.14159/8):
			s[0] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(rgates[2])








		#APPLY ON QUBIT 2
		moveGate(hgates[1])
		while (r[1]<3.14159):
			r[1] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(hgates[1])
		moveGate(rgates[3])
		moveGate(rgates[3])
		moveGate(rgates[4])
		while (s[1]<3.14159/4):
			s[1] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(rgates[4])











		#APPLY ON QUBIT 3
		moveGate(hgates[2])
		while (r[2]<3.14159):
			r[2] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(hgates[2])
		moveGate(rgates[5])
		while (s[2]<3.14159/2):
			s[2] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(rgates[5])



		#APPLY ON QUBIT 4

		moveGate(hgates[3])
		while (r[3]<3.14159):
			r[3] += 0.05
			frame.increment_theta(0.1*0.015)
			self.wait(0.001)
		moveGate(hgates[3])


		self.wait(10)
		nowALL = Group(*hgates, *rgates, *the3dqubs, *the3dvects, title)
		self.play(FadeOut(nowALL))
		self.wait(3)






class fourier4(Scene):
	def construct(self):
		title = Text("QFT - Applications").shift(UP*3.5)
		self.play(FadeIn(title))
		self.wait(2)

		qftaddition = Text("Addition: a -> QFT(a) -> QFT(a+b) -> a+b").shift(UP*2).scale(0.5)
		qftmult = Text("Multiplication: a -> QFT(a) -> QFT(a+partial(b)) -> ab").shift(UP*1).scale(0.5)
		qftphase= Text("Quantum Phase Estimation: a -> Unitary(a) -> InverseQFT(a) -> Phase of a").shift(UP*0).scale(0.5)
		qftlinear = Text("Sys. of Lin. Eq: M -> QPE(M) -> Ancilla(M) -> InverseQFT(M) -> M inverse").shift(DOWN*1).scale(0.5)
		qftMonteCarlo = Text("Monte Carlo: M -> Controlled QPE(M) -> InverseQFT(M) -> Random").shift(DOWN*2).scale(0.5)
		qftPrinciple = Text("Principle Comp. Analysis: M -> QSVT(M) -> QFT(M) -> AncillaPhaseShift(M) -> InverseQFT(M)").shift(DOWN*3).scale(0.5)

		qfts = Group(qftaddition, qftmult, qftphase, qftlinear, qftMonteCarlo, qftPrinciple)
		self.play(FadeIn(qftaddition))
		self.wait(6)
		self.play(FadeIn(qftmult))
		self.wait(6)
		self.play(FadeIn(qftphase))
		self.wait(6)
		self.play(FadeIn(qftlinear))
		self.wait(6)
		self.play(FadeIn(qftMonteCarlo))
		self.wait(6)
		self.play(FadeIn(qftPrinciple))
		self.wait(15)



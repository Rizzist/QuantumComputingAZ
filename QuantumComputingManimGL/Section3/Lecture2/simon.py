from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Simon's Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class simon(Scene):
	def construct(self):
		text = Text("Simon's Algorithm").scale(1.3)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))	

		title = Text("The Problem").shift(UP*3.5)
		self.play(Write(title))

		letssay = Text("Suppose f(x) takes an n-bit string and has a secret code 's'").shift(UP*2.8).scale(0.7)
		self.play(FadeIn(letssay))
		self.wait(6)
		letssay2 = Text("This code makes f(x) = f(y) if y = x + s").shift(UP*2.2).scale(0.7)
		self.play(FadeIn(letssay2))
		self.wait(8)
		letssay3 = Text("How do we find s?").shift(UP*1.6).scale(0.7)
		self.play(FadeIn(letssay3))
		self.wait(4)

		table = Tex(r"\begin{tabular}{||c c||} \hline x & f(x)\\ [0.5ex] \hline\hline 000 & 100 \\ \hline 001 & 010 \\ \hline 010 & 011 \\ \hline 011 & 001 \\ \hline 100 & 001 \\ \hline 101 & 100 \\  \hline 110 & 010 \\ \hline 111 & 011 \\ [1ex]  \hline \end{tabular}").shift(DOWN*1 + LEFT*4.5).scale(0.8)
		self.play(FadeIn(table))
		self.wait(8)

		thecode = Text("Secret Code is: 101").shift(RIGHT*2).scale(0.7)
		self.play(FadeIn(thecode))
		self.wait(10)
		self.play(FadeOut(Group(letssay3, letssay2, letssay, table, thecode)))


		title2 = Text("Stringy Vectors").shift(UP*3.5)
		self.play(Transform(title, title2))
		#convert string to vector, then show inner product and mod 2
		stringy = Tex(r"x = x_2x_1x_0 \ \ \ \ \ y=y_2y_1y_0").shift(UP*2.8)
		self.play(FadeIn(stringy))
		self.wait(4)

		stringy2 = Tex(r"x = \begin{bmatrix} x_2 \\ x_1 \\ x_0 \end{bmatrix}").shift(LEFT*3 + UP*1)
		self.play(FadeIn(stringy2))

		stringy3 = Tex(r"y = \begin{bmatrix} y_2 \\ y_1 \\ y_0 \end{bmatrix}").shift(RIGHT*2 + UP*1)
		self.play(FadeIn(stringy3))
		self.wait(4)

		dotit = Text("'Stringy' Dot Product").shift(DOWN*3)
		self.play(FadeIn(dotit))

		stringy5 = Tex(r"x \cdot y = x_2y_2 + x_1y_1 + x_0y_0").shift(DOWN*0.8)
		self.play(FadeIn(stringy5))
		self.wait(10)
		


		stringy4 = Tex(r"x \cdot y &\equiv (x_2y_2 + x_1y_1 + x_0y_0)\mod 2").shift(DOWN*1.7).scale(1.2)
		self.play(FadeIn(stringy4))
		self.wait(4)
		dotit2 = Text("'Stringy' Dot Product Mod 2").shift(DOWN*3)
		self.play(Transform(dotit, dotit2))
		self.wait(12)

		stringsBro = Group(stringy, stringy2, stringy3, dotit, stringy4, stringy5)
		self.play(FadeOut(stringsBro))






		title3 = Text("Generalized Born Rule").shift(UP*3.5)
		self.play(Transform(title, title3))

		it = Tex(r"\ket{\phi}^{n+m} = \ket{0}_A^n\ket{\psi_0}_B^m + \ket{1}_A^n\ket{\psi_1}_B^m + \cdots + \ket{2^n-1}_A^n\ket{\psi_{(2^n-1})}_B^m").shift(UP*2)
		self.play(FadeIn(it))
		self.wait(15)

		ifam = Tex(r"\text{Measure  } A \ \ \searrow \ \ 1 \ \ \ \ \Rightarrow \ \ \ \ B \ \ \searrow \ \ \ket{\psi_1}_B^m")
		self.play(FadeIn(ifam))

		self.wait(30)
		self.play(FadeOut(it), FadeOut(ifam))

		

		title4 = Text("Simon Algorithm - Circuit").shift(UP*3.5)
		self.play(Transform(title, title4))
		#make a 
		base = 1.5
		offset = 1.5
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.45, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}^n"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
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
				qubits.append(qubit(i, 'x', 'x'))
			elif (i == 1):
				qubits.append(qubit(i, '0', 'f(x)'))
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
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def xgate(pos,down):
			cx = pos
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot = Group(cnot2)
			return cnot
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def nhadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes n}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.5)
			measure2 = Text('M').set_color(BLACK)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def oracle():
			oracle1 = Square(fill_color=WHITE, fill_opacity=1).scale(0.7)
			oracle2 = Tex(r"U_f").set_color(BLACK).scale(1.7)
			oracle = Group(oracle1, oracle2).scale(1.5)
			oracle.shift(UP*0.8)
			return oracle



		o1 = oracle()
		h1 = nhadamard(-3, 0)
		h2 = nhadamard(2.5, 0)
		m1 = measure(2.5, 1)
		m2 = measure(4, 0)
		gates = Group(h1, h2, m1, m2)
		self.play(FadeIn(o1))
		self.wait(5)
		self.play(FadeIn(gates))


		nophase = Text("Bottom Input is 0: No Phase Kickback!").shift(DOWN*2)
		self.play(FadeIn(nophase))
		self.wait(4)
		nophase2 = Text("Write this circuit down!!!").shift(DOWN*3)
		self.play(FadeIn(nophase2))
		self.wait(20)

		for i in range(0, 2):
			self.remove(qubits[i].get())

		self.play(FadeOut(nophase), FadeOut(nophase2), FadeOut(gates), FadeOut(o1))









		states = []
		states.append( Tex(r"\text{Hadamard Gates: } \frac{1}{\sqrt{(2^N})} \sum_{i=0}^{2^N - 1} \ket{i}^n\ket{0}^n").shift(UP*2) )
		self.play(FadeIn(states[0]))
		self.wait(10)

		states.append( Tex(r"\text{Unknown Function: } \frac{1}{\sqrt{(2^N})} \sum_{i=0}^{2^N - 1} \ket{i}^n\ket{f(i)}^n").shift(UP*0) )
		self.play(FadeIn(states[1]))
		self.wait(10)

		states.append( Tex(r"\text{ReWrite: } \frac{1}{\sqrt{(2^{N-1} })} \sum_{i \in R} \frac{(\ket{i}^n + \ket{i + s}^n)}{\sqrt{(2})}\ket{f(i)}^n").shift(DOWN*2) )
		self.play(FadeIn(states[2]))
		self.wait(10)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(DOWN*4)
		self.play(MoveToTarget(frame))

		states.append( Tex(r"\text{Measure 1 (GBR) Collapse: } \frac{(\ket{i_0}^n + \ket{i_0 + s}^n)}{\sqrt{(2})}\ket{f(i_0)}^n").shift(DOWN*4) )
		self.play(FadeIn(states[3]))
		self.wait(10)

		states.append( Tex(r"\text{Hadamard (first n qubits): } \frac{(H^{\otimes n}(\ket{i_0}^n) + H^{\otimes n}(\ket{i_0 + s}^n))}{\sqrt{(2})}").shift(DOWN*6) )
		self.play(FadeIn(states[4]))
		self.wait(10)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(DOWN*4)
		self.play(MoveToTarget(frame))

		states.append( Tex(r"\uparrow \text{ : } \frac{1}{\sqrt{(2^{N+1} })} (\sum_{j=0}^{2^N-1} (-1)^{j \cdot i_0} * (1 + (-1)^{j \cdot s})\ket{j})").shift(DOWN*8) )
		self.play(FadeIn(states[5]))
		self.wait(10)

		states.append( Tex(r"\text{ReWrite : } \frac{1}{\sqrt{(2^{N-1} })} (\sum_{j \cdot s =0} (-1)^{j \cdot i_0}\ket{j})").shift(DOWN*10) )
		self.play(FadeIn(states[6]))
		self.wait(10)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(DOWN*4)
		self.play(MoveToTarget(frame))

		states.append( Tex(r"\text{Measure 2 : } j_0 \mid j_0 \cdot s = 0").shift(DOWN*13) )
		self.play(FadeIn(states[7]))
		self.wait(10)

		states.append( Tex(r"\text{Repeat until N-1 j's: } \{j_0, j_1, \cdots, j_{N-1}\}").shift(DOWN*14) )
		self.play(FadeIn(states[8]))
		self.wait(10)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(DOWN*3)
		self.play(MoveToTarget(frame))

		states.append( Tex(r"j_0 \cdot s &\equiv 0 \mod 2").shift(DOWN*15) )
		states.append( Tex(r"j_1 \cdot s &\equiv 0 \mod 2").shift(DOWN*15.5) )
		states.append( Tex(r"\cdots").shift(DOWN*16) )
		states.append( Tex(r"j_{N-1} \cdot s &\equiv 0 \mod 2").shift(DOWN*16.5) )
		thejs = Group(*states[9:])
		self.play(FadeIn(thejs))
		self.wait(10)

		states.append( Text("Gaussian Elimination").shift(DOWN*17.5) )
		self.play(FadeIn(states[13]))
		self.wait(10)

		frame = self.camera.frame
		frame.generate_target()
		frame.target.shift(UP*15)
		self.play(MoveToTarget(frame, run_time=5.0))
		self.play(FadeOut(Group(*states)))

		#example:
		jays = []
		jays.append( Tex(r"j_0 = 010").shift(UP*2 + LEFT*4) )
		jays.append( Tex(r"j_1 = 101").shift(UP*0 + LEFT*4) )
		jays.append( Tex(r"j_2 = 000").shift(DOWN*2 + LEFT*4) )
		self.play(FadeIn(Group(*jays)))
		self.wait(10)

		jays.append( Tex(r"j_0*s = 0").shift(UP*2 + LEFT*0) )
		jays.append( Tex(r"j_1*s = 0").shift(UP*0 + LEFT*0) )
		jays.append( Tex(r"j_2*s = 0").shift(DOWN*2 + LEFT*0) )
		self.play(FadeIn(Group(*jays[3:])))
		self.wait(10)

		jays.append( Tex(r"s = 101").shift(UP*0 + RIGHT*4) )
		self.play(FadeIn(jays[6]))

		self.wait(15)
		#self.play(FadeOut(Group(*jays)))

















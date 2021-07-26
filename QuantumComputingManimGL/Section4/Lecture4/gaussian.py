from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Boson Sampling Model").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class gaussian(Scene):
	def construct(self):
		text = Text("Boson Sampling Model")
		self.play(FadeIn(text))
		self.wait(15)
		self.play(FadeOut(text))


		title = Text("Boson Sampling Model").shift(UP*3.5)
		self.play(FadeIn(title))

		#make a 
		base = 4
		offset = 1
		offsetY = 0.5
		x = 0
		class qubit90():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*(base+offset*self.n-5) + DOWN*x + UP*3 + UP*self.upper + LEFT*0.4 + DOWN*offsetY).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(RIGHT*(base+offset*self.n-5) + DOWN*x + UP*3).add_updater(update_qubit)
				self.l = Line(np.array([offset*self.n + base -5, 0-offsetY, 0]), np.array([offset*self.n + base-5, 3-offsetY, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([base+offset*self.n-5,3-x-offsetY,0]),fill_color=BLUE))
				self.qub = Dot(np.array([base+offset*self.n-5,3-x,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(RIGHT*(base+offset*self.n-5) + UP*3.5 + DOWN*offsetY).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(RIGHT*(base+offset*self.n-5) + DOWN*3.5 + DOWN*offsetY).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)

		qubits = []
		for i in range(0, 3):
			qubits.append(qubit90(i, str(i), ''))
			self.add(qubits[i].get())

		def unknownf(pos,right):
			hx = pos
			h2 = Tex(r"U_f").scale(1).shift(RIGHT*(offset*right + base-5) + DOWN*hx).set_color(BLACK)
			h3 = Rectangle(width=3.5, height=1.5, fill_color=YELLOW, fill_opacity=1, color=YELLOW).shift(RIGHT*(offset*right + base-5) + DOWN*hx)
			hadamard = Group(h3, h2)
			return hadamard
		gate = unknownf(-1, 1)
		self.play(FadeIn(gate))
		
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{0}"

		stuff = []
		stuff.append( Tex(r"\ket{1, 1, 0}").shift(LEFT*4.5 + UP*2.5) )
		stuff.append( Tex(r"\ket{0, 1, 1}").shift(LEFT*4.5 + DOWN*1) )
		stuff.append( Tex(r"\sum_{j=1} U_{i,j} \hat{a}_j^\dag").shift(LEFT*4.5 + UP*1.25) )
		stuff.append( Tex(r"\sum_S \gamma_S \ket{n_1^{(S)}, n_2^{(S)}, n_3^{(S)}}").shift(LEFT*4.25 + UP*0) )
		stuff.append( Tex(r"P_S = {\mid\gamma_S\mid}^2").shift(LEFT*4.5 + DOWN*2.5) )
		
		for i in stuff:
			self.play(FadeIn(i))
			self.wait(6)
		while(x<1.5):
			x += 0.05
			self.wait(0.001)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		qubits[2].dq = r"\ket{1}"
		while(x<3):
			x += 0.05
			self.wait(0.001)

		stuff2 = []
		stuff2.append(  DashedLine(np.array([-1, 1.25 + offsetY, 0]), np.array([1, -0.25 + offsetY, 0]), color=RED) )
		stuff2.append(  DashedLine(np.array([0, 1.25 + offsetY, 0]), np.array([0, -0.25 + offsetY, 0]), color=RED) )
		stuff2.append(  DashedLine(np.array([-1, 1.25 + offsetY, 0]), np.array([0, -0.25 + offsetY, 0]), color=GREEN) )
		stuff2.append(  DashedLine(np.array([0, 1.25 + offsetY, 0]), np.array([1, -0.25 + offsetY, 0]), color=GREEN) )
		for i in stuff2:
			self.play(FadeIn(i))
			self.wait(4)

		stuff3 = []
		stuff3.append( Tex(r"\gamma_{2,3} = U_{1,2}U_{2,3} + U_{1,3}U_{2,2}").shift(RIGHT*4 + UP*2.5) )
		stuff3.append( Tex(r"\gamma_{2,3} = Per( \begin{bmatrix} U_{1,2} & U_{1,3} \\ U_{2,2} & U_{2,3} \end{bmatrix} )").shift(RIGHT*4 + DOWN*0.25) )
		for i in stuff3:
			self.play(FadeIn(i))
			self.wait(10)

		stuff4 = []
		stuff4.append( Tex(r"det(A) = \sum_{\sigma \in S_n} sgn(\sigma)\prod_{i=1} a_{i, \sigma_i}").shift(RIGHT*0 + DOWN*2) )
		stuff4.append( Tex(r"Per(A) = \sum_{\sigma \in S_n} \prod_{i=1} a_{i, \sigma_i}").shift(RIGHT*0 + DOWN*3.25) )
		for i in stuff4:
			self.play(FadeIn(i))
			self.wait(4)
		self.wait(3)
		for i in range(0, 3):
			self.remove(qubits[i].get())
		self.play(FadeOut(Group(*stuff, *stuff2, *stuff3, *stuff4, gate)))
		



		title2 = Text("Boson Sampling Formalism").shift(UP*3.5)
		self.play(Transform(title, title2))


		stuff5 = []
		stuff5.append( Tex(r"\ket{\psi} = \ket{1_1,...,1_n, 0_{n+1}, ..., 0_m}").shift(UP*2.7) )
		stuff5.append( Tex(r"\ket{\psi} = \hat{a}_1^\dag ... \hat{a}_n^\dag\ket{0_{1}, ..., 0_m}").shift(UP*2) )
		stuff5.append( Tex(r"\hat{U}a_i^\dag\hat{U}^\dag = \sum_{j=1} U_{i,j} \hat{a}_j^\dag \to \text{Photonic Gate}").shift(UP*0.75) )
		stuff5.append( Tex(r"\ket{\psi} = \sum_S \gamma_S \ket{n_1^{(S)}, ..., n_m^{(S)}}").shift(DOWN*0.5) )
		stuff5.append( Tex(r"\gamma_S = \frac{Per(U)}{\sqrt{(n_1^S!...n_m^S!})}").shift(DOWN*2 + LEFT*3) )
		stuff5.append( Tex(r"Per(A) = Haf(\begin{bmatrix} 0 & A \\ A^T & 0 \end{bmatrix})").shift(DOWN*2 + RIGHT*3) )
		for i in stuff5:
			self.play(FadeIn(i))
			self.wait(7)
		self.wait(4)
		self.play(FadeOut(Group(*stuff5)))































		title2 = Text("Gaussian Boson Sampling").shift(UP*3.5)
		self.play(Transform(title, title2))

		#make a 
		base = 2
		offset = 0.6
		x = -5
		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
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
		for i in range(0, 4):
			if (i == 0):
				qubits.append(qubit(i, 'A', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'B', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'C', ''))
			elif (i == 3):
				qubits.append(qubit(i, 'E', ''))
			elif (i == 7):
				qubits.append(qubit(i, '1', ''))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		
		
		def squeeze(pos,down):
			hx = pos
			h2 = Tex(r"S").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def rotation(pos,down):
			hx = pos
			h2 = Tex(r"R(\theta_"+str(down)+")").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(fill_color=RED, fill_opacity=1, color=RED).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def beamsplitter(pos,down):
			hx = pos
			h2 = Tex(r"BS").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Rectangle(width=1, height=1.1,fill_color=WHITE, fill_opacity=1, color=WHITE).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).shift(DOWN*0.375)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.25)
			measure2 = Tex(r'\hat{n}').set_color(BLACK).scale(0.85)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure

		gates = []
		for i in range(4):
			gates.append(squeeze(-4.2, i))
			gates.append(rotation(-3, i))
			gates.append(measure(5, i))

		gates.append(beamsplitter(-1.5, 0))
		gates.append(beamsplitter(-1.5, 2))

		gates.append(beamsplitter(-0.25, 1))

		gates.append(beamsplitter(1, 0))
		gates.append(beamsplitter(1, 2))

		gates.append(beamsplitter(2.25, 1))

		gates.append(beamsplitter(3.5, 0))
		gates.append(beamsplitter(3.5, 2))

		self.play(FadeIn(Group(*gates)))

		self.wait(15)
		item = Text("For N Input Modes, N+1 BS Columns Required").shift(DOWN*3).scale(0.7)
		self.play(Write(item))
		self.wait(5)
		item2 = Text("Run Circuit X Times: Get Probabilities").shift(DOWN*1.75).scale(0.7)
		self.play(Write(item2))
		self.wait(30)
		


















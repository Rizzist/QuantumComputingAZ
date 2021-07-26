from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Grover's Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class grover(Scene):
	def construct(self):
		text = Text("Grover's Algorithm").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))


		title = Text("The Problem - Searching Unordered Dataset").shift(UP*3.5)
		self.play(FadeIn(title))

		origs = []
		for i in range(-4, 5):
			comp1 = Square(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.4)
			comp1.shift(RIGHT*i)
			origs.append( comp1 )


		itslist = []
		for i in range(-4, 5):
			comp1 = Square(color=BLACK, fill_color=RED, fill_opacity=1).scale(0.45)
			comp2 = Text("" + str(i**5 % 23))
			total = Group(comp1, comp2)
			total.shift(RIGHT*i)
			itslist.append( total )
		self.add(*origs)
		self.play(FadeIn(Group(*itslist)))




		#find 9
		findit = Text("Classical: Find 9").shift(DOWN*3).scale(0.8)
		self.play(FadeIn(findit))

		for i in range(-4, 3):
			if (i == -4):
				self.play(ApplyMethod(origs[i+4].scale, 1.3))
			else:
				self.play(ApplyMethod(origs[i+4].scale, 1.3), ApplyMethod(origs[i+3].scale, 0.6))

		self.wait(6)
		title2 = Text("Inversion & Inversion along mean").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.remove(*origs)
		origs = []
		for i in range(-4, 5):
			comp1 = Square(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.4)
			comp1.shift(RIGHT*i)
			origs.append( comp1 )
		self.add(*origs)
		self.remove(*itslist)
		self.add(*itslist)

		#quantum method
		findit2 = Text("Quantum: Find 9").shift(DOWN*3).scale(0.8)
		self.play(Transform(findit, findit2))

		self.play( ApplyMethod(origs[0].scale, 1.5),ApplyMethod(origs[1].scale, 1.5),ApplyMethod(origs[2].scale, 1.5),ApplyMethod(origs[3].scale, 1.5),ApplyMethod(origs[4].scale, 1.5),ApplyMethod(origs[5].scale, 1.5),ApplyMethod(origs[6].scale, 1.5),ApplyMethod(origs[7].scale, 1.5),ApplyMethod(origs[8].scale, 1.5), )
		self.wait(3)
		self.play( ApplyMethod(origs[0].scale, 1.1),ApplyMethod(origs[1].scale, 1.1),ApplyMethod(origs[2].scale, 1.1),ApplyMethod(origs[3].scale, 1.1),ApplyMethod(origs[4].scale, 1.1),ApplyMethod(origs[5].scale, 1.1),ApplyMethod(origs[6].scale, 0.5),ApplyMethod(origs[7].scale, 1.1),ApplyMethod(origs[8].scale, 1.1), )
		self.wait(8)
		self.play( ApplyMethod(origs[0].scale, 0.5),ApplyMethod(origs[1].scale, 0.5),ApplyMethod(origs[2].scale, 0.5),ApplyMethod(origs[3].scale, 0.5),ApplyMethod(origs[4].scale, 0.5),ApplyMethod(origs[5].scale, 0.5),ApplyMethod(origs[6].scale, 2.5),ApplyMethod(origs[7].scale, 0.5),ApplyMethod(origs[8].scale, 0.5), )
		self.wait(5)
		self.play(FadeOut(Group(*itslist, *origs, findit)))





		#superposition graph
		axes = Axes(x_range=(0, 15), y_range=(0, 1, 1), height=3, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(UP*1)

		self.play(FadeIn(axes))
		
		graphdots = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			dot.move_to(axes.c2p(i, 1/5))
			graphdots.append(dot)

		self.play(FadeIn(Group(*graphdots)))

		xlabel = Tex(r"x \to \ket{x}").shift(DOWN*2.5)
		ylabel = Tex(r"y \to \bra{\psi}\ket{x}").shift(DOWN*3.25)
		self.play(FadeIn(xlabel), FadeIn(ylabel))


		self.wait(10)

		#inversion
		graphdots2 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 1.2/5))
			else:
				dot.move_to(axes.c2p(i, -1/5))
			graphdots2.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots2)))

		self.wait(5)

		#inversion along mean
		graphdots3 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 1/7))
			else:
				dot.move_to(axes.c2p(i, 2/5))
			graphdots3.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots3)))

		self.wait(5)

		#inversion
		graphdots4 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 2/7))
			else:
				dot.move_to(axes.c2p(i, -2/5))
			graphdots4.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots4)))


		self.wait(5)

		#inversion along mean
		graphdots5 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 1/10))
			else:
				dot.move_to(axes.c2p(i, 3/5))
			graphdots5.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots5)))



		self.wait(5)




		#inversion
		graphdots6 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 3/7))
			else:
				dot.move_to(axes.c2p(i, -3/5))
			graphdots6.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots6)))


		self.wait(5)

		#inversion along mean
		graphdots7 = []
		for i in range(0, 15):
			dot = Dot(color=RED)
			if (i != 9):
				dot.move_to(axes.c2p(i, 1/15))
			else:
				dot.move_to(axes.c2p(i, 4/5))
			graphdots7.append(dot)
		self.play(Transform(Group(*graphdots), Group(*graphdots7)))


		self.wait(10)
		self.play(FadeOut(Group(axes, *graphdots, xlabel, ylabel)))























		#Quantum Circuit
		title3 = Text("Grover's Algorithm - Circuit").shift(UP*3.5)
		self.play(FadeOut(title), FadeIn(title3))

		#make a 
		base = 2.75
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
		for i in range(0, 8):
			qubits.append(qubit(i, str(i), ''))
			self.add(qubits[i].get())
		#qubits[7].dq = r"\ket{1}"
		
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def xgate(pos,down, on=1):
			hx = pos
			h2 = Tex(r"X").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=GREEN, fill_opacity=on, color=GREEN).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"H").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.2)
			measure2 = Text('M').set_color(BLACK).scale(0.6)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def gCGate(pos, up, down, control, color):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"" + control).scale(1.1).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=color, fill_opacity=1, color=color).scale(0.325).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot3, vnot4, vnot1, vnot2)
			return vnot
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gGate(pos, depth, down, name):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"" + name).scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gCGateN(pos, up, down, control, color, depth):
			qft1 = Rectangle(width=0.5, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gates = []
		for i in range(0, 8):
			gates.append( hadamard(-4.25, i) )

		gates.append( gGate(-1.5, 2, 3.5, r'U_{f}') )
		gates.append( gGate(1.5, 2, 3.5, r'U_{m}') )

		self.play(FadeIn(Group(*gates)))

		tobrace = Group(*gates[8:])
		brace = always_redraw(Brace, tobrace, DOWN)
		self.add(brace)

		text, number = label = Group(Text("Repeat = "),Tex(r"\sqrt{n}"))
		label.arrange(RIGHT)
		always(label.next_to, brace, DOWN)

		gatesm = []
		for i in range(0, 8):
			gatesm.append( measure(5, i) )
		self.play(FadeIn(Group(*gatesm)))

		
		self.play(FadeIn(label))
		self.wait(5)
		self.play(FadeOut(Group(label, brace)))

		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		qubits[4].dq = r"\ket{0}"
		qubits[5].dq = r"\ket{0}"
		qubits[6].dq = r"\ket{0}"
		qubits[7].dq = r"\ket{0}"
		self.wait(5)
		while(x < -4.25):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{+}"
		qubits[4].dq = r"\ket{+}"
		qubits[5].dq = r"\ket{+}"
		qubits[6].dq = r"\ket{+}"
		qubits[7].dq = r"\ket{+}"
		self.wait(0.5)


		while(x < -1.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{?}"
		qubits[1].dq = r"\ket{?}"
		qubits[2].dq = r"\ket{?}"
		qubits[3].dq = r"\ket{?}"
		qubits[4].dq = r"\ket{?}"
		qubits[5].dq = r"\ket{?}"
		qubits[6].dq = r"\ket{?}"
		qubits[7].dq = r"\ket{?}"
		self.wait(0.5)

		#explain inversion
		inv = []
		inv.append(  Tex(r"U_f = \mathbb{I} - 2\ket{x}\bra{x}").shift(DOWN*2.5).scale(0.8)  )
		self.play(FadeIn(inv[0]))
		self.wait(15)

		frame = self.camera.frame
		frame.generate_target()

		inv.append(  Tex(r"U_f\ket{\psi} =  \ket{\psi} - \frac{2}{\sqrt{(N})}\ket{x}").shift(DOWN*3.25).scale(0.8)  )
		self.play(FadeIn(inv[1]))
		self.wait(15)



		while(x < 1.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{?}"
		qubits[1].dq = r"\ket{?}"
		qubits[2].dq = r"\ket{?}"
		qubits[3].dq = r"\ket{?}"
		qubits[4].dq = r"\ket{?}"
		qubits[5].dq = r"\ket{?}"
		qubits[6].dq = r"\ket{?}"
		qubits[7].dq = r"\ket{?}"
		self.wait(0.5)


		frame.target.shift(DOWN*4)
		self.play(MoveToTarget(frame, run_time=2.0))

		inv.append(  Tex(r"U_m = 2\ket{\psi}\bra{\psi} - \mathbb{I}").shift(DOWN*4).scale(0.8)  )
		self.play(FadeIn(inv[2]))
		self.wait(15)

		frame.target.shift(DOWN*2)
		self.play(MoveToTarget(frame, run_time=2.0))

		inv.append(  Tex(r"U_mU_f = (2\ket{\psi}\bra{\psi} - \mathbb{I})*(\mathbb{I} - 2\ket{x}\bra{x})").shift(DOWN*5).scale(0.8)  )
		inv.append(  Tex(r"U_mU_f = 2\ket{\psi}\bra{\psi} + 2\ket{x}\bra{x} - \frac{4}{\sqrt{(N})}\ket{\psi}\bra{x} - \mathbb{I}").shift(DOWN*6).scale(0.8)  )
		inv.append(  Tex(r"U_mU_f\ket{\psi} = \sqrt{(1-\frac{4}{(N})})\ket{\psi} + \frac{2}{\sqrt{(N})}\ket{x}").shift(DOWN*7).scale(0.8)  )
		inv.append(  Tex(r"(U_mU_f)^n\ket{\psi} = \sqrt{(1-p})\ket{\psi} + \sqrt{(p})\ket{x}").shift(DOWN*8).scale(0.8)  )
		inv.append(  Tex(r"p \to 90\% \mid \sqrt{n}").shift(DOWN*9).scale(0.8)  )


		for i in range(3, 8):
			self.play(FadeIn(inv[i]))
			self.wait(15)

		


















		








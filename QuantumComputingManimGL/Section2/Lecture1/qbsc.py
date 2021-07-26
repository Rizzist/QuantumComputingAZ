from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Bit String Comparator").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class qbsc(Scene):
	def construct(self):
		text = Text("Quantum Bit String Comparator, Midpoint Quantum Comparator").scale(0.65)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		title = Text("QBSC").shift(UP*3.5)
		self.play(FadeIn(title))
		isgreater = Tex(r"\begin{tabular}{||c c c||} \hline X & Y & (Y>X)?\\ [0.5ex] \hline\hline 0 & 0 & 0 \\ \hline 0 & 1 & 1 \\ \hline 1 & 0 & 0 \\ \hline 1 & 1 & 0 \\ [1ex]  \hline \end{tabular}")
		self.play(FadeIn(isgreater))
		self.wait(7)
		self.play(FadeOut(isgreater))

		base = 1
		offset = 1.5
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*1 + UP*base))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*1+ UP*base))
		def update_q3(self):
			self.become(Tex(r"" + str(dq3) + "_3").shift(RIGHT*x + DOWN*offset*2 + UP*1+ UP*base))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7+ UP*base).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7+ UP*base).add_updater(update_q2)
		q3 = Tex(r"\ket{0}_3").shift(LEFT*5 + DOWN*offset*2 + UP*0.7+ UP*base).add_updater(update_q3)

		l1 = Line(np.array([-5, base, 0]), np.array([5, base, 0]))
		l2 = Line(np.array([-5, -offset+ base, 0]), np.array([5, -offset+ base, 0]))
		l3 = Line(np.array([-5, -offset*2+ base, 0]), np.array([5, -offset*2+ base, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,base,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset+ base,0]),fill_color=BLUE))
		def update_qubit3(self):
			self.become(Dot(np.array([x,-offset*2+ base,0]),fill_color=BLUE))
		qubit1 = Dot(np.array([x,base,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset+ base,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)
		qubit3 = Dot(np.array([x,-offset*2+ base,0]), fill_color=BLUE)
		qubit3.add_updater(update_qubit3)

		qlabel1 = Tex(r"X").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"Y").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"(Y>X)?").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, qubit1, qubit2, qubit3, qlabel1, qlabel2, qlabel3)
		itslines = Group(l1, l2, l3)
		self.play(FadeIn(itsg), FadeIn(itslines))

		#v gate
		vx = -3
		vnot1 = Dot(np.array([vx,base-offset,0]), fill_color=BLACK)
		vnot2 = Tex(r"V").scale(1.5).shift(DOWN*offset*2 + RIGHT*vx + UP*base).set_color(BLACK)
		vnot3 = Line(np.array([vx, base-offset, 0]), np.array([vx, -offset*2 + base, 0]))
		vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*2 + RIGHT*vx + UP*base)
		vnot = Group(vnot4, vnot3, vnot1, vnot2)
		self.play(FadeIn(vnot))

		#cx gate
		cx = -2
		cnot1 = Dot(np.array([cx,base,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base, 0]), np.array([cx, -offset + base, 0]))
		cnot = Group(cnot1, cnot2, cnot3)
		self.play(FadeIn(cnot))

		#v dag gate
		vvx = -1
		vnot11 = Dot(np.array([vvx,base,0]), fill_color=BLACK)
		vnot21 = Tex(r"V^\dag").scale(1.5).shift(DOWN*offset*2 + RIGHT*vvx + UP*base).set_color(BLACK)
		vnot31 = Line(np.array([vvx, base, 0]), np.array([vvx, -offset*2 + base, 0]))
		vnot41 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*2 + RIGHT*vvx + UP*base)
		vnot1 = Group(vnot41, vnot31, vnot21, vnot11)
		self.play(FadeIn(vnot1))


		#v gate
		vnot2 = vnot.copy()
		vnot2.shift(RIGHT*4)
		self.play(FadeIn(vnot2))

		#cnot gate
		cnot22=cnot.copy()
		cnot22.shift(RIGHT*4)
		self.play(FadeIn(cnot22))

		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(3)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(1)




		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		self.wait(1)



		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{+i}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{+i}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		self.wait(1)

		self.wait(2)
		thegates = Group(vnot, vnot1, vnot2, cnot, cnot22)
		self.play(FadeOut(thegates))

		title3 = Text("QBSC + Fredkin Gate").shift(UP*3.5)
		self.play(Transform(title, title3))

		qbsc1 = Tex(r"QBSC").set_color(BLACK)
		qbsc2 = Rectangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.9).rotate(PI/2)
		qbsc = Group(qbsc2,qbsc1)
		qbsc.shift(LEFT*2.5 + DOWN*0.5)
		self.play(FadeIn(qbsc))

		cx = 0
		cnot1 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*cx + UP*base).set_color(RED)
		cnot11 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cx + UP*base).set_color(RED)
		cnot2 = Dot(np.array([cx,base -offset*2,0]), fill_color=RED)
		cnot3 = Line(np.array([cx, base, 0]), np.array([cx, -offset*2+ base, 0]))
		cnot = Group(cnot1, cnot11, cnot2, cnot3)
		self.play(FadeIn(cnot))

		qlabel4 = Tex(r"max\{X, Y\}").shift(UP*base + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel5 = Tex(r"min\{X, Y\}").shift(UP*base + DOWN*offset + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel6 = Tex(r"(Y>X)?").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + DOWN*0.5).set_color(GREEN)
		labels = Group(qlabel4, qlabel5, qlabel6)
		self.play(FadeIn(labels))


		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -2.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		self.wait(1)



		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -2.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		self.wait(1)


		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -2.5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		self.wait(1)
















		#greater, less, equal
		self.play(FadeOut(itsg), FadeOut(itslines), FadeOut(qbsc), FadeOut(labels), FadeOut(cnot))

		title2 = Text("Midpoint Qubit Comparison Circuit (MQC)").shift(UP*3.5)
		self.play(Transform(title, title2))

		isgreater = Tex(r"\begin{tabular}{||c c c c c||} \hline X & Y & E(X, Y) & G(X, Y) & L(X, Y)\\ [0.5ex] \hline\hline 0 & 0 & 1 & 0 & 0\\ \hline 0 & 1 & 0 & 0 & 1\\ \hline 1 & 0 & 0 & 1 & 0\\ \hline 1 & 1 & 1 & 0 & 0\\ [1ex]  \hline \end{tabular}")
		self.play(FadeIn(isgreater))
		self.wait(10)
		self.play(FadeOut(isgreater))

		base = 1.75
		offset = 1.5
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*1 + UP*base))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*1+ UP*base))
		def update_q3(self):
			self.become(Tex(r"" + str(dq3) + "_3").shift(RIGHT*x + DOWN*offset*2 + UP*1+ UP*base))
		def update_q4(self):
			self.become(Tex(r"" + str(dq4) + "_4").shift(RIGHT*x + DOWN*offset*3 + UP*1+ UP*base))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7+ UP*base).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7+ UP*base).add_updater(update_q2)
		q3 = Tex(r"\ket{0}_3").shift(LEFT*5 + DOWN*offset*2 + UP*0.7+ UP*base).add_updater(update_q3)
		q4 = Tex(r"\ket{0}_3").shift(LEFT*5 + DOWN*offset*3 + UP*0.7+ UP*base).add_updater(update_q4)

		l1 = Line(np.array([-5, base, 0]), np.array([5, base, 0]))
		l2 = Line(np.array([-5, -offset+ base, 0]), np.array([5, -offset+ base, 0]))
		l3 = Line(np.array([-5, -offset*2 + base, 0]), np.array([5, -offset*2 + base, 0]))
		l4 = Line(np.array([-5, -offset*3 + base, 0]), np.array([5, -offset*3 + base, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,base,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset+ base,0]),fill_color=BLUE))
		def update_qubit3(self):
			self.become(Dot(np.array([x,-offset*2 + base,0]),fill_color=BLUE))
		def update_qubit4(self):
			self.become(Dot(np.array([x,-offset*3 + base,0]),fill_color=BLUE))
		qubit1 = Dot(np.array([x,base,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset+ base,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)
		qubit3 = Dot(np.array([x,-offset*2+ base,0]), fill_color=BLUE)
		qubit3.add_updater(update_qubit3)
		qubit4 = Dot(np.array([x,-offset*3+ base,0]), fill_color=BLUE)
		qubit4.add_updater(update_qubit4)

		qlabel1 = Tex(r"X").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"Y").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"(X>Y)?").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel4 = Tex(r"(X<Y)?").shift(UP*base + DOWN*offset*3 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, q4, qubit1, qubit2, qubit3, qubit4, qlabel1, qlabel2, qlabel3, qlabel4)
		itslines = Group(l1, l2, l3, l4)
		self.play(FadeIn(itsg), FadeIn(itslines))

		qlabel7 = Tex(r"g").shift(UP*base + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel8 = Tex(r"E(X, Y)").shift(UP*base + DOWN*offset + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel9 = Tex(r"G(X, Y)").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel10 = Tex(r"L(X, Y)").shift(UP*base + DOWN*offset*3 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		labels = Group(qlabel7, qlabel8, qlabel9, qlabel10)
		self.play(FadeIn(labels))




		##c gate
		cx = -3
		cnot1 = Dot(np.array([cx,base,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base, 0]), np.array([cx, -offset*2 + base, 0]))
		cnot = Group(cnot3, cnot2, cnot1)
		self.play(FadeIn(cnot))

		#v gate
		vx = -2
		vnot1 = Dot(np.array([vx,base-offset*2,0]), fill_color=BLACK)
		vnot2 = Tex(r"V^\dag").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx + UP*base).set_color(BLACK)
		vnot3 = Line(np.array([vx, base-offset*2, 0]), np.array([vx, -offset*3 + base, 0]))
		vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx + UP*base)
		vnot = Group(vnot4, vnot3, vnot1, vnot2)
		self.play(FadeIn(vnot))

		#c2 gate
		cx2 = -1
		cnot12 = Dot(np.array([cx2,base-offset,0]), fill_color=RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot32 = Line(np.array([cx2, base-offset, 0]), np.array([cx2, -offset*2 + base, 0]))
		cnot2 = Group(cnot32, cnot22, cnot12)
		self.play(FadeIn(cnot2))

		#v2 gate
		vx2 = 0
		vnot12 = Dot(np.array([vx2,base-offset*1,0]), fill_color=BLACK)
		vnot22 = Tex(r"V").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx2 + UP*base).set_color(BLACK)
		vnot32 = Line(np.array([vx2, base-offset*1, 0]), np.array([vx2, -offset*3 + base, 0]))
		vnot42 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx2 + UP*base)
		vnot2 = Group(vnot42, vnot32, vnot12, vnot22)
		self.play(FadeIn(vnot2))

		#v3 gate
		vx3 = 2
		vnot13 = Dot(np.array([vx3,base-offset*2,0]), fill_color=BLACK)
		vnot23 = Tex(r"V").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx3 + UP*base).set_color(BLACK)
		vnot33 = Line(np.array([vx3, base-offset*2, 0]), np.array([vx3, -offset*3 + base, 0]))
		vnot43 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx3 + UP*base)
		vnot3 = Group(vnot43, vnot33, vnot13, vnot23)
		self.play(FadeIn(vnot3))

		#c3 gate
		cx3 = 3
		cnot13 = Dot(np.array([cx3,base-offset*3,0]), fill_color=RED)
		cnot23 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx3 + UP*base).set_color(RED)
		cnot33 = Line(np.array([cx3, base-offset*3, 0]), np.array([cx3, -offset*2 + base, 0]))
		cnot3 = Group(cnot33, cnot23, cnot13)
		self.play(FadeIn(cnot3))

		#o gate
		cx4 = 3
		cnot14 = Dot(np.array([cx4,base-offset*1,0]), fill_color=RED)
		cnot44 = Dot(np.array([cx4,base,0]), fill_color=RED)
		cnot24 = Tex(r"O").scale(2).shift(DOWN*offset*1 + RIGHT*cx4 + UP*base).set_color(RED)
		cnot34 = Line(np.array([cx4, base-offset*0, 0]), np.array([cx4, -offset*1 + base, 0]))
		cnot4 = Group(cnot34, cnot24, cnot14, cnot44)
		self.play(FadeIn(cnot4))

		sequaler = SurroundingRectangle(cnot4)
		self.play(ShowCreation(sequaler))
		self.wait(8)
		self.play(FadeOut(sequaler))

		#-3, -2, -1, 0, 2, 3
		#initial 1000
		self.wait(3)
		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(1)









		#initial 0100
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{1}"
		self.wait(0.5)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(1)








		#initial 1100
		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(1)





















		#initial 0000
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(1)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(12)










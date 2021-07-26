from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Half-Substractor, Full Substractor").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class sub(Scene):
	def construct(self):
		text = Text("Quantum Half-Substractor, Full Substractor").scale(1.0)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))


		title = Text("Quantum Half-Substractor").shift(UP*3.5)
		self.play(Write(title))
	
		isgreater = Tex(r"\begin{tabular}{||c c c c||} \hline X & Y & Borrow & Difference\\ [0.5ex] \hline\hline 0 & 0 & 0 & 0\\ \hline 0 & 1 & 1 & 1\\ \hline 1 & 0 & 0 & 1\\ \hline 1 & 1 & 0 & 0\\ [1ex]  \hline \end{tabular}")
		self.play(FadeIn(isgreater))
		self.wait(7)
		self.play(FadeOut(isgreater))

		#visualize half adder
		corona= ImageMobject("./halfsub.jpeg").shift(DOWN*0.2)
		self.play(FadeIn(corona))

		self.wait(8)
		self.play(FadeOut(corona))


		#half subber
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

		qlabel1 = Tex(r"Y").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"X").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"0").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		qlabel4 = Tex(r"Y").shift(UP*base + RIGHT*5.75).set_color(GREEN)
		qlabel5 = Tex(r"Diff").shift(UP*base + DOWN*offset + RIGHT*5.75).set_color(GREEN)
		qlabel6 = Tex(r"Borrow").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, qubit1, qubit2, qubit3, qlabel1, qlabel2, qlabel3, qlabel4, qlabel5, qlabel6)
		itslines = Group(l1, l2, l3)
		op = Tex(r"X - Y \to \{Diff, Borrow\}").shift(UP*2.5)
		self.play(FadeIn(itsg), FadeIn(itslines), FadeIn(op))



		#v gate
		vx = -2
		vnot1 = Dot(np.array([vx,base-offset,0]), fill_color=BLACK)
		vnot2 = Tex(r"V^\dag").scale(1.5).shift(DOWN*offset*2 + RIGHT*vx + UP*base).set_color(BLACK)
		vnot3 = Line(np.array([vx, base-offset, 0]), np.array([vx, -offset*2 + base, 0]))
		vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*2 + RIGHT*vx + UP*base)
		vnot = Group(vnot4, vnot3, vnot1, vnot2)
		self.play(FadeIn(vnot))

		#cx gate
		cx = -1
		cnot1 = Dot(np.array([cx,base,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base, 0]), np.array([cx, -offset + base, 0]))
		cnot = Group(cnot1, cnot2, cnot3)
		self.play(FadeIn(cnot))

		#v dag gate
		vvx = 0
		vnot11 = Dot(np.array([vvx,base,0]), fill_color=BLACK)
		vnot21 = Tex(r"V").scale(1.5).shift(DOWN*offset*2 + RIGHT*vvx + UP*base).set_color(BLACK)
		vnot31 = Line(np.array([vvx, base, 0]), np.array([vvx, -offset*2 + base, 0]))
		vnot41 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*2 + RIGHT*vvx + UP*base)
		vnot1 = Group(vnot41, vnot31, vnot21, vnot11)
		self.play(FadeIn(vnot1))


		#v gate
		vqx = 2
		vnot12 = Dot(np.array([vqx,base-offset,0]), fill_color=BLACK)
		vnot22 = Tex(r"V").scale(1.5).shift(DOWN*offset*2 + RIGHT*vqx + UP*base).set_color(BLACK)
		vnot32 = Line(np.array([vqx, base-offset, 0]), np.array([vqx, -offset*2 + base, 0]))
		vnot42 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*2 + RIGHT*vqx + UP*base)
		vnot11 = Group(vnot42, vnot32, vnot12, vnot22)
		self.play(FadeIn(vnot11))



		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(8)
		##ccnot animations
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
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
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < -1):
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
		dq3 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		self.wait(1)



		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(1)
		##ccnot animations
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{-i}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{-i}"
		self.wait(0.5)
		while (x < 0):
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
		self.wait(4)
		circuit = Group(vnot, cnot, vnot1, vnot11)
		self.play(FadeOut(itsg), FadeOut(itslines), FadeOut(op), FadeOut(circuit))
		







		title2 = Text("Quantum Full-Substractor").shift(UP*3.5)
		self.play(Transform(title, title2))

		isgreater2 = Tex(r"\begin{tabular}{||c c c c c||} \hline X & Y & Carry In & Diff & Borrow \\ [0.5ex] \hline\hline 0 & 0 & 0 & 0 & 0\\ \hline 0 & 0 & 1 & 1 & 1\\ \hline 0 & 1 & 0 & 1 & 1\\ \hline 0 & 1 & 1 & 1 & 0\\ \hline 1 & 0 & 0 & 0 & 1\\ \hline 1 & 0 & 1 & 0 & 0\\ \hline 1 & 1 & 0 & 0 & 0\\ \hline 1 & 1 & 1 & 1 & 1\\ [1ex]  \hline \end{tabular}")
		isgreater2.shift(DOWN*0.5)
		self.play(FadeIn(isgreater2))
		self.wait(7)
		self.play(FadeOut(isgreater2))


		#draw full subber
		number1 = Tex(r"X = 1").shift(UP*2.5 + LEFT*1)
		number2 = Tex(r"Y = 1").shift(UP*2.5 + RIGHT*1)
		number3 = Tex(r"C_{in} = 1").shift(RIGHT*4)

		number4 = Tex(r"Diff = 1").shift(LEFT*4)
		number5 = Tex(r"Borrow = 1").shift(DOWN*2.5)

		fadder1 = Rectangle(width=4, length=2, color=BLUE, fill_color=BLUE, fill_opacity=1)
		fadder2 = Text("Full Subber").set_color(BLACK)

		input1 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input1.rotate(PI).shift(UP*1.3 + LEFT*1)

		input2 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input2.rotate(PI).shift(UP*1.3 + RIGHT*1)

		input3 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input3.rotate(PI/2).shift(RIGHT*2.5 + DOWN*0.25)

		output1 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		output1.rotate(PI/2).shift(LEFT*2.5 + DOWN*0.25)

		output2 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		output2.rotate(PI).shift(DOWN*1.8)

		fadder = Group(number1, number2, number3, number4, number5, fadder1, fadder2, input1, input2, input3, output1, output2)
		fadder.shift(DOWN*0.5)
		self.play(FadeIn(fadder))
		self.wait(8)
		self.play(FadeOut(fadder))
	

		#create full subber
		#create full subber circuit
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

		qlabel1 = Tex(r"C_{in}").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"Y").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"X").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel4 = Tex(r"0").shift(UP*base + DOWN*offset*3 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, q4, qubit1, qubit2, qubit3, qubit4, qlabel1, qlabel2, qlabel3, qlabel4)
		itslines = Group(l1, l2, l3, l4)
		

		qlabel7 = Tex(r"g").shift(UP*base + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel8 = Tex(r"g").shift(UP*base + DOWN*offset + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel9 = Tex(r"Diff").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel10 = Tex(r"Borrow").shift(UP*base + DOWN*offset*3 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		labels = Group(qlabel7, qlabel8, qlabel9, qlabel10)
		op = Tex(r"X - (Y + C_{in}) \to \{Diff, Borrow\}").shift(UP*2.5)
		self.play(FadeIn(itsg), FadeIn(itslines), FadeIn(op), FadeIn(labels))

		self.wait(2)
		self.play(FadeOut(op))

		#v gate
		#v gate
		vx = -3
		vnot1 = Dot(np.array([vx,base-offset*2,0]), fill_color=BLACK)
		vnot2 = Tex(r"V^\dag").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx + UP*base).set_color(BLACK)
		vnot3 = Line(np.array([vx, base-offset*2, 0]), np.array([vx, -offset*3 + base, 0]))
		vnot4 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx + UP*base)
		vnot = Group(vnot4, vnot3, vnot1, vnot2)
		self.play(FadeIn(vnot))

		#cx gate
		cx = -2
		cnot1 = Dot(np.array([cx,base-offset,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base-offset, 0]), np.array([cx, -offset*2 + base, 0]))
		cnot = Group(cnot3, cnot2, cnot1)
		self.play(FadeIn(cnot))

		#v gate
		vx2 = -1
		vnot12 = Dot(np.array([vx2,base-offset,0]), fill_color=BLACK)
		vnot22 = Tex(r"V").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx2 + UP*base).set_color(BLACK)
		vnot32 = Line(np.array([vx2, base-offset, 0]), np.array([vx2, -offset*3 + base, 0]))
		vnot42 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx2 + UP*base)
		vnot2 = Group(vnot42, vnot32, vnot12, vnot22)
		self.play(FadeIn(vnot2))


		#c2 gate
		cx2 = 0
		cnot12 = Dot(np.array([cx2,base,0]), fill_color=RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot32 = Line(np.array([cx2, base, 0]), np.array([cx2, -offset*2 + base, 0]))
		cnot2 = Group(cnot32, cnot22, cnot12)
		self.play(FadeIn(cnot2))

		#vgate 3
		vx3 = 1
		vnot13 = Dot(np.array([vx3,base,0]), fill_color=BLACK)
		vnot23 = Tex(r"V").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx3 + UP*base).set_color(BLACK)
		vnot33 = Line(np.array([vx3, base, 0]), np.array([vx3, -offset*3 + base, 0]))
		vnot43 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx3 + UP*base)
		vnot3 = Group(vnot43, vnot33, vnot13, vnot23)
		self.play(FadeIn(vnot3))


		#v4 gate
		vx4 = 3
		vnot14 = Dot(np.array([vx4,base-offset*2,0]), fill_color=BLACK)
		vnot24 = Tex(r"V").scale(1.5).shift(DOWN*offset*3 + RIGHT*vx4 + UP*base).set_color(BLACK)
		vnot34 = Line(np.array([vx4, base-offset*2, 0]), np.array([vx4, -offset*3 + base, 0]))
		vnot44 = Square(fill_color=WHITE, fill_opacity=1).scale(0.5).shift(DOWN*offset*3 + RIGHT*vx4 + UP*base)
		vnot4 = Group(vnot44, vnot34, vnot14, vnot24)
		self.play(FadeIn(vnot4))



		#-3, -2, -1, 1, 2, 3
		#initial 1000
		
		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(10)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(1)










		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(10)
		##ccnot animations
		while (x < -3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{-i}"
		self.wait(0.5)
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		dq4 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(7)








from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Multiplexer, Demultiplexer").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class mux(Scene):
	def construct(self):
		text = Text("Quantum Multiplexer, Demultiplexer").scale(1.0)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))


		title = Text("Quantum Multiplexer").shift(UP*3.5)
		self.play(Write(title))
	
	
		isgreater = Tex(r"\begin{tabular}{||c c c||} \hline S1 & S2 & Output\\ [0.5ex] \hline\hline 0 & 0 & I1 \\ \hline 0 & 1 & I2\\ \hline 1 & 0 & I3\\ \hline 1 & 1 & I4\\ [1ex]  \hline \end{tabular}")
		self.play(FadeIn(isgreater))
		self.wait(7)
		self.play(FadeOut(isgreater))

		#visualize mutiplexer
		mcenter = Square(color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75)
		mup = Polygon(ORIGIN, LEFT*2, LEFT*2+UP*2,color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75).shift(UP*0.5 + RIGHT*1)
		mdown = Polygon(ORIGIN, LEFT*2, LEFT*2+DOWN*2,color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75).shift(DOWN*0.5 + RIGHT*1)
		mtext = Text("Mux").set_color(BLACK)

		input1 = Arrow(DOWN*0.5, UP*1, fill_color=RED)
		input1.rotate(3*PI/2).shift(LEFT*1.5 + DOWN*0.75)

		input2 = Arrow(DOWN*0.5, UP*1, fill_color=GREEN)
		input2.rotate(3*PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)

		input3 = Arrow(DOWN*0.5, UP*1, fill_color=GREY)
		input3.rotate(3*PI/2).shift(LEFT*1.5 + DOWN*0.75+ DOWN*1)

		input4 = Arrow(DOWN*0.5, UP*1, fill_color=BLUE)
		input4.rotate(3*PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)

		select1 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		select1.shift(DOWN*0.75 + DOWN*2)

		select2 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		select2.shift(DOWN*0.75 + DOWN*2 + RIGHT*0.5)

		output = Arrow(DOWN*0.5, UP*1, fill_color=BLUE)
		output.rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)

		inouts = Group(input1, input4, select1, output)
		corona = Group(mcenter, mup, mdown, mtext)
		self.play(FadeIn(corona), FadeIn(inouts))



		select1.generate_target()
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2)
		output.generate_target()
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=RED).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=RED).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(output))
		self.wait(1)


		#add other ones
		select2.generate_target()
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)

		output.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(output), FadeIn(input2), FadeIn(input3))
		self.wait(1)

		#add more targets
		#RED GREEN GREY BLUE
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=GREEN).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=GREY).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=RED).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(output))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		output.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(3*PI/2).shift(RIGHT*1.5 + DOWN*0.25)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(output))
		self.wait(5)

		themux = Group(input1, input2, input3, input4, select1, select2, mcenter, mup, mdown, mtext, output)
		self.play(FadeOut(themux))














		#draw the circuit
		base = 1.75
		offset = 1
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*0.5 + UP*base))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*0.5 + UP*base))
		def update_q3(self):
			self.become(Tex(r"" + str(dq3) + "_3").shift(RIGHT*x + DOWN*offset*2 + UP*0.5+ UP*base))
		def update_q4(self):
			self.become(Tex(r"" + str(dq4) + "_4").shift(RIGHT*x + DOWN*offset*3 + UP*0.5+ UP*base))
		def update_q5(self):
			self.become(Tex(r"" + str(dq5) + "_5").shift(RIGHT*x + DOWN*offset*4 + UP*0.5+ UP*base))
		def update_q6(self):
			self.become(Tex(r"" + str(dq6) + "_6").shift(RIGHT*x + DOWN*offset*5 + UP*0.5+ UP*base))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7+ UP*base).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7+ UP*base).add_updater(update_q2)
		q3 = Tex(r"\ket{0}_3").shift(LEFT*5 + DOWN*offset*2 + UP*0.7+ UP*base).add_updater(update_q3)
		q4 = Tex(r"\ket{0}_4").shift(LEFT*5 + DOWN*offset*3 + UP*0.7+ UP*base).add_updater(update_q4)
		q5 = Tex(r"\ket{0}_5").shift(LEFT*5 + DOWN*offset*4 + UP*0.7+ UP*base).add_updater(update_q5)
		q6 = Tex(r"\ket{0}_6").shift(LEFT*5 + DOWN*offset*5 + UP*0.7+ UP*base).add_updater(update_q6)

		l1 = Line(np.array([-5, base, 0]), np.array([5, base, 0]))
		l2 = Line(np.array([-5, -offset+ base, 0]), np.array([5, -offset+ base, 0]))
		l3 = Line(np.array([-5, -offset*2 + base, 0]), np.array([5, -offset*2 + base, 0]))
		l4 = Line(np.array([-5, -offset*3 + base, 0]), np.array([5, -offset*3 + base, 0]))
		l5 = Line(np.array([-5, -offset*4 + base, 0]), np.array([5, -offset*4 + base, 0]))
		l6 = Line(np.array([-5, -offset*5 + base, 0]), np.array([5, -offset*5 + base, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,base,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset+ base,0]),fill_color=BLUE))
		def update_qubit3(self):
			self.become(Dot(np.array([x,-offset*2 + base,0]),fill_color=BLUE))
		def update_qubit4(self):
			self.become(Dot(np.array([x,-offset*3 + base,0]),fill_color=BLUE))
		def update_qubit5(self):
			self.become(Dot(np.array([x,-offset*4 + base,0]),fill_color=BLUE))
		def update_qubit6(self):
			self.become(Dot(np.array([x,-offset*5 + base,0]),fill_color=BLUE))
		qubit1 = Dot(np.array([x,base,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset+ base,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)
		qubit3 = Dot(np.array([x,-offset*2+ base,0]), fill_color=BLUE)
		qubit3.add_updater(update_qubit3)
		qubit4 = Dot(np.array([x,-offset*3+ base,0]), fill_color=BLUE)
		qubit4.add_updater(update_qubit4)
		qubit5 = Dot(np.array([x,-offset*4+ base,0]), fill_color=BLUE)
		qubit5.add_updater(update_qubit5)
		qubit6 = Dot(np.array([x,-offset*5+ base,0]), fill_color=BLUE)
		qubit6.add_updater(update_qubit6)

		qlabel1 = Tex(r"S_1").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"S_2").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"I_3").shift(UP*base + DOWN*offset*1 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel4 = Tex(r"I_1").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel5 = Tex(r"I_4").shift(UP*base + DOWN*offset*3 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel6 = Tex(r"I_2").shift(UP*base + DOWN*offset*4 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, q4, q5, q6, qubit1, qubit2, qubit3, qubit4, qubit5, qubit6)
		itslines = Group(l1, l2, l3, l4, l5, l6)
		itslabels = Group(qlabel1, qlabel2, qlabel3, qlabel4, qlabel5, qlabel6)
		

		qlabel7 = Tex(r"g").shift(UP*base + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel8 = Tex(r"g").shift(UP*base + DOWN*offset + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel9 = Tex(r"g").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel10 = Tex(r"Output").shift(UP*base + DOWN*offset*3 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel11 = Tex(r"g").shift(UP*base + DOWN*offset*4 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel12 = Tex(r"g").shift(UP*base + DOWN*offset*5 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		labels = Group(qlabel7, qlabel8, qlabel9, qlabel10, qlabel11, qlabel12)
		self.play(FadeIn(itsg), FadeIn(itslines), FadeIn(labels), FadeIn(itslabels))






		#cswap gate
		cx = -2
		cnot1 = Dot(np.array([cx,base-offset,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*3 + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base-offset, 0]), np.array([cx, -offset*3 + base, 0]))
		cnot = Group(cnot3, cnot2, cnot1, cnot22)
		self.play(FadeIn(cnot))

		#cswap2 gate
		cx2 = 0
		cnot12 = Dot(np.array([cx2,base-offset,0]), fill_color=RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*4 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*5 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot32 = Line(np.array([cx2, base-offset, 0]), np.array([cx2, -offset*5 + base, 0]))
		cnot99 = Group(cnot32, cnot22, cnot12, cnot222)
		self.play(FadeIn(cnot99))


		#cswap2 gate
		cx3 = 2
		cnot122 = Dot(np.array([cx3,base,0]), fill_color=RED)
		cnot222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*3 + RIGHT*cx3 + UP*base).set_color(RED)
		cnot2222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*5 + RIGHT*cx3 + UP*base).set_color(RED)
		cnot322 = Line(np.array([cx3, base, 0]), np.array([cx3, -offset*5 + base, 0]))
		cnot992 = Group(cnot322, cnot222, cnot122, cnot2222)
		self.play(FadeIn(cnot992))

		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{A}"
		dq4 = r"\ket{0}"
		dq5 = r"\ket{B}"
		dq6 = r"\ket{0}"
		self.wait(10)
		##ccnot animations
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{A}"
		dq5 = r"\ket{B}"
		dq6 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{A}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{B}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{A}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{B}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(7)








		thegates = Group(cnot, cnot99, cnot992)
		self.play(FadeOut(itslines), FadeOut(itsg), FadeOut(itslabels), FadeOut(labels), FadeOut(thegates))
	
		title2 = Text("Quantum Demultiplexer").shift(UP*3.5)
		self.play(Transform(title, title2))



















		#do the demultiplexer
		#visualize mutiplexer
		mcenter = Square(color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75)
		mup = Polygon(ORIGIN, LEFT*2, LEFT*2+UP*2,color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75).shift(UP*0.5 + RIGHT*1)
		mdown = Polygon(ORIGIN, LEFT*2, LEFT*2+DOWN*2,color=YELLOW,fill_color=YELLOW, fill_opacity=1).scale(0.75).shift(DOWN*0.5 + RIGHT*1)
		mtext = Text("Mux").set_color(BLACK)

		input1 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input1.rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)

		input2 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input2.rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)

		input3 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input3.rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75+ DOWN*1)

		input4 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input4.rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)

		select1 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		select1.shift(DOWN*0.75 + DOWN*2)

		select2 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		select2.shift(DOWN*0.75 + DOWN*2 + RIGHT*0.5)

		output = Arrow(DOWN*0.5, UP*1, fill_color=BLUE)
		output.rotate(PI/2).shift(RIGHT*1.5 + DOWN*0.25)

		inouts = Group(input1, input4, select1, output)
		corona = Group(mcenter, mup, mdown, mtext)
		self.play(FadeIn(corona), FadeIn(inouts))



		select1.generate_target()
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2)
		input1.generate_target()
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		self.play(MoveToTarget(select1), MoveToTarget(input1))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2)
		input4.generate_target()
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(input1), MoveToTarget(input4))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2)
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(input1), MoveToTarget(input4))
		self.wait(1)

		#add other ones
		select2.generate_target()
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)

		self.play(MoveToTarget(select1), MoveToTarget(select2), FadeIn(input2), FadeIn(input3))
		self.wait(1)

		input2.generate_target()
		input3.generate_target()
		#add more targets
		#RED GREEN GREY BLUE
		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input2.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)
		input3.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + DOWN*1)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(input1), MoveToTarget(input2), MoveToTarget(input3), MoveToTarget(input4))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)
		input3.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + DOWN*1)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(input1), MoveToTarget(input2), MoveToTarget(input3), MoveToTarget(input4))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=BLACK).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)
		input3.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + DOWN*1)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(input1), MoveToTarget(input2), MoveToTarget(input3), MoveToTarget(input4))
		self.wait(1)

		select1.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + LEFT*0.5)
		select2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).shift(DOWN*0.75 + DOWN*2 + RIGHT*0.25)
		input1.target = Arrow(DOWN*0.5, UP*1, fill_color=BLUE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75)
		input2.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*1)
		input3.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + DOWN*1)
		input4.target = Arrow(DOWN*0.5, UP*1, fill_color=WHITE).rotate(PI/2).shift(LEFT*1.5 + DOWN*0.75 + UP*2)
		self.play(MoveToTarget(select1), MoveToTarget(select2), MoveToTarget(input1), MoveToTarget(input2), MoveToTarget(input3), MoveToTarget(input4))
		self.wait(2)

		themux = Group(input1, input2, input3, input4, select1, select2, mcenter, mup, mdown, mtext, output)
		self.play(FadeOut(themux))












		#draw the circuit
		base = 1.75
		offset = 1
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*0.5 + UP*base))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*0.5 + UP*base))
		def update_q3(self):
			self.become(Tex(r"" + str(dq3) + "_3").shift(RIGHT*x + DOWN*offset*2 + UP*0.5+ UP*base))
		def update_q4(self):
			self.become(Tex(r"" + str(dq4) + "_4").shift(RIGHT*x + DOWN*offset*3 + UP*0.5+ UP*base))
		def update_q5(self):
			self.become(Tex(r"" + str(dq5) + "_5").shift(RIGHT*x + DOWN*offset*4 + UP*0.5+ UP*base))
		def update_q6(self):
			self.become(Tex(r"" + str(dq6) + "_6").shift(RIGHT*x + DOWN*offset*5 + UP*0.5+ UP*base))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7+ UP*base).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7+ UP*base).add_updater(update_q2)
		q3 = Tex(r"\ket{0}_3").shift(LEFT*5 + DOWN*offset*2 + UP*0.7+ UP*base).add_updater(update_q3)
		q4 = Tex(r"\ket{0}_4").shift(LEFT*5 + DOWN*offset*3 + UP*0.7+ UP*base).add_updater(update_q4)
		q5 = Tex(r"\ket{0}_5").shift(LEFT*5 + DOWN*offset*4 + UP*0.7+ UP*base).add_updater(update_q5)
		q6 = Tex(r"\ket{0}_6").shift(LEFT*5 + DOWN*offset*5 + UP*0.7+ UP*base).add_updater(update_q6)

		l1 = Line(np.array([-5, base, 0]), np.array([5, base, 0]))
		l2 = Line(np.array([-5, -offset+ base, 0]), np.array([5, -offset+ base, 0]))
		l3 = Line(np.array([-5, -offset*2 + base, 0]), np.array([5, -offset*2 + base, 0]))
		l4 = Line(np.array([-5, -offset*3 + base, 0]), np.array([5, -offset*3 + base, 0]))
		l5 = Line(np.array([-5, -offset*4 + base, 0]), np.array([5, -offset*4 + base, 0]))
		l6 = Line(np.array([-5, -offset*5 + base, 0]), np.array([5, -offset*5 + base, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,base,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset+ base,0]),fill_color=BLUE))
		def update_qubit3(self):
			self.become(Dot(np.array([x,-offset*2 + base,0]),fill_color=BLUE))
		def update_qubit4(self):
			self.become(Dot(np.array([x,-offset*3 + base,0]),fill_color=BLUE))
		def update_qubit5(self):
			self.become(Dot(np.array([x,-offset*4 + base,0]),fill_color=BLUE))
		def update_qubit6(self):
			self.become(Dot(np.array([x,-offset*5 + base,0]),fill_color=BLUE))
		qubit1 = Dot(np.array([x,base,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset+ base,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)
		qubit3 = Dot(np.array([x,-offset*2+ base,0]), fill_color=BLUE)
		qubit3.add_updater(update_qubit3)
		qubit4 = Dot(np.array([x,-offset*3+ base,0]), fill_color=BLUE)
		qubit4.add_updater(update_qubit4)
		qubit5 = Dot(np.array([x,-offset*4+ base,0]), fill_color=BLUE)
		qubit5.add_updater(update_qubit5)
		qubit6 = Dot(np.array([x,-offset*5+ base,0]), fill_color=BLUE)
		qubit6.add_updater(update_qubit6)

		qlabel1 = Tex(r"S_1").shift(UP*base + LEFT*5.75).set_color(GREEN)
		qlabel2 = Tex(r"S_2").shift(UP*base + DOWN*offset + LEFT*5.75).set_color(GREEN)
		qlabel3 = Tex(r"D").shift(UP*base + DOWN*offset*1 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel4 = Tex(r"0").shift(UP*base + DOWN*offset*2 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel5 = Tex(r"0").shift(UP*base + DOWN*offset*3 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)
		qlabel6 = Tex(r"0").shift(UP*base + DOWN*offset*4 + LEFT*5.75 + DOWN*0.5).set_color(GREEN)

		itsg = Group(q1, q2, q3, q4, q5, q6, qubit1, qubit2, qubit3, qubit4, qubit5, qubit6)
		itslines = Group(l1, l2, l3, l4, l5, l6)
		itslabels = Group(qlabel1, qlabel2, qlabel3, qlabel4, qlabel5, qlabel6)
		

		qlabel7 = Tex(r"g").shift(UP*base + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel8 = Tex(r"g").shift(UP*base + DOWN*offset + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel9 = Tex(r"Out_1").shift(UP*base + DOWN*offset*2 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel10 = Tex(r"Out_2").shift(UP*base + DOWN*offset*3 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel11 = Tex(r"Out_3").shift(UP*base + DOWN*offset*4 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		qlabel12 = Tex(r"Out_4").shift(UP*base + DOWN*offset*5 + RIGHT*5.75 + UP*0.35).set_color(GREEN)
		labels = Group(qlabel7, qlabel8, qlabel9, qlabel10, qlabel11, qlabel12)
		self.play(FadeIn(itsg), FadeIn(itslines), FadeIn(labels), FadeIn(itslabels))






		#cswap gate
		cx = -2
		cnot1 = Dot(np.array([cx,base-offset,0]), fill_color=RED)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*3 + RIGHT*cx + UP*base).set_color(RED)
		cnot3 = Line(np.array([cx, base-offset, 0]), np.array([cx, -offset*3 + base, 0]))
		cnot = Group(cnot3, cnot2, cnot1, cnot22)
		self.play(FadeIn(cnot))

		#cswap2 gate
		cx2 = 0
		cnot12 = Dot(np.array([cx2,base,0]), fill_color=RED)
		cnot22 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*4 + RIGHT*cx2 + UP*base).set_color(RED)
		cnot32 = Line(np.array([cx2, base, 0]), np.array([cx2, -offset*4 + base, 0]))
		cnot99 = Group(cnot32, cnot22, cnot12, cnot222)
		self.play(FadeIn(cnot99))


		#cswap2 gate
		cx3 = 2
		cnot122 = Dot(np.array([cx3,base,0]), fill_color=RED)
		cnot222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*3 + RIGHT*cx3 + UP*base).set_color(RED)
		cnot2222 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*5 + RIGHT*cx3 + UP*base).set_color(RED)
		cnot322 = Line(np.array([cx3, base, 0]), np.array([cx3, -offset*5 + base, 0]))
		cnot992 = Group(cnot322, cnot222, cnot122, cnot2222)
		self.play(FadeIn(cnot992))

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{A}"
		dq4 = r"\ket{0}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{0}"
		self.wait(10)
		##ccnot animations
		while (x < -2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{A}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{A}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{0}"
		self.wait(0.5)
		while (x < 2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		dq4 = r"\ket{0}"
		dq5 = r"\ket{0}"
		dq6 = r"\ket{A}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		self.wait(7)





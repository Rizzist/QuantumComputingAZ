from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Boolean Algebra, Truth Tables").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class bool(Scene):
	def construct(self):
		text = Text("Boolean Algebra, Truth Tables").scale(1.0)
		self.play(FadeIn(text))
		self.wait(3)
		self.play(FadeOut(text))

		title = Text("Boolean Algebra").shift(UP*3.5)
		self.play(FadeIn(title))

		thebase = Text("Base 2").shift(DOWN*3.5)

		add0 = Tex(r"00 + 00 = 00").shift(UP*2 + LEFT*3)
		add1 = Tex(r"01 + 00 = 01").shift(UP*1 + LEFT*3)
		add2 = Tex(r"00 + 01 = 01").shift(UP*0 + LEFT*3)
		add3 = Tex(r"01 + 01 = 10").shift(UP*-1 + LEFT*3)
		allofit = Group(thebase, add0, add1, add2, add3)
		self.play(FadeIn(allofit))
		self.wait(10)
		itsavar = Tex(r"x + y").shift(RIGHT*2 + UP*2)
		self.play(FadeIn(itsavar))
		self.wait(5)
		self.play(FadeOut(allofit), FadeOut(itsavar))


		title2 = Text("Truth Table").shift(UP*3.5)
		self.play(Transform(title, title2))

		table = Tex(r"\begin{tabular}{||c c||} \hline X & Y\\ [0.5ex] \hline\hline 0 & 0 \\ \hline 0 & 1 \\ \hline 1 & 0 \\ \hline 1 & 1 \\ [1ex]  \hline \end{tabular}").shift(LEFT*5.75)
		self.play(FadeIn(table))

		table2 = Tex(r"\begin{tabular}{||c c c||} \hline X & Y & OR\\ [0.5ex] \hline\hline 0 & 0 & 0 \\ \hline 0 & 1 & 1 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 1 \\ [1ex]  \hline \end{tabular}").shift(LEFT*2.75)
		self.play(FadeIn(table2))

		table3 = Tex(r"\begin{tabular}{||c c c||} \hline X & Y & AND\\ [0.5ex] \hline\hline 0 & 0 & 0 \\ \hline 0 & 1 & 0 \\ \hline 1 & 0 & 0 \\ \hline 1 & 1 & 1 \\ [1ex]  \hline \end{tabular}").shift(RIGHT*1.125)
		self.play(FadeIn(table3))

		table4 = Tex(r"\begin{tabular}{||c c c||} \hline X & Y & XOR\\ [0.5ex] \hline\hline 0 & 0 & 0 \\ \hline 0 & 1 & 1 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ [1ex]  \hline \end{tabular}").shift(RIGHT*5.125)
		self.play(FadeIn(table4))
		self.wait(10)

		tables=Group(table, table2, table3, table4)
		self.play(FadeOut(tables))




		title3 = Text("Truth Table - CNOT").shift(UP*3.5)
		self.play(Transform(title, title3))
		cnottable = Tex(r"\begin{tabular}{||c c c c||}  \hline  X & Y & X & Y\\ [0.5ex] \hline\hline 0 & 0 & 0 & 0 \\ \hline 0 & 1 & 0 & 1 \\ \hline 1 & 0 & 1 & 1 \\ \hline 1 & 1 & 1 & 0 \\ [1ex]  \hline \end{tabular}")
		self.play(Write(cnottable))
		self.wait(7)


		title4 = Text("Truth Table - Toffoli").shift(UP*3.5)
		self.play(Transform(title, title4))
		toffolitable = Tex(r"\begin{tabular}{||c c c c c c||} \hline  X & Y & Z & X & Y & Z\\ [0.5ex] \hline\hline 0 & 0 & 0 & 0 & 0 & 0 \\ \hline 0 & 1 & 0 & 0 & 1 & 0 \\ \hline 1 & 0 & 0 & 1 & 0 & 0 \\ \hline 0 & 1 & 1 & 0 & 1 & 1 \\ \hline 1 & 0 & 1 & 1 & 0 & 1 \\ \hline 1 & 1 & 0 & 1 & 1 & 1 \\ \hline 1 & 1 & 1 & 1 & 1 & 0 \\ [1ex]  \hline \end{tabular}")
		self.play(FadeOut(cnottable), Write(toffolitable))
		self.wait(15)













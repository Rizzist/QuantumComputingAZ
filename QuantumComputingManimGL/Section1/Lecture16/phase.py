from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Toffoli, SWAP, Controlled Phase Gates").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class phase(Scene):
	def construct(self):
		text = Text("Toffoli, SWAP, Controlled Phase Gates").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
		self.play(FadeOut(text))

		title = Text("Toffoli/CCNOT - AND Gate").shift(UP*3.5)
		self.play(Write(title))

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

		itsg = Group(q1, q2, q3, qubit1, qubit2, qubit3)
		itslines = Group(l1, l2, l3)
		self.play(FadeIn(itsg), FadeIn(itslines))


		def update_cnot1(self):
			self.become(Dot(np.array([cx,base,0]), fill_color=RED))
		def update_cnot11(self):
			self.become(Dot(np.array([cx,-offset+ base,0]), fill_color=RED))
		def update_cnot2(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED))
		def update_cnot3(self):
			self.become(Line(np.array([cx, base, 0]), np.array([cx, -offset*2+ base, 0]), fill_color=RED))
		cx = 0
		cnot1 = Dot(np.array([cx,base,0]), fill_color=RED)
		cnot1.add_updater(update_cnot1)
		cnot11 = Dot(np.array([cx,-offset+ base,0]), fill_color=RED)
		cnot11.add_updater(update_cnot11)
		cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx+ base)
		cnot2.add_updater(update_cnot2)
		cnot3 = Line(np.array([cx, base, 0]), np.array([cx, -offset*2+ base, 0]))
		cnot3.add_updater(update_cnot3)
		cnot = Group(cnot1, cnot11, cnot2, cnot3)
		self.play(FadeIn(cnot))


		##ccnot animations
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq2 = r"\ket{1}"

		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"

		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"

		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)


		self.play(FadeOut(itslines), FadeOut(itsg), FadeOut(cnot))













		title2 = Text("SWAP Gate").shift(UP*3.5)
		self.play(Transform(title, title2))
		self.remove(itslines, itsg)
		itslines2 = Group(l1, l2)
		itsg2 = Group(q1, q2, qubit1, qubit2)
		self.play(FadeIn(itslines2), FadeIn(itsg2))

		def update_swap1(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(RIGHT*cx + UP*base).set_color(RED))
		def update_swap2(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(RED))
		def update_swap3(self):
			self.become(Line(np.array([cx, base, 0]), np.array([cx, -offset+ base, 0]), fill_color=RED))
		cx = 0
		swap1 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*cx+ base)
		swap1.add_updater(update_swap1)
		swap2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cx+ base)
		swap2.add_updater(update_swap2)
		swap3 = Line(np.array([cx, base, 0]), np.array([cx, -offset+ base, 0]))
		swap3.add_updater(update_swap3)
		swap = Group(swap1, swap2, swap3)
		self.play(FadeIn(swap))

		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq2 = r"\ket{1}"
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		dq2 = r"\ket{0}"
		dq1 = r"\ket{1}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		dq2 = r"\ket{1}"
		dq1 = r"\ket{0}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		dq2 = r"\ket{1}"
		dq1 = r"\ket{1}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		self.play(FadeOut(itslines2), FadeOut(itsg2), FadeOut(swap))










		title3 = Text("Controlled Phase Shift").shift(UP*3.5)
		self.play(Transform(title, title3), FadeIn(itslines2), FadeIn(itsg2))

		def update_phase1(self):
			self.become(Dot(np.array([cx,base,0]), fill_color=GREEN))
		def update_phase2(self):
			self.become(Tex(r"R_\theta").scale(1.2).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(BLACK))
		def update_phases(self):
			self.become(Square(1, color=GREEN, fill_color=GREEN, fill_opacity=1.0).shift(DOWN*offset + RIGHT*cx + UP*base))
		def update_phase3(self):
			self.become(Line(np.array([cx, base, 0]), np.array([cx, -offset+ base, 0]), fill_color=RED))
		cx = 0
		phase3 = Line(np.array([cx, base, 0]), np.array([cx, -offset+ base, 0]))
		phase3.add_updater(update_phase3)

		phase1 = Dot(np.array([cx,base,0]), fill_color=RED)
		phase1.add_updater(update_phase1)

		phases = Square(fill_color=GREEN).scale(1.2).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(GREEN)
		phases.add_updater(update_phases)

		phase2 = Tex(r"R_\theta").scale(1.2).shift(DOWN*offset + RIGHT*cx + UP*base).set_color(RED)
		phase2.add_updater(update_phase2)
		
		phase = Group(phase3, phases, phase1, phase2)
		self.play(FadeIn(phase))

		x = -5
		dq2 = r"\ket{1}"
		dq1 = r"\ket{0}"
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		dq2 = r"\ket{1}"
		dq1 = r"\ket{1}"
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		dq2 = r"e^{i\theta}\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		dq2 = r"e^{2*i\theta}\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		dq2 = r"e^{3*i\theta}\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(8)









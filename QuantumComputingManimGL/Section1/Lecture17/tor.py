from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Fredkin Gate").scale(0.7)
		self.play(FadeIn(text))
		self.wait(3)

class tor(Scene):
	def construct(self):
		text = Text("Fredkin Gate")
		self.play(FadeIn(text))
		#self.wait(3)
		text.generate_target()
		text.target = Text("Fredkin Gate/CSWAP").shift(UP*3.5)
		self.play(MoveToTarget(text))

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
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*cx + UP*base).set_color(RED))
		def update_cnot11(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cx + UP*base).set_color(RED))
		def update_cnot2(self):
			self.become(Dot(np.array([cx,base -offset*2,0]), fill_color=RED))
		def update_cnot3(self):
			self.become(Line(np.array([cx, base, 0]), np.array([cx, -offset*2+ base, 0]), fill_color=RED))
		cx = 0
		cnot1 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*cx + UP*base).set_color(RED)
		cnot1.add_updater(update_cnot1)
		cnot11 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cx + UP*base).set_color(RED)
		cnot11.add_updater(update_cnot11)
		cnot2 = Dot(np.array([cx,base -offset*2,0]), fill_color=RED)
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

		dq3 = r"\ket{1}"

		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		self.play(FadeOut(cnot))

		cxx = -1
		def update_cnot21(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cxx + UP*base).set_color(RED))
		def update_cnot22(self):
			self.become(Dot(np.array([cxx,base -offset*0,0]), fill_color=RED))
		def update_cnot23(self):
			self.become(Line(np.array([cxx, base, 0]), np.array([cxx, -offset + base, 0]), fill_color=RED))
		cnot21 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*cxx + UP*base).set_color(RED)
		cnot21.add_updater(update_cnot21)
		cnot22 = Dot(np.array([cxx,base -offset,0]), fill_color=RED)
		cnot22.add_updater(update_cnot22)
		cnot23 = Line(np.array([cxx, base, 0]), np.array([cxx, -offset+ base, 0]))
		cnot23.add_updater(update_cnot23)
		cnott = Group(cnot21, cnot22, cnot23)
		self.play(FadeIn(cnott))

		ccx = 0
		def update_cnot31(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*ccx + UP*base).set_color(RED))
		def update_cnot32(self):
			self.become(Dot(np.array([ccx,base -offset,0]), fill_color=RED))
		def update_cnot33(self):
			self.become(Line(np.array([ccx, base, 0]), np.array([ccx, -offset+ base, 0]), fill_color=RED))
		cnot31 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*0 + RIGHT*ccx + UP*base).set_color(RED)
		cnot31.add_updater(update_cnot31)
		cnot32 = Dot(np.array([ccx,base -offset,0]), fill_color=RED)
		cnot32.add_updater(update_cnot32)
		cnot33 = Line(np.array([ccx, base, 0]), np.array([ccx, -offset+ base, 0]))
		cnot33.add_updater(update_cnot33)
		cnottt = Group(cnot31, cnot32, cnot33)
		self.play(FadeIn(cnottt))

		cccx = 1
		def update_cnot41(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cccx + UP*base).set_color(RED))
		def update_cnot42(self):
			self.become(Dot(np.array([cccx,base -offset*0,0]), fill_color=RED))
		def update_cnot43(self):
			self.become(Line(np.array([cccx, base, 0]), np.array([cccx, -offset+ base, 0]), fill_color=RED))
		cnot41 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*1 + RIGHT*cccx + UP*base).set_color(RED)
		cnot41.add_updater(update_cnot41)
		cnot42 = Dot(np.array([cccx,base -offset*0,0]), fill_color=RED)
		cnot42.add_updater(update_cnot42)
		cnot43 = Line(np.array([cccx, base, 0]), np.array([cccx, -offset+ base, 0]))
		cnot43.add_updater(update_cnot43)
		cnotttt = Group(cnot41, cnot42, cnot43)
		self.play(FadeIn(cnotttt))


		x = -5

		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"

		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
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
		while (x < 1):
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

		x = -5

		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"

		while (x < -1):
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
		while (x < 1):
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

		self.wait(1)
		def update_cnot322(self):
			self.become(Dot(np.array([ccx,base -offset*2,0]), fill_color=RED))
		cnot322 = Dot(np.array([ccx,base -offset*2,0]), fill_color=RED)
		cnot322.add_updater(update_cnot322)

		def update_cnot333(self):
			self.become(Line(np.array([ccx, base, 0]), np.array([ccx, -offset*2+ base, 0]), fill_color=RED))
		cnot33.remove_updater(update_cnot33)
		cnot33.add_updater(update_cnot333)
		self.add(cnot322)

		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
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






		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		while (x < -1):
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
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 1):
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


		cnotg = Group(cnott, cnottt, cnotttt, cnot322)
		#self.play(FadeOut(itslines), FadeOut(itsg), FadeOut(cnotg))
		self.wait(8)






















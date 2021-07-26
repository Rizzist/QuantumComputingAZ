from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("V Gate, Quantum OR Gate, Peres Gate").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class v(Scene):
	def construct(self):
		text = Text("V Gate, Peres Gate, Quantum OR Gate").scale(0.9)
		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		title = Text("V Gate (Sqrt(NOT))").shift(UP*3.5)
		self.play(Write(title))

		offset = 2
		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{0}"
		def update_q1(self):
			self.become(Tex(r"" + str(dq1) + "_1").shift(RIGHT*x + UP*1))
		def update_q2(self):
			self.become(Tex(r"" + str(dq2) + "_2").shift(RIGHT*x + DOWN*offset + UP*1))
		q1 = Tex(r"\ket{0}_1").shift(LEFT*5 + UP*0.7).add_updater(update_q1)
		q2 = Tex(r"\ket{0}_2").shift(LEFT*5 + DOWN*offset + UP*0.7).add_updater(update_q2)

		l1 = Line(np.array([-5, 0, 0]), np.array([5, 0, 0]))
		l2 = Line(np.array([-5, -offset, 0]), np.array([5, -offset, 0]))

		def update_qubit1(self):
			self.become(Dot(np.array([x,0,0]),fill_color=BLUE))
		def update_qubit2(self):
			self.become(Dot(np.array([x,-offset,0]),fill_color=BLUE))

		qubit1 = Dot(np.array([x,0,0]), fill_color=BLUE)
		qubit1.add_updater(update_qubit1)
		qubit2 = Dot(np.array([x,-offset,0]), fill_color=BLUE)
		qubit2.add_updater(update_qubit2)

		itsg = Group(q1, q2, qubit1, qubit2)
		self.play(FadeIn(itsg), FadeIn(l1), FadeIn(l2))
		#cnot gate
		def update_cnot1(self):
			self.become(Dot(np.array([cx,0,0]), fill_color=RED))
		def update_cnot2(self):
			self.become(Tex(r"V").scale(1.5).set_color(BLACK).shift(DOWN*offset + RIGHT*cx))
		def update_cnot3(self):
			self.become(Line(np.array([cx, 0, 0]), np.array([cx, -offset, 0]), fill_color=RED))
		def update_cnot4(self):
			self.become(Square(fill_color=WHITE, fill_opacity=1).set_color(WHITE).scale(0.5).shift(DOWN*offset + RIGHT*cx))
		cx = 0
		cnot1 = Dot(np.array([cx,0,0]), fill_color=RED)
		cnot1.add_updater(update_cnot1)
		cnot2 = Tex(r"V").scale(1.5).set_color(BLACK).shift(DOWN*offset + RIGHT*cx)
		cnot2.add_updater(update_cnot2)
		cnot3 = Line(np.array([cx, 0, 0]), np.array([cx, -offset, 0]))
		cnot3.add_updater(update_cnot3)
		cnot4 = Square().set_color(WHITE).scale(0.5).shift(DOWN*offset + RIGHT*cx)
		cnot4.add_updater(update_cnot4)
		cnot = Group(cnot1, cnot4, cnot2, cnot3)
		self.play(FadeIn(cnot))
		self.wait(3)
		
		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"

		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)
		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{+i}"

		while (x < 0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		while (cx > -1):
			cx -= 0.1
			self.wait(0.001)

		

		cxx = 1
		def update_cnot11(self):
			self.become(Dot(np.array([cxx,0,0]), fill_color=RED))
		def update_cnot21(self):
			self.become(Tex(r"V^\dag").scale(1.5).set_color(BLACK).shift(DOWN*offset + RIGHT*cxx))
		def update_cnot31(self):
			self.become(Line(np.array([cxx, 0, 0]), np.array([cxx, -offset, 0]), fill_color=RED))
		def update_cnot41(self):
			self.become(Square(fill_color=WHITE, fill_opacity=1).set_color(WHITE).scale(0.5).shift(DOWN*offset + RIGHT*cxx))
		cnot11 = Dot(np.array([cxx,0,0]), fill_color=RED)
		cnot11.add_updater(update_cnot11)
		cnot21 = Tex(r"V^\dag").scale(1.5).set_color(BLACK).shift(DOWN*offset + RIGHT*cxx)
		cnot21.add_updater(update_cnot21)
		cnot31 = Line(np.array([cxx, 0, 0]), np.array([cxx, -offset, 0]))
		cnot31.add_updater(update_cnot31)
		cnot41 = Square().set_color(WHITE).scale(0.5).shift(DOWN*offset + RIGHT*cxx)
		cnot41.add_updater(update_cnot41)
		cnot1 = Group(cnot11, cnot41, cnot21, cnot31)
		self.play(FadeIn(cnot1))



		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"

		while (x < -1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{+i}"
		self.wait(0.5)
		while (x < 1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		dq2 = r"\ket{0}"
		self.wait(0.5)
		while (x < 5):
			x += 0.05
			self.wait(0.001)

		self.wait(5)
		notgroup = Group(cnot, cnot1, itsg, l1, l2)
		x = -5
		self.play(FadeOut(notgroup))










		title2 = Text("Peres Gate").shift(UP*3.5)
		self.play(Transform(title, title2))

		#add PERES Gate
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

		#toffolis
		def update_cnot1(self):
			self.become(Dot(np.array([cx,base,0]), fill_color=RED))
		def update_cnot11(self):
			self.become(Dot(np.array([cx,-offset+ base,0]), fill_color=RED))
		def update_cnot2(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset*2 + RIGHT*cx + UP*base).set_color(RED))
		def update_cnot3(self):
			self.become(Line(np.array([cx, base, 0]), np.array([cx, -offset*2+ base, 0]), fill_color=RED))
		cx = -1
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

		#cnot gate
		ccx = 0
		def update_cnot18(self):
			self.become(Dot(np.array([ccx,base,0]), fill_color=RED))
		def update_cnot28(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*ccx + UP*base).set_color(RED))
		def update_cnot38(self):
			self.become(Line(np.array([ccx, base, 0]), np.array([ccx, -offset+base, 0]), fill_color=RED))
		
		cnot18 = Dot(np.array([ccx,base,0]), fill_color=RED)
		cnot18.add_updater(update_cnot18)
		cnot28 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*ccx + UP*base)
		cnot28.add_updater(update_cnot28)
		cnot38 = Line(np.array([ccx, base, 0]), np.array([ccx, -offset+base, 0]))
		cnot38.add_updater(update_cnot38)
		cnot8 = Group(cnot18, cnot28, cnot38)
		self.play(FadeIn(cnot8))

		"""
		#cnot gate

		cox = 1
		def update_cnot19(self):
			self.become(Dot(np.array([cox,base-1.5,0]), fill_color=RED))
		def update_cnot29(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cox + UP*base + DOWN*1.5).set_color(RED))
		def update_cnot39(self):
			self.become(Line(np.array([cox, base-1.5, 0]), np.array([cox, -offset+base-1.5, 0]), fill_color=RED))
		
		cnot19 = Dot(np.array([cox,base-1.5,0]), fill_color=RED)
		cnot19.add_updater(update_cnot19)
		cnot29 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cox + UP*base + DOWN*1.5)
		cnot29.add_updater(update_cnot29)
		cnot39 = Line(np.array([cox, base-1.5, 0]), np.array([cox, -offset+base-1.5, 0]))
		cnot39.add_updater(update_cnot39)
		cnot9 = Group(cnot19, cnot29, cnot39)
		self.play(FadeIn(cnot9))
		"""


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
		while (x < 5):
			x += 0.05
			self.wait(0.001)


		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
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
		dq2 = r"\ket{1}"
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

		self.wait(15)











		#OR Gate
		self.play(FadeOut(cnot), FadeOut(cnot8))

		title3 = Text("Quantum OR Gate").shift(UP*3.5)
		self.play(Transform(title, title3))

		x = -5
		#cnot gate
		cox = 1
		def update_cnot19(self):
			self.become(Dot(np.array([cox,base-1.5,0]), fill_color=RED))
		def update_cnot29(self):
			self.become(Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cox + UP*base + DOWN*1.5).set_color(RED))
		def update_cnot39(self):
			self.become(Line(np.array([cox, base-1.5, 0]), np.array([cox, -offset+base-1.5, 0]), fill_color=RED))
		
		cnot19 = Dot(np.array([cox,base-1.5,0]), fill_color=RED)
		cnot19.add_updater(update_cnot19)
		cnot29 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset + RIGHT*cox + UP*base + DOWN*1.5)
		cnot29.add_updater(update_cnot29)
		cnot39 = Line(np.array([cox, base-1.5, 0]), np.array([cox, -offset+base-1.5, 0]))
		cnot39.add_updater(update_cnot39)
		cnot9 = Group(cnot19, cnot29, cnot39)
		self.play(FadeIn(cnot9))

		#peres gate
		peresText = Group(Text("Peres", color=BLACK), Text("Gate", color=BLACK)).arrange(DOWN)
		peresBox = Rectangle(color=RED, fill_color=RED, fill_opacity=1).scale(0.9).rotate(PI/2)
		peres = Group(peresBox, peresText)
		peres.shift(LEFT*2 + DOWN*0.5)
		self.play(FadeIn(peres))

		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		while (x < -2):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 1):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.025
			self.wait(0.001)





		x = -5
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		while (x < -2):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{0}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.025
			self.wait(0.001)




		x = -5
		dq1 = r"\ket{1}"
		dq2 = r"\ket{0}"
		dq3 = r"\ket{0}"
		while (x < -2):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{0}"
		self.wait(0.5)
		while (x < 1):
			x += 0.025
			self.wait(0.001)
		self.wait(0.5)
		dq1 = r"\ket{1}"
		dq2 = r"\ket{1}"
		dq3 = r"\ket{1}"
		self.wait(0.5)
		while (x < 5):
			x += 0.025
			self.wait(0.001)

		self.wait(10)








from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum RAM").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class ram(Scene):
	def construct(self):
		text = Text("Quantum RAM").scale(1.0)
		self.play(FadeIn(text))
		#self.wait(4)
		self.play(FadeOut(text))	

		title = Text("Quantum RAM").shift(UP*3.5)
		self.play(FadeIn(title))

		#encoder
		denc1 = Rectangle(fill_opacity=1, fill_color=YELLOW).rotate(PI/2).scale(1.2).set_color(YELLOW)
		denc2 = Text("Denc").set_color(BLACK)
		dencx = []
		dency = []
		rects = []
		for i in range(0, 3):
			for j in range(0, 3):
				if (i == j and j == 1):
					pass
				else:
					rects.append(Square(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.5).shift(RIGHT*i*2 + DOWN*j*2 + UP*2))
		self.add(*rects)
		for i in range(0, 3):
			for k in range(0, 3):
				if (i == k and k ==1):
					pass
				else:
					dencx.append(Line(np.array([0, ((k+3*i)+0.5)/2-2.5, 0]), np.array([2*k + 4, -2*(2-i)+2, 0])))
					dencx[i].generate_target()
		for i in range(0, 3):
			dency.append(Line(np.array([-5, (i+0.5)/2-1, 0]), np.array([0, (i+0.5)/2-1, 0])))
			dency[i].generate_target()
			dency[i].target.shift(LEFT*4)
		denc = Group(*dencx, *dency, denc1, denc2).shift(LEFT*4)
		self.play(FadeIn(denc))

		for i in range(0, 8):
			dencx[i].generate_target()

		for k in range(0, 8):
			for i in range(0, 8):
				dencx[i].target.set_color(RED)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (int(current[j]) == 1):
						dency[j].target.set_color(RED)
					else:
						dency[j].target.set_color(WHITE)
				for j in range(len(current),  3):
					dency[j].target.set_color(WHITE)
				for r in range(0, 3):
					self.play(MoveToTarget(dency[r], run_time=0.01))
				for q in range(0, 8):
					self.play(MoveToTarget(dencx[q], run_time=0.01))
				dencx[i].target.set_color(WHITE)
				current = bin(i)[2:][::-1]
				for j in range(0, len(current)):
					if (current[j] == 1):
						dency[j].target.set_color(WHITE)
				self.wait(0.1)
		self.wait(8)





















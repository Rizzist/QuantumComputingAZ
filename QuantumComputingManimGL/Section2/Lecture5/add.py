from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Adder Circuit").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class add(Scene):
	def construct(self):
		text = Text("Quantum Adder Circuit").scale(1.0)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Quantum 4-bit Adder").shift(UP*3.5)
		self.play(Write(title))

		#draw full adder
		number1 = Tex(r"X").shift(UP*2.5 + LEFT*1)
		number2 = Tex(r"Y").shift(UP*2.5 + RIGHT*1)
		number3 = Tex(r"C_{in}").shift(RIGHT*4)

		number4 = Tex(r"C_{out}").shift(LEFT*4)
		number5 = Tex(r"Sum").shift(DOWN*2.5)

		fadder1 = Rectangle(width=4, length=2, color=RED, fill_color=RED, fill_opacity=1)
		fadder2 = Text("Full Adder").set_color(BLACK)

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
		fadder.scale(0.9).shift(DOWN*1)
		self.play(FadeIn(fadder))


		firstNum = Tex(r"X = 10").shift(UP*2.5 + LEFT*1)
		secondNum = Tex(r"Y = 11").shift(UP*2.5 + RIGHT*1)
		nums = Group(firstNum, secondNum)
		self.play(FadeIn(nums))

		self.wait(3)

		firstNum2 = Tex(r"X = 10 = x_1x_0").shift(UP*2.5 + LEFT*2)
		secondNum2 = Tex(r"Y = 11 = y_1y_0").shift(UP*2.5 + RIGHT*2)
		nums2 = Group(firstNum2, secondNum2)
		self.play(Transform(nums, nums2))


		number1.generate_target()
		number2.generate_target()
		number1.target = Tex(r"x_0").shift(UP*1.1 + LEFT*0.9)
		number2.target = Tex(r"y_0").shift(UP*1.1 + RIGHT*0.9)
		self.play(MoveToTarget(number1), MoveToTarget(number2))

		self.wait(3)

		fadder.generate_target()
		fadder.target.scale(0.6).shift(RIGHT*3 + UP*1)
		self.play(MoveToTarget(fadder))



		



		#draw anotehr full addder
		#draw full adder
		number11 = Tex(r"x_1").shift(UP*2.5 + LEFT*1)
		number21 = Tex(r"y_1").shift(UP*2.5 + RIGHT*1)
		number31 = Tex(r"C_{in}").shift(RIGHT*4)

		number41 = Tex(r"C_{out}").shift(LEFT*4)
		number51 = Tex(r"Sum").shift(DOWN*2.5)

		fadder11 = Rectangle(width=4, length=2, color=RED, fill_color=RED, fill_opacity=1)
		fadder21 = Text("Full Adder").set_color(BLACK)

		input11 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input11.rotate(PI).shift(UP*1.3 + LEFT*1)

		input21 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input21.rotate(PI).shift(UP*1.3 + RIGHT*1)

		input31 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		input31.rotate(PI/2).shift(RIGHT*2.5 + DOWN*0.25)

		output11 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		output11.rotate(PI/2).shift(LEFT*2.5 + DOWN*0.25)

		output21 = Arrow(DOWN*0.5, UP*1, fill_color=WHITE)
		output21.rotate(PI).shift(DOWN*1.8)

		fadderq = Group(number11, number21, number31, number41, number51, fadder11, fadder21, input11, input21, input31, output11, output21)
		fadderq.scale(0.9).shift(DOWN*1.025).scale(0.6).shift(LEFT*2 + UP*1)
		self.play(FadeIn(fadderq))

		self.wait(3)


		#new number
		number5.generate_target()
		number51.generate_target()
		number5.target = Tex(r"z_0").shift(DOWN*1.5 + RIGHT*3)
		number51.target = Tex(r"z_1").shift(DOWN*1.5 + LEFT*2)

		number41.generate_target()
		number41.target = Tex(r"z_2").shift(LEFT*4.5)

		self.play(MoveToTarget(number5), MoveToTarget(number51), MoveToTarget(number41))

		thesummation = Tex(r"Z = 101 = z_2z_1z_0").shift(DOWN*2.5)
		self.play(Write(thesummation))

		self.wait(6)

		self.play(FadeOut(fadder), FadeOut(fadderq), FadeOut(thesummation), FadeOut(nums))






		#4 bit adder



		#draw full adder
		number4 = Tex(r"C_{out}").shift(LEFT*4)
		number5 = Tex(r"Sum").shift(DOWN*2.5)

		fadder1 = Rectangle(width=4, length=2, color=RED, fill_color=RED, fill_opacity=1)
		fadder2 = Text("Full Adder").set_color(BLACK)

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

		fadder = Group(number4, number5, fadder1, fadder2, input1, input2, input3, output1, output2)
		fadder.scale(0.3).shift(RIGHT*4.5)
		self.play(FadeIn(fadder))
		fadder2 = fadder.copy().shift(LEFT*2.5)
		fadder3 = fadder.copy().shift(LEFT*5)
		fadder4 = fadder.copy().shift(LEFT*7.5)
		self.play(FadeIn(fadder2), FadeIn(fadder3), FadeIn(fadder4))



		self.wait(12)






























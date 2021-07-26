from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Quantum Key Distribution").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
class key(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Quantum Key Distribution").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		title = Text("Quantum Key Distribution").shift(UP*3.5)
		self.play(FadeIn(title))
		
		
		stuff = []
		thesetter = Group(Tex(r"Alice").shift(LEFT*6), Tex(r"Bob").shift(RIGHT*6), Dot().shift(LEFT*4.5).scale(1), Dot().shift(RIGHT*4.5).scale(1), Dot().shift(LEFT*0.25).scale(1), Dot().shift(RIGHT*0.25).scale(1), Line(np.array([0.25, 0, 0]), np.array([4.5, 0, 0])), Line(np.array([-4.5, 0, 0]), np.array([-0.25, 0, 0])) )
		theclassicaller = Group(Dot().shift(LEFT*4.5 + UP*1).scale(1).set_color(ORANGE), Dot().shift(RIGHT*4.5 + UP*1).scale(1).set_color(ORANGE), Line(np.array([-4.5, 1, 0]), np.array([4.5, 1, 0])).set_color(ORANGE) )


		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Tex(r"\text{BB84 Protocol}").shift(UP*2.7) )
		stuff.append( thesetter.shift(UP*2)  )
		stuff.append( Group(Dot().shift(LEFT*0.25 + UP*2).scale(3).set_color(BLUE), Dot().shift(RIGHT*0.25 + UP*2).scale(3).set_color(BLUE)) )
		stuff.append( theclassicaller.shift(UP*0.5)  )
		for i in stuff:
			self.play(FadeIn(i))
		#self.play(FadeOut(Group(*stuff)))
		
		stuff2 = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff2.append( Tex(r"\text{Measure Z: } \ket{0} or \ket{1} \to \{1,-1\}").shift(DOWN*-1 + LEFT*3.5) )
		stuff2.append( Tex(r"\text{Measure X: } \ket{+} or \ket{-} \to \{1,-1\}").shift(DOWN*-1 + RIGHT*3.5) )
		stuff2.append( Tex(r"\ket{\psi} \quad \text{Measure ZZXZXX: }  \to \ket{10+1--} \to [-1, 1, 1, -1, -1, -1]").shift(DOWN*-0.3).scale(0.9) )
		stuff2.append( Tex(r"\text{Encode X and Z: } \ket{\psi} = \ket{+1-+00}").shift(DOWN*0.4) )
		stuff2.append( Tex(r"\text{Measure ZZZZZZ: } \ket{011000} \ \ \ket{110100} \ \ \ket{010100}").shift(DOWN*1.1) )
		stuff2.append( Tex(r"\text{Measure ZZZZZZ: } \ket{p1pp00} \to 100").shift(DOWN*1.8) )
		stuff2.append( Tex(r"\text{Measure XZZXZX: } \ket{+11+0-} \ \ \ket{+10+0-} \ \ \ket{+11+0+}").shift(DOWN*2.5) )
		stuff2.append( Tex(r"\text{Measure XZZXZX: } \ket{+1p+0p} \to +1+0").shift(DOWN*3.3) )
		for i in stuff2:
			self.play(FadeIn(i))
			waiter(6)
		self.play(FadeOut(Group(*stuff2)))
		






		
		step1 = Tex(r"\text{1. Encoding Qubit w/ Random Basis XZXZZZ: } \ket{-0+1-1}").shift(DOWN*-0.2)
		self.play(FadeIn(step1))
		waiter(3)

		#send qubit
		qubit = Dot().shift(LEFT*4.5 + UP*2).scale(3).set_color(RED)
		self.play(FadeIn(qubit))
		qubit.generate_target()
		qubit.target.shift(RIGHT*4.25)
		self.play(MoveToTarget(qubit))
		self.remove(stuff[-2], qubit)
		qubit.shift(RIGHT*0.5)
		self.add(qubit)
		qubit.target.shift(RIGHT*4.75)
		self.play(MoveToTarget(qubit))
		self.wait(0.5)
		self.remove(qubit)

		step2 = Tex(r"\text{2. Choose Random Basis to Measure ZXXZXZ: } \ket{-0+1-1} \to \ket{0++1-1}").shift(DOWN*0.6).scale(0.8)
		self.play(FadeIn(step2))
		waiter(7)
		step3 = Tex(r"\text{3. Send Measurement Basis via Classical Channel: } ZXXZXZ \to Alice").shift(DOWN*1.4).scale(0.9)
		self.play(FadeIn(step3))

		waiter(3)
		#send basis
		basis = Text(r"ZXXZXZ").shift(RIGHT*4.5 + UP*1.5).scale(0.7).set_color(RED)
		self.play(FadeIn(basis))
		basis.generate_target()
		basis.target.shift(LEFT*9)
		self.play(MoveToTarget(basis, run_time=10))
		self.wait(0.5)
		

		step4 = Tex(r"\text{4. Send Incorrect Basis for Removal } --XZXZ").shift(DOWN*2.2)
		self.play(FadeIn(step4))
		waiter(6)
		self.remove(basis)
		basis = Text(r"--XZXZ").shift(LEFT*4.5 + UP*1.5).scale(0.7).set_color(BLUE)
		self.add(basis)
		basis.generate_target()
		basis.target.shift(RIGHT*9)
		self.play(MoveToTarget(basis, run_time=10))
		self.wait(0.5)
		



		step5 = Tex(r"\text{5. Alice and Bob now have Secret Key: } +1-1").shift(DOWN*3)
		self.play(FadeIn(step5))
		waiter(1)
		hw = Tex(r"\text{Homework: Implement in Qiskit! }").shift(UP*1).scale(0.8)
		self.play(FadeIn(hw))

		waiter(15)










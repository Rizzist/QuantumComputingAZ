from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Deutsch's-Jozha Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class jozha(Scene):
	def construct(self):
		text = Text("Deutsch's-Jozha Algorithm").scale(1.3)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))	

		title = Text("Deutsch's-Jozha Algorithm").shift(UP*3.5)
		self.play(FadeIn(title))
		

		useless = Text("No considerable applications, ie: useless").shift(DOWN*3.5).scale(0.5)
		self.play(FadeIn(useless))
		self.wait(3)
		conceptual = Text("Conceptually Invaluable").shift(DOWN*3).scale(0.7)
		self.play(FadeIn(conceptual))
		self.wait(3)

		circuit = Text("Circuit Implements: f(x) - 1 bit").shift(UP*2.5).scale(0.8)
		self.play(FadeIn(circuit))
		circs = []
		circs.append(Tex("f_1(x) = 0").shift(LEFT*4 + UP*1.5).scale(0.8))
		circs.append(Tex("f_2(x) = 1").shift(LEFT*4 + UP*0.5).scale(0.8))
		circs.append(Tex("f_3(x) = x").shift(LEFT*4 + DOWN*0.5).scale(0.8))
		circs.append(Tex("f_4(x) = x+1").shift(LEFT*4 + DOWN*1.5).scale(0.8))
		circG = Group(*circs)
		self.play(FadeIn(circG))

		self.wait(25)

		constants1 = Tex(r"\Bigg]").shift(LEFT*2 + UP*1)
		self.play(FadeIn(constants1))
		constants2 = Tex(r"Constant Functions").shift(RIGHT*1 + UP*1)
		self.play(FadeIn(constants2))

		constants3 = Tex(r"\Bigg]").shift(LEFT*2 + DOWN*1)
		self.play(FadeIn(constants3))
		constants4 = Tex(r"Balanced Functions").shift(RIGHT*1 + DOWN*1)
		self.play(FadeIn(constants4))

		self.wait(5)

		self.play(FadeOut(constants4), FadeOut(constants2), FadeOut(constants1), FadeOut(constants3))

		circG.generate_target()
		circG.target.shift(RIGHT*9)
		self.play(MoveToTarget(circG))

		whatisF = Text("f(x) = ?").shift(LEFT*2 + UP*1).scale(0.7)
		self.play(FadeIn(whatisF))

		check1 = Tex(r"f(0) = 0 \text{ -> } f_1 \text{ or } f_3").shift(LEFT*2)
		self.play(FadeIn(check1))
		self.wait(5)
		check2 = Tex(r"f(1) = 1 \text{ -> } f_3").shift(LEFT*2 + DOWN*1)
		self.play(FadeIn(check2))
		self.wait(5)
		self.play(FadeOut(check1), FadeOut(check2))
		

		check3 = Tex(r"f(0) = 1 \text{ -> } f_2 \text{ or } f_4").shift(LEFT*2)
		self.play(FadeIn(check3))
		self.wait(5)
		check4 = Tex(r"f(1) = 1 \text{ -> } f_2").shift(LEFT*2 + DOWN*1)
		self.play(FadeIn(check4))
		self.wait(5)
		self.play(FadeOut(check3), FadeOut(check4))


		toCheck = Text("Two Classical Bits").shift(LEFT*2 + DOWN*1).scale(0.9)
		self.play(FadeIn(toCheck))

		toCheck2 = Text("Two Classical Bits = One Quantum Bit").shift(LEFT*2 + DOWN*1).scale(0.8)
		self.play(Transform(toCheck, toCheck2))

		self.wait(5)

		jozhaFriends = Group(toCheck, conceptual, useless, circG, circuit, whatisF)
		self.play(FadeOut(jozhaFriends))
	
		#make a 
		base = 1.5
		offset = 1.5
		x = -5

		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.45, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq) + "_" + str(self.n)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
				self.q = Tex(r"\ket{0}_" + str(self.n)).shift(LEFT*5 + DOWN*offset*self.n + UP*0.7+ UP*base).add_updater(update_qubit)
				self.l = Line(np.array([-5, -offset*self.n + base, 0]), np.array([5, -offset*self.n + base, 0]))
				def update_qub(self2):
					self2.become(Dot(np.array([x,base-offset*self.n,0]),fill_color=BLUE))
				self.qub = Dot(np.array([x,-offset*self.n + base,0]), fill_color=BLUE).add_updater(update_qub)
				self.qlabel1 = Tex(r"" + labelLeft).shift(UP*base + DOWN*offset*self.n + LEFT*5.75).set_color(GREEN)
				self.qlabel2 = Tex(r"" + labelRight).shift(UP*base + DOWN*offset*self.n + RIGHT*5.75).set_color(GREEN)
			def get(self):
				if (self.show==1):
					return Group(self.q, self.l, self.qub, self.qlabel1, self.qlabel2)
				else:
					return Group(self.l, self.qlabel1, self.qlabel2)

		
		qubits = []
		for i in range(0, 2):
			if (i == 0):
				qubits.append(qubit(i, 'x', 'x'))
			elif (i == 1):
				qubits.append(qubit(i, 'y', 'f(x)+y'))
			elif (i == 2):
				qubits.append(qubit(i, 'X_1', 'X_2'))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def xgate(pos,down):
			cx = pos
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot = Group(cnot2)
			return cnot
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"H").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.5).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		
		whichFunction = Tex(r"f(x) = 0").shift(DOWN*3)
		self.play(FadeIn(whichFunction))
		self.wait(10)
		self.play(FadeOut(whichFunction))


		whichFunction = Tex(r"f(x) = 1").shift(DOWN*3)
		self.play(FadeIn(whichFunction))
		g1 = cxgate(-2, 0, 1)
		g2 = xgate(0, 0)
		g3 = cxgate(2, 0, 1)
		gates = Group(g1, g2, g3)
		self.play(FadeIn(gates))
		self.wait(10)
		self.play(FadeOut(gates), FadeOut(whichFunction))


		whichFunction = Tex(r"f(x) = x").shift(DOWN*3)
		self.play(FadeIn(whichFunction))
		g2 = cxgate(0, 0, 1)
		gates = Group(g2)
		self.play(FadeIn(gates))
		self.wait(10)
		self.play(FadeOut(gates), FadeOut(whichFunction))

		whichFunction = Tex(r"f(x) = \neg x").shift(DOWN*3)
		self.play(FadeIn(whichFunction))
		g2 = xgate(-1, 0)
		g3 = cxgate(1, 0, 1)
		gates = Group(g2, g3)
		self.play(FadeIn(gates))
		self.wait(10)
		self.play(FadeOut(gates), FadeOut(whichFunction))




		oracle1 = Square(fill_color=WHITE, fill_opacity=1).scale(0.7)
		oracle2 = Tex(r"U_f").set_color(BLACK).scale(1.7)
		oracle = Group(oracle1, oracle2).scale(1.5)
		oracle.shift(UP*0.8)
		self.play(FadeIn(oracle))


		itsanoracle = Text("Oracle Function = Unknown -> Must Analyse!").shift(DOWN*2).scale(0.8)
		self.play(FadeIn(itsanoracle))
		self.wait(7)
		self.play(FadeOut(itsanoracle))

		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		self.wait(4)

		h1 = superHadamard(-3, 0.5)
		h2 = superHadamard(3, 0.5)
		self.play(FadeIn(h1))
		self.play(FadeIn(h2))

		measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.5)
		measure2 = Text('M').set_color(BLACK)
		measure= Group(measure1, measure2)
		measure.shift(RIGHT*5 + UP*1.5)
		self.play(FadeIn(measure))

		writeit = Text("Write this Circuit Down!!!").shift(DOWN*2)
		self.play(FadeIn(writeit))
		self.wait(15)

		allthestuff = Group(h1, h2, measure, writeit, oracle)

		for i in range(0, 2):
			self.remove(qubits[i].get())
		self.play(FadeOut(allthestuff))


		equation1 = Tex(r"\text{Initial State: } \ket{10}").shift(UP*2 + LEFT*4)
		self.play(FadeIn(equation1))
		self.wait(10)

		equation2 = Tex(r"\text{Hadamard Gates: } \ket{-+} = 0.5 * (\ket{00} - \ket{10} + \ket{01} - \ket{11})").shift(UP*1)
		self.play(FadeIn(equation2))
		self.wait(10)

		equation3 = Tex(r"\text{Unknown Function: } \ket{-?}= 0.5 * (\ket{f(0)0} - \ket{\tilde{f}(0)0} + \ket{f(1)1} - \ket{\tilde{f}(1)1})").scale(0.8)
		self.play(FadeIn(equation3))
		self.wait(10)

		assumption1 = Tex(r"\text{Assume f(0) = f(1) ie. Constant Function}").shift(RIGHT*2 + UP*2).scale(0.7)
		self.play(FadeIn(assumption1))
		self.wait(10)

		line = Line(np.array([-7, -0.5, 0]), np.array([7, -0.5, 0]))
		self.play(FadeIn(line))

		equation41 = Tex(r"\text{Unknown Function: } \ket{-?}= 0.5 * (\ket{f(0)0} - \ket{\tilde{f}(0)0} + \ket{f(1)1} - \ket{\tilde{f}(1)1})").shift(DOWN*1).scale(0.8)
		self.play(FadeIn(equation41))
		self.wait(10)
		equation42 = Tex(r"\text{Unknown Function: } \ket{-+}= 0.5 * (f(0) - \tilde{f}(1)) * (\ket{0} + \ket{1}) ").shift(DOWN*2).scale(0.7)
		self.play(FadeIn(equation42))
		self.wait(10)
		equation43 = Tex(r"\text{Hadamard Gates: } \ket{10}= \ket{1} * \ket{0} \text{ -> 0 means Constant, 1 query}").shift(DOWN*3).scale(0.7)
		self.play(FadeIn(equation43))
		self.wait(10)

		assumption2 = Tex(r"\text{Assume f(0) = } \tilde{f(1)} \text{ ie. Balanced Function}").shift(RIGHT*2 + UP*2).scale(0.7)
		self.play(Transform(assumption1, assumption2))
		self.wait(10)
		eqs = Group(equation41, equation42, equation43)
		self.play(FadeOut(eqs))

		equation51 = Tex(r"\text{Unknown Function: } \ket{-?}= 0.5 * (\ket{f(0)0} - \ket{\tilde{f}(0)0} + \ket{f(1)1} - \ket{\tilde{f}(1)1})").shift(DOWN*1).scale(0.8)
		self.play(FadeIn(equation51))
		self.wait(10)
		equation52 = Tex(r"\text{Unknown Function: } \ket{--}= 0.5 * (f(0) + \tilde{f}(0)) * (\ket{0} - \ket{1}) ").shift(DOWN*2).scale(0.7)
		self.play(FadeIn(equation52))
		self.wait(10)
		equation53 = Tex(r"\text{Hadamard Gates: } \ket{11}= \ket{1} * \ket{1} \text{ -> 1 means Balanced, 1 query}").shift(DOWN*3).scale(0.7)
		self.play(FadeIn(equation53))
		self.wait(10)

		
		eqgroup = Group(equation51, equation52, equation51, assumption1, line, equation3, equation2, equation1)
		self.play(FadeOut(eqgroup))
		







		#Phase Kickback
		title2 = Text("Phase Kickback").shift(UP*3.5)
		self.play(Transform(title, title2))

		qubits = []
		for i in range(0, 2):
			if (i == 0):
				qubits.append(qubit(i, '0', '?'))
			elif (i == 1):
				qubits.append(qubit(i, '1', '-'))
			elif (i == 2):
				qubits.append(qubit(i, 'X_1', 'X_2'))
			elif (i == 3):
				qubits.append(qubit(i, 'X_2', 'X_3'))
			elif (i == 4):
				qubits.append(qubit(i, 'X_3', '0'))
			elif (i == 5):
				qubits.append(qubit(i, '0', 'g'))
			else:
				qubits.append(qubit(i, '', '', 0))
			self.add(qubits[i].get())
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		had1 = hadamard(-3, 0)
		had2 = hadamard(-3, 1)

		cpp = cxgate(0, 0, 1)
		cpp2 = cxgate(-1, 0, 1)
		cpp3 = cxgate(1, 0, 1)

		had3 = hadamard(3, 0)
		had4 = hadamard(3, 1)

		gatas = Group(had1, had2, cpp, had3, had4)
		self.play(FadeIn(gatas))

		matrixRep = Tex(r"\begin{bmatrix} 0.5\\-0.5\\0.5\\-0.5 \end{bmatrix} ").shift(DOWN*2 + LEFT*2.5)
		matrixRepCNOT = Tex(r"\begin{bmatrix} 1 & 0 & 0 & 0\\ 0  & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} ").shift(DOWN*2 + LEFT*2 + LEFT*3)
		self.play(FadeIn(matrixRep))

		x = -5
		while(x<-3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} + \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)
		while(x<0):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} + \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)

		self.play(FadeIn(matrixRepCNOT))
		matrixRep2 = Tex(r"=  \begin{bmatrix} 0.5\\-0.5\\ -0.5\\0.5 \end{bmatrix} = \ket{--}").shift(DOWN*2 + RIGHT * 2 + LEFT*1)
		self.play(FadeIn(matrixRep2))

		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} - \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)
		while(x<3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)

		while(x<5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(5)
		self.play(FadeOut(cpp), FadeIn(cpp2), FadeIn(cpp3))

		x = -5
		while(x<-3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} + \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)
		while(x<-1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} - \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)
		while(x<1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"0.5*(\ket{0} + \ket{1})"
		qubits[1].dq = r"0.5*(\ket{0} - \ket{1})"
		self.wait(0.5)
		while(x<3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{1}"
		self.wait(0.5)
		while(x<5):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{1}"
		qubits[1].dq = r"\ket{1}"
		self.wait(5)


		morestufftogroup = Group(matrixRep, matrixRep2, matrixRepCNOT, gatas, cpp2, cpp3)
		for i in range(0, 2):
			self.remove(qubits[i].get())
		self.play(FadeOut(morestufftogroup))
		
		self.wait(5)
		corona1 = ImageMobject("./f1.jpeg").scale(0.5).shift(UP*2 + LEFT*4.5)
		self.play(FadeIn(corona1))
		self.wait(4)
		corona2 = ImageMobject("./f2.jpeg").scale(0.5).shift(UP*0.5 + LEFT*4.5)
		self.play(FadeIn(corona2))
		self.wait(4)
		corona3 = ImageMobject("./f3.jpeg").scale(0.7).shift(DOWN*1.5 + LEFT*4.5)
		self.play(FadeIn(corona3))
		self.wait(4)
		corona4 = ImageMobject("./f4.jpeg").scale(0.4).shift(DOWN*3 + LEFT*4.5)
		self.play(FadeIn(corona4))
		self.wait(4)


		explainIt = Text("Balanced have ODD CNOT Gates - 1 Phase Kickback").shift(RIGHT*2 + UP*1).scale(0.5)
		explainIt2 = Text("Constant have EVEN CNOT Gates - 0 or 2 Phase Kickback").shift(RIGHT*2 + DOWN*1).scale(0.5)

		self.play(FadeIn(explainIt), FadeIn(explainIt2))
		self.wait(30)



















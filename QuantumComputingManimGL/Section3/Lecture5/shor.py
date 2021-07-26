from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Shor's Algorithm").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)

class shor(Scene):
	def construct(self):
		text = Text("Shor's Algorithm").scale(1.1)
		self.play(FadeIn(text))
		self.wait(4)
		self.play(FadeOut(text))

		title = Text("Number Theory").shift(UP*3.5)
		self.play(Write(title))

		review = []
		review.append( Text("Euclidean Algorithm").shift(UP*2.5).scale(0.8) )
		review.append( Text("Modulo Groups - Periodic").shift(UP*1.25).scale(0.8) )
		review.append( Text("Quantum Fourier Transform").shift(DOWN*0).scale(0.8) )
		review.append( Text("Continued Fractions").shift(DOWN*1.25).scale(0.8) )
		review.append( Text("RSA Encryption").shift(DOWN*2.5).scale(0.8) )

		for i in review:
			self.play(FadeIn(i))
			self.wait(5)
		self.wait(5)
		self.play(FadeOut(Group(*review)))

		title2 = Text("Shor's Algorithm").shift(UP*3.5)
		self.play(Transform(title, title2))
		nums = []
		nums.append( Tex(r"N = p \cdot q").shift(UP*2.8) )
		nums.append( Tex(r"g - guess").shift(UP*2.3) )
		nums.append( Tex(r"gcd(g, N) - \text{ Euclidean Algorithm (most likely not factor) } = 1").shift(UP*1.8).scale(0.8) )
		nums.append( Tex(r"p \mid g^p \equiv 1 \mod N").shift(UP*1) )

		for i in nums:
			self.play(FadeIn(i))
			self.wait(10)

		self.wait(5)
		self.play(FadeOut(Group(*nums)))
		corona = ImageMobject("./modgroup.png").scale(2)
		self.play(FadeIn(corona))
		self.wait(50)
		self.play(FadeOut(corona))
		self.play(FadeIn(Group(*nums)))

		nums.append( Tex(r"g^p - 1 \equiv 0 \mod N \to \text{ Restart if p is odd}").shift(UP*0) )
		nums.append( Tex(r"(g^{p/2} - 1)(g^{p/2} + 1) \equiv 0 \mod N").shift(DOWN*1) )
		nums.append( Tex(r"gcd((g^{p/2} - 1), N)=p \ \ \ \ \ \ \ gcd((g^{p/2} + 1), N)=q").shift(DOWN*2) )
		nums.append( Tex(r"\text{Non Trivial Factors: }N = p \cdot q - \text{We are done!}").shift(DOWN*3) )

		for i in nums[4:]:
			self.play(FadeIn(i))
			self.wait(10)

		diff = SurroundingRectangle(nums[3])
		self.play(ShowCreation(diff))
		self.wait(10)
		self.play(FadeOut(Group(*nums, diff)))

		title3 = Text("Shor's Algorithm - Caveats").shift(UP*3.5)
		self.play(Transform(title, title3))



		cavs = []
		cavs.append( Text("Must contain atleast 2 periods").shift(UP*2.5).scale(0.5) )
		
		for i in cavs:
			self.play(FadeIn(i))
		

		axes = Axes(x_range=(0, 15), y_range=(0, 5, 1), height=3, width=10, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(DOWN*0.5).scale(0.8)

		self.play(FadeIn(axes))
		
		graphdots = []
		for i in range(0, 5):
			dot = Dot(color=RED)
			dot.move_to(axes.c2p(i, i))
			graphdots.append(dot)
		for i in range(5, 10):
			dot = Dot(color=RED)
			dot.move_to(axes.c2p(i, i-5))
			graphdots.append(dot)
		for i in range(10, 15):
			dot = Dot(color=RED)
			dot.move_to(axes.c2p(i, i-10))
			graphdots.append(dot)

		self.play(FadeIn(Group(*graphdots)))
		self.wait(20)
		self.play(FadeOut(Group(*graphdots, axes)))


		cavs.append( Tex(r"M \mid N^2 \leq M \leq 2*N^2").shift(UP*1.5))
		cavs.append( Tex(r"M = 2^q").shift(UP*0.5))
		cavs.append( Text("q - # of qubits").shift(DOWN*0.5))
		cavs.append( Text("RSA - 1000+ qubits - not including error correction").shift(DOWN*1.5).scale(0.5) )
		for i in cavs[1:]:
			self.play(FadeIn(i))
			self.wait(10)
		self.wait(10)
		self.play(FadeOut(Group(*cavs)))



		#apply circuit
		title4 = Text("Shor's Algorithm - Circuit Implementation").shift(UP*3.5)
		self.play(Transform(title, title4))

		#make a 
		base = 2
		offset = 0.6
		x = -5
		class qubit():
			def __init__(self,m, labelLeft, labelRight, upper=0.0, show=1):
				self.n = m
				self.show = show
				self.dq = r"\ket{0}"
				self.upper = upper
				def update_qubit(self2):
					self2.become(Tex(r"" + str(self.dq)).shift(RIGHT*x + UP*0.3 + UP*base + DOWN*offset*self.n + UP*self.upper).scale(0.7))
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
		for i in range(0, 8):
			if (i == 0):
				qubits.append(qubit(i, 'A', ''))
			elif (i == 1):
				qubits.append(qubit(i, 'B', ''))
			elif (i == 2):
				qubits.append(qubit(i, 'C', ''))
			elif (i == 3):
				qubits.append(qubit(i, 'E', ''))
			elif (i == 7):
				qubits.append(qubit(i, '1', ''))
			else:
				qubits.append(qubit(i, '0', ''))
			self.add(qubits[i].get())
		
		
		def cxgate(pos,up, down):
			cx = pos
			cnot1 = Dot(np.array([cx,base-offset*up,0]), fill_color=RED)
			cnot2 = Tex(r"\otimes").scale(1.5).shift(DOWN*offset*down + RIGHT*cx + UP*base).set_color(RED)
			cnot3 = Line(np.array([cx, base-offset*up, 0]), np.array([cx, -offset*down + base, 0]))
			cnot = Group(cnot1, cnot2, cnot3)
			return cnot
		def xgate(pos,down, on=1):
			hx = pos
			h2 = Tex(r"X").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=GREEN, fill_opacity=on, color=GREEN).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def superHadamard(pos,down):
			hx = pos
			h2 = Tex(r"H^{\otimes 2}").scale(1.5).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.8).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2).scale(1.5)
			return hadamard
		def hadamard(pos,down):
			hx = pos
			h2 = Tex(r"H").scale(1).shift(DOWN*offset*down + RIGHT*hx + UP*base).set_color(BLACK)
			h3 = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).scale(0.325).shift(DOWN*offset*down + RIGHT*hx + UP*base)
			hadamard = Group(h3, h2)
			return hadamard
		def measure(pos, down):
			measure1 = Square(fill_color=BLUE, fill_opacity=1, color=BLUE).scale(0.2)
			measure2 = Text('M').set_color(BLACK).scale(0.6)
			measure= Group(measure1, measure2)
			measure.shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return measure
		def gCGate(pos, up, down, control, color):
			vx = pos
			vnot1 = Dot(np.array([vx,base-offset*up,0]), fill_color=BLACK)
			vnot2 = Tex(r"" + control).scale(1.1).shift(DOWN*offset*down + RIGHT*vx + UP*base).set_color(BLACK)
			vnot3 = Line(np.array([vx, base-offset*up, 0]), np.array([vx, -offset*down + base, 0]))
			vnot4 = Square(fill_color=color, fill_opacity=1, color=color).scale(0.325).shift(DOWN*offset*down + RIGHT*vx + UP*base)
			vnot = Group(vnot3, vnot4, vnot1, vnot2)
			return vnot
		def qftdag(pos, depth, down):
			qft1 = Rectangle(width=2, height=offset*down*depth + 0.5, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
			qft2 = Tex(r"QFT^\dag").scale(1.2).set_color(BLACK)
			qft = Group(qft1, qft2).shift(DOWN*offset*down + RIGHT*pos + UP*base)
			return qft
		def gCGateN(pos, up, down, control, color, depth):
			qft1 = Rectangle(width=0.5, height=offset*(down)*depth + 0.5, color=color, fill_color=color, fill_opacity=1).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			qft2 = Tex(r"" + control).scale(0.75).set_color(BLACK).shift(DOWN*offset*down*1.375 + RIGHT*pos + UP*base)
			vnot1 = Dot(np.array([pos,base-offset*up,0]), fill_color=BLACK)
			vnot3 = Line(np.array([pos, base-offset*up, 0]), np.array([pos, -offset*down + base, 0]))
			qft = Group(vnot1, vnot3, qft1, qft2)
			return qft

		gates = []
		gates.append( xgate(-4.25, 7) )
		for i in range(0, 4):
			gates.append( hadamard(-4.25, i) )
		for i in range(0, 1):
			gates.append( gCGateN(-3.5, 0, 4, r'U_f^a', PURPLE, 0.7) )
		for i in range(0, 2):
			gates.append( gCGateN(-2.75 + 3*i/4, 1, 4, r'U_f^a', PURPLE, 0.7) )
		for i in range(0, 4):
			gates.append( gCGateN(-1.25 + 3*i/4, 2, 4, r'U_f^a', PURPLE, 0.7) )
		#gates.append( gCGateN(-1.25 + 9/4, 2, 4, r'U_{f_4}', PURPLE, 0.7) )
		gates.append( gCGateN(1.75, 3, 4, r'U_{f_8}^a', PURPLE, 0.7) )
		self.play(FadeIn(Group(*gates)))


		qft = qftdag(3.5, 2, 1.5)
		self.play(FadeIn(qft))

		gatesm = []
		for i in range(0, 4):
			gatesm.append( measure(5, i) )
		self.play(FadeIn(Group(*gatesm)))
		self.wait(5)
		x = -5
		qubits[0].dq = r"\ket{0}"
		qubits[1].dq = r"\ket{0}"
		qubits[2].dq = r"\ket{0}"
		qubits[3].dq = r"\ket{0}"
		self.wait(15)
		while(x < -4.25):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		qubits[3].dq = r"\ket{+}"
		qubits[7].dq = r"\ket{1}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*1):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)
		while(x < -4.25 + 0.75*2):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^\theta}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)

		while(x < -4.25 + 0.75*3):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+}"
		self.wait(0.5)

		for i in range(4, 8):
			while(x < -4.25 + 0.75*i):
				x += 0.05
				self.wait(0.001)
			self.wait(0.5)
			qubits[0].dq = r"\ket{+^\theta}"
			qubits[1].dq = r"\ket{+^{2\theta}}"
			qubits[2].dq = r"\ket{+^{"+ str(i-3) + r"\theta}}"
			self.wait(0.5)
		while(x < -4.25 + 0.75*8):
			x += 0.05
			self.wait(0.001)
		self.wait(0.5)
		qubits[0].dq = r"\ket{+^\theta}"
		qubits[1].dq = r"\ket{+^{2\theta}}"
		qubits[2].dq = r"\ket{+^{4\theta}}"
		qubits[3].dq = r"\ket{+^{8\theta}}"
		self.wait(0.5)
		while(x < 3.5):
			x += 0.05
			self.wait(0.001)

		frame = self.camera.frame
		frame.generate_target()
		self.play(MoveToTarget(frame, run_time=2.0))
		steps = []
		steps.append(  Tex(r"\text{1. Create Unitary Matrix U: } U_a\ket{1} = \ket{a \mod N}").shift(DOWN*3)  )
		steps.append(  Tex(r"f(x) = a^x \mod N").shift(DOWN*4)  )
		#
		steps.append(  Tex(r"\text{2. Initialize Register: } \ket{0}^q \ \ \ \ \ \ket{1}\ket{0}^{n-1}").shift(DOWN*5)   )
		steps.append(  Tex(r"\text{3. Put q qubits into Superposition: } \frac{1}{2^{(q/2})}\bigotimes_{k=0}^{q} \ket{+}").shift(DOWN*6)   )
		steps.append(  Tex(r"\text{4. Perform Multiplication: } \frac{1}{2^{(q/2})}\bigotimes_{k=0}^{q} \big( \ket{0} + e^{2\pi i \theta 2^k}\ket{1} \big)").shift(DOWN*7.5)   )
		steps.append(  Tex(r"\text{5. Inverse QFT: } \frac{1}{2^q} \sum_{x=0}^{2^q-1}\sum_{k=0}^{2^q-1} \omega_{2^q}^{k(2^q\theta-x)} \ket{x}").shift(DOWN*9)   )
		steps.append(  Tex(r"\text{6. Measure Phase: } \theta = x/2^q").shift(DOWN*11)   )
		steps.append(  Tex(r"\text{How is } \theta \text{ related to Period?}").shift(DOWN*13)   )

		for i in steps:
			frame.target.shift(DOWN*1.33)
			self.play(MoveToTarget(frame, run_time=2.0))
			self.play(FadeIn(i))
			self.wait(10)
		frame.target.shift(UP*1.33*7)
		self.play(MoveToTarget(frame, run_time=2.0))
		self.play(FadeOut(Group(*steps)))

		omg = []
		omg.append( Tex(r"\omega_p \propto \theta").shift(DOWN*3))
		omg.append(  Tex(r"\theta \to Frac(\theta) \to \text{Denominator: }Frac(\theta)").shift(DOWN*4))

		for i in omg:
			self.play(FadeIn(i))
			self.wait(10)
		self.wait(50)







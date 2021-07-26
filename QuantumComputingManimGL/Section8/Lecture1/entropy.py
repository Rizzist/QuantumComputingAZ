from manimlib import *
import numpy as np
import random

class FirstScene(Scene):
	def construct(self):
		text = Text("Types of Entropy and Mutual Information").scale(0.9)
		self.play(FadeIn(text))
		self.wait(3)
interupdate = False
cy = 0
pvy = 1/1000
class entropy(Scene):
	def construct(self):
		wait = True
		def waiter(n):
			if (wait == True):
				self.wait(n)
		text = Text("Types of Entropy and Mutual Information").scale(1.0)
		self.play(FadeIn(text))
		waiter(4)
		self.play(FadeOut(text))
		#print(YELLOW)
		title = Text("Entropy").shift(UP*3.5)
		self.play(FadeIn(title))
		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*2) )
		stuff.append( Text(r"- Measure of how disorderly a system is").shift(UP*2.6).scale(0.7) )
		stuff.append( Text(r"- Availability of Thermal Energy for Mechanical Work").shift(UP*1.8).scale(0.7) )
		stuff.append( Tex(r"\text{Von Neumann Entropy: } S = k_b \ln (\Omega)").shift(UP*1) )
		stuff.append( Tex(r"\Omega = \text{\# of Microstates} \quad k_b = \text{Boltzman Constant}").shift(UP*0.2) )
		stuff.append( Tex(r"\text{Shannon Entropy: } S = -\sum_{i=1}^{n} P(x_i) \log P(x_i)").shift(DOWN*1) )
		stuff.append( Tex(r"\rho = \text{Density Matrix}").shift(DOWN*1.8) )
		stuff.append( Tex(r"\text{Von Neumann Quantum Entropy: } S = -k_b Tr(\rho \ln (\rho))").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))


		#GRAPH OF x * ln(x)
		axes = Axes(x_range=(0.000001, 1, 0.2), y_range=(-0.1, 0.5, 0.25), height=5, width=5, axis_config={"stroke_color": GREY_A, "stroke_width": 2, }, y_axis_config={"include_tip": False, } ) 
		axes.add_coordinate_labels(font_size=20, num_decimal_places=1, )
		axes.shift(DOWN*0.2).scale(1.0)

		self.play(FadeIn(axes))
		func = lambda t : -1*math.log(t) * t
		sin_graph = axes.get_graph(func, color='#FFFF00', step_size=0.01, ) 
		self.play(ShowCreation(sin_graph))
		obj = Tex(r"y = -x \ln (x)").shift(UP*2.5)
		self.play(FadeIn(obj))
		waiter(5)
		self.play(FadeOut(Group(obj, axes, sin_graph)))

		boundLR = [-1, 1]
		boundUD = [-2, 2]
		objUD = [0.5, 1]
		class ball():
			def __init__(self, x, y, vx, vy):
				self.x = x
				self.y = y
				self.vx = vx
				self.vy = vy
				self.col = 250
				def update_qub(self2):
					speedX = 50
					speedY = 10
					self.x += self.vx/speedX
					self.y += self.vy/speedY
					self.col = int(150*(self.vy*self.vy)**(0.5)) + 16 + 60
					if (self.col > 230):
						self.col = 230
					if (self.col < 17):
						self.col = 17
					if (self.x < boundLR[0]):
						self.vx = -self.vx
					if (self.x > boundLR[1]):
						self.vx = -self.vx
					if (self.y < boundUD[0]):
						self.vy = -self.vy
					if (self.y > boundUD[1]):
						self.vy = -self.vy
					if (self.y < objUD[1] + cy and self.y > objUD[0] + cy):
						self.vy = -self.vy
						if (self.y < objUD[1] + cy and self.y > (objUD[0] + objUD[1])*0.5 + cy ):
							self.y = objUD[1] + cy + 0.01
						else:
							self.y = objUD[0] + cy - 0.01
						
						global pvy
						if (pvy*self.vy > 0):
							self.vy *= 1.1
							if (self.vy > 1):
								self.vy = 1
						else:
							self.vy *= 0.9
							if (self.vy > 1):
								self.vy = 1
						
						if ( np.abs(self.y -  objUD[0] - cy) < np.abs(self.y -  objUD[1] - cy) ):
							pvy += 1/1000
						else:
							pvy -= 1/1000
					self2.become(Dot(np.array([self.x,self.y,0]),fill_color='#' + hex(self.col)[2:] + '00'  + hex(254-self.col)[2:]) )
				self.drawDot = Dot(np.array([self.x,self.y,0]),fill_color=BLUE).add_updater(update_qub)
			def get(self):
				return Group(self.drawDot)
		backer = Rectangle(width=boundLR[1]-boundLR[0], height=boundUD[1] - boundUD[0], fill_color=WHITE, fill_opacity=1.0 )
		self.play(FadeIn(backer))

		
		def update_piston(self2):
			global interupdate, cy
			if (interupdate == False):
				self2.y = cy
				interupdate = True
			self2.pvy = pvy
			self2.y += self2.pvy/10
			cy = self2.y
			self2.become(Rectangle(width=boundLR[1]-boundLR[0], height=objUD[1] - objUD[0], fill_color=GREY, fill_opacity=1.0 ).shift(UP*(objUD[1] + objUD[0])*0.5 + UP*self2.y) )
		piston = Rectangle(width=boundLR[1]-boundLR[0], height=objUD[1] - objUD[0], fill_color=GREY, fill_opacity=1.0 ).shift(UP*(objUD[1] + objUD[0])*0.5)
		piston.add_updater(update_piston)
		self.play(FadeIn(piston))

		balls = []
		for i in range(10):
			balls.append( ball(random.randint(-10, 10)/20, random.randint(-100, 0)/100 - 1, random.randint(-100, 100)/100, random.randint(-100, 100)/300) )
		for i in range(10):
			balls.append( ball(random.randint(-10, 10)/20, random.randint(0, 100)/100 + 1, random.randint(-100, 100)/100, random.randint(-100, 100)/100) )
		for i in balls:
			self.add(i.get())
		self.wait(5)
		waiter(60*4)

		self.play(FadeOut(Group(piston, backer)))
		for i in balls:
			self.remove(i.get())

		







		title2 = Text("Self-Information & Conditional Entropy").shift(UP*3.5)
		self.play(Transform(title, title2))

		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*0) )
		stuff.append( Tex(r"\text{Self-Information: } I(x) = -\log (P(x))").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Entropy: } H(X) = E(I(x)) \to x \in X").shift(UP*1.5) )
		stuff.append( Tex(r"H(X) = -\sum_{x \in X} P(X = x)I(x)").shift(UP*0.5) )
		stuff.append( Tex(r"\text{Given y, what is Entropy of X?}").shift(DOWN*0.5) )
		stuff.append( Tex(r"H(X \mid Y = y) = -\sum_{x \in X} P(X = x \mid Y = y) * \log (P(X = x \mid Y = y))").shift(DOWN*1.5) )
		stuff.append( Tex(r"H(X \mid Y) = \sum_{x \in X} P(X = x) * H(X \mid Y = y)").shift(DOWN*3) )

		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(5)
		self.play(FadeOut(Group(*stuff)))




		title3 = Text("Quantum Mutual Information").shift(UP*3.5)
		self.play(Transform(title, title3))

		stuff = []
		stuff.append( Tex(r"I(X, Y) = H(X) - H(X \mid Y)").shift(UP*2.5) )
		stuff.append( Tex(r"I(X, Y) = H(Y) - H(Y \mid X)").shift(UP*1.5) )
		stuff.append( Tex(r"I(X, Y) = H(X, Y) - H(X \mid Y) - H(Y \mid X)").shift(UP*0.5) )
		stuff.append( Tex(r"I(X, Y) = H(X) + H(Y) - H(X,Y)").shift(DOWN*0.5) )
		stuff.append( Tex(r"\text{Independent Variables: } H(X \mid Y) = H(X)").shift(DOWN*1.5) )
		stuff.append( Tex(r"\text{Independent Variables: } I(X, Y) = 0").shift(DOWN*2.5) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		self.play(FadeOut(Group(*stuff)))

		corona = ImageMobject("./entropyk.png").shift(DOWN*1).scale(2)
		self.play(FadeIn(corona))
		waiter(15)
		self.play(FadeOut(corona))











		
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*0) )
		stuff.append( Tex(r"I(X, Y) = H(X) + H(Y) - H(X,Y)").shift(UP*2.5) )
		stuff.append( Tex(r"\text{Von Neumann Quantum Entropy: } H(\rho ) = -Tr(\rho \ln (\rho)) = E(I(\rho))").shift(UP*1.5) )
		stuff.append( Tex(r"\text{Partial Trace: } \rho^A = Tr_B(\rho^{AB})").shift(UP*0.5) )
		stuff.append( Tex(r"H(\rho^A) = -Tr(Tr_B (\rho^{AB}) \ln (Tr_B (\rho^{AB}))) = E(I(Tr_B (\rho^{AB})))  ").shift(DOWN*1.5) )
		stuff.append( Tex(r"I(\rho^A, \rho^B) = H(\rho^A) + H(\rho^B) - H(\rho^A,\rho^B)").shift(DOWN*2.5) )


		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))



		title3 = Text("Entropy Example").shift(UP*3.5)
		self.play(Transform(title, title3))
		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*0) )
		stuff.append( Tex(r"S(\rho) = -Tr(\rho \log(\rho))").shift(UP*2.5 + LEFT*4) )
		stuff.append( Tex(r"S(\rho) = -\sum_i \lambda_i \log(\lambda_i)").shift(UP*2.5 + RIGHT*4) )
		stuff.append( Tex(r"\rho_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \to \lambda_i = \{ 0, 1 \}").shift(UP*1.5) )
		stuff.append( Tex(r"S(\rho_0) = - 0 - \log(1) = 0 \to \text{Certain State}").shift(UP*0.5) )
		stuff.append( Tex(r"\rho_\psi = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \to \lambda_i = \{ \frac{3-5^{(0.5})}{6}, \frac{3+5^{(0.5})}{6} \}").shift(DOWN*1.5) )
		stuff.append( Tex(r"S(\rho_\psi) = 0.37858514452 + 0.17146261506 \approx \text{0.55 bits}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		self.play(FadeOut(Group(*stuff)))








		stuff = []
		#stuff.append( Tex(r"").shift(DOWN*0) )
		stuff.append( Tex(r"S(\rho) = -Tr(\rho \log(\rho))").shift(UP*2.5 + LEFT*4) )
		stuff.append( Tex(r"\ket{\psi} = \frac{1}{\sqrt{(2})}\ket{01} + \frac{1}{\sqrt{(2})}\ket{10}").shift(UP*2.5 + RIGHT*4) )
		stuff.append( Tex(r"\rho_a = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix} \to \lambda_i = \{ \frac{1}{2}, \frac{1}{2} \}").shift(UP*0.8) )
		stuff.append( Tex(r"S(\rho_a) = -\frac{1}{2} \log(\frac{1}{2}) - \frac{1}{2} \log(\frac{1}{2}) = -\log(\frac{1}{2})").shift(DOWN*0.4) )
		stuff.append( Tex(r"S(\rho_a) = \text{1 bit} = S(\rho_b)").shift(DOWN*1.9) )
		stuff.append( Tex(r"S(\rho_a) + S(\rho_b) = \text{2 bits}").shift(DOWN*3) )
		for i in stuff:
			self.play(FadeIn(i))
			waiter(10)
		waiter(10)
		#self.play(FadeOut(Group(*stuff)))

		self.wait()


















from manimlib import *
import numpy as np

class FirstScene(Scene):
	def construct(self):
		text = Text("Bloch Sphere").scale(0.8)
		self.play(FadeIn(text))
		self.wait(3)

class Bloch(Scene):
	def construct(self):
		text = Text("Bloch Sphere").scale(2)
		self.play(FadeIn(text))
		self.wait(3)
		self.play(FadeOut(text))
		
		#explain why we can represent in 3D
		title = Text("Why 3D?").shift(UP*3.5)
		self.play(Write(title))
		self.wait(3)
		represent = Tex(r"a + bi = \{R_1, \theta\}").shift(UP)
		self.play(FadeIn(represent))
		self.wait(3)
		represent2 = Tex(r"c + di = \{R_2, \phi\}")
		self.play(FadeIn(represent2))
		self.wait(3)

		represent3 = Tex(r"(\mid R_1 \mid)^2 + (\mid R_2 \mid)^2 = 1").shift(DOWN)
		self.play(FadeIn(represent3))
		self.wait(3)

		represent2.generate_target()
		represent2.target = Tex(r"c + di = \{\sqrt{1-R_1^2}, \phi\}")
		self.play(MoveToTarget(represent2))
		self.wait(3)

		represent3.generate_target()
		represent3.target = Tex(r"f(R, \theta, \phi)").shift(DOWN)
		self.play(MoveToTarget(represent3))
		self.wait(3)

		stuffgroup = Group(title, represent, represent2, represent3)
		self.play(FadeOut(stuffgroup))
		

		frame = self.camera.frame

		frame.set_euler_angles(
			theta=-10 * DEGREES,
			phi=50 * DEGREES,
		)

		frame.set_width(6)
		sphere = Sphere(radius = 1, point=ORIGIN, color=RED)
		sphereMesh = SurfaceMesh(sphere, resolution=(7, 7), flat_stroke=True, color=GREY)

		labelpX = Tex(r'\ket{-}').shift(RIGHT*1.5)
		labelrX = Tex(r'\ket{+}').shift(LEFT*1.5)

		labelpY = Tex(r'\ket{-i}').shift(UP*1.5)
		labelrY = Tex(r'\ket{+i}').shift(DOWN*1.5)

		labelpZ = Tex(r'\ket{0}').rotate(PI/2, axis=RIGHT).shift(OUT*1.5)
		labelrZ = Tex(r'\ket{1}').rotate(PI/2, axis=RIGHT).shift(IN*1.5)

		x = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), fill_color=GREY_E, color=GREY_E)
		y = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), fill_color=GREY_E, color=GREY_E)
		z = Line(np.array([0, 0, -1]), np.array([0, 0, 1]), fill_color=GREY_E, color=GREY_E)
		#self.add_fixed_in_frame_mobjects(labelX, labelY, labelZ)

		self.play(ShowCreation(sphere))
		self.play(ShowCreation(sphereMesh))
		self.play(FadeIn(labelpX), FadeIn(labelpY), FadeIn(labelpZ), FadeIn(labelrX), FadeIn(labelrY), FadeIn(labelrZ), FadeIn(x), FadeIn(y), FadeIn(z))
		self.play(FadeOut(sphere))

		self.play(
			frame.increment_phi, -10 * DEGREES,
			frame.increment_theta, -20 * DEGREES,
			run_time=1
		)
		
		#
		self.wait(1)
		#SHOW VECTOR ON SPHERE
		vect = Vector(direction=[0, 0, 1])
		self.play(FadeIn(vect))
		vect.generate_target()
		vect.target = Vector(direction=[0, 0, -1])
		self.play(MoveToTarget(vect))
		vect.target = Vector(direction=[0, 0, 1])
		self.play(MoveToTarget(vect))
		line =  DashedLine(np.array([-1.2, 1.2, 0]), np.array([1.2, -1.2, 0]), color=RED).rotate(3*PI/2, LEFT)
		self.wait()
		qgroup = Group(sphereMesh, labelpZ, labelrZ, labelrY, labelpY, labelrX, labelpX, line, vect)

		frame.generate_target()
		frame.target.set_width(7)
		gate = Text("Hadamard").shift(UP*2.5)
		self.play(MoveToTarget(frame), FadeIn(gate))
		self.play(ShowCreation(line))
		self.wait(3)
		frame.target.set_euler_angles(
			theta=60 * DEGREES,
			phi=30 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		frame.target.set_euler_angles(
			theta=160 * DEGREES,
			phi=30 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		frame.target.set_euler_angles(
			theta=160 * DEGREES,
			phi=150 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		frame.target.set_euler_angles(
			theta=-40 * DEGREES,
			phi=40 * DEGREES,
		)
		self.play(MoveToTarget(frame))
		self.wait(3)
		#move vector
		#vect.target.rotate_about_origin(PI, np.array([1, 0, -1]))
		#self.play(MoveToTarget(vect))
		frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))
		r = 0
		def update_vector(self):
			self.become(Vector(direction=[0, 0, 1]).rotate_about_origin(r, np.array([1, 0, -1])))
		vect.add_updater(update_vector)

		#PATH UPDATOR
		line2 = Line(ORIGIN,vect.get_end())
		# Path
		path = VMobject(color=BLUE)
		# Path can't have the same coord twice, so we have to dummy point
		path.set_points_as_corners([vect.get_end(),vect.get_end()+UP*0.001])
		# Path group
		path_group = VGroup(line2,path)

		def update_group(group):
			l,previus_path = group
			old_path = path.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect.get_end())
			path.become(old_path)
		self.add(path_group)
		self.wait(2)
		n = 10
		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group(path_group)
			self.wait(0.0001)
		self.wait(6)
		while(i<2*n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group(path_group)
			self.wait(0.0001)
		self.wait(6)
		#the results:
		hr = Tex(r"H\ket{0} = \ket{+}").rotate(PI).shift(DOWN*2.3)
		self.play(Write(hr))
		self.wait(3)
		hr.generate_target()
		hr.target = Tex(r"H\ket{+} = \ket{0}").rotate(PI).shift(DOWN*2.3)
		self.play(MoveToTarget(hr))
		self.wait(3)
		self.play(FadeOut(hr))
		
		vect2 = Vector(direction=[0, 0, -1])
		self.remove(vect)
		self.play(FadeIn(vect2))
		
		def update_vector2(self):
			self.become(Vector(direction=[0, 0, -1]).rotate_about_origin(r, np.array([1, 0, -1])))
		vect2.add_updater(update_vector2)

		#PATH UPDATOR
		line3 = Line(ORIGIN,vect2.get_end())
		# Path
		path2 = VMobject(color=GREEN)
		# Path can't have the same coord twice, so we have to dummy point
		path2.set_points_as_corners([vect2.get_end(),vect2.get_end()+UP*0.001])
		# Path group
		path_group2 = VGroup(line3,path2)
		def update_group2(group):
			l,previus_path = group
			old_path = path2.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect2.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect2.get_end())
			path2.become(old_path)
		self.add(path_group2)
		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group2(path_group2)
			self.wait(0.0001)
		self.wait(3)
		while(i<2*n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group2(path_group2)
			self.wait(0.0001)
		self.wait(3)
		hr2 = Tex(r"H\ket{1} = \ket{-}").rotate(3*PI/2).shift(RIGHT*2.3)
		self.play(Write(hr2))
		self.wait(3)
		hr2.generate_target()
		hr2.target = Tex(r"H\ket{-} = \ket{1}").rotate(3*PI/2).shift(RIGHT*2.3)
		self.play(MoveToTarget(hr2))
		self.wait(3)
		self.play(FadeOut(hr2))
		frame.target.set_euler_angles(
			theta=-40 * DEGREES,
			phi=40 * DEGREES,
		)
		self.play(FadeOut(path_group), FadeOut(path_group2))
		self.play(MoveToTarget(frame))
		gate.generate_target()
		gate.target = Tex(r"Pauli X: \sigma_x").shift(UP*2.5)
		self.play(MoveToTarget(gate))

		#make line
		line.generate_target()
		line.target =  DashedLine(np.array([1, 0, 0]), np.array([-1, 0, 0]), color=RED)
		self.play(MoveToTarget(line))

		#PATH UPDATOR
		line4 = Line(ORIGIN,vect2.get_end())
		# Path
		path3 = VMobject(color=BLUE)
		# Path can't have the same coord twice, so we have to dummy point
		path3.set_points_as_corners([vect2.get_end(),vect2.get_end()+UP*0.001])
		# Path group
		path_group3 = VGroup(line4,path3)
		def update_group3(group):
			l,previus_path = group
			old_path = path3.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect2.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect2.get_end())
			path3.become(old_path)
		self.add(path_group3)

		vect2.remove_updater(update_vector2)
		def update_vector3(self):
			self.become(Vector(direction=[0, 0, -1]).rotate_about_origin(r, np.array([1, 0, 0])))
		vect2.add_updater(update_vector3)

		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group3(path_group3)
			self.wait(0.0001)
		self.wait(3)
		while(i<2*n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group3(path_group3)
			self.wait(0.0001)
		self.wait(3)






		#reflect on y axis
		frame.target.set_euler_angles(
			theta=-10 * DEGREES,
			phi=40 * DEGREES,
		)
		self.play(FadeOut(path_group3))
		self.play(MoveToTarget(frame))
		gate.target = Tex(r"Pauli Y: \sigma_y").shift(UP*2.5)
		self.play(MoveToTarget(gate))

		#make line
		line.target =  DashedLine(np.array([0, 1, 0]), np.array([0, -1, 0]), color=RED)
		self.play(MoveToTarget(line))

		#PATH UPDATOR
		line5 = Line(ORIGIN,vect2.get_end())
		# Path
		path4 = VMobject(color=BLUE)
		# Path can't have the same coord twice, so we have to dummy point
		path4.set_points_as_corners([vect2.get_end(),vect2.get_end()+UP*0.001])
		# Path group
		path_group4 = VGroup(line5,path4)
		def update_group4(group):
			l,previus_path = group
			old_path = path4.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect2.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect2.get_end())
			path4.become(old_path)
		self.add(path_group4)

		vect2.remove_updater(update_vector3)
		def update_vector4(self):
			self.become(Vector(direction=[0, 0, -1]).rotate_about_origin(r, np.array([0, 1, 0])))
		vect2.add_updater(update_vector4)

		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group4(path_group4)
			self.wait(0.0001)
		self.wait(3)
		while(i<2*n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group4(path_group4)
			self.wait(0.0001)
		self.wait(3)











		#reflect on z axis
		frame.target.set_euler_angles(
			theta=-10 * DEGREES,
			phi=40 * DEGREES,
		)
		vect2.remove_updater(update_vector4)
		vect2.target = Vector(direction=[0, -1, 0])
		self.play(MoveToTarget(vect2))
		def update_vector5(self):
			self.become(Vector(direction=[0, -1, 0]).rotate_about_origin(r, np.array([0, 0, 1])))
		vect2.add_updater(update_vector5)

		self.play(FadeOut(path_group4))
		self.play(MoveToTarget(frame))
		gate.target = Tex(r"Pauli Z: \sigma_z").shift(UP*2.5)
		self.play(MoveToTarget(gate))

		#make line
		line.target =  DashedLine(np.array([0, 0, 1]), np.array([0, 0, -1]), color=RED)
		self.play(MoveToTarget(line))

		#PATH UPDATOR
		line6 = Line(ORIGIN,vect2.get_end())
		# Path
		path5 = VMobject(color=BLUE)
		# Path can't have the same coord twice, so we have to dummy point
		path5.set_points_as_corners([vect2.get_end(),vect2.get_end()+UP*0.001])
		# Path group
		path_group5 = VGroup(line6,path5)
		def update_group5(group):
			l,previus_path = group
			old_path = path5.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect2.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect2.get_end())
			path5.become(old_path)
		self.add(path_group5)
		self.play(FadeOut(line6))
		

		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group5(path_group5)
			self.wait(0.0001)
		self.wait(3)
		while(i<2*n):
			i += 0.1
			r = -PI*i/n
			frame.increment_theta(-0.1*0.06*10/n)
			update_group5(path_group5)
			self.wait(0.0001)
		self.wait(3)







		#phase shift
		frame.target.set_euler_angles(
			theta=150 * DEGREES,
			phi=40 * DEGREES,
		)
		vect2.remove_updater(update_vector5)
		vect2.target = Vector(direction=[0, -1/(2**(0.5)), 1/(2**(0.5))])
		self.play(MoveToTarget(vect2))
		def update_vector6(self):
			self.become(Vector(direction=[0, -1/(2**(0.5)), 1/(2**(0.5))]).rotate_about_origin(r, np.array([0, 0, 1])))
		vect2.add_updater(update_vector6)

		self.play(FadeOut(path_group5))
		self.play(MoveToTarget(frame))
		gate.target = Tex(r"R_\theta Gate").shift(UP*2.5)
		self.play(MoveToTarget(gate))

		#make line
		line.target =  DashedLine(np.array([0, 0, 1]), np.array([0, 0, -1]), color=RED)
		self.play(MoveToTarget(line))

		#PATH UPDATOR
		line7 = Line(ORIGIN,vect2.get_end())
		# Path
		path6 = VMobject(color=BLUE)
		# Path can't have the same coord twice, so we have to dummy point
		path6.set_points_as_corners([vect2.get_end(),vect2.get_end()+UP*0.001])
		# Path group
		path_group6 = VGroup(line7,path6)
		def update_group6(group):
			l,previus_path = group
			old_path = path6.copy()
			# See manimlib/mobject/types/vectorized_mobject.py
			old_path.append_vectorized_mobject(Line(old_path.get_points()[-1],vect2.get_end()))
			#old_path.make_smooth()
			l.put_start_and_end_on(ORIGIN,vect2.get_end())
			path6.become(old_path)
		self.add(path_group6)
		self.play(FadeOut(line7))
		

		i = 0
		while(i<n):
			i += 0.1
			r = -PI*i/(2*n)
			frame.increment_theta(-0.1*0.06*10/n)
			update_group6(path_group6)
			self.wait(0.0001)
		self.wait(3)
		while(i<2*n):
			i += 0.1
			r = -PI*i/(2*n)
			frame.increment_theta(-0.1*0.06*10/n)
			update_group6(path_group6)
			self.wait(0.0001)
		self.wait(12)





















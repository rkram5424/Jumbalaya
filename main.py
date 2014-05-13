#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#imports
import random as r
import sys
import kivy
from kivy.garden.magnet import Magnet
from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
	ListProperty, ObjectProperty
import Jumbalaya

class JumbalayaMenu(Screen):
	pass

class BowlScreen(Screen):
	def art(self):
		gs = sm.current_screen
		gs.set_bowl('ArtLiterature')
	def ent(self):
		gs = sm.current_screen
		gs.set_bowl('Entertainment')
	def geo(self):
		gs = sm.current_screen
		gs.set_bowl('Geography')
	def his(self):
		gs = sm.current_screen
		gs.set_bowl('History')
	def sci(self):
		gs = sm.current_screen
		gs.set_bowl('ScienceNature')
	def msc(self):
		gs = sm.current_screen
		gs.set_bowl('Misc')

##################################################

class DraggableImage(Magnet):
	img = ObjectProperty(None, allownone=True)
	app = ObjectProperty(None)

	def on_img(self, *args):
		self.clear_widgets()

		if self.img:
			Clock.schedule_once(lambda *x: self.add_widget(self.img), 0)

	def on_touch_down(self, touch, *args):
		if self.collide_point(*touch.pos):
			touch.grab(self)
			self.remove_widget(self.img)
			self.app.root.add_widget(self.img)
			self.center = touch.pos
			self.img.center = touch.pos
			return True

		return super(DraggableImage, self).on_touch_down(touch, *args)

	def on_touch_move(self, touch, *args):
		grid_layout = self.app.root.ids.grid_layout
		float_layout = self.app.root.ids.float_layout

		if touch.grab_current == self:
			self.img.center = touch.pos
			if grid_layout.collide_point(*touch.pos):
				grid_layout.remove_widget(self)
				float_layout.remove_widget(self)

				for i, c in enumerate(grid_layout.children):
					if c.collide_point(*touch.pos):
						grid_layout.add_widget(self, i - 1)
						break
				else:
					grid_layout.add_widget(self)
			else:
				if self.parent == grid_layout:
					grid_layout.remove_widget(self)
					float_layout.add_widget(self)

				self.center = touch.pos

		return super(DraggableImage, self).on_touch_move(touch, *args)

	def on_touch_up(self, touch, *args):
		if touch.grab_current == self:
			self.app.root.remove_widget(self.img)
			self.add_widget(self.img)
			touch.ungrab(self)
			return True

		return super(DraggableImage, self).on_touch_up(touch, *args)


##################################################

class GameScreen(Screen):
	bowl = StringProperty()
	hint = StringProperty()
	word = StringProperty()
	jumble = ListProperty()
	j_rows = NumericProperty()

	def set_bowl(self, bowl):
		jb = Jumbalaya.Jumbalaya(bowl)
		self.bowl = self.display_bowl(bowl)
		self.hint = jb.return_data()[0]
		self.word = jb.return_data()[1]
		self.jumble = jb.return_data()[2]
		if len(self.jumble) == 10:
			self.j_rows = 1
		else:
			self.j_rows = 2
		self.load_slots()
		self.load_jumble()

	def load_slots(self):
		for letter in self.word:
			let_lab = Label
			let_lab.text = letter
			if not letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				self.ids.slot_grid.add_widget(Label(text=letter, font_size=24))
			else:
				self.ids.slot_grid.add_widget(Image(source='Art/Tiles/slot.png'))

	def load_jumble(self):
		for letter in range(1):#self.jumble:
			mag = self.ids.magneto
			with mag.canvas:
			  	Color(0,1,0)
			  	Rectangle()
			#self.ids.jumble_container.add_widget(mag)

	def update_jumble(self):
		pass

	def load_tiles(self):
		pass

	def display_bowl(self, bowl):
		bowl = bowl.replace('ArtLiterature','Art & Literature')
		bowl = bowl.replace('ScienceNature','Science & Nature')
		bowl = bowl.replace('Misc','Miscellaneous')
		return bowl

Builder.load_string("""
#:kivy 1.8.0

<Jumbalaya>:
	canvas:
		Color:
			rgb: 0, 1, 1
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

<JumbalayaMenu>:
	canvas:
		Color:
			rgb: 0, 1, 1
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size
	BoxLayout:
		orientation: 'vertical'
		Image:
			source: 'Art/Title.png'
		BoxLayout:
			orientation: 'vertical'
			size_hint:(.4,1)
			pos: (1, .5)
			Button:
				background_normal: 'Art/Buttons/new_bowl.png'
				allow_stretch: False
				on_press: root.manager.current = 'bowls'
			Button:
				background_normal: 'Art/Buttons/about.png'
			Button:
				background_normal: 'Art/Buttons/quit.png'

<BowlScreen>:
	canvas:
		Color:
			rgb: 0, 1, 1
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

	BoxLayout:
		orientation: 'vertical'
		padding: 50
		Button:
			text: 'Art & Literature'
			on_press: root.manager.current = 'game'; root.art()
		Button:
			text: 'Entertainment'
			on_press: root.manager.current = 'game'; root.ent()
		Button:
			text: 'Geography'
			on_press: root.manager.current = 'game'; root.geo()
		Button:
			text: 'History'
			on_press: root.manager.current = 'game'; root.his()
		Button:
			text: 'Science & Nature'
			on_press: root.manager.current = 'game'; root.sci()
		Button:
			text: 'Misc'
			on_press: root.manager.current = 'game'; root.msc()
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'

<GameScreen>:
	canvas:
		Color:
			rgb: 0, 1, 1
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			size_hint:(1, 0.3)
			##padding: 50
			orientation: 'horizontal'
			Button:
				text: 'Back'
				on_press: root.manager.current = 'bowls'
			Label:
				font_size: 24
				text: root.bowl
			Button:
				text: 'Skip'
				on_press: root.manager.current = 'game'
		Label:
			text: root.hint
			font_size: 24
		GridLayout:
			id: slot_grid
			cols: 15
			rows: 2
		BoxLayout:
			id: jumble_container
			Magnet:
				id: magneto
				transitions: {'pos': 'out_quad', 'size': 'out_elastic'}
				duration: 1
				Label:
					text: 'poop'
					canvas:
						Color: 
							rgb: 0,0,1
						Rectangle
			##cols: len(root.jumble)
			##rows: root.j_rows
""")

sm = ScreenManager()
sm.add_widget(JumbalayaMenu(name='menu'))
sm.add_widget(BowlScreen(name='bowls'))
sm.add_widget(GameScreen(name='game'))

class JumbalayaApp(App):
	def build(self):
		#draggable = DraggableImage(img=image, app=self, size_hint=(None, None), size=(32, 32))
		#self.root.ids.grid_layout.add_widget(draggable)
		return sm
	
if __name__ == '__main__':
	JumbalayaApp().run()

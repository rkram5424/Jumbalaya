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
		self.load_jumble()

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

<JumbalayaMenu>:
	BoxLayout:
		orientation: 'vertical'
		padding: 200
		spacing: 50
		Button:
			text: 'New Bowl'
			on_press: root.manager.current = 'bowls'
			width: 50
		Button:
			text: 'Quit'
		Button:
			text: 'About'

<BowlScreen>:
	BoxLayout:
		orientation: 'vertical'
		padding: 50
		Button:
			text: 'Art & Literature'
			on_press: root.manager.current = 'game'
			on_release: root.art()
		Button:
			text: 'Entertainment'
			on_press: root.manager.current = 'game'
			on_release: root.ent()
		Button:
			text: 'Geography'
			on_press: root.manager.current = 'game'
			on_release: root.geo()
		Button:
			text: 'History'
			on_press: root.manager.current = 'game'
			on_release: root.his()
		Button:
			text: 'Science & Nature'
			on_press: root.manager.current = 'game'
			on_release: root.sci()
		Button:
			text: 'Misc'
			on_press: root.manager.current = 'game'
			on_release: root.msc()
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'

<GameScreen>:
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			padding: 50
			orientation: 'horizontal'
			Button:
				text: 'Back'
				on_press: root.manager.current = 'bowls'
			Label:
				text: root.bowl
			Button:
				text: 'Skip'
				on_press: root.manager.current = 'game'
		Label:
			text: root.hint
		GridLayout:
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

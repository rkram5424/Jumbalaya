#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#imports
import random as r
import sys
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
	ListProperty
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
				text: 'Next'
				on_press: root.manager.current = 'game'
		Label:
			text: root.hint
		GridLayout:
			cols: 15
			rows: 2
		GridLayout:
			cols: 10
			rows: root.j_rows
""")

sm = ScreenManager()
sm.add_widget(JumbalayaMenu(name='menu'))
sm.add_widget(BowlScreen(name='bowls'))
sm.add_widget(GameScreen(name='game'))

class JumbalayaApp(App):
	def build(self):
		return sm
	
if __name__ == '__main__':
	JumbalayaApp().run()

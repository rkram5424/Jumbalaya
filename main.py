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
import Jumblaya

class JumblayaMenu(Screen):
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
	hint = ""
	def set_bowl(self, bowl):
		jb = Jumblaya.Jumblaya(bowl)
		self.hint = jb.return_data()[0]
		l = Label(text=self.hint)
		self.add_widget(l)

Builder.load_string("""

#:kivy 1.8.0

<JumblayaMenu>:
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
""")

sm = ScreenManager()
sm.add_widget(JumblayaMenu(name='menu'))
sm.add_widget(BowlScreen(name='bowls'))
sm.add_widget(GameScreen(name='game'))

class JumblayaApp(App):
	def build(self):
		return sm
	
if __name__ == '__main__':
    JumblayaApp().run()

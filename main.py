#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#imports
import random as r
import sys
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import Jumblaya

Builder.load_string("""
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
			on_press: root.bowl = 'ArtLiterature'
		Button:
			text: 'Entertainment'
			on_press: root.manager.current = 'game'
			on_press: root.bowl = 'Entertainment'
		Button:
			text: 'Geography'
			on_press: root.manager.current = 'game'
			on_press: root.bowl = 'Geography'
		Button:
			text: 'History'
			on_press: root.manager.current = 'game'
			on_press: root.bowl = 'History'
		Button:
			text: 'Science & Nature'
			on_press: root.manager.current = 'game'
			on_press: root.bowl = 'ScienceNature'
		Button:
			text: 'Misc'
			on_press: root.manager.current = 'game'
			on_press: root.bowl = 'Misc'
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'

<GameScreen>:
	FloatLayout:
		Label:
			text: root.hint

""")

class JumblayaMenu(Screen):
	pass

class BowlScreen(Screen):
    pass

class GameScreen(Screen):
	jb = Jumblaya.Jumblaya('ArtLiterature') # How to set the param dynamically...
	hint = jb.return_data()[0]
	word = jb.return_data()[1]
	jumble = jb.return_data()[2]

class JumblayaApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(JumblayaMenu(name='menu'))
		sm.add_widget(BowlScreen(name='bowls'))
		sm.add_widget(GameScreen(name='game'))
		return sm
	
if __name__ == '__main__':
    JumblayaApp().run()

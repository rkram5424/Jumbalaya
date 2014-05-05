#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#imports
import random as r
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<JumblayaMenu>:
	BoxLayout:
		orientation: 'vertical'
		padding: 50
		Button:
			text: 'New Bowl'
			on_press: root.manager.current = 'bowls'
		Button:
			text: 'Quit'

<BowlScreen>:
	BoxLayout:
		orientation: 'vertical'
		padding: 50
		Button:
			text: 'Art & Literature'
		Button:
			text: 'Entertainment'
		Button:
			text: 'Geography'
		Button:
			text: 'History'
		Button:
			text: 'Science & Nature'
		Button:
			text: 'Misc'
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu'
""")

# Declare both screens
class JumblayaMenu(Screen):
	pass

class BowlScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(JumblayaMenu(name='menu'))
sm.add_widget(BowlScreen(name='bowls'))

class JumblayaApp(App):
	def build(self):
		return sm

class Jumblaya():
	#Bowl constants for filenames
	art = "ArtLiterature"
	ent = "Entertainment"
	geo = "Geography"
	his = "History"
	sci = "ScienceNature"
	msc = "Misc"
	
	def __init__(self, bowl): 
		hint, word = self.random_line(bowl).split('|')
		word = word.lower()
		print (self.jumble_letters(word))
		
	def jumble_letters(self, word): # takes in word and spits out a jumbled mess.
		word = word.replace(' ', '')
		jumble_num = 0
		new_num = 0
		jumble_arr = []
		if self.count_letters(word) > 1 & self.count_letters(word) < 10:
			jumble_num = 10
		elif self.count_letters(word) > 10 & self.count_letters(word) <= 20:
			jumble_num = 20
		new_num = jumble_num - self.count_letters(word)
		for i in range(new_num):
			word = word + self.random_letter()
		jumble_arr = list(word)
		r.shuffle(jumble_arr)
		return jumble_arr
		
	def count_letters(self, answer):
		non_letters = 0
		answer = answer.lower()
		letters = 'abcdefghijklmnopqrstuvwxyz'
		for i in range(len(answer)):
			if not(letters.contains(answer[i])):
				non_letters += 1
		return len(answer) - non_letters
		
	def random_letter(self):
		letters = 'abcdefghijklmnopqrstuvwxyz'
		return r.choice(letters)
		
	def random_line(afile):
		afile = afile + ".txt"
		line = next(afile)
		for num, aline in enumerate(afile):
		if r.randrange(num + 2): continue
			line = aline
		return line

if __name__ == '__main__':
    JumblayaApp().run()

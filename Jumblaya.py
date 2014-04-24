#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# RYAN'S NOTES
# Maybe we could have a threshold of tens in 
# terms of how many jumbled letters to show.
# < 10, show 10 letters.
# 10 < x <= 20 show 20 letters.
# 10 to a row so it's not scrunched.
# Maybe make 20 letters the limit.
# Spaces allowable, not tiles though. Spaces
# appear as gaps in fillable slots.

# imports
import random as r
import sys

class Jumblaya:
	def __init__(self):
		word = sys.argv[1]
		word = word.lower()
		print (self.jumble_letters(word))
		
	def jumble_letters(self, word): # takes in word and spits out a jumbled mess.
		word = word.replace(' ', '')
		jumble_num = 0
		new_num = 0
		jumble_arr = []
		if self.letter_num(word) > 1 & self.letter_num(word) < 10:
			jumble_num = 10
		elif self.letter_num(word) > 10 & self.letter_num(word) <= 20:
			jumble_num = 20
		new_num = jumble_num - self.letter_num(word)
		for i in range(new_num):
			word = word + self.random_letter()
		jumble_arr = list(word)
		r.shuffle(jumble_arr)
		return jumble_arr
		
	def letter_num(self, word):
		non_space = 0
		for i in range(len(word)):
			if word[i] != ' ':
				non_space += 1
		return non_space
		
	def random_letter(self):
		letters = 'abcdefghijklmnopqrstuvwxyz'
		return r.choice(letters)

if __name__ == '__main__':
	Jumblaya()


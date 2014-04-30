#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# RYAN'S NOTES
# Maybe we could have a threshold of tens in 
# terms of how many jumbled letters to show.
# < 10, show 10 letters.
# 10 < x <= 20 show 20 letters.
# 10 to a row so it's not scrunched.
# Maybe make 20 characters the limit.
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

if __name__ == '__main__':
	Jumblaya()


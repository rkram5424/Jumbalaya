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

class Jumbalaya:

	jb = ['','','']

	def __init__(self, bowl):
		hint, word = self.random_line(bowl).split('|')
		word = word.upper()
		self.jb = [hint, word, self.jumble_letters(word)]
		self.return_data()

	def return_data(self):
		return self.jb
		
	def jumble_letters(self, word): # takes in word and spits out a jumbled mess.
		word = word.replace(' ', '')
		word = word.replace('\n', '')
		jumble_num = 0
		new_num = 0
		jumble_arr = []
		letter_count = self.count_letters(word)
		print(letter_count)
		if (letter_count > 1 and letter_count <= 10):
			jumble_num = 10
		else:
			jumble_num = 20
		new_num = jumble_num - letter_count
		print(new_num)
		for i in range(new_num):
			word = word + self.random_letter()
		jumble_arr = list(word)
		r.shuffle(jumble_arr)
		print(jumble_arr)
		return jumble_arr
		
	def count_letters(self, answer):
		non_letters = 0
		answer = answer.upper()
		letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		for i in range(len(answer)):
			if not answer[i] in letters:
				non_letters += 1
		return len(answer) - non_letters
		
	def random_letter(self):
		letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		return r.choice(letters)
		
	def random_line(self, afile):
		return r.choice(list(open(afile + '.txt')))

if __name__ == '__main__':
	Jumbalaya()


#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib

class TriviaCrawler:
	cat_array = ['ArtLiterature','Geography','Entertainment','History','ScienceNature','Misc']
	root_url = 'http://www.randomtriviagenerator.com/'
	num_ret_array = ['arts.php','geography.php','entertainment.php','history.php','science.php','misc.php']
	add_array = ['question_a.php?q=','question_g.php?q=','question_e.php?q=','question_h.php?q=','question_s.php?q=','question_m.php?q=']
	cat_nums = [0,0,0,0,0,0]
	
	def __init__(self):
		self.crawl()
	
	def crawl(self):
		for i in range(6):
			response = urllib.urlopen(self.root_url + self.num_ret_array[i])
			page_source = response.read()
			self.cat_nums[i] = self.extract_between(page_source,'There are <b>','</b> questions', 1)
			self.cat_nums[i] = int(self.cat_nums[i])
			f = open(self.cat_array[i] + '.txt', 'w')
			for j in range(self.cat_nums[i]):
				question = ""
				answer = ""
				response = urllib.urlopen(self.root_url + self.add_array[i] + str(j))
				page_source = response.read()
				question = self.extract_between(page_source,'<td align="left">','</td>',1)
				answer = self.extract_between(page_source,'<td align="left">','</td>',2)
				question = question.strip()
				answer = answer.strip()
				answer = self.refine_answer(answer)
				answer = answer.upper()
				if question != '' and answer != '':
					print(question)
					print(answer)
					f.writelines(question + '|' + answer + '\n')
			f.close()
	
	def refine_answer(self, answer):
		if self.contains_digits(answer):
			return ''
		if self.count_letters(answer) > 20:
			return ''
		if self.count_letters(answer) < 4:
			return ''
		return answer
		
	def count_letters(self, answer):
		non_letters = 0
		answer = answer.lower()
		letters = 'abcdefghijklmnopqrstuvwxyz'
		for i in range(len(answer)):
			if not answer[i] in letters:
				non_letters += 1
		return len(answer) - non_letters
		
	def contains_digits(self, answer):
		return any(char.isdigit() for char in answer)
	
	def extract_between(self, text, sub1, sub2, nth):
		"""
		extract a substring from text between two given substrings sub1 (nth occurrence) and sub2 (nth occurrence) arguments are case sensitive
		"""
		# prevent sub2 from being ignored if it's not there
		if sub2 not in text.split(sub1, nth)[-1]:
			return None
		return text.split(sub1, nth)[-1].split(sub2, nth)[0]

if __name__ == '__main__':
	TriviaCrawler()


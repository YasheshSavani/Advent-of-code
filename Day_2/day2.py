# Author: Yashesh Savani
# Advent of Code Day 2
# Date: December 2, 2020

import re

def part_1(policies):

	counter = 0
	for text in policies:
		password = text.split(':')[1].strip()
		condition = text.split(':')[0] 
		range_ = condition.split(' ')[0].split('-')
		start = int(range_[0])
		end = int(range_[1])
		letter = condition.split(' ')[1].strip()
		
		match = re.findall(r"{}".format(letter),password)
		if start <= len(match) <= end:
			counter += 1

	return counter

def part_2(policies):

	counter = 0
	for text in policies:
		password = text.split(':')[1].strip()
		condition = text.split(':')[0] 
		range_ = condition.split(' ')[0].split('-')
		start = int(range_[0])
		end = int(range_[1])
		letter = condition.split(' ')[1].strip()
		
		if letter == password[start-1] and letter != password[end-1]or letter != password[start-1] and letter == password[end-1]:
			counter += 1
			
	return counter


if __name__ == "__main__":

	with open('password_policies.txt', 'r') as f:
		policies = f.readlines()

	print(f"Part 1: {part_1(policies)}")
	print(f"Part 2: {part_2(policies)}")
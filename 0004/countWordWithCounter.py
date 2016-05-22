#! /usr/bin/python3
# -*- coding:utf-8 -*-

'''
	This py module use  Counter inner class in python 3
'''

__author__ = 'TonyZhu'

from collections import Counter
import re

def statisticsWithCount(path='word.txt') :
	c = Counter()
	partsAfterSplitByRe = re.findall(r'\w+',open(path,'r').read().lower())
	return Counter(partsAfterSplitByRe).most_common()

if __name__ == '__main__':
	print(statisticsWithCount())
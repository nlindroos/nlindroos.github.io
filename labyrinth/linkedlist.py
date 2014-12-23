#!/usr/bin/env python
#-*- coding: UTF-8 -*-

class ListNode:
	
	def __init__(self, data, previous, next1):
		self.data = data
		self.prev = previous
		self.next = next1
	
	

class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0
		
	
	def getFirst(self):
		return self.first


	def addFirst(self, item):
		if self.size==0:
			self.first = ListNode(item, None, None)
			self.last = self.first
			self.size+=1

		else:
			temp = self.first
			self.first = ListNode(item, None, temp)
			temp.prev = self.first
			self.size+=1
			
			
	def addLast(self, item):
		if self.size==0:
			self.first = ListNode(item, None, None)
			self.last = self.first
			self.size+=1
			
		else:
			temp = self.last
			self.last = ListNode(item, temp, None)
			temp.next = self.last
			self.size+=1


	def addPosition(self, n, item):
		temp = self.first
		if n==0:
			self.addFirst(item)
		elif n==(self.size-1):
			self.addLast(item)
		else:
			while n>0:
				temp = temp.next
				n-=1
			new = ListNode(item, temp.prev, temp)
			temp.prev.next = new
			temp.prev = new
			self.size+=1
		

	def removePosition(self, n):
		temp = self.first
		if self.size==1:
			self.first.data = None
			self.last = self.first
		elif n==(self.size-1):
			self.last.prev.next = None
		elif n==0:
			self.first = self.first.next
			self.first.prev = None
		else:
			while n>0:
				temp = temp.next
				n-=1
			temp.prev.next = temp.next
			temp.next.prev = temp.prev

		self.size-=1
		
		
	def getPosition(self, n):
		temp = self.first
		while n>0:
			temp = temp.next
			n-=1
		return temp.data


	def getSize(self):
		return self.size




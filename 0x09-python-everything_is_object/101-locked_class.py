#!/usr/bin/python3

class LockedClass:
	"""
	prevent the user from dynamically creating
        new instance attributes except one called 'first_name'
	"""
	_slots_ = ["first_name"]

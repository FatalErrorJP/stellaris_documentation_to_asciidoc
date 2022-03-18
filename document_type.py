#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum

class DocumentType(Enum):
	Effects = {
		'name' : 'effects'
		, 'num' : 4
		, 'headers' : '：Name ： Description ： Example ： Support Scopes'
	}
	Triggers = {
		'name' : 'triggers'
		, 'num' : 4
		, 'headers' : '：Name ： Description ： Example ： Support Scopes'
	}
	Scopes = {
		'name' : 'scopes'
		, 'num' : 2
		, 'headers' : '：Name ： Description'
	}
	Modifiers = {
		'name' : 'modifiers'
		, 'num' : 2
		, 'headers' : '：Name ： Description'
	}

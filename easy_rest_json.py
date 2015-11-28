#!/usr/bin/python
# -*- coding: utf8 -*-

# Easy REST JSON
# Copyright (C) 2015  Antoine FERRON

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import json
import urllib
import urllib2

class rest_json:
	def __init__(self,url="",params=""):
		self.url=url
		self.params=dict(params)
		self.jsres=[]
		self.post=False
	
	def set_url(self,url):
		self.url=url
	
	def add_param(self,param):
		self.params.update(param)
	
	def add_data(self,data):
		self.data=data
		self.post=True
	
	def get_data(self):
		params_enc = urllib.urlencode( self.params )
		try:
			if self.post:
				self.webrsc = urllib2.urlopen(self.url,self.data)
			else:
				self.webrsc = urllib2.urlopen(self.url+"?"+params_enc)
			self.jsres=json.load(self.webrsc)
		except:
			raise IOError("Error while processing request:\n%s"%(self.url))
	
	def getkey(self,keychar):
		out=self.jsres
		path=keychar.split("/")
		for key in path:
			if key.isdigit(): key=int(key)
			try:
				out=out[key]
			except:
				raise KeyError("Key Error. Did you get data?")
		return out

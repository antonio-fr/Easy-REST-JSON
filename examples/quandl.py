#!/usr/bin/python
# -*- coding: utf8 -*-

from easy_rest_json import * 

quandl = rest_json()
quandl.set_url('http://www.quandl.com/api/v1/datasets/LBMA/GOLD.json')
quandl.add_param({"rows":"1"})
quandl.add_param({"auth_token":"xxxx"})
quandl.get_data()
gold_price = quandl.getkey("data/0/1")

print "Data from London Bullion Market Association"
print "provided by Quandl"
print "Gold Price at London A.M. Fixing :"
print gold_price, "USD per troy ounce"

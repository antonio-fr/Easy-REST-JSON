#!/usr/bin/python
# -*- coding: utf8 -*-

from easy_rest_json import * 

RateApi = rest_json('http://openexchangerates.org/api/latest.json',{"app_id":"xxxx"})
RateApi.get_data()
eur_price = RateApi.getkey("rates/EUR")
print "Euro Rate"
print "provided by OpenExchangeRates"
print eur_price, "USD"



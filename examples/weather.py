#!/usr/bin/python
# -*- coding: utf8 -*-

from easy_rest_json import * 

myres = rest_json()
myres.set_url('http://api.openweathermap.org/data/2.5/weather')
myres.add_param({"zip":"75014,fr"})
myres.add_param({"units":"metric"})
myres.get_data()
pres_temp = myres.getkey("main/temp")
weather = myres.getkey("weather/0/main")
print u"\nToday, the weather in Paris is : %s" % weather
print u"Temperature : %s°C" % pres_temp

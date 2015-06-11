Easy REST JSON
==============

Easy REST JSON client library dedicated for API queries for Python 2.x

Provides high level function to get data from REST API servers (JSON).

* Quickly and easily extracts variable from JSON API HTTP server
* Automatically deals with encodings and server communication
* No dependency except python built-in
* Connect to HTTP or HTTPS
* Get parameter again in a single command (refresh)
* Handles query parameters in a simple form


## Using library

To use the library, just copy easy_rest_json.py and use import as usual
    import easy_rest_json
or
    from easy_rest_json import *


#### Initialisation
easy_rest_json.rest_json([URL][,query_parameters]) returns a library object.

    myclient = easy_rest_json.rest_json()
    myclient.set_url('http://URL')

or 

    myclient = easy_rest_json.rest_json('http://URL')


#### Set URL
In case URL was not given during initialisation, URL can be provided this way.

    MyQueryClient.set_url('http://URL')

#### Add Params
In case the server needs any parameter ( ...?a=1234&b=5678 ), add_param adds a parameter to the query object.

Parameter shall be a single entry dictionnary. Several parameters can be given , with a dictionnary, at the initialisation level.

The encoding is directly performs by the library. 

    MyQueryClient.add_param(param_as_a_key_dict)

#### Get Data
The central function of the library: sends actually the query to the server, gets the data, decode the JSON and automatically saves it internally, for futur use as "getkey". Returns nothing. 

    MyQueryClient.get_data()

#### Get key variable
Returns the value of the given path in the JSON response.

    MyQueryClient.getkey("PATH/TO/VAR/NEEDED")

Path can be keys (strings) or index (integers) , even mixed.

Can be used with int() of float() to convert data to number.

    usd_rate = float(MyClient.getkey("rate/currency/USD"))


**Form more details: see code in examples directory**


## Example :
The following example prints the present temperature in Paris France, in celsius degres. Data are retrieved from OpenWeatherMap free API.

    import easy_rest_json
    queryweather = easy_rest_json.rest_json()
    queryweather.set_url('http://api.openweathermap.org/data/2.5/weather')
    queryweather.add_param({"zip":"75014,fr"})
    queryweather.add_param({"units":"metric"})
    queryweather.get_data()
    pres_temp = queryweather.getkey("main/temp")
    print pres_temp


Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

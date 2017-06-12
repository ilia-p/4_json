# **Prettify JSON**

The script transfer json row to a more readable view.

# Quickstart

initial json:

{ "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA", "_id" : "01001" }

Launch/path:

python pprint_json.py -p test.json

Result:

{'_id': '01001',\n
'city': 'AGAWAM',\n
'loc': [-72.622739, 42.070206],\n
'pop': 15338,\n
'state': 'MA'}\n

# **Project Goals**

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

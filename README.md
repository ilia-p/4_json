# Prettify JSON

The script transfer json row to a more readable view.

# Quickstart

**Initial json:**

>{ "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA", "_id" : "01001" }

**Launch/path:**

>python pprint_json.py -p test.json

**Result:**

'''
{
    "_id": "01001",
    "city": "AGAWAM",
   "loc": [
       -72.622739,
      42.070206
   ],
   "pop": 15338,
   "state": "MA"
}
'''

# **Project Goals**

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

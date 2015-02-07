"""
capital_one_test.py - Class for testing whatever our project is supposed to do.
msimo & mzamani - 2/5/15 - Python 2.7.6
VTHacksII - Capital One Testing


"""

import requests

api_key = ("ENT3ca7af9505d019675832108f51888dff", "CUST3ca7af9505d019675832108f51888dff")
customer_key = ("54b604dfa520e02948a0f50d", "54b604dfa520e02948a0f50e", "54b604dfa520e02948a0f50f")

api_domain = "http://api.reimaginebanking.com"


def customer_query(api_domain, customer_key, api_key):
	for key in customer_key:
		req = requests.get(http_string)
		print("\nExpected API call: {}\nError Code: {}".format(http_string, req.status_code)

		query = ("/customers/{}?key={}".format(key, api_key[1])
		http_string = (api_domain + query)
		print(req.text) #//contains the response code = requests.get

customer_query(api_domain, customer_key, api_key)
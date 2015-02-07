"""
capital_one_test.py - Class for testing whatever our project is supposed to do.
msimo & mzamani - 2/5/15 - Python 2.7.6
VTHacksII - Capital One Testing
"""

import requests, sys

api_key = {"ent_api" : "ENT3ca7af9505d019675832108f51888dff",
		   "cust_api" : "CUST3ca7af9505d019675832108f51888dff"}

customer_key = ("54b604dfa520e02948a0f50d", "54b604dfa520e02948a0f50e", "54b604dfa520e02948a0f50f")

api_domain = "http://api.reimaginebanking.com"
customer_queries = ["/customers", "/customers/{0}/", "/customers/{0}/accounts/", "/customers/{0}/bills/", "/customers/{0}/bills/{1}"]


def customer_query(api_domain, customer_key, api_key):
	api_key = "?key={}".format(api_key)
	
	for key in customer_key:
		#query = ("/customers/{0}".format(key))
		query = customer_queries[2].format(key)
		http_string = (api_domain + query + api_key)
		req = requests.get(http_string)
		print("Expected API call: {0}\nError Code: {1}".format(http_string, req.status_code))
		print(req.text)

def main():
	customer_query(api_domain, customer_key, api_key["cust_api"])

if __name__ == "__main__":
	sys.exit(main())
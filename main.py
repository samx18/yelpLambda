# Import packages

import json
import requests
import config

# Set global variables

API_KEY=config.API_KEY

# make a request to get the data

def getRequest(api_key):
	url='https://api.yelp.com/v3/businesses/search?term=musical&location=ca&limit=1'
	headers = {
       'Authorization': 'Bearer %s' % api_key,
       }
 	response = requests.request('GET', url, headers=headers)
 	return response.json()

# Parse data to dict

def responseParse(jsonResponse):

# Traverse dict to get values

# Store as a file in S3
	return

def main():
	print getRequest(API_KEY)
	return

if __name__ == '__main__':
		main()
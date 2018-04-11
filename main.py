# Import packages

import json
import requests
import config

# Set global variables

API_KEY=config.API_KEY

# make a request to get the data

def getRequest(api_key):
	url='https://api.yelp.com/v3/businesses/search?term=musical&location=ca&limit=10'
	headers = {
       'Authorization': 'Bearer %s' % api_key,
       }
 	response = requests.request('GET', url, headers=headers)
 	return response.json()

# Parse data to dict

def responseParse(jsonResponse):
	respDict = json.loads(jsonResponse)


# Traverse dict to get values

# Store as a file in S3
	return respDict

def main():
	response=getRequest(API_KEY)
	for i in  response['businesses']:
		print i['rating']
	return

if __name__ == '__main__':
		main()
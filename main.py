# Import packages

import json
import requests
import config

# Set global variables

API_KEY=config.API_KEY

# make a request to get the data

def getRequest(api_key):
	url='https://api.yelp.com/v3/businesses/search?term=musical&location=ca&limit=50'
	headers = {
       'Authorization': 'Bearer %s' % api_key,
       }
 	response = requests.request('GET', url, headers=headers)
 	return response.json()


def main():
	
	# Get respponse as a dict by passing API KEY 

	response=getRequest(API_KEY)
	
	# Open a file for writing 
	
	file = open("rating.csv", "w")
	
	# Iterate through the dict to retrive specific values

	for i in  response['businesses']:
		a = str(i['name'])+","+str(i['location']['city'])+","+str(i['location']['state'])+","+str(i['rating'])+"\n"
		file.write(a)
	
	# Close file when done
	
	file.close()
	
	return

if __name__ == '__main__':
		main()
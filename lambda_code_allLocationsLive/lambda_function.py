# AWS Lambda code to get the live parameter from all locations in melbourne

# Import Libs
import json
import requests

print("loading CheckLocation Lambda function")

# Define a function to find health advice given pm25 value - https://www.epa.vic.gov.au/for-community/environmental-information/air-quality/pm25-particles-in-the-air
def findHealthAdvice(pm25):
    if(pm25<27):
        return 1 #good
    elif 27 <= pm25 < 62:
        return 2 #moderate
    elif 62 <= pm25 < 97:
        return 3 #poor
    elif 97<= pm25 < 370:
        health_advice = 4 #very poor
    elif pm25 >= 370:
        return 5 #Hazardous
    else:
        return 1
        

# Define lambda handler
def lambda_handler(event, context):

    # build request URL
    request_latest_url = 'https://api.openaq.org/v1/latest?parameter=pm25&city=Melbourne'
    print('QP - Request URL = ' + request_latest_url)

    # read request
    request = requests.get(request_latest_url).json()
    request_results = request['results']

	# Build response in case of valid response
    if request_results:
        responseObj = []
        for location in request_results:
            data = {}
            data['location'] = location['location']
            for param in location['measurements']:
                data[param['parameter']] = param['value']
                data['health_advice'] = findHealthAdvice(param['value'])
            
            responseObj.append(data)

			
	# Construct body of response in case of data fetch failure
    if request_results:
        transactionResponse = {}
        transactionResponse['live'] = responseObj

	# Construct body of response
    else:
        transactionResponse = {}
        transactionResponse['error'] = 'Data not retrived from source'

		
    # Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # 4. Return the response object
    return responseObject
import re
import os
import json

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email): 
	if(re.search(regex,email)): 
		return "Valid Email"
	else: 
		return "Invalid Email" 

def handler(event, context):
    # assign email from lambda environment variable
    email = os.environ.get("email_address")

    is_valid = check(email)

    return {
        'statusCode': 200,
        'body': json.dumps(is_valid)
    }

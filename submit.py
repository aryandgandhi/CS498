import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "aryang6@illinois.edu" # <put your coursera account email>,
YOUR_SECRET = "pe8xpC89zeuSqdpx" # <put your secret token from coursera>

# Section 1
IP_ADDRESS1 = "3.137.206.17:5000" # <put your first EC2 instance's IP address:port>
IP_ADDRESS2 = "13.59.244.37:5000" # <put your second instance's IP address:port>
YOUR_LOAD_BALANCER1 = "MP1LB-1093444444.us-east-2.elb.amazonaws.com:5000" # <put your load_balancer address for section 1>
# Section 2
YOUR_LOAD_BALANCER2 = "my-first-asg-1-39788473.us-east-2.elb.amazonaws.com:5000" # <put your load_balancer address for section 2>, 

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
			'ip_address1': IP_ADDRESS1,
			'ip_address2': IP_ADDRESS2,
			'load_balancer1': YOUR_LOAD_BALANCER1, 
			'load_balancer2': YOUR_LOAD_BALANCER2,
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
		}
payload = { "input": json.dumps(input),
			"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
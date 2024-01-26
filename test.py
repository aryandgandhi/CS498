import requests

r = requests.get("http://MP1LB-1093444444.us-east-2.elb.amazonaws.com:5000")

print(r.json())
import requests

from pprint import pprint

files_url = 'https://api.stackexchange.com/2.3/questions?fromdate=1674691200&todate=1674864000&order=desc&min=1674691200&max=1674864000&sort=activity&site=stackoverflow'
response = requests.get(files_url)

for question in response.json()['items']:
    if 'python' in question['tags']:
        print(question['title'])
   

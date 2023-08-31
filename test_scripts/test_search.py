import json
import re
import requests
import urllib.request as urllib2

# with open('json_file.json') as f:
#     validation = (json.load(f))
#     print(validation)
#     print('yes')
# import re
# match = re.search(r'[\w\.-]+@[\w\.-]+', str(validation))
# print(match.group(0))

# url = 'https://qa1-shore.dxp-decurtis.com/reservation-bff/booknow'
# headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyR1VJRCI6IjE3MDllMWY5LThkMTEtNGI1NS05N2EzLTEzYTk1NjZiNzE5NiIsInVzZXJfbmFtZSI6InZpY3RvcmlhLnJvYmVydF85NjYzQG1haWxpbmF0b3IuY29tIiwicm9sZXMiOltdLCJ1c2VydHlwZSI6Imd1ZXN0IiwidXNlcmlkIjoiMTcwOWUxZjktOGQxMS00YjU1LTk3YTMtMTNhOTU2NmI3MTk2IiwiY2xpZW50X2lkIjoiNmM3ZjE1ZWUtMWRlYy00NzRmLWFhMmEtZjI1MjY4ODg2ZTdjIiwiY29tcGFueWlkIjoiYjM1YTMyNWEtMDM2YS00YWQ0LTg4MzYtNjQ2OTIzZTYwMWRlIiwic2NvcGUiOlsicmVhZCIsInRydXN0Iiwid3JpdGUiXSwicGVyc29uSWQiOm51bGwsImlkIjoiMTcwOWUxZjktOGQxMS00YjU1LTk3YTMtMTNhOTU2NmI3MTk2IiwiZXhwIjoxNTgyMTc2NzkyLCJ0b2tlblR5cGUiOiJ1c2VyVG9rZW4iLCJqdGkiOiIzNmE2YzQyNi04NjlmLTRiNzctOGM4Zi05NGJkMzIxOGJmOTQifQ.okJPjPUogHrtj2Bi3PqgE31sYncY_LTImr01q0CfRoZ2fr4idY3wtKWj8inKqVV9LMbfqzLrVkVabqxayz8B-eMpQdR01Vadb22p-Du7KFDYfadS6f3bot8xRYeFl4iZFj2H_AGMYjuVWEToaL1aRfETA6fdcERMW1TE5z704x759sfZ0K_29WG4nvm1k1WPbJ5p3BMCxmnb51qngCDwK0Sjmv4RY_A4lgK4CYYL4JXy9vO8JKx4AachaavVH_f3no-tHjhAjDCWNJ4GH4sv5n6ruCwaL9HNDQ2822P-is26vrZjeEFROHnj7iwcENsvxiRhAzR4Aootx_1eEqBQTw'}
#
# r = requests.post(url, data=json.dumps(headers))

url = 'https://jsonplaceholder.typicode.com/posts'
headers = {
        'userId': 5,
        'title': 'Stuff and Things',
        "body": 'An amazing blog post about both stuff and things.'
}
r = requests.post(url, data=json.dumps(headers))



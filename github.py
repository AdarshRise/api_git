import json
import requests
#Your access token
api_token = '7f7e460e5bb75b659ef5e386fd770b7598271cd0'
url="https://api.github.com/"
headers = {'Content-Type': 'application/json',
            'User-Agent': 'Student',
            'Accept': 'application/vnd.github.v3+json'}



def get_account_info(username):
    api_url = '{}users/{}/repos'.format(url,username)

    response = requests.get(api_url,headers=headers)

    if response.status_code == 200:
        return(response.content)

    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

repo_list = get_account_info('MeghaSharma33')

if repo_list is not None:
    print(repo_list)
else:
    print('No Repo List Found')

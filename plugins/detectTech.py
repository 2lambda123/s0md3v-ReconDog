import sys
import json
from requests import get


def detectTech(url):
    api=''
    
    # wappalyzer.txt will store API key for future use.
    try:

      with open('wappalyzer_api_key.txt') as f:
           api=f.read()

    except FileNotFoundError:

      api=input('\nPlease Enter Wappalyzer API KEY:')
      with open('wappalyzer_api_key.txt','w') as w:
           w.write(api)

    data=get('https://api.wappalyzer.com/lookup/v2/?urls='+url,headers={'x-api-key':api}).text
    jsoned_data = json.loads(data)
    technologies = []
    for one in jsoned_data[0]['technologies']:
        technologies.append(one['name'])
    for tech in technologies:
        sys.stdout.write(tech+'\n')

import sys
import os
from requests import get
from core.colors import bad, info, red, green, end

def honeypot(inp):
    key = os.environ.get('SHODAN_API_KEY', '')
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=%s' % (inp, key)
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('%s No information available' % bad + '\n')
    if result:
        if float(result) < 0.5:
            color = green
        else:
            color = red
        probability = str(float(result) * 10)
        sys.stdout.write('%s Honeypot Probabilty: %s%s%%%s' %
                         (info, color, probability, end) + '\n')

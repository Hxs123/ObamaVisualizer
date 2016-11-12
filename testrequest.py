########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

apiFile = open('secrets.txt', 'r')

apiKey = apiFile.readline()

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': apiKey,
}

# 12 Months of the year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Current month (last month with data)
finalMonth = months[11]

# First year to get data from
year = 2009

# Last month to get data from
finalYear = 2016

personQuery = 'Obama'

#queryString = 
params = urllib.parse.urlencode({
    # Request parameters
    'q': 'Obama January 2009',
    'count': '10',
    'offset': '0',
    'mkt': 'en-us',
    'safeSearch': 'Moderate',
})

try:
    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    #data = response.read()
    str_response = response.read().decode('utf-8')
    json_obj = json.loads(str_response)
    for i in range(0,10):
        contenturl = json_obj['value'][i]['contentUrl']
        print(contenturl)
    #print(data[:100])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

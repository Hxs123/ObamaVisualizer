########### Python 3.5 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

apiFile = open('secrets.txt', 'r')

apiFile.readline();
apiKey = apiFile.readline().replace("\n", "")


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': apiKey,
}

params = urllib.parse.urlencode({
})

emotions = ["anger", "contempt", "disgust", "fear", "happiness", "neutral", "sadness", "surprise"]

def getEmotionsVector(url):
    requestBody = '{ "url" : "' + url + '" }'
    emotionsVector = [];
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, requestBody, headers)
        response = conn.getresponse()
        # data = response.read()

        str_response = response.read().decode('utf-8')
        json_obj = json.loads(str_response)

        numFaces = len(json_obj)

        if numFaces != 1:
            return emotionsVector

        for face in json_obj:
            for e in emotions:
                emo = face['scores'][e];
                emotionsVector.append(emo)
        conn.close()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return emotionsVector

url = "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/terminal05/2012/5/10/10/enhanced-buzz-22789-1336660082-20.jpg";

vec = getEmotionsVector(url);

print(vec)


# open the pkl file.

# build structure of database

# for each url, call emotions api.
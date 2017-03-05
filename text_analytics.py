# import httplib, urllib, base64

# headers = {
#     # Request headers
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': "07b4ff5662b443399a37c9cd8bffff16",
# }

# params = urllib.urlencode({
#     # Request parameters
#     'numberOfLanguagesToDetect': '{integer}',
# })

# try:
#     conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/text/analytics/v2.0/languages?%s" % params, '{"documents": [{"id": "string","text": "Today is a very nice day in Los angeles and traffic is not that bad surprisignly"}]}', headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

import httplib, urllib, base64, io

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "07b4ff5662b443399a37c9cd8bffff16",
}

params = urllib.urlencode({
})



with io.open("disorders/paranoid1.txt", "r", encoding="utf-8") as f:
    text = f.read()


try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, '{"documents": [{"language":"en", "id": "string","text": "' + text.encode("utf-8", 'ignore') + '"}]}', headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
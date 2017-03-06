import httplib
import urllib
import io


def get_similarity(microsoft_key, text1, text2):
    """
    """
    with io.open(text1, "r", encoding="utf-8") as f:
        text1 = f.read()

    with io.open(text2, "r", encoding="utf-8") as f:
        text2 = f.read()

    headers = {
        # Request headers
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': microsoft_key,
    }

    params = urllib.urlencode({
    })

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/academic/v1.0/similarity?%s" % params, "s1=<first " +
                     str(text1.encode('utf-8')) + "to compare>&s2=<second " +
                     str(text2.encode('utf-8')) + "to compare>", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("{}".format(e))

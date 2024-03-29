import requests
import json
from urls import url, token

def get_depression_scoring(userId):
    # try:
    # Api = 'http://localhost:8000/OpenHealthBot/OpenHealthAssessmentByUserId/{}/'.format(userId)
    # headers = {'Content-Type': 'application/json',
    #            'Authorization': 'Bearer <replace the token with open health bot Api (https://github.com/vivifyhealthcare/Open-Health-Bot-API) >'}
    # response = requests.get(url=Api, headers=headers)

    api = url+'OpenHealthBot/OpenHealthAssessmentByUserId/{}/'.format(userId)
    headers = {'Content-Type': "application/json",'Authorization': token}
    response = requests.get(api,headers=headers)
    data = response.json()['Result']
    # print(data)
    concatination = ''
    try:
        a = data['Risk to Depression']
        # a1 = data['Risk to Depression'][1:45]
        b = " ".join(map(str, a))
        # b1 = " ".join(map(str, a1))
        # print(concatination[9:])
        concatination += b
        return concatination[9:]
    except:
        a = 'No'
        concatination += a
        print(concatination)
    return concatination
# print(get_depression_scoring(17))
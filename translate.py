import re
import os
import sys
import json
import urllib.request

from mattermost_bot.bot import listen_to

# translate KR - EN
@listen_to('`ko` (.*)')
def KR_translate(message, translate):
    client_id =  "<PAPAGO ID>"
    client_secret = "<PAPAGO PASSWORD>"
    encText = urllib.parse.quote(translate)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        dict = json.loads(response_body)
        translatedText = dict['message']['result']['translatedText']
        message.send('`En` : %s' % translatedText)
        
    else:
        print("Error Code:" + rescode)
    


# translate EN - KR
@listen_to('`en` (.*)')
def EN_translate(message, translate):
    client_id =  "<PAPAGO ID>"
    client_secret = "<PAPAGO PASSWORD>"
    encText = urllib.parse.quote(translate)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        dict = json.loads(response_body)
        translatedText = dict['message']['result']['translatedText']
        message.send('`Ko` : %s' % translatedText)
        
    else:
        print("Error Code:" + rescode)
        

# translate Unsupported Language
@listen_to('`(.*)` (.*)')
def not_support(message, mag1, mag2):
    if mag1 == 'ko':
        return 0;
    elif mag1 == 'en':
        return 0;
    else:
        message.send("""| 지원하는 언어 & Support Language |
                        | :----------------------------
                        | ko (Korean)|
                        | en (English)|""")
       
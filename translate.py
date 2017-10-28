import urllib.request
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

url = "https://openapi.naver.com/v1/papago/n2mt"#번역 API 사용을 위한 주소
client_id = "<ID>"              #비로그인 API 사용을 위한 아이디
client_secret = "<PASSWORD>"                    #비로그인 API 사용을 위한 비밀번호

@listen_to('koen (.*)')                         #대화 채널에서 입력을 받으면 호출
def KoListen(message,original):
    translated = trans(original,1)
    message.reply('%s' % translated)

@respond_to('koen (.*)')                        #DM 또는 @Botname에서 입력을 받으면 호출
def KoRespond(message,original):
    translated = trans(original,1)
    message.reply('%s' % translated)

@listen_to('enko (.*)')
def EnListen(message,original):
    translated = trans(original,2)
    message.reply('%s' % translated)

@respond_to('enko (.*)')
def EnRespond(message,original):
    translated = trans(original,2)
    message.reply('%s' % translated)

def trans(input,dist):
    if dist == 1:                               #한영 분기
        src="ko"
        trg="en"
    if dist == 2:
        src="en"
        trg="ko"
    data = "source="+src+"&target="+trg+"&text=" + input
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data = data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        input = response_body.decode('utf-8')
        splited = input.split('translatedText":"')  #출력값 자르기
        moresplited = splited[1].split('"}}}')
        return moresplited[0]
    else:
        print("Error Code:" + rescode)              #오류 코드 출력

KoListen.__doc__ = "Translate Korean to English"
EnListen.__doc__ = "Translate English to Korean"
KoRespond.__doc__ = "Translate Korean to English"
EnRespond.__doc__ = "Translate English to Korean"

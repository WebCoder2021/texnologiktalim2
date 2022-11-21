import requests
from all_test.models import UserTestResult

from home.models import IncomingMessages
token='5787008554:AAFRcFiz8vbHsaShhfk85DFqm7mLhaOqLe4'
chat_id='-1001890361218'

def bot_send(text,img=None):
    if img:
        resp = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&caption={text}&parse_mode=html',files=img)
    else: resp = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=html')
    return resp

def get_mess(id):
    m = IncomingMessages.objects.filter(id=id).first()
    if m:
        data = ""
        data += f'%23xabar\n'
        data += f'<b>✍️ Saytdan kelgan xabar</b>  №{m.id}\n\n'
        data+=f'<b>👤FIO</b>: {m.fullname}\n'
        data+=f'<b>🏢Fakultet</b>: {m.faculty}\n'
        data+=f'<b>🪪Yo\'nalish</b>: {m.direction}\n'
        data+=f'<b>📱Telefon raqam</b>: {m.phone}\n'
        data+=f'<b>✉️Xabar</b>: {m.content}\n'
        return data

def get_test_result(id):
    r = UserTestResult.objects.filter(id=id).first()
    if r:
        data = ""
        data += f'№{r.id} <b>✍️ TEST NATIJASI</b>  \n\n'
        data+=f'<b>👤 FIO</b>: {r.user.get_full_name()}\n\n'
        if r.user.faculty:
          data+=f'🏛 <b>Fakultet</b>: {r.user.faculty}\n\n'
        if r.user.direction:
          data+=f' <b>🔗 Yo\'nalish</b>: {r.user.direction}\n\n'
        if r.user.group:
          data+=f'<b>🏫 Guruh</b>: {r.user.group}\n\n'
        data+=f'<b>🗓 Testlar soni</b>: {r.tests.all().count()}\n\n'
        data+=f'<b>✅ To\'g\'ri javoblar soni</b>: {r.is_trues()}\n\n'
        data+=f'<b>🏆 Natija</b>: {r.result()}%\n'
        return data
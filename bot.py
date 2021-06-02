from vkbottle.bot import Bot, Message
import requests, time, datetime, asyncio, vk_api, sqlite3
from bs4 import BeautifulSoup

name_days = {'mon': 'Понедельник', 'tue': 'Вторник', 'wed': 'Среда', 'thu': 'Четверг', 'fri': 'Пятница', 'sat': 'Суббота', 
             'sun': 'Воскресенье', 'пн': 'Понедельник', 'вт': 'Вторник', 'ср': 'Среда', 'чт': 'Четверг', 'пт': 'Пятница',
             'сб': 'Суббота', 'вс': 'Воскресенье'}

async def WEATtimer2(time2):
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        q = requests.get(
            'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BA%D0%B0%D0%BB%D0%B0%D1%87+%D0%B2%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BA%D0%B0%D0%BB%D0%B0%D1%87+%D0%B2%D0%BE%D1%80%D0%BE&aqs=chrome.0.35i39i285j69i57j0i457j0l5.4995j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)

        soup = BeautifulSoup(q.content, 'html.parser')
        items = soup.findAll("div", {"class": "R3Y3ec rr3bxd", 'class': 'wob_df'})
        Ldays = []
        r = 1
        for item in items:
            if r == 1:
                Ldays.append({
                    'title': item.find('div', {'class': 'QrNVmd Z1VzSb'}).get_text(strip=True),
                    'weather': str(item.find('div', {'class': 'DxhUm'})).split(' ')[2].split('=')[1].replace('"',
                                                                                                             '').replace(
                        '"', '')
                })
            else:
                pass
            if Ldays[-1]['title'] == 'вс':
                r = 0
        SDays = str()
        for day in Ldays:
            if day['weather'].lower() in ['дождь', 'дожди', 'местами', 'rain', 'showers']:
                if day['weather'].lower() == 'местами':
                    SDays = f'{SDays}\n[&#127783;] > {name_days.get(day["title"])} - дождь |'
                else:
                    SDays = f'{SDays}\n[&#127783;] > {name_days.get(day["title"])} - дождь |'
            elif day["weather"].lower() in ['гроза', 'грозы', 'thunderstorm']:
                SDays = f'{SDays}\n[&#127785;] > {name_days.get(day["title"])} - гроза |'
            elif day["weather"].lower() in ['ясно', 'clear']:
                SDays = f'{SDays}\n[&#127780;] > {name_days.get(day["title"])} - ясно |'
            elif day["weather"].lower() in ['облачно', 'cloudy']:
                SDays = f'{SDays}\n[&#127781;] > {name_days.get(day["title"])} - облачно |'
            elif day["weather"].lower() in ['переменная облачность', 'partially cloudy']:
                SDays = f'{SDays}\n[&#9925;] > {name_days.get(day["title"])} - переменная облачность |'
        #print(Ldays[0]['weather'].lower())
        if Ldays[0]["weather"].lower() in ['дождь', 'дожди', 'гроза', 'грозы', 'местами']:
            vkA.messages.send(user_id='487334215', message=f'Сегодня ожидаются дожди!\nПроверено в {str(datetime.timedelta(seconds=round(time.time()) + 10800)).split(" ")[2]}', random_id=0)
        await asyncio.sleep(time2)

async def CHECK_WEATHER():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    q = requests.get('https://www.google.com/search?q=погода+калач+воронежская+область', headers=headers)
    soup = BeautifulSoup(q.content, 'html.parser')
    items = soup.findAll("div", {"class": "R3Y3ec rr3bxd", 'class': 'wob_df'})
    Ldays = []
    r = 1
    for item in items:
        if r == 1:
            Ldays.append({
                'title': item.find('div', {'class': 'QrNVmd Z1VzSb'}).get_text(strip=True),
                'weather': str(item.find('div', {'class': 'DxhUm'})).split(' ')[2].split('=')[1].replace('"', '').replace(
                    '"', '')
            })
        else:
            pass
        if Ldays[-1]['title'].lower() == 'вс' or Ldays[-1]['title'].lower() == 'sun':
            r = 0
    SDays = str()
    for day in Ldays:
        if day['weather'].lower() in ['дождь', 'дожди', 'местами', 'rain', 'showers']:
            if day['weather'].lower() == 'местами':
                SDays = f'{SDays}\n[&#127783;] > {name_days.get(day["title"])} - дождь |'
            else:
                SDays = f'{SDays}\n[&#127783;] > {name_days.get(day["title"])} - дождь |'
        elif day["weather"].lower() in ['гроза', 'грозы', 'thunderstorm']:
            SDays = f'{SDays}\n[&#127785;] > {name_days.get(day["title"])} - гроза |'
        elif day["weather"].lower() in ['ясно', 'clear']:
            SDays = f'{SDays}\n[&#127780;] > {name_days.get(day["title"])} - ясно |'
        elif day["weather"].lower() in ['облачно', 'cloudy']:
            SDays = f'{SDays}\n[&#127781;] > {name_days.get(day["title"])} - облачно |'
        elif day["weather"].lower() in ['переменная облачность', 'partially cloudy']:
            SDays = f'{SDays}\n[&#9925;] > {name_days.get(day["title"])} - переменная облачность |'
    return [Ldays, SDays]

async def alarmclock(min=0, name='1', *args):
    tm = round(min * 60)
    g = 0
    while g == 1:
        await asyncio.sleep(3)
        print('asf')
        g = 1

async def update_u(col, val, key):
    db.execute(f'UPDATE USERS SET "{col}" = "{val}" WHERE "user_id" = "{key}"')
    dbconn.commit()

async def insert_u(user_id):
    db.execute(f'INSERT INTO USERS(user_id, vip_w, date_reg) VALUES({user_id}, 1, {round(time.time())})')
    dbconn.commit()

async def select_u(uid):
    db.execute(f'SELECT * FROM USERS WHERE "user_id" = "{uid}"')
    return db.fetchone()

dbconn = sqlite3.connect('database/DATABASE.sql')
db = dbconn.cursor()

vkconn = Bot(token='f2db190e74d543b75f710f9e33fb5986d92f1b3988d4e64747a3b2ff28396d2fafe9124de597d76b5e37b')

vkA = vk_api.VkApi(token='f2db190e74d543b75f710f9e33fb5986d92f1b3988d4e64747a3b2ff28396d2fafe9124de597d76b5e37b')
vkA = vkA.get_api()

@vkconn.on.message()
async def HANDLER(msg: Message):
    if (await select_u(msg.from_id)) is None:
        await insert_u(msg.from_id)
    if msg.text.lower() in ['помощь', 'команды', 'меню']:
        await msg.answer('[&#128214;] > Что я умею:'
                         '\n[&#127760;] > Погода - просмотр погоды')
        return
    elif msg.text.lower() == 'погода':
        await msg.answer(f'[&#128467;] > Погода на оставшуюся неделю: {(await CHECK_WEATHER())[1]}'
                         f'\n[&#128197;] > Погода сейчас: {(await CHECK_WEATHER())[1].split(" |")[0]}')
        return
    else:
        await msg.answer(user_id=487334215, message='Напиши "помощь", я даун просто, не умею учиться.')
        return

async def MAIN():
    vkconn.run_forever()

lp = asyncio.get_event_loop()
tasks = [
    lp.create_task(MAIN()),
    lp.create_task(WEATtimer2(7200))
    #lp.create_task(alarmclock())
]
while True:
    lp.run_until_complete(asyncio.wait(tasks))
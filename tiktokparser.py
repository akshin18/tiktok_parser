import requests
import re
import time




from aiogram import Bot, Dispatcher,executor, types


bot = Bot(token = '')

dp = Dispatcher(bot)

tvar = True

@dp.message_handler()
async def da(message: types.Message):
    if message.from_user.id == 653327229:
        print('hello')
        serch = r'''playAddr":"(.*?)a=1233'''

        s = requests.Session()

        cooko = {

            'sid_tt': 'a03c0037a8a490b9a224ebccafd427d4',
            'sessionid_ss': 'a03c0037a8a490b9a224ebccafd427d4',
            'sessionid': 'a03c0037a8a490b9a224ebccafd427d4'

        }

        r = s.get(
            'https://m.tiktok.com/api/following/item_list/?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.141+Safari%2F537.36+OPR%2F73.0.3856.344&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ru-RU&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.141+Safari%2F537.36+OPR%2F73.0.3856.344&browser_online=true&ac=4g&timezone_name=Asia%2FBaku&page_referer=https:%2F%2Fwww.tiktok.com%2F%3Flang%3Dru-RU&priority_region=AZ&verifyFp=verify_klazppxq_vr1K4rhg_9cmh_4q9l_BKOv_961DHMfkJWGU&appId=1233&region=TR&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6930618450813568514&tt-web-region=AZ&uid=6869816700666528769&level=1&count=30&cursor=0&language=ru-RU&pullType=1',
            cookies=cooko)

        video_link = re.findall(serch, r.text)
        r = requests.get(video_link[0])
        with open('conte.mp4', 'wb')as f:
            f.write(r.content)
        with open('conte.mp4', 'rb')as f:

            await bot.send_video(-1001388181569,f)



@dp.channel_post_handler(chat_id=-1001388181569)
async def da(post: types.Message):
        global tvar
        if tvar == True:
            tvar = False

            await tata()







async def tata():
    while True:
        try:

            print('start2')
            serch = r'''playAddr":"(.*?)a=1233'''
            s = requests.Session()
            cooko = {
                'sid_tt': 'a03c0037a8a490b9a224ebccafd427d4',
                'sessionid_ss': 'a03c0037a8a490b9a224ebccafd427d4',
                'sessionid': 'a03c0037a8a490b9a224ebccafd427d4'
            }
            r = s.get(
                'https://m.tiktok.com/api/following/item_list/?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.141+Safari%2F537.36+OPR%2F73.0.3856.344&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ru-RU&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.141+Safari%2F537.36+OPR%2F73.0.3856.344&browser_online=true&ac=4g&timezone_name=Asia%2FBaku&page_referer=https:%2F%2Fwww.tiktok.com%2F%3Flang%3Dru-RU&priority_region=AZ&verifyFp=verify_klazppxq_vr1K4rhg_9cmh_4q9l_BKOv_961DHMfkJWGU&appId=1233&region=TR&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6930618450813568514&tt-web-region=AZ&uid=6869816700666528769&level=1&count=2&cursor=0&language=ru-RU&pullType=1',
                cookies=cooko)
            video_link = re.findall(serch, r.text)
            r = requests.get(video_link[0])
            with open('conte.mp4', 'wb')as f:
                f.write(r.content)
            print('start3')
            with open('conte.mp4', 'rb')as f:
                await bot.send_video(-1001388181569, f)
            time.sleep(4000)
        except Exception as e:
            await tata()








executor.start_polling(dp, skip_updates=True)
# SiteOverseer by SfortzaPhantom
# version 1.0

import requests, datetime, time
from datetime import timedelta

def statuscheck():
    online = datetime.datetime.now() # this one will be soon-ish configured for uptime portion of SiteOverseer
    ejected = 0 # sets an argument for 403 error
    print('SiteOverseer v 1.0 by SfortzaPhantom')
    print('First launch detected at ' + online.strftime("%d.%m.%y, %H:%M:%S."))
    checks = 0 # setting up the checks counter here
    print('Since it is the first time you\'re (re)launching the script, please state which site should be tried to ping')
    site = input() # stating the site we're going to ping. Enter valid site, otherwise the program will crash with code 1
    while True:
        resp = requests.get('https://' + site, verify=False)
        respcode = resp.status_code
        now = datetime.datetime.now()
        # here we can get some important things, like 
        if resp.status_code == 200: # this one will return the routine on resp code 200
            checks = checks + 1
            nextcheck = now + timedelta(minutes=5) # that thing is responsible for getting the time for next check
            sender = requests.get(
                'https://api.telegram.org/botHOLDER/sendMessage?chat_id=@CHANNELHOLDER&parse_mode=markdown&text=' +
                '*🔍 Let\'s see if ' + site + ' works by date of ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + '!*\n\n🟩 *Site status:* OK (access code: ' + str(respcode) + ').\n'
                '*⚖ Actions:* you don\'t have to do anything as everything works just fine now. \n'
                '*⌛ Next check time:* ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S")) + '.\n*👁 Total checks:* '
                + str(checks) + ' _(as SiteOverseer detects)_.&disable_notification=true')
            print('Telegram API request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(sender.status_code))
            print('Site ' + site + ' GET request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(resp.status_code))
            print('This is check № ' + str(checks))
            print('Next GET request will be delivered at ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S")))
            # print the information into log
            time.sleep(300) # waiting for 5 mins just to suffer from cringe and to ensure that next check will be in 5 mins. Actually it _might_ be delayed for one-two seconds.
        elif resp.status_code == 403:
            checks = checks + 1
            nextcheck = now + timedelta(minutes=15)
            sender = requests.get('https://api.telegram.org/botHOLDER/sendMessage?chat_id=@CHANNELHOLDER&parse_mode=markdown&text=' +
            '*🔍 Let\'s see if ' + 'google.com' + ' works by date of ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + '!*\n\n⛔ *Site status:* SiteOverseer is blocked and can\'t retrieve the status of the site! (access code: ' + str(respcode) + ')\n'
            '*⚖ Actions:* we\'ve contacted this bot admins, so they know that bot is blocked.\n⌛ *Next check time: * ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S")) + '.\n'
            '*👁 Total checks:* '
                + str(checks) + ' _(as SiteOverseer detects)_.&disable_notification=true')
            if ejected == 0:
                sender = requests.get('https://api.telegram.org/botHOLDER/sendMessage?chat_id=-CHANNELHOLDER&parse_mode=markdown&text=Bot is down! '
                                      'Please maintain the script: @someone\_you\_want\_to\_ping\_once')
            print ('Info sent!')
            ejected = ejected + 1
            if ejected == 1:
                pass # that thing pings only ONCE for each instance of SiteOverseer banned. Go ahead and restart it when it's blocked!
            print('Telegram API request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(sender.status_code))
            print('Site ' + site + ' GET request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(resp.status_code))
            print('This is check № ' + str(checks))
            print('Next GET request will be delivered at ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S")))
            time.sleep(900) # wait 15 mins, so it doesn't spam a lot to the channel
        else:
            checks = checks + 1
            nextcheck = now + timedelta(minutes=5)
            sender = requests.get(
                'https://api.telegram.org/botHOLDER/sendMessage?chat_id=@CHANNELHOLDER&parse_mode=markdown&text=' +
                '*🔍 Let\'s see if ' + site + ' works by date of ' + str(now.strftime(
                    "%d.%m.%Y, %H:%M:%S")) + '!*\n\n🟥 *Site status:* downed (access code: ' + str(
                    respcode) + ')\n'
                                '*⚖ Actions:* contact the support of the site being checked. Or just wait if site will rise up again.\n'
                                '*⌛ Next check time:* ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S") + '.\n*👁 Total checks:* '
                + str(checks) + ' _(as SiteOverseer detects)_.&disable_notification=true'))
            print('Telegram API request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(sender.status_code))
            print('Site ' + site + ' GET request at ' + str(now.strftime("%d.%m.%Y, %H:%M:%S")) + ' returned code ' + str(resp.status_code))
            print('This is check № ' + str(checks))
            print('Next GET request will be delivered at ' + str(nextcheck.strftime("%d.%m.%Y, %H:%M:%S")))
            time.sleep(300)
            # basically same routine as first one


statuscheck() # let's call the func
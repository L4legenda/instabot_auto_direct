
import instabot

name = "****"

follow = []

nowFollow = []

lastFollow = []

bot = instabot.Bot()
bot.login()

follow = bot.get_user_followers(name)


while True:
    bot.small_delay()
    nowFollow = bot.get_user_followers(name)

    _nf = nowFollow

    follow = set(follow)
    nowFollow = set(nowFollow)

    lastFollow = list( nowFollow.difference(follow) )

    print("new follow", lastFollow)

    for i in lastFollow:
        bot.send_message("test follow" ,i)

    follow = _nf
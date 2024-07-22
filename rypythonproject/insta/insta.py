"""
An Instagram bot is a service that can automatically perform actions like liking, commenting, and following other Instagram accounts.
 Bots can also follow other accounts, like posts, and leave comments on targeted lists of Instagram accounts. 

"""

from instabot import Bot
bot=Bot()
bot.login( username=" ",password="")
bot.follow("wscubetechindia")
#to upload image
#bot.upload_photo("link or path of image",caption="i love python")
bot.unfollow("ronakyadav_5755")
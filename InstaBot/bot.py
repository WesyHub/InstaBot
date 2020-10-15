from instapy import InstaPy
from instapy_chromedriver import binary_path
import configparser

"""
Config section in Config.ini

Username
Password
Tags
"""
config_path = 'config.ini'
cparser = configparser.ConfigParser()
cparser.read(config_path)
user = cparser['AUTH']['USERNAME']
passw = cparser['AUTH']['PASSWORD']
tag1 = cparser['HTAGS']['TAG1']
tag2 = cparser['HTAGS']['TAG2']
tag3 = cparser['HTAGS']['TAG3']
tag4 = cparser['HTAGS']['TAG4']

#Login section
session = InstaPy(username=user, password=passw, headless_browser=False)
session.login()


#follow section
session.set_do_follow(enabled=True, percentage=25, times=2)
#session.follow_by_tags(['Kidding', 'FunnyVideos', 'memes'], amount=25)

#Comment section
session.set_do_comment(enabled=True, percentage=10)
session.set_comments([u'Love it 😍', u'Nice post 👌', u'Im done 😂😂😂'])
#session.set_do_comment(True, percentage=25)

#interact section 
#session.set_user_interact(amount=6, randomize=True, percentage=72, media='Photo')

#like section
session.like_by_tags([tag1, tag2, tag3, tag4], amount=200)
#session.like_by_feed(amount=15)

#follow section2
session.follow_likers(['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)

#Unfollow section
session.unfollow_users(amount=200, instapy_followed_enabled=True, nonFollowers=True, style="FIFO", unfollow_after=90*60*60, sleep_delay=501)




session.end()

from instapy import InstaPy
from credentials import insta_username, insta_password

session = InstaPy(username=insta_username, password=insta_password)
session.login()
session.follow_user_followers(['spotify'], amount=10, randomize=True, sleep_delay=60) #by default, sleep_delay=600
#TODO: myPic = lastUploadedPic
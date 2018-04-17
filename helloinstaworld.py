from instapy import InstaPy
from credentials import insta_username, insta_password

session = InstaPy(username=insta_username, password=insta_password)
session.login()
from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8f8629885b7fd647e3a5006fb27c38d6")
      API_ID = int(getenv("API_ID", "21478717"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8095404437:AAFaDzSAPuk1EjQM0zBTU3IZ8kXz89VcAVI")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002469727946:-1002441740132").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

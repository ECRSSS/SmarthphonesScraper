from ScraperBot.AliBot import AliBot
from DataBase.Connection import Connection


itemName="Mi 6"


alibot = AliBot()
items=alibot.run(itemName)
alibot.close()

con=Connection()
con.init()
con.fillBaseWithItems(itemName,items)
con.close()

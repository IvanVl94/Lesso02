from adress import Adress
from mailing import Mailing

to_address = Adress(" 8888222", " Воркута",  " Сизам", " 21",  " 4")
from_address = Adress(" 2223232", " Киркуду", " Волшебная", " 12", " 4")


mail = Mailing(to_address, from_address, 2770, "HYD567")

print(mail)
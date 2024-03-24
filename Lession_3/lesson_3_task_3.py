from classes.address import Address
from classes.mailing import Mailing

letter = Mailing(Address("129090", "город Москва", "проспект Мира", "дом 22", "квартира 15"),
                 Address("167019", "город Сыктывкар", "улица Быковского", "дом 3", "квартира 11"),
                 "1234567890", "256")

print(f"Отправление {letter.track} из {letter.from_address} в {letter.to_address}. Стоимость {letter.cost} рублей")
from classes.smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14 Pro Max", "+79552345821"))
catalog.append(Smartphone("Samsung", "Galaxy S24 Ultra", "+79854231685"))
catalog.append(Smartphone("Xiaomi", "Redmi K60", "+7985023156"))
catalog.append(Smartphone("Honor", "Magic5", "+79034257614"))
catalog.append(Smartphone("Sony", "Xperia 10 Plus", "+79250132659"))

for phone in catalog:
    print(f"{phone.mark} - {phone.model}. {phone.number}")
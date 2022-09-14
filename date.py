from datetime import date, datetime

dt = datetime.now().strftime('%d.%m.%y')
# dt_str = datetime.
asdf = int(date(datetime.now().strftime('%d.%m.%y')))
print(asdf)

#выводим дату (вчера)
print()

#выводим текущую дату
print(datetime.now().strftime('%d.%m'))
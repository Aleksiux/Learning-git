import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''


# 2 ---- -- - - - - -
# pattern = re.compile(r'\w*\s\d{2},\s\d{4}')
# from_text = pattern.findall(text)
# for _ in from_text:
#     print(_)
# 3

# def keistidata(data):
#     return re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\3-\\2-\\1', data)
#
#
# datanew = "10-03-1998"
# print("dd.mm.yyyy ", datanew)
# print("yyyy mm dd: ", keistidata(datanew))

# dien_men_met = input("Iveskite data formatu (diena.menuo.metai 17.06.2222): ")
#
# pattern = re.compile(r'(?P<diena>\d{2})\.(?P<menuo>\d{2})\.(?P<metai>\d{4})')
# result = pattern.search(dien_men_met)
# print(f'{result.group("metai")}.{result.group("menuo")}.{result.group("diena")}')

# pattern = re.compile(r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})')
#
# user_date = '23.11.1989'
#
# result = pattern.search(user_date)
#
# print(f'{result.group("year")} {result.group("month")} {result.group("day")}')


# def split_lines(events):
#     for indx, line in enumerate(events.splitlines()):
#         pattern = re.compile(r'(.*?):(.*)')
#         result = pattern.search(line)
#
#         if result:
#             print(f"{indx + 1}.")
#             print(f"Event: {result.group(1)}")
#             print(f"Date: {result.group(2)}")
#
#
# split_lines(text)
# pattern = re.compile(r'(.*?):(.*)')
# result = pattern.search(text)
# counter = 1
# for (words, date) in re.findall(pattern, text):
#     print(f"{counter}.")
#     counter +=1
#     print(f"Event: {words}\nDate:{date}")


def cenzura(tekstas, *keiksmai):
    swear_words = [*keiksmai]
    for _ in swear_words:
        pattern = re.compile(_, re.I)
        x = len(_)
        tekstas = pattern.sub(f'{_[0]}{"*" * (x - 2)}{_[-1]}', tekstas)
    print(tekstas)


#
cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')

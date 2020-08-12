#! python3
import re

valid_date = re.compile(r"([0-3]\d)(/|-|.)([0-1]\d)(/|-|.)([1-2]\d\d\d)")

def find_valid_date(text):
    dates = valid_date.findall(text)
    for date in dates:
        if (date[0][0] == "3" and date[0][1] > 1)\
        or (date[2][0] == 1 and date[2][1] > 2)\
        or (date[2] in ["04, 06, 09, 11"] and date[0] != 30)\
        or (date[2] in ["01","03","05","07","08","10","12"] and date[0] != 31):
            del date
        elif (date[2] == "02" and date[0] != 28)\
        or (date[4] % 4 == 0 and date[4] % 100 != 0 )\
        and (date[2] == "02" and date[0] != 29):
            del date
    return dates

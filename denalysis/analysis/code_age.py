from calendar import monthrange
from datetime import datetime, timedelta
import logging

class CodeAge:
    def __init__(self, data):
        self.data = data
        logging.debug("CodeAge data injected: \n" + data)

    def code_age(self):
        aging = {}
        for commit in self.data:
            for entry in commit.get_files():
                if entry in aging.keys():
                    current = aging[entry.get_name()]
                    found = commit.date
                    if found > current:
                        aging[entry.get_name()] = found
                else:
                    aging[entry.get_name()] = commit.date

        for entry in aging.keys():
            aging[entry] = str(1+CodeAge.monthdelta(aging[entry],datetime.date(datetime.today())))

        return aging

    def monthdelta(d1, d2):
        delta = 0
        while True:
            mdays = monthrange(d1.year, d1.month)[1]
            d1 += timedelta(days=mdays)
            if d1 <= d2:
                delta += 1
            else:
                break
        return delta

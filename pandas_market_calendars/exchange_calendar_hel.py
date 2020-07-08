from datetime import time

from pandas.tseries.holiday import Holiday, GoodFriday, EasterMonday, AbstractHolidayCalendar
from pytz import timezone

from .common_holidays import (
    new_years_day,
    epiphany,
    european_labour_day,
    ascension_day,
    midsummer_eve,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)
from .market_calendar import MarketCalendar #HolidayCalendar

NewYearsDay = new_years_day()

Epiphany = epiphany()

LabourDay = european_labour_day()

AscensionDay = ascension_day()

MidsummerEve = midsummer_eve()

IndependenceDay = Holiday('Finland Independence Day', month=12, day=6)

ChristmasEve = christmas_eve()
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve()


class HELExchangeCalendar(MarketCalendar):
    """
    Calendar for the Helsinki Stock Exchange in Finland.
    Open Time: 10:00 AM, CET (Eastern European Time)
    Close Time: 6:30 PM, CET (Eastern European Time)
    Regularly-Observed Holidays:
      - New Year's Day
      - Epiphany
      - Good Friday
      - Easter Monday
      - Labour Day
      - Ascension Day
      - Midsummer Eve
      - Independence Day
      - Christmas Eve
      - Christmas Day
      - Boxing Day
      - New Year's Eve
    Early Closes:
      - None
    """

    aliases = ['HEL']

    @property
    def name(self):
        return "HEL"

    @property
    def tz(self):
        return timezone("Europe/Helsinki")

    @property
    def open_time_default(self):
        return time(10, 1, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(18, 30, tzinfo=self.tz)

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            NewYearsDay,
            Epiphany,
            GoodFriday,
            EasterMonday,
            LabourDay,
            AscensionDay,
            MidsummerEve,
            IndependenceDay,
            ChristmasEve,
            Christmas,
            BoxingDay,
            NewYearsEve,
        ])
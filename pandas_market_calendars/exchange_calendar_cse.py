from datetime import time

from pandas.tseries.holiday import (
    Holiday,
    GoodFriday,
    Easter,
    EasterMonday,
)
from pandas.tseries.offsets import Day
from pytz import timezone

from .common_holidays import (
    new_years_day,
    maundy_thursday,
    ascension_day,
    whit_monday,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)
from .market_calendar import HolidayCalendar, MarketCalendar

NewYearsDay = new_years_day()

MaundyThursday = maundy_thursday()
GeneralPrayerDay = Holiday(
    'General Prayer Day',
    month=1,
    day=1,
    offset=[Easter(), Day(26)],
)
AscensionDay = ascension_day()
BankHoliday = Holiday(
    'Bank Holiday',
    month=1,
    day=1,
    offset=[Easter(), Day(40)],
    start_date='2009',
)
WhitMonday = whit_monday()

ConstitutionDay = Holiday('Constitution Day', month=6, day=5)

ChristmasEve = christmas_eve()
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve()


class CSExchangeCalendar(MarketCalendar):
    """
    Calendar for the Copenhagen Stock Exchange in Denmark.
    Open Time: 9:00 AM, CET (Central European Time)
    Close Time: 5:00 PM, CET (Central European Time)
    Regularly-Observed Holidays:
      - New Year's Day
      - Maundy Thursday
      - Good Friday
      - Easter Monday
      - General Prayer Day
      - Ascension Day
      - Bank Holiday
      - Whit Monday
      - Constitution Day
      - Christmas Eve
      - Christmas Day
      - Boxing Day
      - New Year's Eve
    Early Closes:
      - None
    """

    aliases = ['CSE']

    @property
    def name(self):
        return "CSE"

    @property
    def tz(self):
        return timezone("Europe/Copenhagen")

    @property
    def open_time_default(self):
        return time(9, 1, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(17, 0, tzinfo=self.tz)

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            NewYearsDay,
            MaundyThursday,
            GoodFriday,
            EasterMonday,
            GeneralPrayerDay,
            AscensionDay,
            BankHoliday,
            WhitMonday,
            ConstitutionDay,
            ChristmasEve,
            Christmas,
            BoxingDay,
            NewYearsEve,
        ])
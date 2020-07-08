from datetime import time

from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    Holiday,
    GoodFriday,
    Easter,
    EasterMonday,
    DateOffset,
    FR,
)
from pandas.tseries.offsets import Day
from pytz import timezone

from .common_holidays import (
    new_years_day,
    epiphany,
    maundy_thursday,
    ascension_day,
    whit_monday,
    european_labour_day,
    midsummer_eve,
    christmas_eve,
    christmas,
    boxing_day,
    new_years_eve,
)
from .market_calendar import MarketCalendar #HolidayCalendar

WEEKDAYS = (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY)

NewYearsDay = new_years_day()

DayBeforeEpiphany = Holiday(
    'Day Before Epiphany',
    month=1,
    day=5,
    days_of_week=WEEKDAYS,
)
Epiphany = epiphany()

DayBeforeLabourDay = Holiday(
    'Day Before Labour Day',
    month=4,
    day=30,
    days_of_week=WEEKDAYS,
)
LabourDay = european_labour_day()

MaundyThursday = maundy_thursday(days_of_week=WEEKDAYS)

DayBeforeAscensionDay = Holiday(
    'Day Before Ascension Day',
    month=1,
    day=1,
    offset=[Easter(), Day(38)],
)
AscensionDay = ascension_day()
WhitMonday = whit_monday(end_date='2005')

NationalDay = Holiday('Sweden National Day', month=6, day=6, start_date='2004')

MidsummerEve = midsummer_eve()

# This falls on the Friday between October 30th and November 5th.
AllSaintsEve = Holiday(
    "All Saints' Eve",
    month=10,
    day=30,
    offset=DateOffset(weekday=FR(1)),
)

ChristmasEve = christmas_eve()
Christmas = christmas()
BoxingDay = boxing_day()

NewYearsEve = new_years_eve()


class STOExchangeCalendar(MarketCalendar):
    """
    Calendar for the Stockholm Stock Exchange in Sweden.
    Open Time: 9:00 AM, CET (Central European Time)
    Close Time: 5:30 PM, CET (Central European Time)
    Regularly-Observed Holidays:
      - New Year's Day
      - Epiphany
      - Good Friday
      - Easter Monday
      - Labour Day
      - Ascension Day
      - National Day
      - Midsummer Eve
      - Christmas Eve
      - Christmas Day
      - Boxing Day
      - New Year's Eve
    Holidays No Longer Observed:
      - Whit Monday
    Early Closes:
      - Day before Epiphany
      - Maundy Thursday
      - Day before Labour Day
      - Day before Ascension Day
      - All Saints' Eve
    """

    aliases = ['STO']

    @property
    def name(self):
        return "STO"

    @property
    def tz(self):
        return timezone("Europe/Stockholm")

    @property
    def open_time_default(self):
        return time(9, 1, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(17, 30, tzinfo=self.tz)

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            NewYearsDay,
            Epiphany,
            GoodFriday,
            EasterMonday,
            LabourDay,
            AscensionDay,
            WhitMonday,
            NationalDay,
            MidsummerEve,
            ChristmasEve,
            Christmas,
            BoxingDay,
            NewYearsEve,
        ])

    @property
    def special_closes(self):
        return [(
            time(13, 0, tzinfo=self.tz),
            AbstractHolidayCalendar(rules=[
                DayBeforeEpiphany,
                MaundyThursday,
                DayBeforeLabourDay,
                DayBeforeAscensionDay,
                AllSaintsEve,
            ])
        )]
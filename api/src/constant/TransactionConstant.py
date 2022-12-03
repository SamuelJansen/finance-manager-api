from python_helper import DateTimeHelper
from enumeration.TransactionType import TransactionType
from enumeration.TransactionStatus import TransactionStatus


YEARS_AHEAD = 10


timeNow = DateTimeHelper.timeNow()
dateNow = DateTimeHelper.dateNow()
dateAhead = DateTimeHelper.dateOf(
    dateTime = DateTimeHelper.forcedlyParse(f'{dateNow.year + YEARS_AHEAD}-{dateNow.month:02}-{dateNow.day:02} {timeNow}')
)


DEFAULT_VALUE = 0.0
DEFAULT_TYPE = TransactionType.NONE
DEFAULT_STATUS = TransactionStatus.NONE
DEFAULT_OPERATION_KEY = 'UNKNOWN'

MIN_START_DATE_TIME = DateTimeHelper.forcedlyParse('1969-01-01 00:00:01.000')
MAX_END_DATE_TIME = DateTimeHelper.of(date=dateAhead, time=timeNow) ###- DateTimeHelper.forcedlyParse('2999-12-31 23:59:59.999')

FROM_DATE_TIME_QUERY_KEY = 'fromDateTime'
TO_DATE_TIME_QUERY_KEY = 'toDateTime'
OPERATION_KEY_IN = 'operationKeyList'
USER_KEY = 'userKey'

DATE_TIME_QUERY_KEY_LIST = [
    FROM_DATE_TIME_QUERY_KEY,
    TO_DATE_TIME_QUERY_KEY
]

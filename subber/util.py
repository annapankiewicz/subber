import datetime
import time


def utc_epoch_sec_to_years(sec):
    """Converts seconds from UTC epoch to elapsed time from current time"""

    # Elapsed seconds from time
    elapsed_sec = time.time() - sec

    # Elapsed years from time
    days = datetime.timedelta(seconds=elapsed_sec).days
    return (days/365)


def age_string_from_utc_epoch(sec):
    """Returns elapsed time string (in years) from UTC epoch seconds"""

    y = utc_epoch_sec_to_years(sec)

    if y < 1:
        return 'less than one year.'
    else:
        return '{} years.'.format(y)

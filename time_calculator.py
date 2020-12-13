'''
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
'''

full_day_minutes = 24 * 60
# no libs to be used, otherwise datetime would have these
weekdays = ['', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']


def split_time(time_str, use24=True):
    """ returns a tuple of hours and minutes of a given string in the form of "8:24" or "8:24 AM"; 
        adds +12 to hours if it detects " PM"

    Args:
        time_str (String): daytime string with optional am/pm indicator
        use24 (bool, optional): use 24h format for returned string. Defaults to True.
    """
    (h, m) = map(int, time_str.split(" ")[0].split(":"))
    try:
        period = time_str.split(" ")[1]
    except IndexError:
        period = ""
    if not use24 and h > 12:
        h = h - 12
        period = "PM"
    if time_str[-2:] == "PM":
        h = h + 12

    return (h, m, period)


def make_time(minutes):
    """returns time, period, days added from minutes

    Args:
        minutes (int): minutes
    """
    days_added = 0
    while minutes > full_day_minutes:
        minutes -= full_day_minutes
        days_added += 1

    h = minutes // 60
    m = minutes % 60

    period = "AM"
    if h >= 12:
        if h > 12:
            h = h - 12
        period = "PM"
    return (h, m, period, days_added)


def pad_time(h, m):
    return f'{str(h)}:{str(m).zfill(2)}'


def add_time(start, duration, weekday=""):
    weekday = weekday.lower()
    weekday_idx = weekdays.index(weekday)
    (start_h, start_m, period) = split_time(start)
    start_minutes = start_h * 60 + start_m
    duration_split = split_time(duration)
    duration_minutes = duration_split[0]*60 + duration_split[1]
    (end_h, end_m, period, days_added) = make_time(duration_minutes)

    new_weekday = ''
    days_later = ''
    if days_added > 0:
        days_later = f' ({days_added} days later)'

    new_time = f'{pad_time(end_h, end_m)} {period}{new_weekday}{days_later}'
    return new_time

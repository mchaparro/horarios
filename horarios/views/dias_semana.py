import datetime

one_day = datetime.timedelta(days=1)

def get_semana(date):
  """Return the full week (Monday first) of the week containing the given date.

  'date' may be a datetime or date instance (the same type is returned).
  """
  day_idx = (date.weekday()) % 7  # turn sunday into 0, monday into 1, etc.
  sunday = date - datetime.timedelta(days=day_idx)
  date = sunday
  for n in xrange(7):
    yield date
    date += one_day

def semana_actual():
    return list(get_semana(datetime.datetime.now().date()))
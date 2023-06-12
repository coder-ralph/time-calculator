def add_time(start, duration, day=None):
  # Parsing the start time
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))

  # Parsing the duration
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Converting start time to 24-hour format
  if period == 'PM':
    start_hour += 12

  # Calculating the end time
  end_minute = (start_minute + duration_minute) % 60
  carry_hour = (start_minute + duration_minute) // 60
  end_hour = (start_hour + duration_hour + carry_hour) % 24
  days_later = (start_hour + duration_hour + carry_hour) // 24

  # Converting end time back to 12-hour format
  if end_hour >= 12:
    period = 'PM'
    if end_hour > 12:
      end_hour -= 12
  else:
    period = 'AM'
    if end_hour == 0:
      end_hour = 12

  # Determining the day of the week
  days_of_week = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
  ]
  if day:
    day = day.capitalize()
    start_index = days_of_week.index(day)
    end_index = (start_index + days_later) % 7
    new_day = days_of_week[end_index]
    if days_later == 1:
      new_time = f'{end_hour}:{end_minute:02d} {period}, {new_day} (next day)'
    elif days_later > 1:
      new_time = f'{end_hour}:{end_minute:02d} {period}, {new_day} ({days_later} days later)'
    else:
      new_time = f'{end_hour}:{end_minute:02d} {period}, {new_day}'
  else:
    if days_later == 1:
      new_time = f'{end_hour}:{end_minute:02d} {period} (next day)'
    elif days_later > 1:
      new_time = f'{end_hour}:{end_minute:02d} {period} ({days_later} days later)'
    else:
      new_time = f'{end_hour}:{end_minute:02d} {period}'

  return new_time

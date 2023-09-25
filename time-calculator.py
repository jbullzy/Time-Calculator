def add_time(start, duration, day=None):

  print("==============")

  new_time = ''
  dayassign = 0
  days = [
      'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
      'sunday'
  ]

  if day:
    day = day.lower()
    dayassign = days.index(day)

  time, period = start.split()
  hours, minutes = time.split(':')
  hours, minutes = int(hours), int(minutes)

  hoursp, minutesp = duration.split(':')
  hoursp, minutesp = int(hoursp), int(minutesp)

  if period == 'PM':
    hours += 12

  new_hour = hours + hoursp
  new_minute = minutes + minutesp
  new_hour += new_minute // 60
  new_minute %= 60

  new_period = period

  days_passed = new_hour // 24


  new_hour %= 24

  new_period = 'AM'
  if new_hour >= 12:
    new_period = 'PM'
    new_hour -= 12

  if new_hour == 0:
    new_hour = 12

  
  new_time = f"{new_hour:}:{new_minute:02} {new_period}"

  if days_passed == 1:
    new_time = f"{new_hour:}:{new_minute:02} {new_period} (next day)"

  elif days_passed > 1:
    new_time = f"{new_hour}:{new_minute:02} {new_period} ({days_passed} days later)"

  if day:
    new_day = divmod(days_passed, 7)[1]
    final_day = divmod((dayassign + new_day), 7)[1]
    today = (days[final_day])
    today = today.capitalize()

    new_time = f"{new_hour:}:{new_minute:02} {new_period}, {today}"

    if days_passed == 1:
      new_time = f"{new_hour:}:{new_minute:02} {new_period}, {today} (next day)"
    
    elif days_passed > 1:
      new_time = f"{new_hour}:{new_minute:02} {new_period}, {today} ({days_passed} days later)"

  print(new_time)

  print("==============")

  return new_time

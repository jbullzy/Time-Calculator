def add_time(start, duration, day=None):
#   Initial variable setup
  new_time = ''
  dayassign = 0
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']

# If day argument is given, make it lowercase and assign it a number according to the index
  if day:
    day = day.lower()
    dayassign = days.index(day)

# split the start time into a time (eg: 11:42) and period (eg: PM)
  time, period = start.split()
# split the time into hours and minutes
  hours, minutes = time.split(':')
  hours, minutes = int(hours), int(minutes)
# split the duration into hours and minutes passed
  hoursp, minutesp = duration.split(':')
  hoursp, minutesp = int(hoursp), int(minutesp)

# convert to 24h clock
  if period == 'PM':
    hours += 12

# total hours from the initial time and hours passed
  new_hour = hours + hoursp
# total minutes from initial minutes and minutes passed
  new_minute = minutes + minutesp
# if minutes exceeds 60, add an hour to new_hour
  new_hour += new_minute // 60
# reassign minutes to the remainder of minutes over 60
  new_minute %= 60
# floor divide the total hours by 24 to find the number of days passed
  days_passed = new_hour // 24
# reassign new hour to the remainder over 24
  new_hour %= 24

# creating new_period variable. default AM
  new_period = 'AM'
# if the new hours are over or equal to 12, make new_period PM and 
# reasssign new_hour to be on a 12h clock
  if new_hour >= 12:
    new_period = 'PM'
    new_hour -= 12

# if new_hour is 0 (midnight), reassign it to be 12
  if new_hour == 0:
    new_hour = 12

# if there are no days, no change of day, and no day given, assign new_time
  new_time = f"{new_hour:}:{new_minute:02} {new_period}"

# if all else except one day has passed, assign new_time with "(next day)"
  if days_passed == 1:
    new_time = f"{new_hour:}:{new_minute:02} {new_period} (next day)"

# if all else except multiple days have passed, assign new_time with "('days_passed' days later)"
  elif days_passed > 1:
    new_time = f"{new_hour}:{new_minute:02} {new_period} ({days_passed} days later)"

# addressing if 'day' argument is given. this could get simplified, but for now it works. 
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

  print("=" * len(new_time))
  print(new_time)
  print("=" * len(new_time))

  return new_time


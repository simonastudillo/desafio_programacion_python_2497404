def convert_time(time):
  time_lower = time.lower()
  hour_minute = time_lower.split(':')
  if time_lower[-2:] == 'pm':
    if hour_minute[0] != '12':
      hour_minute[0] = str(int(hour_minute[0]) + 12)
  elif hour_minute[0] == '12':
      hour_minute[0] = '00'
  return ":".join(hour_minute)[:-2]


print(convert_time("12:40AM")) # 00:40
print(convert_time("12:40PM")) # 12:40
print(convert_time("04:59pm")) # 16:59
print(convert_time("10:00:00PM")) # 22:00
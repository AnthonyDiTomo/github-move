time = 21

#If the time of day is before 9 a.m.
if time < 9:
  print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.")
#Otherwise if the time of day is before or exactly 4 p.m.
elif time <= 16:
  print("Working hard or hardly working?")
#Otherwise, if the time of day is before 8 p.m.
elif time <= 20:
  print("How did it get so late so soon?")
#Otherwise, if the time of day is before 10 p.m.
elif time < 22:
  print("A day without sunshine is like, you know, night.")
#Otherwise, for any time 10 p.m. or later
else:
  print("Burning the midnight oil!")
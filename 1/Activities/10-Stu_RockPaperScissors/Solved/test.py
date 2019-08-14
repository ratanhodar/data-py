x = 'y'
previousCount = 0
while x == 'y':
  count = input("how many times?")

  for i in range(previousCount, int(count)):
    print(i)
    previousCount = i

  x = input("continue?")
a = input('Would you like to see stars?')

if a.lower() in ['yes']:
  print('************')

  b = input('Were they pretty? ')
  if b.lower() in ['yes']:
    print('So is your smile, friend')
  else:
    print('To each their own.')

elif a.lower()in['no']:
  print('Then here some mountains and lakes: ^^')

  c = input('Do you feel like going on a hike?')
  print('That\'s good, me too.')

else:
  print('Maybe tomorrow is a better day for a hike.')

  input('      Press enter to continue     ')
  print()
  print()
  print()

  b = input('Would you like to fish?')

  if a.lower() in ['yes']:
    print('  >>(((0) You Caught One!')
  else:
    print('Swimming is fun too. JKJNKJ')

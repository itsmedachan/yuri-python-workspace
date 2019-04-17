def cal(a,b):
  print(' ', end='')
  i = 1
  while i < a+1:
    print('  ', end='')
    print(i, end='')
    i += 1
  print('\n')
  
  i = 1
  while i < b+1:
    print(i, end='')
    j = 1
    while j < a+1:
      if i*j < 10:
        print('  ', end='')
      else:
        print(' ', end='')
      print(i*j, end='')
      j += 1
    print('\n')
    i += 1

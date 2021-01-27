# -*- coding: utf-8 -*-
N = list(input())

if N.count('R') == 3:
  print(3)
else:
  if N.count('R') == 2:
    if N[1] == 'R':
      print(2)
    else:
      print(1)
  else:
    if N.count('R') == 1:
      print(1)
    else:
      print(0)
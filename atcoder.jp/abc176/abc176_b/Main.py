# -*- coding: utf-8 -*-
N = input()

#q = int(N[0]) // int(N[1])
mod = int(N) % 9

if mod == 0:
  print('Yes')
else:
  print('No')
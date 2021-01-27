# -*- coding: utf-8 -*-
N = list(input().split(' '))

q = int(N[0]) // int(N[1])
mod = int(N[0]) % int(N[1])

if mod > 0:
  q = q + 1

print(q * int(N[2]))
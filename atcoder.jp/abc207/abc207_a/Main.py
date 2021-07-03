# -*- coding: utf-8 -*-
# 整数の入力
# スペース区切りの整数の入力
a, b, c = map(int, input().split())

print(max(a+b,b+c,c+a))
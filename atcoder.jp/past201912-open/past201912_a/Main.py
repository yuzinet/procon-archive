# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
N = input()
if N.isnumeric():
	print(int(N)*2)
else:
	print("error")
# -*- coding: utf-8 -*-
# 入力
S = input()
# list
W = ["Sunny", "Cloudy", "Rainy"]

if W.index(S) == 2:
    print(W[0])
else:
    print(W[W.index(S)+1])

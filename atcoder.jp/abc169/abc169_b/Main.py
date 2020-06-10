def main():
# スペース区切りの整数の入力
	N, *d = map(int, open(0).read().split())

	if 0 in d:
  		print(0)
  		return

	A = 1
	for O in d:
		A *= O
		#print(O)
		if A > 1000000000000000000:
			print(-1)
			return

	print(A)

main()
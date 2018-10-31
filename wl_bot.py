letters = ["A", "Q", "Z", "W", "S", "X", "E", "D", "C", "R", "F", "V", "T", "G", "B", "Y", "H", "N", "U", "J", "M", "I", "K", "O", "L", "P"]

## len(letters) = 26



numbers = [1,2,3,4,5,6,7,8,9,0]

res = []
tot = ""

for l1 in letters:
	res.append(l1)
	for l2 in letters:
		res.append(l2)
		for l3 in letters:
			res.append(l3)
			for l4 in letters:
				res.append(l4)
				for l5 in letters:
					res.append(l5)
					for l6 in letters:
						res.append(l6)
						for l7 in letters:
							res.append(l7)
							for l8 in letters:
								res.append(l8)
								for l9 in letters:
									res.append(l9)
									for l10 in letters:
										res.append(l10)
										for f in res:
											tot += f
										print(tot)
										tot = ""
										res = res[0:9]
									res = res[0:8]
								res = res[0:7]
							res = res[0:6]
						res = res[0:5]
					res = res[0:4]
				res = res[0:3]
			res = res[0:2]
		res = res[0:1]
	res = res[0]
res = []

def titleToNumber(s):
	colNum = 0
	for i,c in enumerate(s[::-1]):
		colNum += (ord(c)-64)*(26**i)
	return colNum
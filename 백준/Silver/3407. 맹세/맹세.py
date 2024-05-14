from collections import deque
elem = {
	"h", "b", "c", "n", "o", "f", "p", "s", "k", "v", "y", "i", "w", "u",
	"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"
	}

N = int(input())

for _ in range(N):
	word = input()
	M = len(word)
	table = [0] * (len(word)+2)
	flag = False
	Q = deque()
	if word[0] in elem:
		Q.append(0)
		table[0] = 1
	if word[:2] in elem:
		Q.append(1)
		table[1] = 1
	while Q:
		cur = Q.popleft()
		if cur >= M-1:
			flag = True
			break
		t = word[cur + 1]
		if t in elem and not table[cur+1]:
			Q.append(cur + 1)
			table[cur+1] = 1
		if cur <= M-3:
			t += word[cur + 2]
			if t in elem and not table[cur+2]:
				Q.append(cur + 2)
				table[cur+2] = 1

	print('YES' if flag else 'NO')
toLatex = lambda py: \
	py.replace("not", "\\neg") \
	.replace("and", "\\wedge") \
	.replace("or", "\\vee") \
	.replace("==", "\\Leftrightarrow ") \
	.replace("im", "") \
	.replace(", ", "\\rightarrow ")

alphabet = lambda: (chr(x) for x in range(ord('A'), ord('Z') + 1))

im = lambda a, b: (not a or b)

usedVars = lambda py: [x for x in alphabet() if x in py]

getDict = lambda variables, bstr: \
	{ variables[i]: bool(int(bstr[i])) for i in range(len(variables))}

def generate(statement):
	variables = usedVars(statement)
	num = len(variables)
	lines = ["\\begin{matrix}", "&".join(variables) + "&" +  toLatex(statement) + "\\\\"]
	i = int("1" * num, 2)
	while i >= 0:
		binstr = bin(i)[2:].rjust(num, "0")
		line = "&".join(binstr)
		line += "&" + str(int(eval(statement, { "im": im, **getDict(variables, binstr)})))
		if i != 0: line += "\\\\"
		lines.append(line)
		i -= 1
	lines.append("\\end{matrix}")
	output = "\n".join(lines)
	return output
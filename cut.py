def gethex(filename: str):
	with open(filename, "r+") as f:
		str = f.read()
	cmds = str.split(',')
	cmds[0] = cmds[0][-8:]
	return [str.strip(" ,;\n") for str in cmds]

def getasm(filename: str):
	with open(filename, "r+") as f:
		coestr = f.read()
	cmds = coestr.split('\n')
	return [str for str in cmds if str]

cmds = getasm("inst.asm")
for str in cmds:
	print(str, end=";\n")
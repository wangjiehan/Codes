#传入的program是按照program.end从小到大排过序的
def bestArrange(program, cur):
	count = 0
	for i in range(0, len(program)):
		if cur <= program[i].start:
			count += 1
			cur = program[i].end
	return count
	

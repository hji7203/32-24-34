with file("treasure_map.txt","r") as text:
	for line in text:
		temp = ""
		for s in line:
			if s.isdigit():
				temp = temp + s
		# print temp
		#print line[int(temp)],
		for line in text:
			var1 = "!@#$%"
			i = line.find("!@#$%")
			if line.find("!@#$%") !=-1:
				print line[i+len(var1)],


import random
import os
#os.mkdir("baseball_save")
print "Game start!"
start = True
save_list = []
while (start == True):
	basenum = ["","","",""]
	basenum[0] = str(random.randrange(0,10,1))
	basenum[1] = basenum[0]
	basenum[2] = basenum[0]
	basenum[3] = basenum[0]
	while (basenum[0] == basenum[1]):
		basenum[1] = str(random.randrange(0,10,1))
	while (basenum[0] == basenum[2] or basenum[1] == basenum[2]):
		basenum[2] = str(random.randrange(0,10,1))
	while (basenum[0] == basenum[3] or basenum[1] == basenum[3] or basenum[2] == basenum[3]):
		basenum[3] = str(random.randrange(0,10,1))
	try_cnt = 0
	ball_cnt = 0
	strike_cnt = 0
	answer = "Answer: "+ str(basenum)
	save_list.append(answer + "\n")


	while (strike_cnt < 4):
		print basenum
		num = raw_input("enter [4 digit numbers] : ")
		print num
		num_list = list(num)
		print num_list
		num_list_set = list(set(num_list))
		guess = "Your Input: "+num
		# print num_list_set

		strike_cnt = 0
		ball_cnt = 0

		if (len(num_list_set) != 4):
			print "error"
			num = str(input("enter [4 digit numbers] : "))

		save_list.append(guess+"\n")


		#num contrast
		for i in range(0,4):
			for j in range(0,4):
				if(num[i] == str(basenum[j]) and i == j):
					strike_cnt += 1
				elif(num[i] == str(basenum[j]) and i != j):
					ball_cnt += 1
		print strike_cnt, "S", ball_cnt, "B"
		result = str(strike_cnt) +"S "+ str(ball_cnt)+"B"
		save_list.append(result+"\n")
		try_cnt += 1
		

		if (strike_cnt >= 4):
			print "You did",try_cnt,"times."
			try_count = "You did "+str(try_cnt)+" times to correct answer."
			print "Ding Ding Dang"
			ding = "Ding Ding Dang"
			save_list.append(ding+"\n")
			save_list.append(try_count+"\n")
			

			again = raw_input("Play again [yes/no] : ")
			while (again != "yes" and again != "no"):
				again = raw_input("error. [yes/no]:")
			if (again == "yes"):
				start = True
			elif (again == "no"):
				save = raw_input("Do you want to save? [yes/no] : ")
				while (save != "yes" and save != "no"):
					save = raw_input("error. [yes/no]:")
				if (save == "yes"):
					rand_num = random.randint(0,100)
					with file("baseball_save" + "/" +"save_%s.txt" %rand_num, "w") as my_file:
						for item in save_list:
							my_file.write(item)
					break
					# print save_list
				elif (save == "no"):
					print "Bye"
					break



#print basenum

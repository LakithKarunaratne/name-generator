from random import randint

def name_generator(qty):
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	name_list = []
	
	for i in range (0,qty): # number of times to repeat
		name_len_ = randint(4,10) # length of name 
		gen = 0 # next character
		i = 0 # iterator
		
		outstring = "" # output string
		
		while i < name_len_:
			gen = randint(0,24)
			outstring = outstring + alphabet[gen]
			i += 1 
		
		name_list.append(outstring)
		
	return name_list

def print_lists(list_name):
	for i in range (len(list_name)):
		print(list_name[i])

def print_sql_commands(list_name, table_name):
	print ("INSERT INTO ", table_name, " VALUES ")
	print ('(')
	for i in range (len(list_name)):
		print('('+"'"+list_name[i]+"'"+')'+',') # remove the last comma manualy
	print (");")

print_sql_commands(name_generator(120),'#namesTable')

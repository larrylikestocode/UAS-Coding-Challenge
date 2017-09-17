
def read_int(file_num, test_num):
	path = '/Users/wangwei/Desktop/2017-winter term/UAS/digits/trainingDigits/';
	file_num = 0;
	test_num = 0;
	num_line = 0;

	files = open(path+str(test_num)+'_'+str(file_num)+'.txt');
	print(files.name);
	
	while(1):
		line = files.readline();
		if len(line) == 0:
			break
		else:
			num_line+=1;
			line_num=int(line,2);
			# line_num = int(line_num,2);
			print(line_num)
	
	files.close()
	return line_num;



	
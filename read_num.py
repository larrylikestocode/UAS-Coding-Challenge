import numpy as np
# file_num: how many num of files we want to process
# test_num: which num are we testing
# train_test: train for 1 test for 0
def read_int(file_num, test_num, train_test):
	if(train_test):
		path = '/Users/wangwei/Desktop/2017-winter term/UAS/digits/trainingDigits/';
	else:
		path = '/Users/wangwei/Desktop/2017-winter term/UAS/digits/testDigits/';
	# file_num = 0;
	# test_num = 0;
	num_line = 0;

	files = open(path+str(test_num)+'_'+str(file_num)+'.txt');
	#print(files.name);
	line_num = np.zeros(35)
	while(1):
		line = files.readline();
		if len(line) == 0:
			break
		else:
			# num_line+=1;
			line_num[num_line]=int(line,2);
			num_line+=1;
			# line_num = int(line_num,2);
			#print(line_num)
	
	files.close()
	return line_num;

#-----------------------------------
def train_2d_num(num,num_file):
# num = 0;
# count = 0;
# num_file = 180;
# create a 2d array to store all the data
	data_2d = np.zeros((num_file,35))

	for i in range(num_file):
		data_2d[i] = read_int(i,num,1)
	# print(data_2d)
	return data_2d;

#-----------------------------------
# first read the testing data
# fix my arraysize to be 35
def test_1d_num(num,num_file):
	data = np.zeros(35) 
	data = read_int(num_file,num,0)
	return data;
#num_rec: which number we want to recognize
#file_num: which file number? 
def com_data(num_rec,file_num):
	num_rec  = 0
	data_2d = train_2d_num(num_rec,180);
	data  = test_1d_num(num_rec,file_num);
	print(data_2d[0]);
	print();
	print();
	print(data);	


com_data(0, 0);







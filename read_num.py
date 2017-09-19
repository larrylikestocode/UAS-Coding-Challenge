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
	line_num = np.zeros(32)
	while(num_line < 32):
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

#----------------------------------------------------------------------
def train_2d_num(num,num_file):
# num = 0;
# count = 0;
# num_file = 180;
# create a 2d array to store all the data
	data_2d = np.zeros((num_file,32))

	for i in range(num_file):
		data_2d[i] = read_int(i,num,1)
	# print(data_2d)
	return data_2d;

#----------------------------------------------------------------------
# first read the testing data
# fix my arraysize to be 35
#num: which num are we testing
#num_file: which file are testing
def test_1d_num(num,num_file):
	data = np.zeros(32) 
	data = read_int(num_file,num,0)
	return data;
#----------------------------------------------------------------------
#cut arrays in chunkand reasssmble
#cut chunk Tested 
def cut_chunk(ary, num_chunks):
	# split my array to 7 size of 5 small array
	# while to get the sum of the 5 ->numpy maybe
	# return size of 7 array
	# 4 0 1 2 3 
	sum_ary = np.zeros(num_chunks);
	chu_ary= np.split(ary, num_chunks);
	for i in range(num_chunks):
		sum_ary[i] = np.sum(chu_ary[i]);
	return sum_ary;
	# print(sum_ary);

#----------------------------------------------------------------------
#num_rec: which number we want to recognize
#num_rec: which number are we tring to recognize
#file_num: which file number we are trying to recgnize
#file_num_train: how many train txt file are we included?
def com_data(num_rec,file_num, file_num_train):
	# file_num_train = 180
	num_chunks = 32
	data_2d = train_2d_num(num_rec,file_num_train);
	# print(data_2d[0])
	# print(data_2d[1])
	# array size 32
	data  = test_1d_num(0,file_num);
	# print(data);
	sum_data_train = np.zeros((file_num_train,num_chunks));

	#sum_data_train[][] contains all the data has been trained for one digits
	for i in range (file_num_train):
		sum_data_train[i] = cut_chunk(data_2d[i],num_chunks)
	
	sum_data_test = cut_chunk(data,num_chunks)
	
	#start doing comparation use test_num - tran_num[i]
	sub_data_train_test = np.zeros((file_num_train,num_chunks));
	for i in range (file_num_train):
		sub_data_train_test[i] = (sum_data_train[i] - sum_data_test)
		sub_data_train_test[i] = np.divide(sub_data_train_test[i], sum_data_test)

	#an array of all averages rate from 180 files 
	result_rate = np.zeros(file_num_train);
	for i in range (file_num_train):
		result_rate[i] = ((np.sum(100 * sub_data_train_test[i])) / num_chunks);

	#for every element in the list -> over 100? delete then sum the rest -> find the average
	print(result_rate)

com_data(1, 1,180);
print();
print();
print();
# com_data(1,1,179);
# x= np.array([1,3,5,7,9,11,15,17]);
# cut_chunk(x,4);








import numpy as np
import heapq 
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
	line_num = np.zeros(30)
	while(num_line < 30):
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
#num: number we want to recognize
#num_file: nums of files
#tra_te: 1 for train; 0 for test
def train_test_2d_num(num,num_file, tra_te):
# num = 0;
# count = 0;
# num_file = 180;
# create a 2d array to store all the data
	data_2d = np.zeros((num_file,30))

	for i in range(num_file):
		data_2d[i] = read_int(i,num,tra_te)
	# print(data_2d)
	return data_2d;

#----------------------------------------------------------------------
# first read the testing data
# fix my arraysize to be 35
#num: which num are we testing
#num_file: which file are testing
def test_1d_num(num,num_file):
	data = np.zeros(30) 
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
def com_data(num_rec,file_num, file_num_train, file_num_test):
	# file_num_train = 180
	num_chunks = 30
	data_2d = train_test_2d_num(num_rec,file_num_train, 1);
	# print(data_2d[0])
	# print(data_2d[1])
	# array size 32
	#  num_rec 0_0 first 0
	#  file_num 0_0 second zero 
	data = test_1d_num(num_rec,file_num);

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



#-----------------------------version 2-----------------------------------------
def train_data_2d(num_rec, file_num_train):
	# # file_num_train = 180
	# num_chunks = 32
	# train data 2d [numof files][32lines decimal] - tested
	data_2d_train = train_test_2d_num(num_rec,file_num_train, 1);	
	# print(data_2d_train);
	return data_2d_train;


def test_data_2d(num_rec,file_num_test):	
	# test data 2d [numof files][32lines decimal] - tested
	data_2d_test = train_test_2d_num(num_rec, file_num_test, 0);
	# print(data_2d_test);
	return data_2d_test

#doing 10*180*32 matrix 
def train_data_3d():
	num = 10
	file_num_train = 180;
	num_chunks = 30;
	data_3d = np.zeros((10,file_num_train, num_chunks));
	for i in range(10):
		data_3d[i] = train_data_2d(i,file_num_train)
	return data_3d
	# print(data_3d[]);

#doing 10*85*32 matrix
def test_data_3d():
	num = 10
	file_num_test = 85;
	num_chunks = 30;
	data_3d = np.zeros((10,file_num_test, num_chunks));
	for i in range(10):
		data_3d[i] = test_data_2d(i,file_num_test)
	# print(data_3d[0]);
	return data_3d

#-----------------------------version 2.4-----------------------------------------
# num_test: which number do we wanna test
# num_data_base: which data base do we want to search 
# num_test_file: which test file do we want to checkout?
def com_3d(num_test,num_data_base, num_test_file):
	file_num_test = 85;
	file_num_train = 180;
	# num_test = 0;
	# num_data_base = 9;
	tra_3d = train_data_3d();
	tes_3d = test_data_3d();
	result_3d = np.zeros((file_num_test,file_num_train,30));
	# print (tes_3d[0][0]);
	for i in range(file_num_test):
		for j in range(file_num_train):
			result_3d[i][j] =  abs(tra_3d[num_data_base][j] - tes_3d[num_test][i]);
			result_3d[i][j] =  np.divide(result_3d[i][j], tes_3d[num_test][i]);

	result_rate = np.zeros(file_num_train);		
	for k in range(file_num_train):
		result_rate[k] =  np.sum(result_3d[num_test_file][k]) / 30

	# print(result_rate);
	avg = (np.sum(result_rate)/file_num_train);
	# print ('data base {}:{}'.format(num_data_base,avg));
	return avg;

#-----------------------------version 2.4-----------------------------------------
# determine if we can recognize the correct 
def deter(res,num):
	ind = np.zeros(3); 
	ind = heapq.nsmallest(3, range(len(res)), key=res.__getitem__);

	if ind[0] == num:
		return True;
	elif ind[1] == num:
		return True
	elif ind[2] == num:
		return True
	else:
		return False




#-----------------------------main-----------------------------------------			
result = np.zeros(10);
count = 0; 
for k in range(85):
	print('we are testing on test file num: {}'.format(k));
	for j in range(10):
		print('we are testing number: {}'.format(j));
		for i in range(10):
			result[i] =  com_3d(j,i,k);
		if deter(result, j) == True:
			count+=1;
			# print(count)
		print();

print(count)



# x= np.array([1,3,5,7,9,11,15,17]);
# print(deter(x,7));
# cut_chunk(x,4);








import numpy as np
import heapq 
#----------------------------------------------------------------------
# file_num: how many num of files we want to process
# test_num: which num are we testing
# train_test: train for 1 test for 0
# file I/O function
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
#put the train data to a 2d array
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


#-----------------------------version 2.0-----------------------------------------
#num_rec: number that we want to determine
#file_num_train: how many training files do we have?
def train_data_2d(num_rec, file_num_train):
	# # file_num_train = 180
	# num_chunks = 32
	# train data 2d [numof files][32lines decimal] - tested
	data_2d_train = train_test_2d_num(num_rec,file_num_train, 1);	
	# print(data_2d_train);
	return data_2d_train;

#----------------------------------------------------------------------
def test_data_2d(num_rec,file_num_test):	
	# test data 2d [numof files][32lines decimal] - tested
	data_2d_test = train_test_2d_num(num_rec, file_num_test, 0);
	# print(data_2d_test);
	return data_2d_test

#----------------------------------------------------------------------
#doing 10*180*32 matrix 
def train_data_3d():
	num = 10
	file_num_train = 180;
	num_chunks = 30;
	data_3d = np.zeros((10,file_num_train, num_chunks));
	for i in range(10):
		data_3d[i] = train_data_2d(i,file_num_train)
	return data_3d


#----------------------------------------------------------------------
#doing 10*85*32 matrix
def test_data_3d():
	num = 10
	file_num_test = 85;
	num_chunks = 30;
	data_3d = np.zeros((10,file_num_test, num_chunks));
	for i in range(10):
		data_3d[i] = test_data_2d(i,file_num_test)
	return data_3d

#-----------------------------version 2.4-----------------------------------------
# num_test: which number do we wanna test
# num_data_base: which data base do we want to search 
# num_test_file: which test file do we want to checkout?
#return a avg for one text file  
def com_3d(num_test,num_data_base, num_test_file):
	file_num_test = 85;
	file_num_train = 180;

	tra_3d = train_data_3d();
	tes_3d = test_data_3d();
	result_3d = np.zeros((file_num_test,file_num_train,30));

	for i in range(file_num_test):
		for j in range(file_num_train):
			result_3d[i][j] =  abs(tra_3d[num_data_base][j] - tes_3d[num_test][i]);
			result_3d[i][j] =  np.divide(result_3d[i][j], tes_3d[num_test][i]);

	result_rate = np.zeros(file_num_train);		
	for k in range(file_num_train):
		result_rate[k] =  np.sum(result_3d[num_test_file][k]) / 30

	avg = (np.sum(result_rate)/file_num_train);
	return avg;

#-----------------------------version 2.4-----------------------------------------
# determine if we can recognize the correct num?
def deter(res,num):
	ind = np.zeros(3); 
	#  find the 3 smallest num put into ind array
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
#this is the num of testing files we want to test
# num_test_files indicate how many files we would like to test eg 1  --> we could put 85 but it's time consuming
num_test_files = 1
for k in range(num_test_files):
	print('we are testing on test file num: {}'.format(k));
	for j in range(10):
		print('we are testing number: {}'.format(j));
		for i in range(10):
			result[i] =  com_3d(j,i,k);
		if deter(result, j) == True:
			count+=1;
		print();

# print(count);
print('The total error rate is: {} %'.format(100*(((num_test_files*10-count)/(num_test_files*10)))));











import re, subprocess, os, fnmatch, shlex, os.path

#bam_path1 = raw_input("enter a find command to identify the required bam files e.g 'find /mnt/Data1/targeted_sequencing/ type -f name '*realigned*bam'")
#bam_path2 = raw_input("enter a find command to identify the required files e.g 'find /mnt/Data4/targeted_sequencing/ type -f name '*realigned*bam'")
bam_path1 = "find /mnt/Data1/targeted_sequencing/ -type f -name '*realigned*bam'"
bam_path2 = "find /mnt/Data4/targeted_sequencing/ -type f -name '*realigned*bam'"
bam_test_path = "find ./bam_test/ -type f -name '*realigned*bam'"

"""program functionality"""

#create a function that uses os to generate a list of all of the realigned.bam files in targeted sequencing. 

patient_ID_list = []
patient_file = raw_input("please enter the file that contains the patient_IDs. It should be within the current directory and in a CSV format: ")
bam_locations = []

def bam_list(bam_find1, bam_find2):
	args = shlex.split(bam_find1)
	args2 = shlex.split(bam_find2)
	bam_1 = subprocess.Popen(args, stdout=subprocess.PIPE)
	stdout = bam_1.communicate()
	bam_2 = subprocess.Popen(args2, stdout=subprocess.PIPE)
	stdoutb2= bam_2.communicate()
	bam_locations_1 = stdout[0].rstrip().split('\n')
	bam_locations_2 = stdoutb2[0].rstrip().split('\n')
	bam_locations = bam_locations_1 + bam_locations_2
	print len(bam_locations)
	return bam_locations
	
def ID_extractor(patient_ID_list):
	with open(patient_file, "r") as file:
		for line in file:
			columns = line.split()
			patient_ID = columns[0]
			patient_ID_list.append(patient_ID)
			assert (patient_ID in patient_ID_list) 
	print len(patient_ID_list)
	return patient_ID_list

#despite this method providing a solution, it ended up taking too long to search every file name against every patient ID. 
#modify the bam_finder to compare the patient_list with
#def bam_finder(directory, patient_ID_list):
#	bam_locations = {}
#	pattern_list = []
#	for PID in patient_ID_list:
#		#bam_pattern = (element + '*realigned*bam')
#		bam_pattern2 = re.compile ('(%s)*realigned*bam'%PID)
#		pattern_list.append(bam_pattern2)
#		for root, dirs, files in os.walk(directory):
#			for filenames in files:
#				if bam_pattern2.match(str(filenames)):
#					print filenames
#			return

#def function to initiate platypus
	

"""test functions and exception capture"""

#this fucntion should provide exception capture for the raw data entry
#it will check the quantityof patient IDs extracted is the same as in the source file (duplicate checking)
#it will also test the format of the extracted patient IDs is correct
#it will also check the each patient_ID is in the generated list
def ID_extractor_exceptions(patient_ID_list):
	assert type(patient_ID_list) is list, "Input data is not a list format!"
	len_ID_list = len(patient_ID_list)
	ID_format1 = re.compile('P5_\d?d{1,3}') #matches P5_a_bcd
	ID_format2 = re.compile('[Pv]\d+_\d+') #matches v5_abc, v501_abcd, P5_abc 
	with open(patient_file, "r") as file:  
		num_lines = sum(1 for line in file)
		assert (num_lines == len_ID_list), "not all patient_IDs  were extracted"
		for element in patient_ID_list:
			element = str(element)
			match1 = ID_format1.match(element)
		        match2 = ID_format2.match(element)
			assert (match1 or match2), "new patient_ID format detected"
		for line in file:
                      columns = line.split()
                      sample_ID = columns[0]
                      assert (sample_ID in patient_ID_list), "there is a patient ID missing from the list"   
	return patient_ID_list  

#this uses a test file with known content to test the output of the ID extractor function. 
def ID_extractor_test(patient_ID_list):
	ID_extractor(patient_ID_list)
	if len(patient_ID_list) == 671:
		return patient_ID_list
	else:
		print "the code failed when generating the patient ID list"
	

def bam_list_test(bam_test_path):
	bam_list(bam_test_path)
	for item in bam_locations:
		if os.path.isfile == False:
			 print "error " + item + " is not a real file"
#	if len(bam_locations) == 1:
#		return		
#	else:
#		print 'incorrectly identified number of bam files in tets suite'


if __name__ == "__main__":
	ID_extractor(patient_ID_list)
	ID_extractor_exceptions(patient_ID_list)
	bam_list(bam_path1, bam_path2)
#	bam_list_test(bam_test_path)
#	ID_extractor_test(patient_ID_list)


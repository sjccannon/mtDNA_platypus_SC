'''this program takes an input csv file taht must have tha patient ID in the first column. for the old versioning numbers it only searches the for bam files in the format /mnt/Data1/targeted_sequencing/P5_nnn-nnn/assembly/P5_nnn-nnn_nnn.realigned.sorted.bam. If you have earlier versions on your patient list then the code must be altered accordingly to identify the pahts to the files you need.'''
'''
import a file containing patient IDs
extract the IDs
locate bamfiles on server
create a list of paths the bam files corresponding to the patient IDs
run the list of bam files through Platypus variant caller
'''


import re, subprocess, os, fnmatch, shlex, os.path

#global variables
bam_path1 = "find /mnt/Data1/targeted_sequencing/ /mnt/Data4/targeted_sequencing/ -type f -name '*realigned*bam'"
patients_in_input_file = re.compile('^\d+')
ID_format1 = re.compile('P5_\d{1,2}_\d{1,3}') #matches P5_a_bcd
ID_format2 = re.compile('[Pv]\d+_\d+') #matches v5_abc, v501_abcd, P5_abc
patient_file = raw_input("please enter the file that contains the patient_IDs. It should be within the current directory and in a CSV format: ")
patient_ID_list = [] #list of patient IDs extracted from an input file
bam_locations_list = [] #list of bam file abolute paths obtained by the specified Linux 'find' command
patient_bam_dict = {} #PatientId:BamFilePath
P5_dict_from_patient_list = {} #ID:last four characters of patient_ID


"""program functionality"""

'''

Function that uses Linux OS to generate a list of all realigned bam files in target sequencing. 
Identifies everyfile on the server ending in '*realigned*bam' and stores them in a list
removes test files or reruns

'''

def bam_list(bam_find1, bam_locations_list):
	args = shlex.split(bam_find1)
	bam_1 = subprocess.Popen(args, stdout=subprocess.PIPE)
	stdout = bam_1.communicate()
	bam_locations_local = stdout[0].rstrip().split('\n')
	if len(bam_locations_list) < len(patient_ID_list):
		for element in bam_locations_local:
			if 'rerun' not in element:
				bam_locations_list.append(element)
	#	for element in bam_locations_list:
	#		if 'test' not in element:
	#			bam_locations_list.append(element)
	return bam_locations_list

'''

Fucntion to extract patient sample IDs from the first column of a csv file

'''

def ID_extractor(patient_ID_list, patient_file):
	with open(patient_file, "r") as file:
		for i, line in enumerate(file):
			#this loop allows the test function to call this function every time. otherwise the patient IDs are re-appended to the list. +1 because the count starts at 0.
			if len(patient_ID_list) < i+1:
				columns = line.split()
				patient_ID = columns[0]
				patient_ID_list.append(patient_ID)
				assert (patient_ID in patient_ID_list)
	return patient_ID_list
'''
Main method - identify the paths to the required bam files from the list of patient IDs and all of the bam files in the target directories.
Will identify every files where the sampleID is in the filename
Will identify every P5 bam file on Data1 - some are duplicated on Data4 - in the format P5_n_abc where the format of the file name is P5_nnn_nnn_abc.
P5 samples 385 -  on Data1 are only included for 'run1'
'''


#function to only identify the bam files needed form the patient ID list
def patient_bam_extractor(patient_ID_list, bam_locations_list):
	#iterate through patient_ID_list
	for patient_ID in patient_ID_list:
		#generate a list of raw matches
		ID_raw_match = [location for location in bam_locations_list if patient_ID in location]
#need to remove reruns etc...
		if ID_raw_match != []:
			#append the raw match to the patientID it is associated with
			patient_bam_dict[patient_ID] = ID_raw_match
		if ID_format1.match(patient_ID):
			match_1_ID_num = patient_ID[-4:]
			P5_dict_from_patient_list[patient_ID] = match_1_ID_num
			#print 'p5_match dict' + str(len(P5_dict_from_patient_list.keys()))
	for patient_ID, ID_num in P5_dict_from_patient_list.iteritems():
		bam_match_format = re.compile('.*Data1.*P5_\d{3}-\d{3}/assembly.*P5_\d{3}-\d{3}.*(%s)\.realigned.sorted.bam'%ID_num)
		bam_match_run1_format = re.compile('.*Data1.*P5_\d{3}-\d{3}_run1/assembly.*P5_\d{3}-\d{3}.*(%s)\.realigned.sorted.bam'%ID_num)
		for bam_location in bam_locations_list:
			p5_match = re.search(bam_match_format, bam_location)
			p5_match2 = re.search(bam_match_run1_format, bam_location)
			if p5_match and patient_ID not in patient_bam_dict.keys():
				patient_bam_dict[patient_ID] = [bam_location]
			if p5_match2 and patient_ID not in patient_bam_dict.keys():
				patient_bam_dict[patient_ID] = [bam_location]
	for patient_ID, bam_path in patient_bam_dict.iteritems():
		if len(bam_path) > 1:
                        for item in bam_path:
                                if 'test' in item:
                                        bam_path.remove(item)
                                        patient_bam_dict[patient_ID] = [bam_path]
 	return patient_bam_dict


'''
Test functions and exception capture
'''

def ID_extractor_test(patient_ID_list, patient_file):
	ID_extractor(patient_ID_list, patient_file)
	assert type(patient_ID_list) is list, "Input data is not a list format!"
        len_ID_list = len(patient_ID_list)
        ID_format1 = re.compile('P5_\d?d{1,3}') #matches P5_a_bcd
        ID_format2 = re.compile('[Pv]\d+_\d+') #matches v5_abc, v501_abcd, P5_abc
        with open(patient_file, "r") as file:
                num_lines = sum(1 for line in file)
                assert (num_lines == len_ID_list), "not all patient_IDs were extracted"
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

def bam_list_test(bam_path1, bam_locations_list):
	bam_list(bam_path1, bam_locations_list)
	for bam_path in bam_locations_list:
		if os.path.isfile == False:
			print "error in bam list: " + item + " is not a real file"
	return bam_locations_list 


def patient_bam_extractor_test(patient_ID_list, bam_locaitons_list):
	patient_bam_extractor(patient_ID_list, bam_locations_list)
	#check all patient ID have bam paths 
	for patient_ID in patient_ID_list:
        	if patient_ID not in patient_bam_dict.iterkeys():
                	print 'This patient ID escapse the pattern match and no bam path is identified: ' + patient_ID
	#check the generated dictionary only has one bam file path as the value
	for patient_ID, bam_path in patient_bam_dict.iteritems():
		if len(bam_path) > 1:
			print 'this patient ' + patient_ID + ' has more than one bam file: ' + str(bam_path)
		if os.path.isfile == False:
			print 'This patient, ' + patient_ID + ', has an incorrect bam path. It is not a real file:' + str(bam_path)

	return patient_bam_dict

#function to make platypus work

 

if __name__ == "__main__":
	ID_extractor_test(patient_ID_list, patient_file)
	bam_list_test(bam_path1, bam_locations_list)
	patient_bam_extractor_test(patient_ID_list, bam_locations_list)

	for key, value in patient_bam_dict.iteritems():
		print str(key) + str(value)
	print len(patient_bam_dict.keys())

''' this program takes an input csv file taht must have tha patient ID in the first column. for the old versioning numbers it only searches the for bam files in the format /mnt/Data1/targeted_sequencing/P5_nnn-nnn/assembly/P5_nnn-nnn_nnn.realigned.sorted.bam. If you have earlier versions on your patient list then the code must be altered accordingly to identify the pahts to the files you need.'''
'''
import a file containing patient IDs
extract the IDs
locate bamfiles on server
create a list of paths the bam files corresponding to the patient IDs
run the list of bam files through Platypus variant caller
'''


import re, subprocess, os, fnmatch, shlex, os.path

#global variables
#the linux find command required to locate the bam files. This could become raw input rather than hard coded to increase functionality
bam_path1 = "find /mnt/Data1/targeted_sequencing/ /mnt/Data4/targeted_sequencing/ -type f -name '*realigned*bam'"
#regular expression to match patient ID in format P5_a_bcd. Separated because legacy filenaming caused additional exceptions to the ID_format2 filenames.
ID_format1 = re.compile('P5_\d{1,2}_\d{1,3}') 
#regular expression to match patient Id in formats v5_abc, v501_abcd, P5_abc. 
ID_format2 = re.compile('[Pv]\d+_\d+')
#raw input where the user specifies the csv file to be analysed
patient_file = raw_input("please enter the file that contains the patient_IDs in column[0]. It should be within the current directory and in a CSV format: ")
#list of patient IDs to be appended by IDs extracted from an input file
patient_ID_list = []
#list of bam file abolute paths to be appended with output of the specified Linux 'find' command
bam_locations_list = [] 
#dictionary containing {key : value} as {Patient_ID: [bam_file_path]} 
patient_bam_dict = {}
#dictionary containing {key : value} as {Patient_ID:last four characters of patient ID}. Used as unique identifier and in combination wiht regular expression to avoid obtaining duplicate bam files for one patient.
P5_dict_from_patient_list = {} #ID:last four characters of patient_ID
#Platypus variant caller to be used on each obtained patient bam file
path_to_platypus = "/usr/share/platypus/Platypus_0.8.1/Platypus.py" 
#GRC build 37 reference genome required for platypus
build_37_ref = "/mnt/Data1/resources/human_g1k_v37.fasta"
#file path for the output of platypus
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus/variants/"

"""program functionality"""

'''
Function that uses Linux OS to generate a list of all realigned bam files in the targeted_sequencing directory. 
Identifies everyfile on the server ending in '*realigned*bam' and stores them in a list
removes test files or reruns
'''
def bam_list(bam_find1, bam_locations_list):
	#inform the user of processing stage
	print "Aggregating bam file paths in targeted_sequencing directory"
	#take the input find command bam_find1 string and split it into separate arguments
	args = shlex.split(bam_find1)
	#using the os to call the arguments and pipe the output. prevents need to write another file
	bam_1 = subprocess.Popen(args, stdout=subprocess.PIPE)
	#capture the piped output as a tuple ([bamfiles], stderrNULL)
	stdout = bam_1.communicate()
	#removes white space and splits by the newline character
	bam_locations_local = stdout[0].rstrip().split('\n')
	#if statement ensures the bam_locations_list is only appended once. Enables the function to be called by the test function 
	if len(bam_locations_list) < len(patient_ID_list):
		#iterates through the bam location strings in the bam_locations_local list
		for element in bam_locations_local:
			#appends bam_locations_list only if 'rerun' is not in the name effectively removign filepaths the any rerun samples
			if 'rerun' not in element:
				bam_locations_list.append(element)
	print "file paths aggregated"
	return bam_locations_list

'''
Fucntion to extract patient sample IDs from the first column of a csv file
'''

def ID_extractor(patient_ID_list, patient_file):
	print "Extracting patient IDs from specified input file. please ensure the patient ID is in the first column of the .csv file"
	with open(patient_file, "r") as file:
		#initiate a for loop that counts the number of lines in the file
		for i, line in enumerate(file):
			#this if statement allows the test function to call this function every time. otherwise the patient IDs are re-appended to the list. +1 because the count starts at 0.
			#if the length of the ID list is less than the number of lines (add 1 because python counts from 0) 
			if len(patient_ID_list) < i+1:
				#extract and append patient_IDs from the file to the list of IDs
				columns = line.split()
				patient_ID = columns[0]
				patient_ID_list.append(patient_ID)
				assert (patient_ID in patient_ID_list)
	print 'Patient ID extraction complete. ' + str(len(patient_ID_list)) + ' patient IDs extracted'
	return patient_ID_list
'''
Main method - identify the paths to the required bam files from the list of patient IDs and all of the bam files in the target directories.
Will identify every files where the sampleID is in the filename
Will identify every P5 bam file on Data1 - some are duplicated on Data4 - in the format P5_n_abc where the format of the file name is P5_nnn_nnn_abc.
P5 samples 385 -  on Data1 are only included for 'run1'
'''

#function to only identify the bam files needed form the patient ID list
def patient_bam_extractor(patient_ID_list, bam_locations_list):
	print 'Locating bam file paths for patient IDs in patient_ID_list and storing in a dictionary'
	#iterate through patient_ID_list
	for patient_ID in patient_ID_list:
		#generate a list of raw matches for the patient IDs using list comprehension. Raw list may include duplicates.
		#include the absolute paths to the bam files from the bam_locations_list, if the patient ID is in there
		ID_raw_match = [location for location in bam_locations_list if patient_ID in location]
		#this statement prevents the list being appended multiple times. 
		if ID_raw_match != []:
			#append the raw matches to the patientID it is associated with in a dictionary 
			#(patient ID is the key, bam paths ) may include duplicates in the values. 
			patient_bam_dict[patient_ID] = ID_raw_match
		#print patient_ID + ' added.' + 'Dictionary length = ' + str(len(patient_bam_dict.keys()))
		#string matching to extract the numerics of the patient_ID. This is required to generate absolute filepaths.
		if ID_format1.match(patient_ID):
			#extract the ID_numbers using negative indexing
			match_1_ID_num = patient_ID[-4:]
			#generate a dictionary of P5 patients. 
			P5_dict_from_patient_list[patient_ID] = match_1_ID_num
	print 'Number of patients identified as tested using p5 and included into a dictionary with all of the bam files containing their : ' + str(len(P5_dict_from_patient_list.keys()))
	#iterates through the patient IDs and ID numbers (numerics) in the p5 dictionary
	for patient_ID, ID_num in P5_dict_from_patient_list.iteritems():
		#this is a generic random expresion compiled to match the majority of samples, notice the interchangeable ID_numbers.
		#this ensures only the 'realigned.sorted.bam' files are included.
		bam_match_format = re.compile('.*Data1.*P5_\d{3}-\d{3}/assembly.*P5_\d{3}-\d{3}.*(%s)\.realigned.sorted.bam'%ID_num)
		#this is to account for exceptions where there is a 'run1' in the filepath. 
		bam_match_run1_format = re.compile('.*Data1.*P5_\d{3}-\d{3}_run1/assembly.*P5_\d{3}-\d{3}.*(%s)\.realigned.sorted.bam'%ID_num)
		#nested loop to compare each match to the bam_location
		for bam_location in bam_locations_list:
			#searches the bam locaton list for realigned.sorted.bam files that ar required for each patient
			p5_match = re.search(bam_match_format, bam_location)
			p5_match2 = re.search(bam_match_run1_format, bam_location)
			#the following two if statements update the dictionary  
			#if the realigned sorted bam file is in the bam locations list, has the patient ID and is not in the patient bam
			#dictionary
			if p5_match and patient_ID not in patient_bam_dict.keys():
				#add it to the dictionary. This ensures each patient_ID for patients tested onthe
				#p5 panel only has one bam file
				patient_bam_dict[patient_ID] = [bam_location]
				print patient_ID + ' added.' + 'Dictionary length = ' + str(len(patient_bam_dict.keys()))
			if p5_match2 and patient_ID not in patient_bam_dict.keys():
				patient_bam_dict[patient_ID] = [bam_location]
				print patient_ID + ' added.' + 'Dictionary length = ' + str(len(patient_bam_dict.keys()))
	for patient_ID, bam_path in patient_bam_dict.iteritems():
		#removes the items with 'test' in the string
		if len(bam_path) > 1:
                        for item in bam_path:
                                if 'test' in item:
                                        bam_path.remove(item)
                                        #exception capture notification
                                        print 'Removed test bam file: ' + item + '. ' + 'Patient ' + patient_ID + ' still has a non-test bam file to be analysed.'
                                        patient_bam_dict[patient_ID] = [bam_path]
	print 'Dictionary complete. ' + str(len(patient_bam_dict.keys())) + ' patient bam files located.'
	return patient_bam_dict

'''
Function to generate vcf files using platypus
'''
'''def platypus_caller(path_to_platypus, build_37_ref, base_path, patient_bam_dict):
	for patient_ID, bam_path in pathient_bam_dict.iteritems():
		print 'Variant Calling - ' + patient_ID  
		vcf_output_file = base_path + key + '.vcf'
		command = "python " + path_to_platypus + " callVariants --bamFiles=" + str(value) + " --refFile=" + build_37_ref + " --output=" + vcf_output + " --regions=MT"
		subprocess.call(command, shell=True)
	print 'Variant calling complete'
	return '''

'''
Fucntion to filter vcf files for mitochondrial mutation 3243G>A
and delete original vcf files once formatted
'''
#with open ("filtered_platypus_varaints", "a") as out_file:
#	list_of_files = os.listdir(vcf_location)

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

'''
Function to test platypus output
'''
'''def test_platypus_output(path_to_platypus, build_37_ref, base_path, patient_bam_dict):
	#call platypus variant caller
	platypus_caller(platypus_location, genome_reference, target_directory, patient_bam_dict)
	#I want to check that there is a vcf file for every patient sample, saved in a specified folder
	#initiate an empty list to store patient_IDs gathered from of looping through the generated vcf filenames
	vcf_test_list = []
	#loop through filenames in target directory base_path
	for file in os.listdir(base_path):
		#vcf files named with patient_ID.vcf, strip .vcf from each 
		patient_ID_file = str(file.strip('.vcf'))
		#append list of patients who have had filenames generated
		vcf_test_list.append(patient_ID_file)
		#open each file to check that some calls have been made
		with open(file, "r") as vcf_file:
			for line in vcf_file:
				if sum(1 for line in vcf_file) > 48:
					break
				else:
					print 'This file, ' + vcf_file + ', has no called variants'
	#loop through vcf_test_list
	for patient_ID_vcf in vcf_tests_list:
		#see if the patient ID is in the bam_dictionary keys
		if patient_ID_vcf not in patient_bam_dict.iterkeys():
			#excepetion message to prompt investigation
			print 'This patient, ' + patient_ID_vcf + ', did not have a vcf generated'	

'''

'''
check the filtered vcf file
'''
#call the variant filter funtion

#check the output file exists 
#check the 

if __name__ == "__main__":
	ID_extractor_test(patient_ID_list, patient_file)
	bam_list_test(bam_path1, bam_locations_list)
	patient_bam_extractor_test(patient_ID_list, bam_locations_list)
	print patient_bam_dict

#	test_platypus_output(path_to_platypus, build_37_ref, base_path, patient_bam_dict)

#	for key, value in patient_bam_dict.iteritems():
#		print str(key) + str(value)
#	print len(patient_bam_dict.keys())

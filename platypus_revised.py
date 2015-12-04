import re, subprocess

bam_path1 = "/mnt/Data1/targeted_sequencing"
bam_path2 = "/mnt/Data4/targeted_sequencing"

"""program functionality"""

def bam_finder(directory, patient_ID_list):
	bam_locations = []
	for root, dirs, files in os.walk(directory):
		matches = fnmatch.filter(files, patter)
		results.extend(os.path.join(base, f) for f in good files)
	return results

def ID_extractor():
	patient_file = raw_input("please enter the file that contains the patient_IDs. It should be within the current directory and in a CSV format.")
	with open(patient_file, "r") as file:
		for line in file:
			
			patient_ID =  	
	return patient_ID_list

"""test functions"""

#this fucntion should test that the quantity of patient IDs etracted is the same as in the source file.
#it will also test the format of the extracted patient IDs is correct
def ID_extractor_test(patient_ID_list):
	assert (patient_ID_list == type(list)), "Input data is not a list format!"
	len_ID_list = len(patient_ID_list)
	ID_format1 = re.compile('P5_\d?d{1,3}') #matches P5_a_bcd
	ID_format2 = re.compile('[Pv]\d+_\d+') #matches v5_abc, v501_abc, P5_abc 
	with open("mitochondrial_sensitivity_MODY.csv", "r") as file:
		num_lines = sum(1 for line in file)
		assert (num_lines == len_ID_list), "not all patient_IDs  were extracted"
	for element in patient_ID_list:
		 assert (ID_format1.match(str(element)) or (ID_format2.match(str(element)), "new patient ID_detected"  

def bam_finder_test():

if __name__ == "__main__":
	ID_extractor()
	ID_extractor_test(patient_ID_list)
	bam_finder(bam_path1, patient_ID_list)
	bam_finder(bam_path_2, patient_ID_list)

	

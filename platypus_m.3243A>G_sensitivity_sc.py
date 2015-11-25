  """script created output the filepaths to patient bam files as a string based on one or a combination of their unique sample ID, batch number, and date of batch
exceptions were created to locate 671 bam files"""

#import the relevant modules
import re, os, fnmatch, subprocess


#path to bam file directories
#the versioning system changed and are stored in different locations so these two variables represetn the two locations
path_to_P5_bam = "/mnt/Data1/targeted_sequencing/"
path_to_V5_bam  = "/mnt/Data4/targeted_sequencing/" #this also includes the old notation in the format P5_xyz where xyz are itegers


#createing regexs for different combinations of bam filename.... as mentioned there are several combinations of the sample names 

#matches samples in the format P5_n_nnn where n are integers
format_P5 = re.compile('P5_\d?\d{1,3}')
#matches samples in the formt v5_nnn, v501_nnn, P5_nnn where n are integers
format_PorV = re.compile('[Pv]\d+_\d+') 

#creating an empty dictionary look up where the sample IDs will be the key and the string path to the associated filename will be the value. 
#each bam file value in the dictionary will then be passed to Platypus variant caller
my_dict = {}

#this fucntion rearranges the path to a bam file name based on the location to the its location and is used to pull out compete path to bam files for exception cases.
#only the files in each bam directory with the exception ID_number need to be added to the dictionary. 

#defines function to take a pre-generated path to the relevnat directory that should contain the bam file for the patient in question. 
def rearrange_bam_location(path_to_bam_directory):
	#the regex uses sample_ID as a variable and ensures each sample_ID, followed by anything, ends in realigned.sorted.bam. 
	#this was necessary to account for a change in naming convention where the gender of patients is now specified in the filename
	bam_pattern = re.compile('(%s).*\.realigned\.sorted\.bam'%sample_ID)
	#this loops through every file in the directory containing the patient filename
	for file in os.listdir(path_to_bam_directory):
		#assigning string of every file to a variable filename
		filename = str(file)
		#if the regex bam pattern matches the filename
		if bam_pattern.match(filename):
			#then it is a match for the sample in question (the sample_ID is specified previously in the for loop where this function is called)
			complete_path_to_bam = path_to_bam_directory + filename
			#the dictionary is updated to have the sample_ID as the filename and the string filepath to the associated bam file
			my_dict[sample_ID] = complete_path_to_bam

			
#Constructiong a dictionary of sample number as key and the path to appropriate bam file as the value
#with open("test.csv", 'r') as in_file: #this was the test file that was used

#the .csv file contains all of the patients who would have previosly been tested for 3243 mutation
with open("mitochondrial_sensitivity_MODY.csv", "r") as in_file:
	#this initiates a loop that contines until the dictionary is contains and entry for every patient in the infile
	for line in in_file:
		#this splits the csv into columns that can be easily refered to
		columns = line.split()
		#matches every line in the file to the format P5_n_nnn
		if format_P5.match(columns[0]): 
			#extracting data from the column and assigning to variable
			sample_ID = columns[0]
			#this extracts the last three digits of the sample ID which can be used in a series of if statements to direct the creation of the path
			#this is necessary because the files are located in directories depending on their ID_num
			ID_num = int(sample_ID[-3:])
			#the end of the bam files have the following common ending
			bam_end = '.realigned.sorted.bam'
			
			#the following if statements construct string pathways to the bam files and append them to the dictionary dependent on the
			#ID_num. it also constructs the bam filename. 
			if ID_num >= 1 and ID_num <= 9:
				additional_path = 'P5_001-048/assembly/'
				bam_file_name = 'P5_001-048_' + '00' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 
				#print statements were included to investigate the length of dictionary keys as a test
				#print len(my_dict.keys())

			elif ID_num >= 10 and ID_num <= 48:
				additional_path = 'P5_001-048/assembly/'
				bam_file_name = 'P5_001-048_' + '0' + str(ID_num) + bam_end
				#append dictionary to include sample_ID as key and string of path to bam file
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
				#print len(my_dict.keys())	

			elif ID_num >= 49 and ID_num <= 96:
				additional_path = 'P5_049-096/assembly/' 
				bam_file_name = 'P5_049-096_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 

			elif ID_num >= 97 and ID_num <= 99:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_097-144_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_paht + bam_file_name

			elif ID_num >= 100 and ID_num <= 144:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_097-144_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
		
			elif ID_num >= 145 and ID_num <= 216:
				additional_path = 'P5_145-216/assembly/'
				bam_file_name = 'P5_145-216_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 217 and ID_num <= 240:
				additional_path = 'P5_217-240/assembly/'
				bam_file_name = 'P5_217-240_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam +additional_path + bam_file_name

			elif ID_num >= 241 and ID_num <= 336:
				additional_path = 'P5_241-336/assembly/'
				bam_file_name = 'P5_241-336_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 337 and ID_num <= 384:
				additional_path = 'P5_337-384/assembly/'
				bam_file_name = 'P5_337-384_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 385 and ID_num <= 432: 
				additional_path = 'P5_385-432_run2/assembly/'
				bam_file_name = 'P5_385-432_' + str(ID_num) + '.realigned.sorted.merged.bam'
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 433 and ID_num <= 480:
				additional_path = 'P5_433-480/assembly/'
				bam_file_name = 'P5_433-480_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
				
			elif ID_num >= 481 and ID_num <= 504:
				extra_path = 'P5_481-504/assembly/'
				bam_file_name = 'P5_481-504_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + extra_path + bam_file_name
				#print "1 " + str(len(my_dict.keys()))	
			else:
				print 'error' + str(ID_num)

	
#if the sample_ID matches the format of the tests implemented at a later stage, this code finds the file location in Data4 based on the batch number and sample number, it is still within the original loop. 
		elif format_PorV.match(columns[0]):
			sample_ID = str(columns[0])
			#naming conventions changed to include the gender of the patients which needed to be accounted for
			file_names_with_sex = sample_ID + "*.realigned.bam"
			#extracts the data containing patient batch and the date of testing
			date_and_batch = str(columns[1])
			#extracts the integers from the sample_ID
			ID_num = int(sample_ID[-3:])
			#takes the last 7 digits of the date_and_batch_string and assign to batch_number
			batch_number = int(date_and_batch[-7:])
			#extraction of batch number allowed for exception capture where the naming conventions in the MODY file were not the same. 
			if batch_number >= 1501266 and batch_number != 1502972:
				#this replaces the '.' with '-' twice because this represents named directories in the filesystem
				path_to_bam_directory = path_to_V5_bam + date_and_batch.replace('.', '-', 2) + '/assembly/'
				#for every file in the given directory
				for file in os.listdir(path_to_bam_directory):
					#if filename (file) matches with pattern variable (file_names_with_sex)
					if fnmatch.fnmatch(file, file_names_with_sex): 	
						#use the file within the directory to complete the path to the bam file for that patient sample			
						complete_path_to_bam = path_to_bam_directory + file
						#update the dictionary
						my_dict[sample_ID] = complete_path_to_bam
#						print "2 " + str(len(my_dict.keys()))
			#this batch did not need the date and batch to be modified
			elif batch_number == 1502972:
				path_to_bam_directory = path_to_V5_bam + '2015-08-11_1503151/assembly/'
				for file in os.listdir(path_to_bam_directory):
					if fnmatch.fnmatch(file, file_names_with_sex):
						complete_path_to_bam = path_to_bam_directory + file
						my_dict[sample_ID] = complete_path_to_bam			
#						print "3 " + str(len(my_dict.keys()))
					
#the following are exceptions to the above norms....
#1404237  and 1404001 need the additional_path 2014-10-27_2014-11-12_rerun/assembly/
	
			elif batch_number == 1404237 and ID_num <= 696:
				path_to_bam_directory = path_to_V5_bam + '2014-11-12_2014-11-26_merged/assembly/'
				rearrange_bam_location(path_to_bam_directory)
			elif batch_number == 1404237 and ID_num > 696:
				path_to_bam_directory = path_to_V5_bam + '2014-10-27_2014-11-12_rerun/assembly/'
				rearrange_bam_location(path_to_bam_directory)
			elif batch_number == 1404001:
				path_to_bam_directory = path_to_V5_bam + '2014-10-27_2014-11-12_rerun/assembly/'
				rearrange_bam_location(path_to_bam_directory)
#				print "6 " + str(len(my_dict.keys()))
			elif batch_number == 1501051:
				path_to_bam_directory = path_to_V5_bam + '2015-03-16_1501051/assembly/'
				rearrange_bam_location(path_to_bam_directory)
#				print "7 " + str(len(my_dict.keys()))

			#1404418 needs additional_path 2014-11-12_2014-11-26_merged
			elif batch_number == 1404418:
				path_to_bam_directory = path_to_V5_bam + '2014-11-12_2014-11-26_merged/assembly/'
				rearrange_bam_location(path_to_bam_directory)
#				print "8 " + str(len(my_dict.keys())) 

			#any batch with the date 170215 require the additional_path 2015-02-15_1500634 
			elif batch_number >= 1500634 and batch_number <= 1500657:
				path_to_bam_directory = path_to_V5_bam + '2015-02-15_1500634/assembly/'
				rearrange_bam_location(path_to_bam_directory)
#				print "9 " + str(len(my_dict.keys()))		


#the batch numbers 1403083(14), 1403237(14), 1403375(14), 1403633(14), 1500047, 1500335, 1501051 need rearranging in the format yyyy-mm-dd_nnnnnnnn where n are integers
	
			elif batch_number < 1501266 and batch_number >= 1403083:
				exception_list = [1404237, 1404001, 1404418, 1500634, 1500635, 1500653, 1500654, 1500655, 1500656, 1500657, 1501051]
				if batch_number not in exception_list:
			#		print batch_number
					#this step takes out the full stops
					date_and_batch_universal_step1 = date_and_batch.replace(".", "")
					#this step takes out the hyphen
					date_and_batch_universal = date_and_batch_universal_step1.replace("-", "")
					#this creates the path to the bam directory if the batch was 2014
					if int(date_and_batch_universal[4]) == 1  and int(date_and_batch_universal[5]) == 4:
						path_to_bam_directory = path_to_V5_bam + '2014-' + date_and_batch_universal[2] + date_and_batch_universal[3] + '-' + date_and_batch_universal[0] + date_and_batch_universal[1] + '_' + str(batch_number) + '/assembly/'  
						rearrange_bam_location(path_to_bam_directory)
#						print "4 " + str(len(my_dict.keys()))
					#same as above but for 2015
					elif int(date_and_batch_universal[4]) == 1 and int(date_and_batch_universal[5]) == 5:
						path_to_bam_directory = path_to_V5_bam + '2015-' + date_and_batch_universal[2] + date_and_batch_universal[3] + '-' + date_and_batch_universal[0] + date_and_batch_universal[1] + '_' + str(batch_number) + '/assembly/' # rearrange ddmmyy to 2015-mm-dd_nnnnnnnn
						rearrange_bam_location(path_to_bam_directory)
#						print "5 " + str(len(my_dict.keys()))

#print str(len(my_dict.keys()))
in_file.close()

#short testing feature to highlight any samples in the in_file that are not included in the dictionary
with open("mitochondrial_sensitivity_MODY.csv", "r") as file:
	for line in file:
		columns = line.split()
		sample_ID = columns[0]
		if sample_ID not in my_dict.keys():
			print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' + str(sample_ID)	
	
							
##ln -s creates symbolic link. I could get the operating system to call this command for each dictionary value

#variables required for platypus
#need to include the path to the platypus.py file
path_to_platypus  = "/usr/share/platypus/Platypus_0.8.1/Platypus.py" 

#path to the reference sequence
build_37_ref  = "/mnt/Data1/resources/human_g1k_v37.fasta" 

#base path to where the script is being run from and the files are being saved/output
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus"

#assigning variable to be called by the command line with platypus.  m.3243A>G mutation with 25bp either side 
#because only looking at a single region there is no need to create an interval list
interval_mtDNA = "chrMt"

#loop through each value in the dictionary

#import os.path
#count = 0
#for value in my_dict.itervalues():
#	if os.path.isfile(value):
#		count += 1
#		print count
#	elif os.path.isfile(value) == False:
#		print value

#uses the operating system to call 
for key, value in my_dict.iteritems():
#key = "v5_673"
#if key in my_dict.keys():
	vcf_output = base_path + "/variants/" + key + "platypus_m.3243A>G.vcf"
#	print vcf_output
	command = "python " + path_to_platypus + " callVariants --bamFiles=" + value + " --refFile=" + build_37_ref + " --output=" + vcf_output + " --regions=MT"
#	print command
	subprocess.call(command, shell=True)



#to use platypus I am going to get the operating system to excecute a concatenated string of cammands and pathways on the Linux command line.
#include here the command to initiate playpus calling on each 

#could look through the log files generated by platypus to create a global log file which outlines what has been r

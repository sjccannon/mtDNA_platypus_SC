#import the relevant modules
import re, os, fnmatch

#assign the following variables:
#path to the platypus variant caller
path_to_platypus  = "usr/share/platypus/Platypus_0.8.1/" 

#path to the reference sequence
build_37_ref  = "/mnt/Data1/resources/human_glk_u37.fasta" 

#path to bam file directories
path_to_P5_bam = "/mnt/Data1/targeted_sequencing/"
path_to_V5_bam  = "/mnt/Data4/targeted_sequencing/" #this also includes the old notation in the format P5_xyz where xyz are itegers

# assigning variable to be called by the command line with platypus.  m.3243A>G mutation with 25bp either side 
#because only looking at a single region there is no need to create an interval list
interval_mtDNA = "chrM:3209-3249"

#base path to where the script is being run from and the files are being saved/output
base_path = "/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus"

#createing regexs for different combinations of bam filename
format_P5 = re.compile('P5_\d?\d{1,3}')#matches samples in format P5_n_nnn
format_PorV = re.compile('[Pv]\d+_\d+') #includes samples in format v5_nnn, v501_nnnn, P5_nnn

#creating a dictionary look up
my_dict = {}

def rearrange_bam_location(path_to_bam_directory):
	bam_pattern = re.compile('(%s).*\.realigned\.sorted\.bam'%sample_ID)
	for file in os.listdir(path_to_bam_directory):
		filename = str(file)
		if bam_pattern.match(filename):
			complete_path_to_bam = path_to_bam_directory + filename
			my_dict[sample_ID] = complete_path_to_bam

			
#Constructiong a dictionary of sample number as key and the path to appropriate bam file as the value
#with open("test.csv", 'r') as in_file:
with open("mitochondrial_sensitivity_MODY.csv", "r") as in_file:
	for line in in_file:
		columns = line.split()
		if format_P5.match(columns[0]): 
			sample_ID = columns[0]
			ID_num = int(sample_ID[-3:])
			bam_end = '.realigned.sorted.bam'
			if ID_num >= 1 and ID_num <= 9:
				additional_path = 'P5_001-48/assembly/'
				bam_file_name = 'P5_001-048_' + '00' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 
				#print len(my_dict.keys())

			elif ID_num >= 10 and ID_num <= 48:
				additional_path = 'P5_001-048/assembly/'
				bam_file_name = 'P5_001-48_' + '0' + str(ID_num) + bam_end
				#append dictionary to include sample_ID as key and string of path to bam file
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
				#print len(my_dict.keys())	

			elif ID_num >=  49 and ID_num <= 96:
				additional_path = 'P5_049_096/assembly/' 
				bam_file_name = 'P5_049-096_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name 

			elif ID_num >= 97 and ID_num <= 99:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_049-144_' + '0' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_paht + bam_file_name

			elif ID_num >= 100 and ID_num <= 144:
				additional_path = 'P5_097-144/assembly/'
				bam_file_name = 'P5_049-144_' + str(ID_num) + bam_end
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
				bam_file_name = 'P5_385-432_' + str(ID_num) + 'realigned.sorted.merged.bam'
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name

			elif ID_num >= 433 and ID_num <= 480:
				additional_path = 'P5_433-480/assembly/'
				bam_file_name = 'P5_433-480_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + additional_path + bam_file_name
				
			elif ID_num >= 481 and ID_num <= 504:
				extra_path = 'P5_481-504/assembly/'
				bam_file_name = 'P5_481-504_' + str(ID_num) + bam_end
				my_dict[sample_ID] = path_to_P5_bam + extra_path + bam_file_name
#				print "1 " + str(len(my_dict.keys()))	
			else:
				print 'error' + str(ID_num)

	
#if the sample_ID matches the later panels this code finds the file location in Data4 based on the batch number and sample number and the deduced naming ocnventions within those files 
		elif format_PorV.match(columns[0]):
			sample_ID = str(columns[0])
			file_names_with_sex = sample_ID + "*.realigned.bam"
			date_and_batch = str(columns[1])
			ID_num = int(sample_ID[-3:])
#ke last 8 digits and assign to batch number
			batch_number = int(date_and_batch[-7:])
			if batch_number >= 1501266 and batch_number != 1502972:
				path_to_bam_directory = path_to_V5_bam + date_and_batch.replace('.', '-', 2) + '/assembly/'
				for file in os.listdir(path_to_bam_directory):
					if fnmatch.fnmatch(file, file_names_with_sex): 				
						complete_path_to_bam = path_to_bam_directory + file
						my_dict[sample_ID] = complete_path_to_bam
#						print "2 " + str(len(my_dict.keys()))
			elif batch_number == 1502972:
				path_to_bam_directory = path_to_V5_bam + '2015-08-11_1503151/assembly/'
				for file in os.listdir(path_to_bam_directory):
					if fnmatch.fnmatch(file, file_names_with_sex):
						complete_path_to_bam = path_to_bam_directory + file
						my_dict[sample_ID] = complete_path_to_bam			
#						print "3 " + str(len(my_dict.keys()))
					
#the following are exceptions 
#1404237  and 1404001 need the additional_path 2014-10-27_2014-11-12_rerun/assembly/
	
			elif batch_number == 1404237 and ID_num <= 696:
				path_to_bam_directory = path_to_V5_bam + '2014-11-12_2014-11-26_merged/assembly'
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

#


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
		
#generate 450 dict keys up to this point

#the batch numbers 1403083(14), 1403237(14), 1403375(14), 1403633(14), 1500047, 1500335, 1501051 need rearranging in the format yyyy-mm-dd_nnnnnnnn #		
	
			elif batch_number < 1501266 and batch_number >= 1403083:
				exception_list = [1404237, 1404001, 1404418, 1500634, 1500635, 1500653, 1500654, 1500655, 1500656, 1500657, 1501051]
				if batch_number not in exception_list:
			#		print batch_number
					date_and_batch_universal_step1 = date_and_batch.replace(".", "")
					date_and_batch_universal = date_and_batch_universal_step1.replace("-", "")
					if int(date_and_batch_universal[4]) == 1  and int(date_and_batch_universal[5]) == 4:
						path_to_bam_directory = path_to_V5_bam + '2014-' + date_and_batch_universal[2] + date_and_batch_universal[3] + '-' + date_and_batch_universal[0] + date_and_batch_universal[1] + '_' + str(batch_number) + '/assembly/'  #rearrange ddmmyy to 2014-mm-dd
						rearrange_bam_location(path_to_bam_directory)
#						print "4 " + str(len(my_dict.keys()))
						
					elif int(date_and_batch_universal[4]) == 1 and int(date_and_batch_universal[5]) == 5:
						path_to_bam_directory = path_to_V5_bam + '2015-' + date_and_batch_universal[2] + date_and_batch_universal[3] + '-' + date_and_batch_universal[0] + date_and_batch_universal[1] + '_' + str(batch_number) + '/assembly/' # rearrange ddmmyy to 2015-mm-dd_nnnnnnnn
						rearrange_bam_location(path_to_bam_directory)
#						print "5 " + str(len(my_dict.keys()))



print my_dict
in_file.close()

with open("mitochondrial_sensitivity_MODY.csv", "r") as file:
	for line in file:
		columns = line.split()
		sample_ID = columns[0]
		if sample_ID not in my_dict.keys():
			print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' + str(sample_ID)	
	



#that leaves 221 and if you add up the exceptions in the exception list you get 95. 221-95 126. when print the length only get 118. I think i'm missing 8 from this range.
#568 up to this point
												
##ln -s creates symbolic link. I could get the operating system to call this command for each dictionary value
#print 'final ' + str(len(my_dict.keys()))	

#loop through each dictionary entry and initiate Platypus calls on it

#create a vcf output file path consisting of: 
#vcf_output = base_path + "/variants/" + sample_id + "platypus_m.3243A>G.vcf"

#to use platypus I am going to get the operating system to excecute a concatenated string of cammands and pathways on the Linux command line.
#include here the command to initiate playpus calling on each 
#command = "python" + platypus_path + "callVariants --bamfiles=" + path_to_bam_files + " --refFile=" + build_37_ref + " --output=" + vcf_output + " --regions=" + interval_mtDNA

#could look through the log files generated by platypus to create a global log file which outlines what has been run

'''
The following code enables historic bam files to be located on the server by sample_id and analysed with platypus variant caller

Reads a tab separated input file and produces an array of sample IDs - sample ID must be in the first column
creates an array of sample instances which are used to locate thier respective bam files

'''

import re, subprocess, shlex, glob, os

#class Test_program:
  
class Sample_list:
    multiple_bam_count = 0

    def __init__(self, samples_file):
        self.samples_file = samples_file
        self.patient_id_array = []
        self.non_recognised_ids = []
        self.sample_instances = []

    #extract the first column of the data into an class array
    def patient_id_to_list(self):
        print 'ensure patient id is in the first column of the input data'
        print 'ensure the input data is tab separated'
        #appends patient Ids from input file to patient_ID array
        with open(self.samples_file, 'r') as input_file:
            for line in input_file:
                columns = line.split()
                patient_id = columns[0]
                self.patient_id_array.append(patient_id)
        return self.patient_id_array

    def check_id_format(self):
        #matches P5_a_bcd	
        format_1 = re.compile('P5_\d{1,2}_\d{1,3}')
        #matches v5_abc, v501_abcd, P5_abc
        format_2 = re.compile('[Pv]\d+_\d+')
        for item in self.patient_id_array:
            if format_1.match(item) or format_2.match(item):
	        pass
	    else:
	        self.non_recognised_ids.append(item)
	        self.patient_id_array.remove(item)
	if self.non_recognised_ids:
	    print 'The following patient IDs are not in the recogised format: '
	    print self.non_recognised_ids
	    print 'They have been removed form the original patient ID list, appended to self.non_recognised_ids list and returned.'
	    print 'They have also been written to non_recognised_ids.txt'
	    with open('non_recognised_ids.txt', "w") as out_file:
	        for item in self.non_recognised_ids:
	            out_file.write(item + '\n')
	    return self.non_recognised_ids
	else:
   	    print 'all patient IDs are in the recognised format'

    #creates an array of samples objects for each sample id    	
    def sample_instance_creator(self):
        for item in self.patient_id_array:
            self.sample_instances.append(Sample(item))
        return self.sample_instances

class Sample:
    data1_base_path = "/mnt/Data1/targeted_sequencing"
    data4_base_path = "/mnt/Data4/targeted_sequencing"

    #initialise
    def __init__(self, sample_id):
        self.sample_id = str(sample_id)
        self.sample_id_numeric = ''
        self.data = ""
        self.bam_array = ''
        self.multiple_bam = 0

    def sample_sorter(self):
        if self.sample_id.startswith('P'):
            self.data = 'data1'
        elif self.sample_id.startswith('v'):
            self.data = 'data4'
        else:
            self.data = 'not_p_or_v'
        return self.data

    def locate_bam_file(self):
        if self.data == 'data1':
            split_id = self.sample_id[-3:]
	    self.bam_array = glob.glob(self.data1_base_path + "/P5*/assembly/P5*" + split_id + ".*bam")
            print self.bam_array
	    self.write_to_file()
            return self.bam_array
	elif self.data == 'data4':
	    self.bam_array = glob.glob(self.data4_base_path + "/*-*-*_*/assembly/*" + self.sample_id + "*realigned*.*bam")
            print self.bam_array
	    return self.bam_array
	elif self.data == 'not_p_or_v':
	    print str(self.sample_id) + " does not match the specified regular expressions and the location of it's bamfile can not be determined"

    def write_to_file(self):
        if len(self.bam_array) > 1:
    	    filename = self.data + '_multiple_bam_files.txt'
	    with open(filename, 'a+') as outfile:
	        outfile.write(str(self.bam_array) + '\n')
	elif len(self.bam_array) == 0:
	    filename = self.data + 'no_bam_files.txt'
	    with open(filename, 'a+') as outfile:
	        outfile.write("check sample_ids against check_id_format regexes \n")
		outfile.write(str(self.sample_id) + "\n")

class Variant_calling(object):

    build_37_ref = "/mnt/Data1/resources/human_g1k_v37.fasta"
    #input array as location of bam file to ba analysed. each bam file should be in a separate array.

    #input array ['path_to_bam_file', 'sample_id']
    def __init__(self, input_path_as_array):
	self.input_array = input_path_as_array
		
    #class methods
    def use_platypus(self, output_directory=None):
        platypus_array = [self.input_array[0]]
        if output_directory:
            platypus_array.append(output_directory)
        else:
            platypus_array.append(os.getcwd() + '/' + self.input_array[1] + '.vcf')
	path_to_platypus = "/usr/share/platypus/Platypus_0.8.1/Platypus.py"
        print platypus_array
        cmd = "#qrun python " + path_to_platypus + " callVariants --bamFiles=" + str(platypus_array[0]) + " --nCPU=8" + " --refFile" + self.build_37_ref + " --output=" + str(platypus_array[1])
        print cmd 
        print

if __name__ == "__main__":
    import time
    sample_list = Sample_list('/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus/obsolete/mitochondrial_sensitivity_MODY.csv')
    sample_list.patient_id_to_list()
    sample_list.check_id_format()
    samples = sample_list.sample_instance_creator()
    print str(len(sample_list.sample_instances)) + ' samples instances have been created'

    bam_count = 0
    all_bam_array = []

    for sample in samples:
	sample.sample_sorter()
	sample.locate_bam_file()
	sample.write_to_file()
        length_bam_array = len(sample.bam_array)
        if length_bam_array > 1:
            bam_count += 1
            all_bam_array.append([sample.bam_array[0], sample.sample_id])
        else:
            all_bam_array.append([sample.bam_array[0], sample.sample_id])

    print str(bam_count) + ' patients had multiple realigned bam_files'
#    time.sleep(5)
    print 'Where there are multiple realigned bam files, the first item in the array is used for variant calling'
#    time.sleep(5)
    print "These have been written to file(s) '*_multiple_bam_files.txt' for manual inspection"
#    time.sleep(5)
    print 'Edit the regular expression(s) in Sample.locate_bam_file() to prevent certain patterns being detected if required'
#    time.sleep(5)
    user_answer = raw_input('Do you wish to analyse all samples with platypus, choosing the first bam file if multiple have been identified? y/n')
    if user_answer == 'y': 
        for sample in all_bam_array:
            Variant_calling(sample).use_platypus()
    elif user_anser == 'n':
        pass
    else:
       print 'please enter lowercase y/n and press return'

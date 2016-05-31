'''the following code enables historic samples to be analysed with platypus variant caller although additional functionality 
could be added to the classes'''

#-------------------------------------------------------
'''reads a tab separated input file and produces an array of sample IDs
samples are read into a 1D array although additional methods could be constructed
where more data fields are included in the input data'''

import re, subprocess, shlex, glob

class Input_data:

        def __init__(self, samples_file):
            self.samples_file = samples_file
            self.patient_id_array = []
	    self.non_recognised_ids = []
	    self.sample_instances = []

        #extract the first column of the data into an class array
        def patient_id_to_list(self):
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
        def samples(self):
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

        def sample_sorter(self):
            if self.sample_id.startswith('P'):
                self.data = 'data1'
            elif self.sample_id.startswith('v'):
                self.data = 'data4'
            else:
                self.data = 'not_P_or_v'
            return self.data

        def locate_bam_file(self):
            if self.data == 'data1':
		split_id = self.sample_id[-3:]
		self.bam_array = glob.glob(self.data1_base_path + "/P5*/assembly/P5*" + split_id + ".*bam")
		self.write_to_file()
                return self.bam_array
	    elif self.data == 'data4':
		print self.sample_id
		self.bam_array = glob.glob(self.data4_base_path + "/*-*-*_*/assembly/*" + self.sample_id + "*realigned*.*bam")
		print self.bam_array
		return self.bam_array

	def write_to_file(self):
	    if len(self.bam_array) > 1:
		filename = self.data + 'multiple_bam_files.txt'
		with open(filename, 'a+') as outfile:
		   outfile.write(str(self.bam_array) + '\n')
	    elif len(self.bam_array) == 0:
		filename = self.data + 'no_bam_files.txt'
		with open(filename, 'a+') as outfile:
		    outfile.write(str(self.sample_id) + "\n")

if __name__ == "__main__":
	pd = Input_data('/mnt/Data4/working_directory/stuart/python-2-7-10/scripts/platypus/obsolete/mitochondrial_sensitivity_MODY.csv')
	pd.patient_id_to_list()
	pd.check_id_format()
	samples = pd.samples()
	for sample in samples:
		sample.sample_sorter()
		sample.locate_bam_file()

	print 'Where there are multiple samples, the first one is selected for analysis'
        print 'See multiple_bam_files.txt to view the files that will have been analysed'


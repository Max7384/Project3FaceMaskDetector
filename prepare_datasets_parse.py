
# program to prepare datasets # insert image dir
import random
import os
import subprocess
import sys
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True,
	help="enter the existing directory to iterate")
ap.add_argument("-n", "--name", required=True,
	help="enter name of txt files - will be used for {}_data_train.txt")
args = vars(ap.parse_args())



#image_dir = "./maskpicsPlusBlanks"
image_dir = "./{}".format(args["dir"])
ntrain = "{}_data_train.txt".format(args["name"])
#print(image_dir,ntrain)
nval = "{}_data_test.txt".format(args["name"])
#f_val = open("maskv3_highres_data_test.txt", 'w')
#f_train = open("maskv3_highres_data_train.txt", 'w')
f_val = open(nval, 'w')
f_train = open(ntrain, 'w')


path, dirs, files = next(os.walk(image_dir))
data_size = len(files)

ind = 0
data_test_size = int(0.2 * data_size)
test_array = random.sample(range(data_size), k=data_test_size)

for f in os.listdir(image_dir):
    if(f.split(".")[-1] == "jpg"):
        ind += 1

        if ind in test_array:
            f_val.write(image_dir+'/'+f+'\n')
        else:
            f_train.write(image_dir+'/'+f+'\n')

f_train.close()
f_val.close()
print("Finished, number of pictures: {}".format(ind))
print("{} and {} were created!".format(ntrain,nval))

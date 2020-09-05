# Project3FaceMaskDetector

Project 3: Train a Face Mask Detector

YoloV3 code and pictures

As I was performing the calculations on my home machine and not in colab you will find a description of the process and code samples below.

Next to the pictures there are also the (shortened) log files which contain the result of the training.

# Process

1. Added more sample pictures which have neither masks or no-mask in them (and empty txt with the according name).

2. I used "prepare_datasets_parse.py" which is an adapation of your "prepare_datasets.py" to create the random test pictures set.

e.g. python3 prepare_datasets_parse.py --dir test_pic_4500 --name test

3. Adaption of yoloV*-mask-train.cfg in order to have a high resolution, (workable) subdivisions, filters, classes, maxbatch and steps

4. Adaption of .data file, adding of correct paths.

5. Adaption of the classes file.

6. Run the detector.

e.g. ./darknet detector train yolov3-ramps2-setup.data yolov3-ramps2-train.cfg ./darknet53.conv.74 -dont_show -mjpeg_port 8090 -map 2> log/train_y3_ramps2_log.txt

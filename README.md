# **Models and Certain Code Scripts for TMLR Paper Submission**

This repository contains all 24 trained YOLOv11 models as well as the two most relevant Python scripts used during experimentation. The models are publicly available for use and further training if desired and maintain the purpose of being used in a variety of environmental settings including litter sorting and detection.

As for the scripts, the first is titled "Inference.py" and is able to take a folder input and produce the resulting inferences from the two highest performing models in either object class: PBW7 and CW7. It mostly contains a function labeled "inferences" which takes two arguments. The first is the path to the image folder while the second is a true or false value as to if the user wants the inferences to be displayed while the model makes predictions.

The second script is titled "Occlusion.py" and was used for producing the artificially occluded datasets. The script itself takes both a path to a folder with images and a corresponding path to a folder with the labels for these images. Then, it randomly selects a chosen number of cells in a 4 by 4 grid of each bounding box annotation and turns it black, therefore creating occlusion. There are three values which need to be manually adjusted before it can be applied to a dataset. The first is the number of cells to be occluded per annotation with a value between 1 and 16 (although higher values may not be applicable). The second and third are the file paths to the folders containing images and labels respectively. It is compatible with YOLOv11 bounding box annotations and the file names for the images and their respective labels should match.

Because of their performance, we advise the use of models PBW7 and CW7 in any applications and future training if applicable.

The abstract for the submission which this paper is referencing is shown below (ignoring the link to this repository):

<h2 align="center">
  Abstract
</h2>

<p align="center">
  This paper assesses the accuracy and efficiency differences between object detection and instance segmentation models across the same dataset, considering how two additional factors contribute to the results: learning rate and use of transfer learning. With two versions of the same dataset, one annotated with bounding boxes and the other with polygons, the effects of using one method of computer vision (CV) over the other were isolated, while keeping other factors constant. This allowed for a clear comparison of the efficiency and accuracy metrics for models under these conditions, thereby highlighting the advantages of each CV technique and quantifying them through the metrics used. For testing, we utilized three levels of visual occlusion, adding a different aspect to the comparison. Additionally, to facilitate the identification of drink container waste products, which benefits from having quick and reliable models to reduce manual effort, we propose a combined model infrastructure for the two object classes studied. This aims to assist in future environmental initiatives that may require this machine learning system. Overall, this system, as well as the results from analyzing the different CV tasks, serve to aid future CV frameworks and provide insights into what differences can be expected when using instance segmentation in place of pure object detection.
</p>

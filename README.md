# **Models and Certain Code Scripts for Paper Submission**

This repository contains all 24 trained YOLOv11 models as well as the two most relevant Python scripts used during experimentation. The models are publicly available for use and further training if desired and maintain the purpose of being used in a variety of environmental settings including litter sorting and detection.

Additionally, the image files referenced in the manuscript are also located in this repository under the same file names for access. Note that there are less files than total number of images as repeated images (for example the output of two models producing no inferences) were only labeled and used once in the LaTeX code.

As for the scripts, the first is titled "Inference.py" and is able to take a folder input and produce the resulting inferences from the two highest performing models in either object class: PBW7 and CW7. It mostly contains a function labeled "inferences" which takes two arguments. The first is the path to the image folder while the second is a true or false value as to if the user wants the inferences to be displayed while the model makes predictions.

The second script is titled "Occlusion.py" and was used for producing the artificially occluded datasets. The script itself takes both a path to a folder with images and a corresponding path to a folder with the labels for these images. Then, it randomly selects a chosen number of cells in a 4 by 4 grid of each bounding box annotation and turns it black, therefore creating occlusion. There are three values which need to be manually adjusted before it can be applied to a dataset. The first is the number of cells to be occluded per annotation with a value between 1 and 16 (although higher values may not be applicable). The second and third are the file paths to the folders containing images and labels respectively. It is compatible with YOLOv11 bounding box annotations and the file names for the images and their respective labels should match.

Because of their performance, we advise the use of models PBW7 and CW7 in any applications and future training if applicable.

The abstract for the submission which this paper is referencing is shown below (ignoring the link to this repository):

<h2 align="center">
  Abstract
</h2>

<p align="center">
  Automated materials recovery facilities (MRFs) depend on computer vision to reduce manual labor and improve recycling stream purity, yet the exact correspondence between detection framework and sorting accuracy remain poorly understood. For object detection and instance segmentation
computer vision frameworks applied in such facilities, there is not yet adequate understanding of accuracy-efficiency tradeoffs due to a lack of prior
direct performance comparison. This study addresses that gap by establishing a framework for evaluating how annotation precision between computer
vision frameworks determines false positive rates in YOLO-based waste detection while applying this framework for 2 waste product tasks. By training
24 total models split between different frameworks and learning rates across
2 distinct datasets of 2,600+ images, we introduce a precision ratio r(i, T)
for analyzing models with identical hyperparameters but differing frameworks. Analysis reveals that the multi-task loss function inherent to instance
segmentation contributes accuracy gains beyond increased annotation precision; our performance ratio r(i, T) indicates that false positive reduction
works alongside physical proportions of training data precision, pointing to
a training regularization effect unique to instance segmentation. Critically
for conveyor belt environments with frequent overlap, instance segmentation
maintained significantly higher detection accuracy under artificial occlusion
of 12.5% and 18.75%, with the performance gap widening as occlusion increases. Further, the 27–33% higher processing time of instance segmentation
is justified for MRF settings by disproportionate gains in F1 and mAP performance, and the resulting open-source models offer a key resource for direct
model implementation.
</p>

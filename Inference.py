from ultralytics import YOLO
import os
#Make sure that Ultralytics is installed

def inferences(path_to_image_folder, view):
  #replace with actual path

  model_PBW = YOLO(r"PBW7.pt")
  model_CW = YOLO(r"CW7.pt")

  Finished_Results = {}

  count_plastic_bottles = 0
  count_drink_cans = 0

  for image in os.listdir(path_to_image_folder):
    results_plastic = model_PBW(rf"{path_to_image_folder}\{image}")
    results_can = model_CW(rf"{path_to_image_folder}\{image}")
    #runs inference

    count_plastic_bottles += len(results_plastic[0])
    count_drink_cans += len(results_can[0])
    #changes counts

    both_results = [results_plastic, results_can]
    Finished_Results[image] = both_results
    #Makes Changes to Dictionary

    if view:
      results_plastic[0].show()
      #shows predictions for plastic model

      wait_between_models = input("Press enter to continue to second model.")
  
      results_can[0].show()
      #shows predictions for can model

      wait = input("Press enter to continue to next inference.")
  return Finished_Results, count_plastic_bottles, count_drink_cans

#Potential Use for a folder with viewing inference outputs
image_inferences = inferences(r"All Images", True)

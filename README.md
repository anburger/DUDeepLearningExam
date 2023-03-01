This project performs checks on the ResNeXt model: 
[Aggregated residual transformations for deep neural networks](https://arxiv.org/abs/1611.05431)

The `resnet.pytorch`-directory has been checked out from another gitlab repository (with slight custom modifications to adapt to custom use): [https://github.com/prlz77/ResNeXt.pytorch]( https://github.com/prlz77/ResNeXt.pytorch) 

============================================

Running the jupyter notebook `ResNeXt_tests_ABurger.ipynb` needs the `TestFigures/`-directory and the `resnext.pytorch`- directory.

`GoogleColabNotebook/ResNeXt_TrainOnFlower-102_Data_ABurger.ipynb` has been tested on google colab and runs without any local files.


============================================

The jupyter notebook `ResNeXt_tests_ABurger.ipynb` loads a pre-trained pytorch model [link](https://pytorch.org/hub/pytorch_vision_resnext/) and performs some basic tests: 
 - load the model
 - have the pre-trained model classify some random images
 - Test the content of the flower-102 dataset
 - Training of the model on the flowers-102 dataset is performed using the script `GoogleColabNotebook/ResNeXt_TrainOnFlower-102_Data_ABurger.ipynb` on the google colab environment (not in this notebook)
 - The logs of the trained models have been saved in `resnext.pytorch/logs/`. This notebook runs plotting scripts taking the files in `resnext.pytorch/logs/` as input.
 
 
 The jupyter notebook `GoogleColabNotebook/ResNeXt_TrainOnFlower-102_Data_ABurger.ipynb` trains and tests the ResNeXt model using the [flowers-102](https://pytorch.org/vision/main/generated/torchvision.datasets.Flowers102.html) dataset.


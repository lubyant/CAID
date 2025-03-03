# CAID
CAID Dataset and Deep Learning Model Training

Download the CAID Dataset

Please download the CAID dataset from the following Dropbox link:
Download CAID Dataset

Setting Up MMSegmentation

To test deep learning model performance on CAID, first download and install MMSegmentation.

Modify voc.py

After installation, modify the voc.py file located under mmseg/datasets to ensure it contains only two classes:

background

water

Also, update the color palette to:

PALETTE = [[0, 0, 0], [128, 0, 0]]

Organizing the Dataset

Navigate to the mmsegmentation folder.

Create a folder named datasets if it does not already exist.

Unzip the downloaded CAID dataset inside this datasets folder.

Rename the extracted folder to voc2012.

Training the Model

Running Training in Terminal

Open a terminal and activate the correct Python environment.

Run the following command to train CCNet on CAID:

python tools/train.py --config ./my_model/CCNetBenchmark/ccnet_r50-d8_4xb4-20k_voc12aug-512x512.py --work-dir /home/weiwang/ResearchProjects/mmsegmentation/my_model_res/CCNetBenchmark/

To train other deep learning models, replace the --config and --work-dir arguments with the appropriate paths for the desired model.


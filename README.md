[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/fadymedhat/ESC50-augmented-for-MCLNN/blob/master/LICENSE)

# ESC50 dataset augmented for MCLNN

The [ESC10](https://github.com/karoldvl/ESC-50) environmental sound dataset.

| Clip Duration  | Format | Original Clips Count | Categories| Augmentation Count | Augmented Clips Count |  
|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 secs | .wav (originally .ogg)  | 2,000 | 50 | 4  | 10,000 | 

A 5-seconds file may contain events shorter than 5 seconds, accordingly the authors of the dataset padded all files
 to unify the 5 seconds length for all files.
 
 This folder contains:
  * Scripts required to prepare an augmented version of the ESC50 dataset for the MCLNN processing.
  * Pretrained weights and indices for the 5-fold cross-validation in addition to the standardization parameters.
  
 ## Prepossessing
 
The following are the steps involved in preparing the augmented ESC50 dataset:
1) Follow the steps in [ESC50-for-MCLNN](https://github.com/fadymedhat/ESC50-for-MCLNN) to download and preprocess the original ESC50 dataset.
2) Apply the controlled deformations for each clip using the scripts provided in this folder.  

  
#### Preparation scripts prerequisites

The [Preparation Scripts](https://github.com/fadymedhat/ESC50-augmented-for-MCLNN/tree/master/ESC50_4augment_preparation_scripts) require the following packages to be installed beforehand:

* [Rubber Band](https://breakfastquay.com/rubberband/) v1.8.1 An audio time-stretching and pitch-shifting library and utility program
* numpy 1.11.2+mkl
* librosa 0.4.0
* h5py 2.6.0
* muda 0.2.0
   
#### Steps

1. Download the dataset using the [ESC50_download](https://github.com/fadymedhat/ESC50-for-MCLNN/tree/master/ESC50_download) script, make sure the files of each category are in a separate folder.
If you prefer to download the dataset directly, make sure the files are ordered following the [esc50_storage_ordering](https://github.com/fadymedhat/ESC50-augmented-for-MCLNN/blob/master/esc50_storage_ordering.txt) file.
2. Position the scripts of the [Preparation Scripts](https://github.com/fadymedhat/ESC50-augmented-for-MCLNN/tree/master/ESC50_4augment_preparation_scripts) directory in the downloaded dataset parent directory and execute them in order following the "id_XX" index in the file name after applying any necessary configuration.
3. Configure the spectrogram transformation within the [Dataset Transformer](https://github.com/fadymedhat/MCLNN/tree/master/dataset_transformer) and generate the MCLNN-Ready hdf5 for the dataset.
4. Generate the indices for the folds using the [Index Generator](https://github.com/fadymedhat/MCLNN/tree/master/index_generator) script.
















# ESC10 dataset for MCLNN

The [ESC10](https://github.com/karoldvl/ESC-10) environmental sound dataset.

| Clip Duration  | Format | Count | Categories|
|:---:|:---:|:---:|:---:|
| 5 secs | .wav (originally .ogg)  | 400 | 10 |

A 5-seconds file may contain events shorter than 5 seconds, accordingly the authors of the dataset padded all files
 to unify the 5 seconds length for all files.
 
 This folder contains:
  * Scripts required to prepare the ESC10 dataset for the MCLNN processing.
  * Pretrained weights and indices for the 5-fold cross-validation in addition to the standardization parameters 
  to replicate the results in:
 
    _Fady Medhat, David Chesmore and John Robinson, "Environmental Sound Recognition Using Masked Conditional Neural Networks," 2017  Advanced Data Mining and Applications (ADMA)_
 
 ## Prepossessing
 
The following are the steps involved to prepare the ESC10 dataset:
1) Trim all files by removing the zero padding added by the authors of the dataset.
2) Clone and concatenate each sample to make its length at least equal to 5 seconds.

__Note:__ 
Some changes were applied on the dataset original repository by the authors:
 * The original files were in .ogg and now they are in .wav
 * The files ESC10 dataset were merged with their parent dataset the ESC50. The merge involved a change to the folders 
 naming convention and consequently the order of the files aa shown below. 
 
 <p align='center'><img height='230'  src='imgs/esc10_orig_new_naming.png'/></p>
 
 The above changes will affect replicating the results reported in this experiment, if the pretrained weights and the 
  indices provded are used in combination with the new structure of the dataset. 
  Accordingly, we provided a download script in the [ESC10_download](https://github.com/fadymedhat/ESC10-for-MCLNN/tree/master/ESC10_download)
  that will pull the required files in the original order and folder naming convention before the authors modifications.
  

  
#### Preparation scripts prerequisites

The [Preparation Scripts](https://github.com/fadymedhat/ESC10-for-MCLNN/tree/master/ESC10_preparation_scripts) require the following packages to be installed beforehand:
   
   * ffmpeg version N-81489-ga37e6dd
   * numpy==1.11.2+mkl
   * librosa==0.4.0
   * h5py==2.6.0
 
#### Steps

1. Download the dataset using the [ESC10_download](https://github.com/fadymedhat/ESC10-for-MCLNN/tree/master/ESC10_download) script, make sure the files of each category are in a separate folder.
If you prefer to download the dataset directly, make sure the files are ordered following the [esc10_storage_ordering](https://github.com/fadymedhat/ESC10-for-MCLNN/blob/master/esc10_storage_ordering.txt) file.
2. Position the scripts of the [Preparation Scripts](https://github.com/fadymedhat/ESC10-for-MCLNN/tree/master/ESC10_preparation_scripts) directory.
in the downloaded dataset parent directory and execute them in order following the "id_XX" index in the file name after applying any necessary configuration.
3. Configure the spectrogram transformation within the [Dataset Transformer](https://github.com/fadymedhat/MCLNN/tree/master/dataset_transformer) and generate the MCLNN-Ready hdf5 for the dataset.
4. Generate the indices for the folds using the [Index Generator](https://github.com/fadymedhat/MCLNN/tree/master/index_generator) script.

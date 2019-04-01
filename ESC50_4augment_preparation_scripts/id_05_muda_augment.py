"""
This script is used to generate the augmentation variants for the dataset
make sure to configure the source and destination folders and have muda installed before your execute this script
 Fady Medhat
 version 0.1
"""

import os
import muda

SRC_PATH = 'I:/dataset-esc50/ESC-50-masterstretched'
DST_PATH = 'I:/dataset-esc50_MUDA/ESC-50-JAMS2'

class_folder = os.listdir(SRC_PATH)
class_folder.sort()

TEMPLATE_FILE_NAME = 'id_05_muda_augment_template.jams'
PITCH_SHIFT_LIST = [-1, 1]
TIME_STRETCH = {'samples': 2, 'lower_bound': -0.3, 'upper_bound': 0.3}

for class_id in class_folder:  # range(0,len(classfolder)):#len(classfolder)
    files = os.listdir(os.path.join(SRC_PATH, class_id))
    files.sort()
    category_path = os.path.join(DST_PATH, class_id)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    for file_name in files:

        file_path = os.path.join(category_path, file_name.rsplit('.', 1)[0])

        j_orig = muda.load_jam_audio(TEMPLATE_FILE_NAME, os.path.join(SRC_PATH, class_id, file_name))  #

        for pitch_shift in PITCH_SHIFT_LIST:
            pitch = muda.deformers.PitchShift(n_semitones=pitch_shift)
            jam_out = pitch.transform(j_orig).next()

            wav_filename = file_path + '_pitch_{0:+}.wav'.format(pitch_shift)
            jams_filename = wav_filename.replace('.wav','.jams')
            muda.save(wav_filename, jams_filename, jam_out)

        stretch = muda.deformers.LogspaceTimeStretch(n_samples=TIME_STRETCH['samples'],
                                                     lower=TIME_STRETCH['lower_bound'],
                                                     upper=TIME_STRETCH['upper_bound'])

        for i, jam_out in enumerate(stretch.transform(j_orig)):
            wav_filename = file_path + '_stretch_' \
                           + str(TIME_STRETCH['lower_bound']) \
                           + '_' + str(TIME_STRETCH['upper_bound'])\
                           + '_{:02d}.wav'.format(i)
            jams_filename = wav_filename.replace('.wav','.jams')

            muda.save(wav_filename, jams_filename, jam_out)

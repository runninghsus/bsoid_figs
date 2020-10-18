import pandas as pd
import numpy as np
import glob

path = '/Users/ahsu/Downloads/exercise_1/'

filenames = glob.glob(path + '/*.json')
xyl_array = np.empty((len(filenames), 75))
for j, f in enumerate(filenames):
    df = pd.read_json(f)
    data_arr = df['people']
    data_length = len(data_arr[0]['pose_keypoints_2d'])
    x_val = data_arr[0]['pose_keypoints_2d'][0:data_length:3]
    y_val = data_arr[0]['pose_keypoints_2d'][1:data_length:3]
    l_val = data_arr[0]['pose_keypoints_2d'][2:data_length:3]
    xyl = []
    for i in range(int(data_length/3)):
        xyl.extend([x_val[i], y_val[i], l_val[i]])
    xyl_array[j, :] = np.array(xyl).reshape(1, len(xyl))
micolumns = pd.MultiIndex.from_tuples([('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood'),
                                       ('body part1', 'x'), ('', 'y'), ('', 'likelilhood')],
                                      names=['Openpose', 'Frame number'])
df = pd.DataFrame(xyl_array, columns=micolumns)
df.to_csv(str.join('', (path, 'exercise1.csv')), index=True, chunksize=10000, encoding='utf-8')


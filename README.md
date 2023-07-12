# Subtitles Analysis

This repository contains two Jupyter Notebook files for analyzing movie subtitles and predicting emotions.

## Subtitles Emotion Prediction

The first file, `Subtitles_Emotion_Prediction.ipynb`, performs emotion detection on movie subtitles using two different approaches. The output of this notebook is saved in the "Predicted emotion" folder. Please ensure that you change the path of the `.csv` files, if necessary, at the beginning of each notebook.

## Analysis of Subtitles

The second file, `Analysis_of_Subtitles.ipynb`, utilizes the subtitle files with predicted emotions to provide various analyses and generate graphs. This notebook also includes functions that accept four parameters: `df`, `s`, `c`, and `name`.

- `df` specifies the data frame on which you want to apply the function (`a1_df_movies` for approach 1 and `a2_df_movies` for approach 2).
- `s` is used to specify whether you want analysis based on category (`c`) or genre (`g`).
- `c` specifies the particular category or genre you are interested in (e.g., `top`, `romance`).
- `name` is the title of the graph generated.

Make sure to update the path of the `.csv` files if necessary, at the beginning of each notebook.

## Output and Graphs

Both notebooks generate output and graphs based on the analysis performed. The output of the `Subtitles_Emotion_Prediction.ipynb` notebook is saved in the "Predicted emotion" folder, while the `Analysis_of_Subtitles.ipynb` notebook generates graphs for further analysis.

Please refer to the notebooks for more detailed information and instructions.

# Short Films Analysis

This repository contains the analysis of short films, which has been divided into three parts: hand tagging of emotion, emotion prediction from background music, and emotion detection from videos. The analysis is based on the data generated from these three parts.

The folder 'Shortfilm Data' has all the related .csv files. Please refer to these files for a proper understanding of the data.

The folder 'codes' contains all the necessary .ipynb files which were used for the analysis and emotion prediction.

Note: The video files and audio files are not included in this repository. For the background music data, you can access the files from the following link: [Background Music Data](https://drive.google.com/drive/folders/1CIgALfOoFEZhZAO1acLN_1D0kxxUumF0).

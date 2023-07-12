# Movie Analysis 
`Analysis of Sequences of Emotions in Movies.pdf` is the final report of our project.
## Subtitles Analysis

This repository contains two Jupyter Notebook files for analyzing movie subtitles and predicting emotions.

### Subtitles Emotion Prediction

The first file, `Subtitles_Emotion_Prediction.ipynb`, performs emotion detection on movie subtitles using two different approaches. The output of this notebook is saved in the "Predicted emotion" folder. Please ensure that you change the path of the `.csv` files, if necessary, at the beginning of each notebook.

### Output and Graphs

Both notebooks generate output and graphs based on the analysis performed. The output of the `Subtitles_Emotion_Prediction.ipynb` notebook is saved in the "Predicted emotion" folder, while the `Analysis_of_Subtitles.ipynb` notebook generates graphs for further analysis.

Please refer to the notebooks for more detailed information and instructions.

### Analysis of Subtitles

The second file, `Analysis_of_Subtitles.ipynb`, utilizes the subtitle files with predicted emotions to provide various analyses and generate graphs. This notebook also includes functions that accept four parameters: `df`, `s`, `c`, and `name`.

- `df` specifies the data frame on which you want to apply the function (`a1_df_movies` for approach 1 and `a2_df_movies` for approach 2).
- `s` is used to specify whether you want an analysis that includes emotion pairs with the same emotions and neutral emotion (`s`) or which only includes distinct emotion pairs and does not include neutral emotion (`d`).
- `c` is for specifying if you want graphs on category (`c`) or genre (`g`).
- `name` is the title of the specific category (`top`, `middle`, `lower`) or the specific genre (eg. `romance`).


## Short Films Analysis

This repository contains the analysis of short films, which has been divided into three parts: hand tagging of emotion, emotion prediction from background music, and emotion detection from videos. The analysis is based on the data generated from these three parts.

### Data Files

The folder 'Shortfilm Data' contains all the related .csv files. Please refer to these files for a proper understanding of the data.

### Code Files

The folder 'codes' contains all the necessary .ipynb files used for the analysis and emotion prediction.

### Video and Audio Files

Please note that the video files and audio files are not included in this repository. You can access the background music data files from the following link: [Background Music Data](https://drive.google.com/drive/folders/1CIgALfOoFEZhZAO1acLN_1D0kxxUumF0). Similarly, you can access the short film video files from the following link: [Video files](https://www.playbook.com/s/happyworld/HQbVZa4BtSS6aUCbcM76ZeXF).


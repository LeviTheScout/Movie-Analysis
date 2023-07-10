import cv2
from deepface import DeepFace
import csv

def add_top_two_dominant_emotions_to_csv(video_path, csv_file):
    # Read the existing CSV file
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Add the columns of top two dominant emotions to the header
    header = data[0]
    header.extend(['Top Dominant Emotion 1', 'Top Dominant Emotion 2'])

    # Iterate over the rows and add the top two dominant emotions
    for row in data[1:]:
        start_time, end_time = map(float, row[:2])
        top_dominant_emotions = get_top_two_dominant_emotions(video_path, start_time, end_time)
        row.extend(top_dominant_emotions)

    # Write the updated data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Top dominant emotions added to '{csv_file}' successfully.")

def get_top_two_dominant_emotions(video_path, start_time, end_time):
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    addedd = {}

    # Calculate frame indexes for start and end time
    start_frame = int(start_time * frame_rate)
    end_frame = int(end_time * frame_rate)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    while frame_count <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % (frame_rate // 4) == 0:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            for d in result[0]['emotion']:
                if d in addedd:
                    addedd[d] += result[0]['emotion'][d]
                else:
                    addedd[d] = result[0]['emotion'][d]

        if frame_count % (frame_rate * 5) == 0 and frame_count != 0:
            top_emotions = sorted(addedd, key=addedd.get, reverse=True)[:2]
            cap.release()
            cv2.destroyAllWindows()
            return top_emotions

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    return None

add_top_two_dominant_emotions_to_csv('Plus Minus.mp4', 'Plus Minus.csv')
#change video path and csv file name 
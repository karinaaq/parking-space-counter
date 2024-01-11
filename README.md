# Parking Spaces Counter
This Python code utilizes the OpenCV library to perform parking spot occupancy detection in a video.
To accomplish this task, we first require a mask to identify all the available parking spaces. Additionally, a static camera is necessary to maintain control over the baseline appearance of the parking spots, distinguishing between empty and occupied states.

![mask](https://github.com/karinaaq/parking-space-counter/assets/67199946/c5766474-9217-4f32-8839-5c18b8756473)

This code essentially processes a video frame by frame, detects changes in specified parking spots, and classifies them as either occupied or empty, displaying the results in real-time.

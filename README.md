# Parking Spaces Counter
This Python code utilizes the OpenCV library to perform parking spot occupancy detection in a video.
To accomplish this task, we first require a mask to identify all the available parking spaces. Additionally, a static camera is necessary to maintain control over the baseline appearance of the parking spots, distinguishing between empty and occupied states
![spots](https://github.com/karinaaq/parking-space-counter/blob/main/media/spots.PNG)
![mask_crop](https://github.com/karinaaq/parking-space-counter/blob/main/media/mask_crop.png)

This code essentially processes a video frame by frame, detects changes in specified parking spots, and classifies them as either occupied or empty, displaying the results in real-time.

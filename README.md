# Parking Spaces Counter 🚖🚘✔️
This Python code utilizes the OpenCV library to perform parking spot occupancy detection in a video.
To accomplish this task, we first require a mask to identify all the available parking spaces. Additionally, a static camera is necessary to maintain control over the baseline appearance of the parking spots, distinguishing between empty and occupied states.

![mask](https://github.com/karinaaq/parking-space-counter/assets/67199946/c5766474-9217-4f32-8839-5c18b8756473)

The video is analyzed every 40 frames, and each parking space in the frame undergoes a model that predicts whether it is occupied or not. For the model, Support Vector Machines (SVMs) are used; these are a set of supervised learning methods employed for classification, regression, and outlier detection, specifically utilizing the SVC model from the sklearn library.

To avoid unnecessary calculations and predictions, each 40 frames are compared with the previous frame (40 frames ago). The average of the image matrices from both frames is calculated, and if the value is significantly different, it indicates a substantial change in the image. When this occurs, the model predicts whether the space is occupied or not.

![output](https://github.com/karinaaq/parking-space-counter/assets/67199946/be458166-dd19-405d-a0ee-1783305d8c3f)

🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲🚗🚕🚙🚚🚲

This code essentially processes a video by frame, detects changes in specified parking spots, and classifies them as either occupied or empty, displaying the results in real-time.


import cv2
import numpy as np
from utils import empty_or_not, calc_diff

mask = "assets/masks/mask_1920_1080.png" 
video_path = "assets/videos/parking_1920_1080_loop.mp4"

mask = cv2.imread(mask, 0)
cap = cv2.VideoCapture(video_path)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

ret = True
step = 40 #frames, how often to classify
fr_nm = 0
spots_status = [None for j in contours]
diff = [None for j in contours]
previous_frame= None
while ret:
    ret, frame = cap.read()
    if fr_nm % step == 0 and previous_frame is not None:
        for spot_indx, contour in enumerate(contours):
            x1, y1, w, h = cv2.boundingRect(contour)
            spot_crop = frame[y1:y1+h, x1:x1+w, :]
            diff[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1+h, x1:x1+w, :])    


    if fr_nm % step == 0:
        if previous_frame is None:
            arr_= range(len(contours))
        else:
            arr_ = [j for j in np.argsort(diff) if diff[j]/np.amax(diff)>0.4]

        for spot_indx in arr_:
            contour = contours[spot_indx]
            x1, y1, w, h = cv2.boundingRect(contour)
            spot_crop = frame[y1:y1+h, x1:x1+w, :]
            spot_status = empty_or_not(spot_crop)
            spots_status[spot_indx]= spot_status

    if fr_nm % step == 0: 
        previous_frame = frame.copy()
    
    for spot_indx, contour in enumerate(contours):
        x1, y1, w, h = cv2.boundingRect(contour)
        spot_status = spots_status[spot_indx]
        if spot_status:
            cv2.rectangle(frame, (x1, y1), (x1+w, y1+h),(0,255,0), 2)
        else:
            cv2.rectangle(frame, (x1, y1), (x1+w, y1+h),(0,0,255), 2)
    fr_nm += 1
    cv2.putText(frame,f'Available spots: {str(sum(spots_status))}/{str(len(spots_status))}'.format(),(150,60), cv2.FONT_HERSHEY_PLAIN, 3,(150,253,253),2)
    cv2.namedWindow('Parking Spaces', cv2.WINDOW_NORMAL)
    cv2.imshow('Parking Spaces', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
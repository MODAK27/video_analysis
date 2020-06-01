
'''video analysis camshift'''

#python H:\github_proj\video_compressor.py -i H:\github_proj\video_analysis\cars_openCV_traffic_square.mp4 -o H:\github_proj\video_compressor.mp4
import numpy as np
import cv2
import argparse
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,help="path to input video")
ap.add_argument("-o", "--output", type=str,
	help="path to output video")
args = vars(ap.parse_args())
# initialize the pointer to the video file and the video writer
print("[INFO] processing video...")
cap = cv2.VideoCapture(args["input"])
writer=None
# take first frame of the video
ret,frame = cap.read()

while(1):
    ret ,frame = cap.read()

    if ret == True:
        cv2.imshow('img2',frame)
        # if the video writer is None
        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            writer = cv2.VideoWriter(args["output"], fourcc, 24,(frame.shape[1], frame.shape[0]), True)
        else:
            # if the writer is not None, write the frame with recognized
            writer.write(frame)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        

    else:
        break

cv2.destroyAllWindows()
cap.release()
writer.release()



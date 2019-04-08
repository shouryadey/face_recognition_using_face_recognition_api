import os
import face_recognition
import cv2
cap=cv2.VideoCapture(0) #create a videocapture object with path to the webcam(usually its 0,-1,2),can be changed to videopath if required 
#but make sure to have the video in the current working directory
 
sdey_img=face_recognition.load_image_file('sdey.jpg')#load the face to be compared against

sdey_face_encoding=face_recognition.face_encodings(sdey_img)[0]#get the encodings for that face ...face_recognition.face_encodings() returns list of encodings of faces
#encodings are the 128 measurements particular to a face.

count=0

print("print ESC to close,make sure you select the video-feed")

while True:

    ret,img=cap.read()

    if ret == False :
        print("cannot open camera")
        break

    if count%4==0:#to consider every  4th frame
        face_loc=face_recognition.face_locations(img)#find the co-ordinates for the reactangle or the bounding boxes for the faces in frame img

        for (y1,x1,y,x) in face_loc:#for each face in the current frame (top,right,bottom,left)

            face_encodings=face_recognition.face_encodings(img,[(y1,x1,y,x)])#get face encodings

            distance=face_recognition.face_distance(sdey_face_encoding,face_encodings)#compare against the known face face_distance() returns the distance between the two faces

            if distance<0.50:#if distance between the two faces < threshold (here .50) ,the face is a known one.You can change it accordingly.
                cv2.putText(img, "Shourya Dey "+str(distance),(x,y1+6),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),1)#using cv2.putText() to write in the current frame
                cv2.rectangle(img,(x,y),(x1,y1),(0,255,0),2,2)#using cv2.rectangle() to draw rectangle

            else:#else unkown
                cv2.putText(img, "Unknown "+str(distance),(x,y1+6),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),1)#similar

                cv2.rectangle(img,(x,y),(x1,y1),(0,255,0),2,2)#similar

        cv2.imshow('video-feed',img)#video-feed
    count=count+1
    k=cv2.waitKey(30) & 0xff#press escape to exit the while loop
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

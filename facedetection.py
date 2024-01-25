#参考 https://konchangakita.hatenablog.com/entry/2020/07/30/220000

import cv2 as cv

face_cascade_path = 'opencv/data/haarcascades/haarcascade_frontalface_default.xml'
glasses_cascade_path = 'opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # 顔の検出
    faces = face_cascade.detectMultiScale(frame_gray)
    glasses = glasses_cascade.detectMultiScale(frame_gray)

    # 複数の顔が検出された場合、ひとつづつ枠を付ける
    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=3, lineType=cv.LINE_4, shift=0)
        
    for (x,y,w,h) in glasses:
        frame = cv.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=3, lineType=cv.LINE_4, shift=0)

    cv.imshow('OpenCV - facedetect', frame)


if __name__ == "__main__":

    face_cascade = cv.CascadeClassifier()
    glasses_cascade = cv.CascadeClassifier()

    if not face_cascade.load(cv.samples.findFile(face_cascade_path)):
        print('--(!)Error loading face cascade')
        exit(0)

    if not glasses_cascade.load(cv.samples.findFile(glasses_cascade_path)):
        print('--(!)Error loading glasses cascade')
        exit(0)

    cap = cv.VideoCapture(11)
    try:   
        while True:
            ret, frame = cap.read()
            if frame is None:
                print('--(!) No captured frame -- Break!')
                break

            detectAndDisplay(frame)

            if cv.waitKey(10) == 27:
                break

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        print("\nCamera Interrupt")

    finally:
        cap.release()
        cv.destroyAllWindows()

#参考 https://konchangakita.hatenablog.com/entry/2020/07/30/220000

import cv2 as cv

face_cascade_path = 'opencv/data/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = 'opencv/data/haarcascades/haarcascade_eye.xml'
glasses_cascade_path = 'opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # 顔の検出
    faces = face_cascade.detectMultiScale(frame_gray)

    # 複数の顔が検出された場合、ひとつづつ枠を付ける
    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=3, lineType=cv.LINE_4, shift=0)

        #顔の範囲切り出し
        faceROI = frame_gray[y:y+h,x:x+w]
        # 顔ごとに目を検出する
        eyes = eye_cascade.detectMultiScale(faceROI)
        # 顔ごとにメガネを検出する
        #glasses = glasses_cascade.detectMultiScale(faceROI)
        
        for (x2,y2,w2,h2) in eyes:
            frame = cv.rectangle(frame, pt1=(x2, y2), pt2=(x2+w2, y2+h2), color=(0, 0, 255), thickness=3, lineType=cv.LINE_4, shift=0)

        #for (x,y,w,h) in glasses:
        #    frame = cv.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 255), thickness=3, lineType=cv.LINE_4, shift=0)

    cv.imshow('OpenCV - facedetect', frame)


if __name__ == "__main__":

    face_cascade = cv.CascadeClassifier()
    eye_cascade = cv.CascadeClassifier()
    glasses_cascade = cv.CascadeClassifier()

    if not face_cascade.load(cv.samples.findFile(face_cascade_path)):
        print('--(!)Error loading face cascade')
        exit(0)

    if not eye_cascade.load(cv.samples.findFile(eye_cascade_path)):
        print('--(!)Error loading eye cascade')
        exit(0)

    if not glasses_cascade.load(cv.samples.findFile(glasses_cascade_path)):
        print('--(!)Error loading glasses cascade')
        exit(0)

    cap = cv.VideoCapture(11)
    #画像サイズ指定
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    #露光自動
    cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)
    #フォーカス自動
    cap.set(cv.CAP_PROP_AUTOFOCUS, 1)

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

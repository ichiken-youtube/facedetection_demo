#参考 https://konchangakita.hatenablog.com/entry/2020/07/30/220000

import cv2 as cv

face_cascade_path = 'opencv/data/haarcascades/haarcascade_frontalface_default.xml'


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # 顔の検出
    faces = face_cascade.detectMultiScale(frame_gray)

    # 複数の顔が検出された場合、ひとつづつ枠を付ける
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        #frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        frame = cv.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=3, lineType=cv.LINE_4, shift=0)
        
        #faceROI = frame_gray[y:y+h,x:x+w]

        '''# 顔ごとに目を検出する
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))


            ex = int((x + x2) - w2 / 2)
            ey = int(y + y2)
            ew = int(w2 * 2.5)
            frame = mosaic_area(frame, ex, ey, ew, h2)
            #frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), -1)'''


    cv.imshow('OpenCV - facedetect', frame)
    #cv.imshow('OpenCV - test', frame_gray)

if __name__ == "__main__":

    face_cascade = cv.CascadeClassifier()
    face_cascade.load(cv.samples.findFile(face_cascade_path))

    if not face_cascade.load(cv.samples.findFile(face_cascade_path)):
        print('--(!)Error loading face cascade')
        exit(0)

    cap = cv.VideoCapture(11)
    try:   
        while True:
            ret, frame = cap.read()
            if frame is None:
                print('--(!) No captured frame -- Break!')
                break

            # ビデオ上にテキストを表示 (カメラデータ, 文字, (表示位置), フォント, フォントサイズ, 色, 太さ, 線の種類)
            #cv.putText(frame, 'mokemoke', (200,50), cv.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv.LINE_AA)

            detectAndDisplay(frame)

            if cv.waitKey(10) == 27:
                break

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        print("\nCamera Interrupt")

    finally:
        cap.release()
        cv.destroyAllWindows()

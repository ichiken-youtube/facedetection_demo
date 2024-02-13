#参考 https://konchangakita.hatenablog.com/entry/2020/07/27/220000

import cv2 as cv

#カメラインスタンス作成
#Rock5Bの外部カメラの場合11
cap = cv.VideoCapture(11)
#画像サイズ指定
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
#露光自動
cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)
#フォーカス自動
cap.set(cv.CAP_PROP_AUTOFOCUS, 1)


assert cap.isOpened(), 'Cannot capture source'

try:   
    while True:
        ret, frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break

        cv.imshow('OpenCV - test', frame)
        
        if cv.waitKey(10) == 27:
            break

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    print("\nCamera Interrupt")

finally:
    cap.release()
    cv.destroyAllWindows()

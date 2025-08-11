import cv2
import numpy as np
import time
from handTracking import handTracking 


def main():
    cap = cv2.VideoCapture(0)
    detector = handTracking()
    canvas = None
    brush_color = (0, 0, 255)
    brush_thickness = 5
    eraser_thickness = 50
    xp, yp = 0, 0
    saved_count = 0
    clear_triggered = False  # 전체 지우기 한 번만 실행을 위한 플래그

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        if canvas is None:
            canvas = np.zeros_like(frame)

        frame = detector.drawHands(frame)
        lmList = detector.importLandmarks(frame)

        if lmList:
            fingers = detector.fingersUp()
            cx, cy = lmList[8][1], lmList[8][2]  # 검지 끝 위치

            # 1. 검지만 펴짐 → 그리기
            if fingers == [0, 1, 0, 0, 0]:
                if xp == 0 and yp == 0:
                    xp, yp = cx, cy
                cv2.line(canvas, (xp, yp), (cx, cy), brush_color, brush_thickness)
                xp, yp = cx, cy
                clear_triggered = False  # 다른 동작 시 플래그 초기화

            # 2. 주먹 → 그림 저장 + 종료
            elif fingers == [0, 0, 0, 0, 0]:
                xp, yp = 0, 0
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"drawing_{timestamp}_{saved_count}.png"
                gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
                _, alpha = cv2.threshold(gray_canvas, 10, 255, cv2.THRESH_BINARY)
                b, g, r = cv2.split(canvas)
                rgba = cv2.merge((b, g, r, alpha))
                cv2.imwrite(filename, rgba)
                print(f"[INFO] 투명 배경으로 그림 저장됨: {filename}")
                saved_count += 1
                print("주먹 인식, 저장 완료 후 프로그램 종료합니다.")
                time.sleep(1)
                cap.release()
                cv2.destroyAllWindows()
                return 

            # 3. 검지 + 중지 펴짐 (브이) → 해당 위치만 지우기
            elif fingers == [0, 1, 1, 0, 0]:
                cv2.circle(canvas, (cx, cy), eraser_thickness // 2, (0, 0, 0), -1)
                xp, yp = 0, 0
                clear_triggered = False

            # 4. 손가락 전부 펴짐 → 전체 지우기 (한 번만)
            elif fingers == [1, 1, 1, 1, 1]:
                if not clear_triggered:
                    canvas = np.zeros_like(frame)
                    print("[INFO] 캔버스 초기화됨")
                    clear_triggered = True
                xp, yp = 0, 0

            # 5. 기타 → 좌표 초기화
            else:
                xp, yp = 0, 0
                clear_triggered = False

        # ====== Bitwise 방식으로 canvas와 frame 합성 ======
        gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_canvas, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
        canvas_fg = cv2.bitwise_and(canvas, canvas, mask=mask)

        output = cv2.add(frame_bg, canvas_fg)

        # 안내 텍스트 표시
        cv2.putText(output, "1 Finger: Draw | 2 Fingers: Erase", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(output, "Fist: Save & Exit | Open Palm: Clear", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # 출력
        cv2.imshow("Virtual Paint", output)

        # 키보드로 수동 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("종료합니다.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
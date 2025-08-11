import cv2
import mediapipe as mp
import numpy as np


class handTracking():
    def __init__(self, model_complexity=1, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.model_complexity = model_complexity

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            model_complexity=self.model_complexity,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]

    def drawHands(self, frame, draw=True):
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(RGB)

        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, handLandmarks, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def importLandmarks(self, frame, handNo=0, draw=True):
        self.landmarkList = []
        if self.results.multi_hand_landmarks and len(self.results.multi_hand_landmarks) > handNo:
            hand = self.results.multi_hand_landmarks[handNo]
            height, width, _ = frame.shape
            for id, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * width), int(lm.y * height)
                self.landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return self.landmarkList

    def fingersUp(self):
        if not self.landmarkList or len(self.landmarkList) < 21:
            return [0, 0, 0, 0, 0]

        fingers = []

        # 엄지
        if self.landmarkList[self.tipIds[0]][1] < self.landmarkList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 검지~새끼
        for id in range(1, 5):
            if self.landmarkList[self.tipIds[id]][2] < self.landmarkList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers


def main():
    cap = cv2.VideoCapture(0)
    detector = handTracking()

    while True:
        ret, frame = cap.read()
        if not ret:
            print('더 이상 가져올 프레임이 없습니다.')
            break

        frame = cv2.flip(frame, 1)
        frame = detector.drawHands(frame)
        landmarkList = detector.importLandmarks(frame)

        if landmarkList:
            fingers = detector.fingersUp()
            print(f"손가락 상태: {fingers}")

        cv2.imshow('Canvas', frame)

        if cv2.waitKey(25) == ord('q'):
            print('사용자 입력에 의해 종료합니다.')
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

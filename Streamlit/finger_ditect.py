import cv2
import mediapipe as mp
import random
import math
import time

# -----------------------------
# Ball class
# -----------------------------
class Ball:
    def __init__(self, frame_width, frame_height):
        self.radius = random.randint(25, 40)
        self.x = random.randint(self.radius, frame_width - self.radius)
        self.y = random.randint(self.radius + 70, frame_height - self.radius)
        self.speed_x = random.choice([-4, -3, 3, 4])
        self.speed_y = random.choice([-4, -3, 3, 4])
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def move(self, frame_width, frame_height):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce from left/right
        if self.x - self.radius <= 0 or self.x + self.radius >= frame_width:
            self.speed_x *= -1
        # Bounce from top/bottom
        if self.y - self.radius <= 70 or self.y + self.radius >= frame_height:
            self.speed_y *= -1

    def draw(self, frame):
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, self.color, -1)
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, (255, 255, 255), 2)

    def is_touched(self, finger_x, finger_y):
        distance = math.hypot(finger_x - self.x, finger_y - self.y)
        return distance <= self.radius + 15

# -----------------------------
# Main program
# -----------------------------
def main():
    # Load MediaPipe HandLandmarker
    BaseOptions = mp.tasks.BaseOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    options = mp.tasks.vision.HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
        num_hands=2,
        running_mode=VisionRunningMode.IMAGE
    )
    detector = mp.tasks.vision.HandLandmarker.create_from_options(options)

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Unable to open the webcam.")

    success, frame = camera.read()
    if not success:
        camera.release()
        raise RuntimeError("Unable to read from the webcam.")

    frame_height, frame_width, _ = frame.shape
    balls = [Ball(frame_width, frame_height) for _ in range(5)]

    score = 0
    game_duration = 30
    start_time = time.time()
    touch_cooldown = 0.4
    last_touch_time = 0

    print("Hand touch game started.")
    print("Touch the moving balls with your index finger.")
    print("Press Q to close.")

    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        result = detector.detect(mp_image)

        fingertip_positions = []
        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:
                # Index fingertip = landmark 8
                index_tip = hand_landmarks[8]
                finger_x = int(index_tip.x * frame_width)
                finger_y = int(index_tip.y * frame_height)
                fingertip_positions.append((finger_x, finger_y))

                # Draw fingertip
                cv2.circle(frame, (finger_x, finger_y), 14, (0, 0, 255), -1)
                cv2.circle(frame, (finger_x, finger_y), 20, (255, 255, 255), 2)

        

        # Move and draw balls
        for ball in balls:
            ball.move(frame_width, frame_height)
            ball.draw(frame)

        current_time = time.time()

        # Check touches
        if current_time - last_touch_time > touch_cooldown:
            touched_ball_index = None
            for finger_x, finger_y in fingertip_positions:
                for index, ball in enumerate(balls):
                    if ball.is_touched(finger_x, finger_y):
                        touched_ball_index = index
                        break
                if touched_ball_index is not None:
                    break

            if touched_ball_index is not None:
                score += 1
                balls[touched_ball_index] = Ball(frame_width, frame_height)
                last_touch_time = current_time

        elapsed_time = current_time - start_time
        remaining_time = max(0, int(game_duration - elapsed_time))

        # Header area
        cv2.rectangle(frame, (0, 0), (frame_width, 65), (30, 30, 30), -1)
        cv2.putText(frame, f"Score: {score}", (20, 42),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Time: {remaining_time}", (frame_width - 180, 42),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, "Touch the balls using your index finger",
                    (180, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        cv2.imshow("Hand Landmark Ball Touch Game", frame)

        if remaining_time <= 0 or cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Final score screen
    final_screen = frame.copy()
    overlay = final_screen.copy()
    cv2.rectangle(overlay, (0, 0), (frame_width, frame_height), (0, 0, 0), -1)
    final_screen = cv2.addWeighted(overlay, 0.7, final_screen, 0.3, 0)

    cv2.putText(final_screen, "Game Over",
                (frame_width // 2 - 140, frame_height // 2 - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)
    cv2.putText(final_screen, f"Final Score: {score}",
                (frame_width // 2 - 150, frame_height // 2 + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 3)
    cv2.putText(final_screen, "Press any key to close",
                (frame_width // 2 - 160, frame_height // 2 + 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Hand Landmark Ball Touch Game", final_screen)
    cv2.waitKey(0)

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import mediapipe as mp
import requests
import time
import os

# ==========================
# TELEGRAM SETTINGS
# ==========================
# Users must set these environment variables
# before running the program.
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError(
        "Telegram credentials are missing.\n"
        "Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID.\n"
        "See README.md for setup instructions."
    )


# ==========================
# MESSAGE MAPPING
# ==========================
messages = {
    1: "🆘 HELP",
    2: "💧 WATER",
    3: "🍛 FOOD",
    4: "🚻 RESTROOM",
    5: "🚨 EMERGENCY"
}


# ==========================
# TELEGRAM FUNCTION
# ==========================
def send_telegram(msg):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    try:

        response = requests.post(
            url,
            data=data,
            timeout=5
        )

        response.raise_for_status()

        print("Sent:", msg)

    except requests.RequestException as e:

        print("Telegram error:", e)


# ==========================
# MEDIAPIPE
# ==========================
mpHands = mp.solutions.hands

hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]


# ==========================
# CAMERA
# ==========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():

    raise RuntimeError(
        "Could not open the camera."
    )


# ==========================
# TELEGRAM COOLDOWN
# ==========================
last_message = ""

last_time = 0

cooldown = 5


# ==========================
# MAIN LOOP
# ==========================
while True:

    success, img = cap.read()

    if not success:

        print(
            "Could not read frame from camera."
        )

        break


    # Mirror image
    img = cv2.flip(img, 1)


    # Convert BGR → RGB
    rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )


    # Process hand
    results = hands.process(rgb)


    fingers = []

    count = 0


    # ==========================
    # HAND DETECTED
    # ==========================
    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]


        # Draw hand landmarks
        draw.draw_landmarks(
            img,
            hand,
            mpHands.HAND_CONNECTIONS
        )


        lmList = []


        h, w, c = img.shape


        # Store landmark coordinates
        for id, lm in enumerate(hand.landmark):

            cx = int(lm.x * w)

            cy = int(lm.y * h)

            lmList.append(
                (cx, cy)
            )


        # ==========================
        # THUMB
        # ==========================
        if lmList[4][0] > lmList[3][0]:

            fingers.append(1)

        else:

            fingers.append(0)


        # ==========================
        # OTHER FOUR FINGERS
        # ==========================
        for id in range(1, 5):

            if (
                lmList[tipIds[id]][1]
                <
                lmList[tipIds[id] - 2][1]
            ):

                fingers.append(1)

            else:

                fingers.append(0)


        # Count raised fingers
        count = fingers.count(1)


    # ==========================
    # MESSAGE
    # ==========================
    message = ""


    if count in messages:

        message = messages[count]


    # ==========================
    # DISPLAY BOX
    # ==========================
    cv2.rectangle(
        img,
        (20, 20),
        (420, 120),
        (0, 255, 0),
        -1
    )


    # Display finger count
    cv2.putText(
        img,
        f"Fingers : {count}",
        (30, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 0),
        2
    )


    # Display message
    cv2.putText(
        img,
        message,
        (30, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255),
        2
    )


    # ==========================
    # SEND TELEGRAM
    # ==========================
    current = time.time()


    if message != "":

        if (
            message != last_message
            or
            current - last_time > cooldown
        ):

            send_telegram(message)

            last_message = message

            last_time = current


    # ==========================
    # SHOW CAMERA
    # ==========================
    cv2.imshow(
        "Patient Monitoring System",
        img
    )


    # ==========================
    # EXIT
    # ==========================
    key = cv2.waitKey(1)


    if key == ord("q"):

        break


# ==========================
# RELEASE RESOURCES
# ==========================
cap.release()

cv2.destroyAllWindows()

hands.close()
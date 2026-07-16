import cv2
import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.set_page_config(
    page_title="Face Detection",
    page_icon="🙂",
    layout="centered"
)

st.title("Real-Time Face Detection")
st.write("Click **START** to open your webcam and detect faces in real time.")

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


class FaceDetector(VideoProcessorBase):

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40,40)
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(
                img,
                (x,y),
                (x+w,y+h),
                (0,255,0),
                3
            )

        cv2.putText(
            img,
            f"Faces: {len(faces)}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="face-detection",
    video_processor_factory=FaceDetector,
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
)
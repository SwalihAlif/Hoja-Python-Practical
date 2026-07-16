import cv2
import numpy as np
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Face Detection",
    page_icon="🙂",
    layout="centered"
)

st.title("Face Detection Using OpenCV")
st.write(
    "Upload an image and the application will detect faces using "
    "a pretrained Haar Cascade classifier."
)


@st.cache_resource
def load_face_detector():
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)

    if detector.empty():
        raise RuntimeError("Unable to load the face detection model.")

    return detector


face_detector = load_face_detector()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    pil_image = Image.open(uploaded_file).convert("RGB")
    image_rgb = np.array(pil_image)

    st.subheader("Original Image")
    st.image(image_rgb, use_container_width=True)

    if st.button("Detect Faces"):
        # Convert RGB image to OpenCV BGR format.
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        gray_image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        faces = face_detector.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40)
        )

        for x, y, width, height in faces:
            cv2.rectangle(
                image_bgr,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                3
            )

        result_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        st.subheader("Detection Result")
        st.image(result_rgb, use_container_width=True)

        if len(faces) == 0:
            st.warning("No faces were detected.")
        elif len(faces) == 1:
            st.success("1 face was detected.")
        else:
            st.success(f"{len(faces)} faces were detected.")
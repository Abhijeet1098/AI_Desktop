import cv2
import face_recognition

def authenticate():

    known_image = face_recognition.load_image_file("data/user.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cam = cv2.VideoCapture(0)

    print("Looking for authorized user...")

    while True:
        ret, frame = cam.read()
        rgb = frame[:, :, ::-1]

        faces = face_recognition.face_encodings(rgb)

        for face in faces:
            match = face_recognition.compare_faces([known_encoding], face)

            if True in match:
                print("Access Granted")
                cam.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow("Zeno Authentication", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    return False
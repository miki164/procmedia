import numpy as np
import cv2
import utils


class Detector:
    def __init__(self, file_path: str, haar_path: str):
        self.file_path = file_path
        self.haar_path = haar_path

    def detect(self) -> np.array:
        if self._check_file_type():
            print("Video detected")
            return self._process_video()
        else:
            print("Image detected")
            return self._process_image()

    def _process_video(self) -> np.array:
        pass

    def _process_image(self) -> np.array:
        cascade = cv2.CascadeClassifier(self.haar_path)
        img = cv2.imread(self.file_path)
        img = cascade.detectMultiScale(img,
                                       scaleFactor=1.2,
                                       minNeighbors=5)

        return img

    # TODO: That's terrible function it's have to change!
    def _check_file_type(self) -> bool:
        return self.file_path[3:] == "mp4"

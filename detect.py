import numpy as np
import cv2
import utils


class Detector:
    def __init__(self, file_path: str, haar_path: str, out_path=""):
        self.file_path = file_path
        self.haar_path = haar_path

        self._type = "video" if self._check_file_type() else "image"
        print(self._type + " detected!")

        if out_path == "":
            if self._type == "video":
                self.out_path = "./detected/"
            else:
                self.out_path = "detected.jpg"
        else:
            self.out_path = out_path

    def detect(self) -> np.array:
        if self._type == "video":
            return self._process_video()
        elif self._type == "image":
            cv2.imwrite(self.out_path, self._process_image())

    def _process_video(self) -> np.array:
        pass

    def _process_image(self, scale_factor=1.2, min_neighbours=5) -> np.array:
        cascade = cv2.CascadeClassifier(self.haar_path)
        print(self.haar_path)
        img = cv2.imread(self.file_path)
        rect = cascade.detectMultiScale(img,
                                        scaleFactor=scale_factor,
                                        minNeighbors=min_neighbours)
        img = utils.draw_rectangles(rect, img)
        return img

    # TODO: That's terrible function it's have to change!
    def _check_file_type(self) -> bool:
        return self.file_path[3:] == "mp4"

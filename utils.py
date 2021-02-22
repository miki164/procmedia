import cv2
import numpy as np


def draw_rectangles(rect, img):
    for (x, y, w, h) in rect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 10)

    return img

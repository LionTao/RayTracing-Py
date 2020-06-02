from __future__ import annotations
import numpy as np  # type: ignore
from PIL import Image  # type: ignore
from typing import List
from utils.vec3 import Color, Vec3List


class Img:
    def __init__(self, w: int, h: int) -> None:
        self.w = w
        self.h = h
        self.frame: np.ndarray = np.zeros((h, w, 3), dtype=np.float64)

    def set_frame(self, array: np.ndarray) -> None:
        self.frame = array

    def write_pixel(self, w: int, h: int, pixel_color: Color,
                    samples_per_pixel: int) -> None:
        color: Color = pixel_color / samples_per_pixel
        self.frame[h][w] = color.clamp(0, 0.999).gamma(2).e

    def write_pixel_list(self, h: int, pixel_color_list: Vec3List,
                         samples_per_pixel: int) -> None:
        color = pixel_color_list.e / samples_per_pixel
        gamma: float = 2
        self.frame[h] = np.clip(color, 0, 0.999) ** (1 / gamma)

    def write_frame(self, frame: Vec3List) -> Img:
        self.frame += frame.e.reshape((self.h, self.w, 3))
        return self

    def average(self, samples_per_pixel: int) -> Img:
        self.frame /= samples_per_pixel
        return self

    def gamma(self, gamma: float) -> Img:
        self.frame = np.clip(self.frame, 0, 0.999) ** (1 / gamma)
        return self

    def up_side_down(self) -> Img:
        self.frame = self.frame[::-1]
        return self

    def save(self, path: str, show: bool = False) -> None:
        im = Image.fromarray((np.uint8(self.frame * 255)))
        im.save(path)
        if show:
            im.show()

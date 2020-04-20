import numpy as np  # type: ignore
from PIL import Image  # type: ignore
from utils.vec3 import Vec3


class Img:
    def __init__(self, w: int, h: int) -> None:
        self.img: np.ndarray = np.zeros((h, w, 3), dtype=np.double)

    def write_pixel(self, w: int, h: int, v: Vec3) -> None:
        self.img[h][w] = v.e

    def save(self, path: str, show: bool = False) -> None:
        im = Image.fromarray(np.uint8(self.img * 255))
        im.save(path)
        if show:
            im.show()
from __future__ import annotations
import numpy as np  # type: ignore
from typing import Union
from utils.rtweekend import random_float, clamp


class Vec3:
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0) -> None:
        self.e: np.ndarray = np.array([e0, e1, e2], dtype=np.double)

    def x(self) -> float:
        return self.e[0]

    def y(self) -> float:
        return self.e[1]

    def z(self) -> float:
        return self.e[2]

    def __getitem__(self, idx: int) -> float:
        return self.e[idx]

    def __str__(self) -> str:
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def length_squared(self) -> float:
        return self.e @ self.e

    def length(self) -> float:
        return np.sqrt(self.length_squared())

    def __add__(self, v: Vec3) -> Vec3:
        return Vec3(*(self.e + v.e))

    def __neg__(self) -> Vec3:
        return Vec3(*(-self.e))

    def __sub__(self, v: Vec3) -> Vec3:
        return self + (-v)

    def __mul__(self, v: Union[Vec3, int, float]) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(*(self.e * v.e))
        elif isinstance(v, (int, float)):
            return Vec3(*(self.e * v))
        raise NotImplementedError

    def __matmul__(self, v: Vec3) -> float:
        return self.e @ v.e

    def __truediv__(self, t: float) -> Vec3:
        return self * (1/t)

    def __iadd__(self, v: Vec3) -> Vec3:
        self.e += v.e
        return self

    def __imul__(self, v: Union[Vec3, int, float]) -> Vec3:
        if isinstance(v, Vec3):
            self.e *= v.e
        elif isinstance(v, (int, float)):
            self.e *= v
        else:
            return NotImplementedError
        return self

    def __itruediv__(self, t: float) -> Vec3:
        self *= (1/t)
        return self

    def cross(self, v: Vec3) -> Vec3:
        return Vec3(*np.cross(self.e, v.e))

    def unit_vector(self) -> Vec3:
        return (self / self.length())

    def clamp(self, _min: float, _max: float) -> Vec3:
        return Vec3(
            clamp(self.e[0], _min, _max),
            clamp(self.e[1], _min, _max),
            clamp(self.e[2], _min, _max)
        )

    def gamma(self, gamma: float) -> Vec3:
        return Vec3(*(self.e ** (1 / gamma)))

    @staticmethod
    def random(_min: float = None, _max: float = None) -> Vec3:
        return Vec3(
            random_float(_min, _max),
            random_float(_min, _max),
            random_float(_min, _max)
        )

    @staticmethod
    def random_in_unit_sphere() -> Vec3:
        while True:
            p: Vec3 = Vec3.random(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p


# Type aliases for Vec3
Point3 = Vec3  # 3D point
Color = Vec3  # RGB color

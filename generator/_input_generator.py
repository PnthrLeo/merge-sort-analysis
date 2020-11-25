import random
from numpy import finfo, float32


FLOAT32_MIN = float(finfo(float32).min)
FLOAT32_MAX = float(finfo(float32).max)


class InputGenerator:
    def __init__(self, input_size):
        self.input_size = input_size

    def __call__(self):
        arr = []
        for i in range(self.input_size):
            num = random.uniform(FLOAT32_MIN, FLOAT32_MAX)
            num = float32(num)
            arr.append(num)
        return arr

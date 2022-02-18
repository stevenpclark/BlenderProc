import numpy as np
import random
import cv2

from typing import Tuple

def generate_random_pattern_img(width: int, height: int, n_points: int) -> Tuple[int, int, int, int]:
    """
    Generate transparent image with random pattern.
    :param width, height: width and height of image to be generated.
    :param n_points: number of white points uniformly placed on image.
    """
    pattern_img = np.zeros((height, width, 4), dtype=np.uint8)

    m_width = int(width // np.sqrt(n_points))
    m_height = int(height // np.sqrt(n_points))

    for i in range(width // m_width):
        for j in range(height // m_height):
            x_idx = random.randint(i * m_width, (i + 1) * m_width - 1)
            y_idx = random.randint(j * m_height, (j + 1) * m_height - 1)
            pattern_img = cv2.circle(pattern_img, (x_idx, y_idx), 1, (255, 255, 255, 255), -1)

    return pattern_img

from manim import *


class CanonicalGrid(ThreeDAxes):

    def __init__(
        self,
        axis_range=(-2, 2, 1),
        axis_length=4,
        **kwargs
    ):

        super().__init__(
            x_range=axis_range,
            y_range=axis_range,
            z_range=axis_range,

            x_length=axis_length,
            y_length=axis_length,
            z_length=axis_length,

            axis_config={
                "color": GRAY,
                "stroke_width": 2
            },

            **kwargs
        )

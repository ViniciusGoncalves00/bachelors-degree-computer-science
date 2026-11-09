
from manim import *


class CanonicalCamera:

    @staticmethod
    def setup(
        scene,
        phi=60,
        theta=-45,
        zoom=1,
        background_color = "#1A1A1A"
    ):

        scene.set_camera_orientation(
            phi=phi * DEGREES,
            theta=theta * DEGREES,
            zoom=zoom
        )
        scene.camera.background_color = background_color
        

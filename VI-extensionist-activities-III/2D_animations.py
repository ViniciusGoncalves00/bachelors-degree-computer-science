
from manim import *
import numpy as np

config.background_color = "#1A1A1A"

class CoordinateConcept(Scene):

    def construct(self):

        # 0–3s: Apresentação do sistema de referência
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False}
        )

        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis, UP)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )

        # 3–6s: Um objeto aparece no sistema
        point = Dot(
            axes.c2p(2, 1),
            color=YELLOW,
            radius=0.09
        )

        self.play(FadeIn(point), run_time=1)

        self.play(
            Indicate(point, color=YELLOW),
            run_time=2
        )

        coordinate = MathTex(
            "(", "2", ",", "1", ")"
        ).to_corner(UR)

        coordinate[1].set_color(BLUE)
        coordinate[3].set_color(GREEN)

        coordinate.to_corner(UR)

        self.play(Write(coordinate), run_time=2)

        self.play(
            Indicate(coordinate, color=YELLOW),
            run_time=2
        )

        # 10–15s: Destacar cada dimensão
        x_value = MathTex("2", color=BLUE)
        y_value = MathTex("1", color=GREEN)

        x_value.move_to(coordinate[1].get_center())
        y_value.move_to(coordinate[3].get_center())

        x_projection = DashedLine(
            axes.c2p(2, 1),
            axes.c2p(2, 0),
            color=BLUE
        )

        y_projection = DashedLine(
            axes.c2p(2, 1),
            axes.c2p(0, 1),
            color=GREEN
        )

        self.play(
            Create(x_projection),
            Transform(coordinate[1], x_value),
            run_time=2
        )

        self.play(
            Create(y_projection),
            Transform(coordinate[3], y_value),
            run_time=2
        )

        # 15–20s: Reforçar a posição determinada pela coordenada
        self.play(
            Indicate(x_label, color=BLUE),
            Indicate(y_label, color=GREEN),
            run_time=2
        )

        self.wait(3)


class CoordinateDimensions(ThreeDScene):

    def construct(self):

        # 0–5s: Sistema unidimensional
        line = NumberLine(
            x_range=[-3, 3, 1],
            length=6,
            include_numbers=True
        )

        point_1d = Dot(
            line.n2p(2),
            color=YELLOW
        )

        coord_1d = MathTex("(2)")
        coord_1d.to_corner(UR)

        title = Text("One dimension", font_size=30)
        title.to_edge(UP)

        self.play(
            Write(title),
            Create(line),
            run_time=2
        )

        self.play(
            FadeIn(point_1d),
            Write(coord_1d),
            run_time=2
        )

        self.wait(1)

        # 5–10s: Sistema bidimensional
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4
        )

        point_2d = Dot(
            plane.c2p(2, 1),
            color=YELLOW
        )

        coord_2d = MathTex("(2, 1)")
        coord_2d.to_corner(UR)

        title_2d = Text("Two dimensions", font_size=30)
        title_2d.to_edge(UP)

        self.play(
            FadeOut(line),
            FadeOut(point_1d),
            FadeOut(coord_1d),
            Transform(title, title_2d),
            Create(plane),
            run_time=2
        )

        self.play(
            FadeIn(point_2d),
            Write(coord_2d),
            run_time=2
        )

        self.wait(1)

        # 10–20s: Sistema tridimensional
        axes_3d = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=5,
            y_length=5,
            z_length=4
        )

        point_3d = Dot3D(
            axes_3d.c2p(2, 1, 1),
            color=YELLOW,
            radius=0.09
        )

        coord_3d = MathTex("(2, 1, 1)")
        coord_3d.to_corner(UR)

        title_3d = Text("Three dimensions", font_size=30)
        title_3d.to_edge(UP)

        self.play(
            FadeOut(plane),
            FadeOut(point_2d),
            FadeOut(coord_2d),
            Transform(title, title_3d),
            Create(axes_3d),
            run_time=3
        )

        self.play(
            FadeIn(point_3d),
            Write(coord_3d),
            run_time=2
        )

        self.move_camera(
            phi=60 * DEGREES,
            theta=-45 * DEGREES,
            run_time=2
        )

        self.wait(3)
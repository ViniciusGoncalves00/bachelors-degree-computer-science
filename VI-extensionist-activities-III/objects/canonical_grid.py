from manim import *
import numpy as np

class CanonicalGrid(VGroup):

    def __init__(
        self,
        axis_range=(-15, 15, 1),
        axis_length=30,
        grid_color=GRAY,
        grid_opacity=0.35,
        **kwargs
    ):

        super().__init__(**kwargs)

        start, end, step = axis_range

        grid = VGroup()

        values = np.arange(
            start,
            end + step * 0.5,
            step
        )

        half = axis_length / 2

        # Grade horizontal no plano XY (Z = 0)
        for value in values:
        
            # Linhas paralelas ao eixo X
            grid.add(
                Line(
                    start=[start, value, 0],
                    end=[end, value, 0],
                    color=grid_color,
                    stroke_width=1,
                    stroke_opacity=grid_opacity
                )
            )

            # Linhas paralelas ao eixo Y
            grid.add(
                Line(
                    start=[value, start, 0],
                    end=[value, end, 0],
                    color=grid_color,
                    stroke_width=1,
                    stroke_opacity=grid_opacity
                )
            )

        # Eixos coordenados
        x_axis = Line(
            [start, 0, 0],
            [end, 0, 0],
            color=RED,
            stroke_width=2
        )

        y_axis = Line(
            [0, start, 0],
            [0, end, 0],
            color=GREEN,
            stroke_width=2
        )

        z_axis = Line(
            [0, 0, -axis_length / 2.0],
            [0, 0,  axis_length / 2.0],
            color=BLUE,
            stroke_width=2
        )

        # Identificação dos eixos
        x_label = MathTex("X", color=RED).scale(0.5)
        y_label = MathTex("Y", color=GREEN).scale(0.5)
        z_label = MathTex("Z", color=BLUE).scale(0.5)

        # Rótulos próximos à origem
        label_offset = 0.2

        x_label.move_to([label_offset, -label_offset, 0])
        y_label.move_to([label_offset, label_offset, 0])
        z_label.move_to([0, label_offset, label_offset])
        
        x_label.rotate(
            angle=90 * DEGREES,
            axis=OUT
        )
        z_label.rotate(
            angle=90 * DEGREES,
            axis=OUT
        )
        z_label.rotate(
            angle=90 * DEGREES,
            axis=UP
        )

        self.grid = grid
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis

        self.labels = VGroup(
            x_label,
            y_label,
            z_label
        )

        self.add(
            grid,
            x_axis,
            y_axis,
            z_axis,
            self.labels
        )
from manim import *

class CoordinateSequence(Scene):
    def construct(self):

        coordinates = [
            MathTex("x"),
            MathTex("(x, y)"),
            MathTex("(x, y, z)"),
            MathTex("(x, y, z, w)"),
            MathTex("(x, y, z, w, \\ldots)")
        ]

        for expression in coordinates:
            expression.scale(1.8)
            expression.set_color(BLUE)

        current = coordinates[0]
        self.play(Write(current))
        self.wait(1)

        for next_expression in coordinates[1:]:
            self.play(
                TransformMatchingTex(
                    current,
                    next_expression
                ),
                run_time=1.0
            )
            self.wait(0.5)

            current = next_expression

        self.wait(2)

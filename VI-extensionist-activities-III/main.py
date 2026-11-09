from manim import *
from itertools import product
from objects.canonical_cube import CanonicalCube
from objects.canonical_camera import CanonicalCamera
from objects.canonical_grid import CanonicalGrid

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

class CubeElements(ThreeDScene):

    def construct(self):

        CanonicalCamera.setup(self)

        cube = CanonicalCube(side_length=2)

        self.play(FadeIn(cube.faces))
        self.play(Create(cube.edge_group))
        self.wait(1)

        # Vértices
        points = cube.get_vertices()

        self.play(FadeIn(points))
        self.wait(1)
        self.play(FadeOut(points))

        # Arestas
        edges = cube.get_highlighted_edges()

        self.play(Create(edges))
        self.wait(1)
        self.play(FadeOut(edges))

        # Faces
        faces = cube.get_highlighted_faces()

        self.play(FadeIn(faces))
        self.wait(2)


class CubeCoordinates(ThreeDScene):

    def construct(self):

        CanonicalCamera.setup(self)

        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube)
        )

        self.wait(1)

        # P2: (1,1,1)
        p1_position = np.array([-1, -1, -1])
        
        p1 = Dot3D(
            point=p1_position,
            radius=0.10,
            color="#DC1A1A"
        )

        label1 = MathTex(
            r"P_1=(-1,-1,-1)",
            color="#e6e6e6"
        ).scale(0.8)

        label1.to_corner(UL)

        self.add_fixed_in_frame_mobjects(label1)

        self.play(
            FadeIn(p1),
            Write(label1)
        )

        self.wait(2)

        # P2: (1,1,1)
        p2_position = np.array([1, 1, 1])

        p2 = Dot3D(
            point=p2_position,
            radius=0.10,
            color="#DC1A1A"
        )

        label2 = MathTex(
            r"P_2=(\,1,\;1,\;1\,)",
            color="#e6e6e6"
        ).scale(0.8)

        label2.next_to(label1, DOWN, aligned_edge=LEFT, buff=0.2)

        self.add_fixed_in_frame_mobjects(label2)

        self.play(
            FadeIn(p2),
            Write(label2)
        )

        self.wait(2)
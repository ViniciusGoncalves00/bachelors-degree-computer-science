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

        grid = CanonicalGrid()
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
        
        
class CubeTransformations(ThreeDScene):

    def construct(self):

        CanonicalCamera.setup(self)

        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube)
        )

        self.wait(1)

        # 1. TRANSLAÇÃO
        self.play(
            cube.animate.shift(RIGHT * 2),
            run_time=2
        )

        self.wait(1)

        self.play(
            cube.animate.shift(LEFT * 2),
            run_time=2
        )

        self.wait(1)

        # 2. ROTAÇÃO
        self.play(
            cube.animate.rotate(PI / 2, axis=UP),
            run_time=2
        )

        self.wait(1)

        self.play(
            cube.animate.rotate(-PI / 2, axis=UP),
            run_time=2
        )

        self.wait(1)

        # 3. ESCALA
        self.play(
            cube.animate.scale(1.5),
            run_time=2
        )

        self.wait(1)

        self.play(
            cube.animate.scale(1 / 1.5),
            run_time=2
        )

        self.wait(2)
        
        



class CubeTranslationCooordinates(ThreeDScene):

    def construct(self):

        CanonicalCamera.setup(self)

        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube)
        )

        self.wait(1)

        # ==================================================
        # COORDENADAS LOCAIS
        # ==================================================

        title_local = Text(
            "Local Coordinates",
            color="#64B5F6"
        ).scale(0.35)

        local_c = MathTex(
            r"C=(0,\;0,\;0)",
            color="#e6e6e6"
        ).scale(0.65)

        local_p0 = MathTex(
            r"P_0=(-1,\;-1,\;-1)",
            color="#e6e6e6"
        ).scale(0.65)

        local_p1 = MathTex(
            r"P_1=(1,\;1,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

        # ==================================================
        # COORDENADAS GLOBAIS
        # ==================================================

        title_global = Text(
            "Global Coordinates",
            color="#81C784"
        ).scale(0.35)

        global_c = MathTex(
            r"C=(0,\;0,\;0)",
            color="#e6e6e6"
        ).scale(0.65)

        global_p0 = MathTex(
            r"P_0=(-1,\;-1,\;-1)",
            color="#e6e6e6"
        ).scale(0.65)

        global_p1 = MathTex(
            r"P_1=(1,\;1,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

        # ==================================================
        # ORGANIZAÇÃO DOS RÓTULOS
        # ==================================================

        local_group = VGroup(
            title_local,
            local_c,
            local_p0,
            local_p1
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15
        )

        global_group = VGroup(
            title_global,
            global_c,
            global_p0,
            global_p1
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15
        )

        labels = VGroup(
            local_group,
            global_group
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.35
        )

        labels.to_corner(UL, buff=0.4)

        self.add_fixed_in_frame_mobjects(labels)

        self.play(Write(labels))
        
        # ==================================================
        # DESTAQUE DOS VÉRTICES P0 E P1
        # ==================================================

        p0_position = cube.get_vertex_position(-1, -1, -1)
        p1_position = cube.get_vertex_position(1, 1, 1)

        # Pontos
        p0_dot = Dot3D(
            point=p0_position,
            radius=0.10,
            color="#DC1A1A"
        )

        p1_dot = Dot3D(
            point=p1_position,
            radius=0.10,
            color="#DC1A1A"
        )

        # Identificadores
        p0_tag = MathTex(
            r"P_0",
            color="#DC1A1A"
        ).scale(0.7)

        p1_tag = MathTex(
            r"P_1",
            color="#DC1A1A"
        ).scale(0.7)

        # Posicionamento dos identificadores no espaço 3D
        p0_tag.move_to(p0_position + np.array([-0.25, -0.25, -0.15]))
        p1_tag.move_to(p1_position + np.array([0.25, 0.25, 0.15]))

        # Adiciona os elementos
        self.play(
            FadeIn(p0_dot),
            FadeIn(p1_dot),
            Write(p0_tag),
            Write(p1_tag)
        )

        self.wait(1)

        # ==================================================
        # MOVIMENTO DO CUBO
        # ==================================================

        self.play(
            cube.animate.shift(np.array([2, 2, 2])),
            p0_dot.animate.shift(np.array([2, 2, 2])),
            p1_dot.animate.shift(np.array([2, 2, 2])),
            p0_tag.animate.shift(np.array([2, 2, 2])),
            p1_tag.animate.shift(np.array([2, 2, 2])),
            run_time=3,
            rate_func=smooth
        )

        # ==================================================
        # ATUALIZAÇÃO DAS COORDENADAS GLOBAIS
        # ==================================================

        new_global_c = MathTex(
            r"C=(2,\;2,\;2)",
            color="#e6e6e6"
        ).scale(0.65)

        new_global_p0 = MathTex(
            r"P_0=(1,\;1,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

        new_global_p1 = MathTex(
            r"P_1=(3,\;3,\;3)",
            color="#e6e6e6"
        ).scale(0.65)

        # Preserva a posição inicial de cada label
        new_global_c.align_to(global_c, LEFT)
        new_global_c.move_to(global_c, aligned_edge=LEFT)

        new_global_p0.align_to(global_p0, LEFT)
        new_global_p0.move_to(global_p0, aligned_edge=LEFT)

        new_global_p1.align_to(global_p1, LEFT)
        new_global_p1.move_to(global_p1, aligned_edge=LEFT)

        self.add_fixed_in_frame_mobjects(
            new_global_c,
            new_global_p0,
            new_global_p1
        )

        self.play(
            ReplacementTransform(global_c, new_global_c),
            ReplacementTransform(global_p0, new_global_p0),
            ReplacementTransform(global_p1, new_global_p1)
        )

        # Atualiza as referências
        global_c = new_global_c
        global_p0 = new_global_p0
        global_p1 = new_global_p1

        self.add_fixed_in_frame_mobjects(
            new_global_c,
            new_global_p0,
            new_global_p1
        )

        self.play(
            Transform(global_c, new_global_c),
            Transform(global_p0, new_global_p0),
            Transform(global_p1, new_global_p1)
        )

        self.wait(2)



class CubeProjection(ThreeDScene):

    def construct(self):

        CanonicalCamera.setup(self)

        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube)
        )

        self.wait(1)

        # Plano de projeção XY
        plane = Square(
            side_length=4,
            fill_color=BLUE,
            fill_opacity=0.12,
            stroke_color=BLUE,
            stroke_width=2
        )

        plane.move_to(np.array([0, 0, -1.5]))

        self.play(
            FadeIn(plane)
        )

        self.wait(1)

        # Calcula projeção
        projection = cube.get_orthographic_projection(
            plane_point=np.array([0., 0., -1.5]),
            plane_normal=np.array([0., 0., 1.])
        )

        # Linhas de projeção
        self.play(
            Create(projection.projection_lines),
            run_time=2
        )

        self.wait(1)

        # Resultado da projeção
        self.play(
            Create(projection.edges),
            FadeIn(projection.dots),
            run_time=2
        )

        self.wait(2)

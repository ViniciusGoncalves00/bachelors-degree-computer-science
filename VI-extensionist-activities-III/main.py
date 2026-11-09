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




class CubePerspectiveProjection(ThreeDScene):

    def construct(self):
        CanonicalCamera.setup(self)

        # Cena
        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube),
        )

        # Parâmetros da câmera
        camera_radius = 6.0
        camera_height = 2.5
        plane_distance = 2.5
        plane_size = 4.0

        angle = ValueTracker(0)

        # Posição do centro de projeção
        def get_camera_position():
            theta = angle.get_value()

            return np.array([
                camera_radius * np.cos(theta),
                camera_radius * np.sin(theta),
                camera_height,
            ])

        # Direção de visão da câmera
        def get_camera_direction():
            direction = -get_camera_position()
            return direction / np.linalg.norm(direction)

        # Centro do plano de projeção
        def get_plane_position():
            return (
                get_camera_position()
                + get_camera_direction() * plane_distance
            )

        # Orientação do plano de projeção
        def get_plane_axes():
            direction = get_camera_direction()

            world_up = np.array([0.0, 0.0, 1.0])

            right = np.cross(direction, world_up)
            right /= np.linalg.norm(right)

            up = np.cross(right, direction)
            up /= np.linalg.norm(up)

            return right, up

        # Plano de projeção sempre voltado para a câmera
        plane = always_redraw(
            lambda: self.create_plane(
                get_plane_position(),
                get_plane_axes(),
                plane_size,
            )
        )

        # Centro de projeção
        camera_dot = always_redraw(
            lambda: Dot3D(
                point=get_camera_position(),
                radius=0.09,
                color=YELLOW,
            )
        )

        camera_label = always_redraw(
            lambda: MathTex("C", color=YELLOW)
            .scale(0.7)
            .move_to(
                get_camera_position()
                + np.array([0.2, 0.2, 0.2])
            )
        )

        # Origem do sistema de coordenadas
        origin_dot = Dot3D(
            point=ORIGIN,
            radius=0.07,
            color=GREEN,
        )

        origin_label = MathTex("O", color=GREEN)
        origin_label.scale(0.7)
        origin_label.move_to(np.array([-0.2, -0.2, -0.2]))

        # Projeção atualizada continuamente
        projection = always_redraw(
            lambda: cube.get_perspective_projection(
                camera_position=get_camera_position(),
                plane_point=get_plane_position(),
                plane_normal=get_camera_direction(),
                edge_color=YELLOW,
                edge_width=3,
                vertex_color=RED,
                show_projection_lines=True,
            )
        )

        self.play(
            FadeIn(plane),
            FadeIn(camera_dot),
            FadeIn(camera_label),
            FadeIn(origin_dot),
            FadeIn(origin_label),
        )

        self.play(
            FadeIn(projection),
            run_time=2,
        )

        self.wait(1)

        # Movimento da câmera ao redor do cubo
        self.play(
            angle.animate.set_value(2 * PI),
            run_time=12,
            rate_func=linear,
        )

        self.wait(2)

    def create_plane(self, center, axes, size):
        right, up = axes
        half = size / 2

        corners = [
            center - right * half - up * half,
            center + right * half - up * half,
            center + right * half + up * half,
            center - right * half + up * half,
        ]

        return Polygon(
            *corners,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.12,
            stroke_width=2,
        )



class CubePerspectiveToScreen(ThreeDScene):

    def construct(self):

        # --------------------------------------------------
        # 1. CONFIGURAÇÃO DA CÂMERA DA CENA
        # --------------------------------------------------

        phi = 65 * DEGREES
        theta = -45 * DEGREES

        self.set_camera_orientation(
            phi=phi,
            theta=theta,
            gamma=0,
        )

        # Direção da câmera da cena, conforme os ângulos
        # utilizados na configuração acima.
        view_direction = np.array([
            -np.sin(phi) * np.cos(theta),
            -np.sin(phi) * np.sin(theta),
            -np.cos(phi),
        ])

        view_direction /= np.linalg.norm(view_direction)

        # Eixos horizontais e verticais da tela.
        world_up = np.array([0.0, 0.0, 1.0])

        screen_right = np.cross(view_direction, world_up)
        screen_right /= np.linalg.norm(screen_right)

        screen_up = np.cross(screen_right, view_direction)
        screen_up /= np.linalg.norm(screen_up)

        # --------------------------------------------------
        # 2. CUBO E REFERÊNCIAS ESPACIAIS
        # --------------------------------------------------

        grid = CanonicalGrid()
        cube = CanonicalCube(side_length=2)

        self.play(
            Create(grid),
            FadeIn(cube),
        )

        origin = Dot3D(
            point=ORIGIN,
            radius=0.07,
            color=GREEN,
        )

        self.add(origin)

        # --------------------------------------------------
        # 3. CÂMERA VIRTUAL
        # --------------------------------------------------

        camera_distance = 8.0
        plane_distance = 3.5

        # A câmera virtual está alinhada à câmera da cena.
        camera_position = -view_direction * camera_distance

        # O plano fica entre a câmera virtual e o cubo.
        plane_center = (
            camera_position
            + view_direction * plane_distance
        )

        camera_dot = Dot3D(
            point=camera_position,
            radius=0.10,
            color=YELLOW,
        )

        camera_label = MathTex(
            "C",
            color=YELLOW,
        ).scale(0.8)

        camera_label.move_to(
            camera_position + screen_right * 0.2 + screen_up * 0.2
        )

        # --------------------------------------------------
        # 4. PLANO DE PROJEÇÃO
        # --------------------------------------------------

        plane_width = 4.0
        plane_height = plane_width * config.frame_height / config.frame_width

        half_w = plane_width / 2
        half_h = plane_height / 2

        plane_corners = [
            plane_center - screen_right * half_w - screen_up * half_h,
            plane_center + screen_right * half_w - screen_up * half_h,
            plane_center + screen_right * half_w + screen_up * half_h,
            plane_center - screen_right * half_w + screen_up * half_h,
        ]

        plane = Polygon(
            *plane_corners,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.15,
            stroke_width=2,
        )

        # --------------------------------------------------
        # 5. PROJEÇÃO DO CUBO
        # --------------------------------------------------

        projection = cube.get_perspective_projection(
            camera_position=camera_position,
            plane_point=plane_center,
            plane_normal=view_direction,
            edge_color=YELLOW,
            edge_width=3,
            vertex_color=RED,
            vertex_radius=0.06,
            show_projection_lines=False,
        )

        # Raios que ligam a câmera aos vértices originais.
        world_vertices = cube.get_world_vertices()

        projection_rays = VGroup()

        for vertex in world_vertices:
            projection_rays.add(
                DashedLine(
                    camera_position,
                    vertex,
                    color=GRAY,
                    stroke_width=1.5,
                    dash_length=0.08,
                )
            )

        # O plano e a projeção formam um único objeto.
        image_plane = VGroup(
            plane,
            projection.edges,
            projection.dots,
        )

        # --------------------------------------------------
        # 6. APRESENTAÇÃO DA PROJEÇÃO
        # --------------------------------------------------

        self.play(
            FadeIn(camera_dot),
            FadeIn(camera_label),
            FadeIn(image_plane),
        )

        self.play(
            Create(projection_rays),
            run_time=3,
        )

        self.wait(2)

        # --------------------------------------------------
        # 7. TRANSIÇÃO PARA A IMAGEM NA TELA
        # --------------------------------------------------

        # Removemos os elementos que não fazem parte da imagem.
        self.play(
            FadeOut(cube),
            FadeOut(grid),
            FadeOut(origin),
            FadeOut(camera_dot),
            FadeOut(camera_label),
            FadeOut(projection_rays),
            run_time=2,
        )

        # O plano é centralizado e ampliado até ocupar a tela.
        final_scale = (
            config.frame_width / plane_width
        ) * 0.95

        self.play(
            image_plane.animate
                .move_to(ORIGIN)
                .scale(final_scale),
            run_time=4,
            rate_func=smooth,
        )

        self.wait(3)




class RasterizationVsRayTracing(ThreeDScene):

    def construct(self):

        # ==================================================
        # CONFIGURAÇÃO DA CENA
        # ==================================================

        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-90 * DEGREES,
            gamma=0,
        )

        cube_size = 1.6
        camera_distance = 4.5
        plane_distance = 2.3
        plane_size = 2.6

        left_center = LEFT * 2.8
        right_center = RIGHT * 2.8

        # ==================================================
        # TÍTULOS
        # ==================================================

        raster_title = Text(
            "RASTERIZAÇÃO",
            color=BLUE,
            weight=BOLD,
        ).scale(0.55).to_corner(UL).shift(DOWN * 0.2)

        ray_title = Text(
            "RAY TRACING",
            color=RED,
            weight=BOLD,
        ).scale(0.55).to_corner(UR).shift(DOWN * 0.2)

        self.add_fixed_in_frame_mobjects(
            raster_title,
            ray_title,
        )

        # ==================================================
        # CUBOS
        # ==================================================

        cube_raster = CanonicalCube(
            side_length=cube_size,
            fill_color=BLUE,
            fill_opacity=0.12,
        ).shift(left_center)

        cube_ray = CanonicalCube(
            side_length=cube_size,
            fill_color=BLUE,
            fill_opacity=0.12,
        ).shift(right_center)

        # ==================================================
        # CÂMERAS VIRTUAIS
        # ==================================================

        raster_camera_position = (
            left_center + DOWN * camera_distance
        )

        ray_camera_position = (
            right_center + DOWN * camera_distance
        )

        raster_camera = Dot3D(
            raster_camera_position,
            color=YELLOW,
            radius=0.10,
        )

        ray_camera = Dot3D(
            ray_camera_position,
            color=YELLOW,
            radius=0.10,
        )

        raster_camera_label = MathTex(
            "C_1",
            color=YELLOW,
        ).scale(0.65).next_to(raster_camera, LEFT)

        ray_camera_label = MathTex(
            "C_2",
            color=YELLOW,
        ).scale(0.65).next_to(ray_camera, RIGHT)

        # ==================================================
        # PLANOS DE IMAGEM
        # ==================================================

        plane_normal = DOWN

        raster_plane_center = (
            left_center + DOWN * plane_distance
        )

        ray_plane_center = (
            right_center + DOWN * plane_distance
        )

        def make_image_plane(center):

            return Square(
                side_length=plane_size,
                fill_color=WHITE,
                fill_opacity=0.08,
                stroke_color=WHITE,
                stroke_width=2,
            ).rotate(
                PI / 2,
                axis=RIGHT,
            ).move_to(center)

        raster_plane = make_image_plane(raster_plane_center)
        ray_plane = make_image_plane(ray_plane_center)

        # ==================================================
        # RASTERIZAÇÃO
        # ==================================================

        raster_projection = cube_raster.get_perspective_projection(
            camera_position=raster_camera_position,
            plane_point=raster_plane_center,
            plane_normal=plane_normal,
            edge_color=YELLOW,
            edge_width=3,
            vertex_color=RED,
            vertex_radius=0.045,
            show_projection_lines=True,
            projection_line_color=GRAY,
        )

        # ==================================================
        # RAY TRACING
        # ==================================================

        ray_group = VGroup()
        ray_plane_points = VGroup()

        half = cube_size / 2

        # Pontos de amostragem na face frontal do cubo.
        sample_coordinates = [-0.5, 0.0, 0.5]

        for x in sample_coordinates:
            for z in sample_coordinates:

                target = right_center + np.array([
                    x,
                    -half,
                    z,
                ])

                direction = target - ray_camera_position

                denominator = np.dot(
                    direction,
                    plane_normal,
                )

                t = np.dot(
                    ray_plane_center - ray_camera_position,
                    plane_normal,
                ) / denominator

                plane_hit = (
                    ray_camera_position + t * direction
                )

                # Raio que atravessa o plano e atinge o cubo.
                ray_group.add(
                    Arrow3D(
                        start=ray_camera_position,
                        end=target,
                        color=RED,
                        thickness=0.018,
                        height=0.12,
                        base_radius=0.025,
                    )
                )

                # Ponto correspondente ao pixel no plano.
                ray_plane_points.add(
                    Dot3D(
                        point=plane_hit,
                        radius=0.045,
                        color=YELLOW,
                    )
                )

        # ==================================================
        # APRESENTAÇÃO
        # ==================================================

        self.play(
            FadeIn(cube_raster),
            FadeIn(cube_ray),
            FadeIn(raster_camera),
            FadeIn(ray_camera),
            FadeIn(raster_camera_label),
            FadeIn(ray_camera_label),
        )

        self.play(
            FadeIn(raster_plane),
            FadeIn(ray_plane),
        )

        self.wait(1)

        # Rasterização: projeção da geometria.
        self.play(
            Create(raster_projection.projection_lines),
            run_time=2,
        )

        self.play(
            Create(raster_projection.edges),
            FadeIn(raster_projection.dots),
            run_time=2,
        )

        self.wait(1)

        # Ray tracing: emissão dos raios.
        self.play(
            LaggedStart(
                *[
                    Create(ray)
                    for ray in ray_group
                ],
                lag_ratio=0.12,
            ),
            run_time=3,
        )

        self.play(
            FadeIn(ray_plane_points),
            run_time=1,
        )

        self.wait(3)

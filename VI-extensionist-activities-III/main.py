
from manim import *
from itertools import product

from objects.canonical_cube import CanonicalCube
from objects.canonical_camera import CanonicalCamera
from objects.canonical_grid import CanonicalGrid

class CubeSceneBase(ThreeDScene):
    """
    Base para cenas independentes que reutilizam visualmente
    o mesmo grid e o mesmo cubo.
    """

    def setup_environment(self, animate_cube=False, animate_grid=False):
        CanonicalCamera.setup(self)

        self.grid = CanonicalGrid()
        self.cube = CanonicalCube(
            side_length=2,
            fill_opacity=0.0
        )

        if animate_cube:
            self.play(
                FadeIn(self.cube)
            )
        elif animate_grid:
            self.add(self.cube)
            self.play(
                FadeIn(self.grid)
            )
        else:
            self.add(self.grid, self.cube)

    def create_plane(self, center, axes, size):
        right, up = axes
        half = size / 2

        corners = [
            center - right * half - up * half,
            center + right * half - up * half,
            center + right * half + up * half,
            center - right * half + up * half
        ]

        return Polygon(
            *corners,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.12,
            stroke_width=2
        )

class CubeElements(CubeSceneBase):

    def construct(self):

        self.setup_environment(animate_cube=True)

        # Vértices
        points = self.cube.get_vertices()

        self.play(FadeIn(points))
        self.wait(1)
        self.play(FadeOut(points))

        # Arestas
        edges = self.cube.get_highlighted_edges()

        self.play(Create(edges))
        self.wait(1)
        self.play(FadeOut(edges))

        # Faces
        faces = self.cube.get_highlighted_faces()

        self.play(FadeIn(faces))
        self.wait(2)
        
class CubeCoordinates(CubeSceneBase):

    def construct(self):

        self.setup_environment(animate_grid=True)

        # Ponto P0
        p0_position = self.cube.get_vertex_position(-1, -1, -1)

        p0 = Dot3D(
            point=p0_position,
            radius=0.10,
            color=PURE_MAGENTA
        )

        p0_label = MathTex(
            r"P_0=(-1,-1,-1)",
            color="#E6E6E6"
        ).scale(0.5).to_corner(UL)

        # Ponto P1
        p1_position = self.cube.get_vertex_position(1, 1, 1)

        p1 = Dot3D(
            point=p1_position,
            radius=0.10,
            color=PURE_MAGENTA
        )

        p1_label = MathTex(
            r"P_1=(1,1,1)",
            color="#E6E6E6"
        ).scale(0.5).next_to(p0_label, DOWN, aligned_edge=LEFT)

        # Etiquetas fixas na tela
        self.add_fixed_in_frame_mobjects(
            p0_label,
            p1_label
        )

        self.play(
            FadeIn(p0),
            FadeIn(p1),
            Write(p0_label),
            Write(p1_label)
        )

        self.wait(2)
        
        
class CubeTransformations(CubeSceneBase):

    def construct(self):

        self.setup_environment()

        # --------------------------------------------------
        # 1. TRANSLAÇÃO
        # --------------------------------------------------

        self.play(
            self.cube.animate.shift(RIGHT * 2),
            run_time=2
        )

        self.wait(1)

        # Retorna à posição inicial
        self.play(
            self.cube.animate.shift(LEFT * 2),
            run_time=2
        )

        self.wait(1)

        # --------------------------------------------------
        # 2. ROTAÇÃO
        # --------------------------------------------------

        self.play(
            Rotate(
                self.cube,
                angle=2 * PI,
                axis=OUT,
                about_point=ORIGIN
            ),
            run_time=4,
            rate_func=smooth
        )

        self.wait(1)

        # --------------------------------------------------
        # 3. ESCALA
        # --------------------------------------------------

        self.play(
            self.cube.animate.scale(1.8),
            run_time=2
        )

        self.wait(1)

        # Retorna ao tamanho original
        self.play(
            self.cube.animate.scale(1 / 1.8),
            run_time=2
        )

        self.wait(2)
        
class LocalAndGlobalCoordinates(CubeSceneBase):
    def construct(self):
        self.setup_environment()

        # --------------------------------------------------
        # COORDENADAS LOCAIS
        # --------------------------------------------------

        title_local = Text(
            "Local Coordinates",
            color="#64B5F6"
        ).scale(0.35)

        local_c = MathTex(
            r"Center=(0,\;0,\;0)",
            color="#e6e6e6"
        ).scale(0.65)

        local_p0 = MathTex(
            r"Point_0=(-1,\;-1,\;-1)",
            color="#e6e6e6"
        ).scale(0.65)

        local_p1 = MathTex(
            r"Point_1=(1,\;1,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

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

        # --------------------------------------------------
        # COORDENADAS GLOBAIS
        # --------------------------------------------------

        title_global = Text(
            "Global Coordinates",
            color="#81C784"
        ).scale(0.35)

        global_c = MathTex(
            r"Center=(0,\;0,\;0)",
            color="#e6e6e6"
        ).scale(0.65)

        global_p0 = MathTex(
            r"Point_0=(-1,\;-1,\;-1)",
            color="#e6e6e6"
        ).scale(0.65)

        global_p1 = MathTex(
            r"Point_1=(1,\;1,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

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

        # --------------------------------------------------
        # DESTAQUE DOS VÉRTICES
        # --------------------------------------------------

        p0_position = self.cube.get_vertex_position(-1, -1, -1)
        p1_position = self.cube.get_vertex_position(1, 1, 1)

        p0_dot = Dot3D(
            point=p0_position,
            radius=0.10,
            color=PURE_MAGENTA
        )

        p1_dot = Dot3D(
            point=p1_position,
            radius=0.10,
            color=PURE_MAGENTA
        )

        p0_tag = MathTex(
            r"P_0",
            color=PURE_MAGENTA
        ).scale(0.7)

        p1_tag = MathTex(
            r"P_1",
            color=PURE_MAGENTA
        ).scale(0.7)

        p0_tag.move_to(
            p0_position + np.array([-0.25, -0.25, -0.15])
        )

        p1_tag.move_to(
            p1_position + np.array([0.25, 0.25, 0.15])
        )

        self.play(
            FadeIn(p0_dot),
            FadeIn(p1_dot),
            Write(p0_tag),
            Write(p1_tag)
        )

        self.wait(1)

        # --------------------------------------------------
        # TRANSLAÇÃO DO CUBO
        # --------------------------------------------------

        translation = np.array([0, 4, 0])

        self.play(
            self.cube.animate.shift(translation),
            p0_dot.animate.shift(translation),
            p1_dot.animate.shift(translation),
            p0_tag.animate.shift(translation),
            p1_tag.animate.shift(translation),
            run_time=3,
            rate_func=smooth
        )

        # --------------------------------------------------
        # ATUALIZAÇÃO DAS COORDENADAS GLOBAIS
        # --------------------------------------------------

        new_global_c = MathTex(
            r"Center=(0,\;4,\;0)",
            color="#e6e6e6"
        ).scale(0.65)

        new_global_p0 = MathTex(
            r"Point_0=(-1,\;3,\;-1)",
            color="#e6e6e6"
        ).scale(0.65)

        new_global_p1 = MathTex(
            r"Point_1=(1,\;5,\;1)",
            color="#e6e6e6"
        ).scale(0.65)

        new_global_c.move_to(global_c, aligned_edge=LEFT)
        new_global_p0.move_to(global_p0, aligned_edge=LEFT)
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

        self.wait(2)

        # --------------------------------------------------
        # RETORNO À ORIGEM
        # --------------------------------------------------

        self.play(
            self.cube.animate.shift(-translation),
            p0_dot.animate.shift(-translation),
            p1_dot.animate.shift(-translation),
            p0_tag.animate.shift(-translation),
            p1_tag.animate.shift(-translation),
            run_time=2
        )

        self.play(
            FadeOut(p0_dot),
            FadeOut(p1_dot),
            FadeOut(p0_tag),
            FadeOut(p1_tag),
            FadeOut(labels),
            FadeOut(new_global_c),
            FadeOut(new_global_p0),
            FadeOut(new_global_p1)
        )


class OrthographicProjection(CubeSceneBase):
    def construct(self):
        self.setup_environment()

        camera_radius = 6.0
        camera_height = 2.5
        plane_distance = 2.5
        plane_size = 4.0

        angle = ValueTracker(0)

        # --------------------------------------------------
        # CÂMERA VIRTUAL
        # --------------------------------------------------

        def get_camera_position():
            theta = angle.get_value()

            return np.array([
                camera_radius * np.cos(theta),
                camera_radius * np.sin(theta),
                camera_height
            ])

        def get_camera_direction():
            direction = -get_camera_position()
            return direction / np.linalg.norm(direction)

        def get_plane_position():
            return (
                get_camera_position()
                + get_camera_direction() * plane_distance
            )

        def get_plane_axes():
            direction = get_camera_direction()
            world_up = np.array([0., 0., 1.])

            right = np.cross(direction, world_up)
            right /= np.linalg.norm(right)

            up = np.cross(right, direction)
            up /= np.linalg.norm(up)

            return right, up

        # --------------------------------------------------
        # PLANO DE PROJEÇÃO
        # --------------------------------------------------

        plane = always_redraw(
            lambda: self.create_plane(
                get_plane_position(),
                get_plane_axes(),
                plane_size
            )
        )

        # --------------------------------------------------
        # MARCADOR DA CÂMERA
        # --------------------------------------------------

        camera_dot = always_redraw(
            lambda: Dot3D(
                point=get_camera_position(),
                radius=0.09,
                color=YELLOW
            )
        )

        camera_label = always_redraw(
            lambda: MathTex(
                "C",
                color=YELLOW
            ).scale(0.7).move_to(
                get_camera_position() + np.array([0.2, 0.2, 0.2])
            )
        )

        # --------------------------------------------------
        # ORIGEM
        # --------------------------------------------------

        origin_dot = Dot3D(
            point=ORIGIN,
            radius=0.07,
            color=GREEN
        )

        origin_label = MathTex(
            "O",
            color=GREEN
        ).scale(0.7)

        origin_label.move_to(
            np.array([-0.2, -0.2, -0.2])
        )

        # --------------------------------------------------
        # PROJEÇÃO ORTOGRÁFICA ATUALIZADA
        # --------------------------------------------------

        projection = always_redraw(
            lambda: self.cube.get_orthographic_projection(
                plane_point=get_plane_position(),
                plane_normal=get_camera_direction()
            )
        )

        # --------------------------------------------------
        # APRESENTAÇÃO
        # --------------------------------------------------

        self.play(
            FadeIn(plane),
            FadeIn(camera_dot),
            FadeIn(camera_label),
            FadeIn(origin_dot),
            FadeIn(origin_label)
        )

        self.play(
            FadeIn(projection),
            run_time=2
        )

        self.wait(1)

        self.play(
            angle.animate.set_value(2 * PI),
            run_time=12,
            rate_func=linear
        )

        self.wait(2)

        self.play(
            FadeOut(plane),
            FadeOut(camera_dot),
            FadeOut(camera_label),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(projection)
        )


class PerspectiveProjection(CubeSceneBase):
    def construct(self):
        self.setup_environment()

        camera_radius = 6.0
        camera_height = 2.5
        plane_distance = 2.5
        plane_size = 4.0

        angle = ValueTracker(0)

        # --------------------------------------------------
        # CÂMERA VIRTUAL
        # --------------------------------------------------

        def get_camera_position():
            theta = angle.get_value()

            return np.array([
                camera_radius * np.cos(theta),
                camera_radius * np.sin(theta),
                camera_height
            ])

        def get_camera_direction():
            direction = -get_camera_position()
            return direction / np.linalg.norm(direction)

        def get_plane_position():
            return (
                get_camera_position()
                + get_camera_direction() * plane_distance
            )

        def get_plane_axes():
            direction = get_camera_direction()
            world_up = np.array([0., 0., 1.])

            right = np.cross(direction, world_up)
            right /= np.linalg.norm(right)

            up = np.cross(right, direction)
            up /= np.linalg.norm(up)

            return right, up

        # --------------------------------------------------
        # PLANO DE PROJEÇÃO
        # --------------------------------------------------

        plane = always_redraw(
            lambda: self.create_plane(
                get_plane_position(),
                get_plane_axes(),
                plane_size
            )
        )

        # --------------------------------------------------
        # MARCADOR DA CÂMERA
        # --------------------------------------------------

        camera_dot = always_redraw(
            lambda: Dot3D(
                point=get_camera_position(),
                radius=0.09,
                color=YELLOW
            )
        )

        camera_label = always_redraw(
            lambda: MathTex(
                "C",
                color=YELLOW
            ).scale(0.7).move_to(
                get_camera_position() + np.array([0.2, 0.2, 0.2])
            )
        )

        # --------------------------------------------------
        # ORIGEM
        # --------------------------------------------------

        origin_dot = Dot3D(
            point=ORIGIN,
            radius=0.07,
            color=GREEN
        )

        origin_label = MathTex(
            "O",
            color=GREEN
        ).scale(0.7)

        origin_label.move_to(
            np.array([-0.2, -0.2, -0.2])
        )

        # --------------------------------------------------
        # PROJEÇÃO ATUALIZADA
        # --------------------------------------------------

        projection = always_redraw(
            lambda: self.cube.get_perspective_projection(
                camera_position=get_camera_position(),
                plane_point=get_plane_position(),
                plane_normal=get_camera_direction(),
                edge_color="#E6E6E6",
                edge_width=3,
                vertex_color="#E6E6E6",
                show_projection_lines=True
            )
        )

        # --------------------------------------------------
        # APRESENTAÇÃO
        # --------------------------------------------------

        self.play(
            FadeIn(plane),
            FadeIn(camera_dot),
            FadeIn(camera_label),
            FadeIn(origin_dot),
            FadeIn(origin_label)
        )

        self.play(
            FadeIn(projection),
            run_time=2
        )

        self.wait(1)

        self.play(
            angle.animate.set_value(2 * PI),
            run_time=12,
            rate_func=linear
        )

        self.wait(2)

        self.play(
            FadeOut(plane),
            FadeOut(camera_dot),
            FadeOut(camera_label),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(projection)
        )


class PerspectiveToScreen(CubeSceneBase):
    def construct(self):
        self.setup_environment()

        # --------------------------------------------------
        # ORIENTAÇÃO DA CÂMERA DO MANIM
        # --------------------------------------------------

        camera_distance = 8.0
        plane_distance = 3.5

        phi = self.camera.get_phi()
        theta = self.camera.get_theta()
        gamma = self.camera.get_gamma()

        view_direction = np.array([
            -np.sin(phi) * np.cos(theta),
            -np.sin(phi) * np.sin(theta),
            -np.cos(phi)
        ])

        view_direction /= np.linalg.norm(view_direction)

        world_up = np.array([0., 0., 1.])

        screen_right = np.cross(view_direction, world_up)
        screen_right /= np.linalg.norm(screen_right)

        screen_up = np.cross(screen_right, view_direction)
        screen_up /= np.linalg.norm(screen_up)

        # Considera a rotação da câmera em torno do eixo de visão
        screen_right_rotated = (
            screen_right * np.cos(gamma)
            + screen_up * np.sin(gamma)
        )

        screen_up_rotated = (
            -screen_right * np.sin(gamma)
            + screen_up * np.cos(gamma)
        )

        screen_right = screen_right_rotated
        screen_up = screen_up_rotated

        camera_position = -view_direction * camera_distance

        origin = Dot3D(
            point=ORIGIN,
            radius=0.07,
            color=GREEN
        )

        self.add(origin)

        # --------------------------------------------------
        # CÂMERA VIRTUAL
        # --------------------------------------------------

        plane_center = (
            camera_position
            + view_direction * plane_distance
        )

        camera_dot = Dot3D(
            point=camera_position,
            radius=0.10,
            color=YELLOW
        )

        camera_label = MathTex(
            "C",
            color=YELLOW
        ).scale(0.8)

        camera_label.move_to(
            camera_position
            + screen_right * 0.2
            + screen_up * 0.2
        )

        # --------------------------------------------------
        # PLANO DE PROJEÇÃO
        # --------------------------------------------------

        plane_width = 4.0
        plane_height = (
            plane_width
            * config.frame_height
            / config.frame_width
        )

        half_w = plane_width / 2
        half_h = plane_height / 2

        plane_corners = [
            plane_center - screen_right * half_w - screen_up * half_h,
            plane_center + screen_right * half_w - screen_up * half_h,
            plane_center + screen_right * half_w + screen_up * half_h,
            plane_center - screen_right * half_w + screen_up * half_h
        ]

        plane = Polygon(
            *plane_corners,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.15,
            stroke_width=2
        )

        # --------------------------------------------------
        # PROJEÇÃO DO CUBO
        # --------------------------------------------------

        projection = self.cube.get_perspective_projection(
            camera_position=camera_position,
            plane_point=plane_center,
            plane_normal=view_direction,
            edge_color="#E6E6E6",
            edge_width=3,
            vertex_color="#E6E6E6",
            vertex_radius=0.06,
            show_projection_lines=False
        )

        # Raios entre a câmera e os vértices
        projection_rays = VGroup()

        for x, y, z in product([-1, 1], repeat=3):
            vertex = self.cube.get_vertex_position(x, y, z)

            projection_rays.add(
                DashedLine(
                    camera_position,
                    vertex,
                    color=GRAY,
                    stroke_width=1.5,
                    dash_length=0.08
                )
            )

        image_plane = VGroup(
            plane,
            projection.edges,
            projection.dots
        )

        # --------------------------------------------------
        # APRESENTAÇÃO
        # --------------------------------------------------

        self.play(
            FadeIn(camera_dot),
            FadeIn(camera_label),
            FadeIn(image_plane)
        )

        self.play(
            Create(projection_rays),
            run_time=3
        )

        self.wait(2)

        # --------------------------------------------------
        # TRANSIÇÃO PARA A IMAGEM NA TELA
        # --------------------------------------------------

        self.play(
            FadeOut(self.cube),
            FadeOut(self.grid),
            FadeOut(origin),
            FadeOut(camera_dot),
            FadeOut(camera_label),
            FadeOut(projection_rays),
            run_time=2
        )

        final_scale = (
            config.frame_width / plane_width
        ) * 0.95

        self.play(
            image_plane.animate
                .move_to(ORIGIN)
                .scale(final_scale),
            run_time=4,
            rate_func=smooth
        )

        self.wait(3)
        self.play(FadeOut(image_plane))


class RasterizationVsRayTracing(CubeSceneBase):
    def construct(self):
        self.setup_environment()

        # --------------------------------------------------
        # POSICIONAMENTO
        # --------------------------------------------------

        cube_size = 1.6
        camera_distance = 4.5
        plane_distance = 2.3
        plane_size = 2.6

        left_center = LEFT * 2.8
        right_center = RIGHT * 2.8

        self.play(FadeOut(self.cube))

        cube_raster = CanonicalCube(
            side_length=cube_size,
            fill_color="#E6E6E6",
            fill_opacity=0.0
        ).shift(left_center)

        cube_ray = CanonicalCube(
            side_length=cube_size,
            fill_color="#E6E6E6",
            fill_opacity=0.0
        ).shift(right_center)

        # --------------------------------------------------
        # TÍTULOS
        # --------------------------------------------------

        raster_title = Text(
            "Rasterization",
            color="#E6E6E6",
            weight=BOLD
        ).scale(0.55).to_corner(UL).shift(DOWN * 0.2)

        ray_title = Text(
            "Ray Tracing",
            color="#E6E6E6",
            weight=BOLD
        ).scale(0.55).to_corner(UR).shift(DOWN * 0.2)

        self.add_fixed_in_frame_mobjects(
            raster_title,
            ray_title
        )

        # --------------------------------------------------
        # CÂMERAS VIRTUAIS
        # --------------------------------------------------

        raster_camera_position = (
            left_center + DOWN * camera_distance
        )

        ray_camera_position = (
            right_center + DOWN * camera_distance
        )

        raster_camera = Dot3D(
            raster_camera_position,
            color=YELLOW,
            radius=0.10
        )

        ray_camera = Dot3D(
            ray_camera_position,
            color=YELLOW,
            radius=0.10
        )

        raster_camera_label = MathTex(
            "C_1",
            color=YELLOW
        ).scale(0.65).next_to(raster_camera, LEFT)

        ray_camera_label = MathTex(
            "C_2",
            color=YELLOW
        ).scale(0.65).next_to(ray_camera, RIGHT)

        # --------------------------------------------------
        # PLANOS DE IMAGEM
        # --------------------------------------------------

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
                fill_color="#E6E6E6",
                fill_opacity=0.08,
                stroke_color="#E6E6E6",
                stroke_width=2
            ).rotate(
                PI / 2,
                axis=RIGHT
            ).move_to(center)

        raster_plane = make_image_plane(raster_plane_center)
        ray_plane = make_image_plane(ray_plane_center)

        # --------------------------------------------------
        # RASTERIZAÇÃO
        # --------------------------------------------------

        raster_projection = cube_raster.get_perspective_projection(
            camera_position=raster_camera_position,
            plane_point=raster_plane_center,
            plane_normal=plane_normal,
            edge_color="#E6E6E6",
            edge_width=3,
            vertex_color="#E6E6E6",
            vertex_radius=0.045,
            show_projection_lines=True,
            projection_line_color="#E6E6E6"
        )

        # --------------------------------------------------
        # RAY TRACING
        # --------------------------------------------------

        ray_group = VGroup()
        ray_plane_points = VGroup()

        half = cube_size / 2
        sample_coordinates = [-0.5, 0.0, 0.5]

        for x in sample_coordinates:
            for z in sample_coordinates:
                target = right_center + np.array([
                    x,
                    -half,
                    z
                ])

                direction = target - ray_camera_position

                denominator = np.dot(
                    direction,
                    plane_normal
                )

                t = np.dot(
                    ray_plane_center - ray_camera_position,
                    plane_normal
                ) / denominator

                plane_hit = (
                    ray_camera_position + t * direction
                )

                ray_group.add(
                    Arrow3D(
                        start=ray_camera_position,
                        end=target,
                        color="#E6E6E6",
                        thickness=0.010,
                        height=0.10,
                        base_radius=0.01
                    )
                )

                ray_plane_points.add(
                    Dot3D(
                        point=plane_hit,
                        radius=0.045,
                        color="#E6E6E6"
                    )
                )

        # --------------------------------------------------
        # APRESENTAÇÃO
        # --------------------------------------------------

        self.play(
            FadeIn(cube_raster),
            FadeIn(cube_ray),
            FadeIn(raster_camera),
            FadeIn(ray_camera),
            FadeIn(raster_camera_label),
            FadeIn(ray_camera_label)
        )

        self.play(
            FadeIn(raster_plane),
            FadeIn(ray_plane)
        )

        self.wait(1)

        # Rasterização: projeção da geometria
        self.play(
            Create(raster_projection.projection_lines),
            run_time=2
        )

        self.play(
            Create(raster_projection.edges),
            FadeIn(raster_projection.dots),
            run_time=2
        )

        self.wait(1)

        # Ray Tracing: emissão dos raios
        self.play(
            LaggedStart(
                *[
                    Create(ray)
                    for ray in ray_group
                ],
                lag_ratio=0.12
            ),
            run_time=3
        )

        self.play(
            FadeIn(ray_plane_points),
            run_time=1
        )

        self.wait(3)


from manim import *
from itertools import product
import numpy as np


class CanonicalCube(VGroup):

    def __init__(
        self,
        side_length=2,
        fill_color="#E6E6E6",
        fill_opacity=0.0,
        edge_color="#E6E6E6",
        edge_width=3,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.side_length = side_length
        self.half = side_length / 2

        # ==================================================
        # GEOMETRIA
        # ==================================================

        s = self.half

        # Vértices: coordenadas locais
        self.vertices = {
            (x, y, z): np.array([x*s, y*s, z*s], dtype=float)
            for x, y, z in product([-1, 1], repeat=3)
        }

        # Lista ordenada de vértices
        self.vertex_keys = list(self.vertices.keys())

        self.vertex_indices = {
            key: i for i, key in enumerate(self.vertex_keys)
        }

        self.vertex_positions = np.array([
            self.vertices[key] for key in self.vertex_keys
        ])

        # Arestas: pares de índices
        self.edge_indices = []

        for vertex in self.vertex_keys:
            for axis in range(3):

                neighbor = list(vertex)
                neighbor[axis] *= -1
                neighbor = tuple(neighbor)

                if vertex[axis] == -1:
                    self.edge_indices.append((
                        self.vertex_indices[vertex],
                        self.vertex_indices[neighbor]
                    ))

        # Faces: índices dos vértices
        face_vertices = [
            [(-1,-1,-1), (-1,-1,1),
             (-1,1,1), (-1,1,-1)],

            [(1,-1,-1), (1,1,-1),
             (1,1,1), (1,-1,1)],

            [(-1,-1,-1), (1,-1,-1),
             (1,-1,1), (-1,-1,1)],

            [(-1,1,-1), (-1,1,1),
             (1,1,1), (1,1,-1)],

            [(-1,-1,1), (1,-1,1),
             (1,1,1), (-1,1,1)],

            [(-1,-1,-1), (-1,1,-1),
             (1,1,-1), (1,-1,-1)]
        ]

        self.face_vertices = face_vertices

        self.face_indices = [
            [self.vertex_indices[v] for v in face]
            for face in face_vertices
        ]

        # ==================================================
        # PROPRIEDADES GEOMÉTRICAS
        # ==================================================

        # Centro local
        self.center = np.zeros(3)

        # Dimensões
        self.dimensions = np.array([
            side_length,
            side_length,
            side_length
        ])

        # Bounding Box local (AABB)
        self.bounds_min = np.min(self.vertex_positions, axis=0)
        self.bounds_max = np.max(self.vertex_positions, axis=0)

        self.bounding_box = {
            "min": self.bounds_min.copy(),
            "max": self.bounds_max.copy(),
            "size": self.bounds_max - self.bounds_min,
            "center": (self.bounds_min + self.bounds_max) / 2
        }

        # Raios
        self.inscribed_radius = self.half
        self.circumscribed_radius = np.linalg.norm(
            self.vertex_positions[0]
        )

        # ==================================================
        # REPRESENTAÇÃO VISUAL
        # ==================================================

        self.edges = [
            Line(
                self.vertex_positions[a],
                self.vertex_positions[b],
                color=edge_color,
                stroke_width=edge_width
            )
            for a, b in self.edge_indices
        ]

        self.faces = VGroup(*[
            Polygon(
                *[self.vertices[v] for v in face],
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_width=0
            )
            for face in face_vertices
        ])

        self.edge_group = VGroup(*self.edges)

        self.add(self.faces, self.edge_group)

    # ======================================================
    # VÉRTICES
    # ======================================================

    def get_vertices(self, color=PURE_MAGENTA, radius=0.05):

        return VGroup(*[
            Dot3D(point=p, radius=radius, color=color)
            for p in self.vertex_positions
        ])

    def get_vertex_position(self, x, y, z):

        return self.vertices[(x, y, z)].copy()

    def get_vertex_by_index(self, index):

        return self.vertex_positions[index].copy()

    # ======================================================
    # ARESTAS
    # ======================================================

    def get_highlighted_edges(self, color=PURE_MAGENTA, width=5):

        return VGroup(*[
            Line(
                self.vertex_positions[a],
                self.vertex_positions[b],
                color=color,
                stroke_width=width
            )
            for a, b in self.edge_indices
        ])

    def get_edge_vertices(self, index):

        a, b = self.edge_indices[index]

        return (
            self.get_vertex_by_index(a),
            self.get_vertex_by_index(b)
        )

    # ======================================================
    # FACES
    # ======================================================

    def get_highlighted_faces(self, color=PURE_MAGENTA, opacity=0.2):

        return VGroup(*[
            Polygon(
                *[self.vertices[v] for v in face],
                fill_color=color,
                fill_opacity=opacity,
                stroke_color=color,
                stroke_width=2
            )
            for face in self.face_vertices
        ])

    def get_face_vertices(self, index):

        return [
            self.get_vertex_by_index(i)
            for i in self.face_indices[index]
        ]

    # ======================================================
    # BOUNDING BOX
    # ======================================================

    def get_bounding_box(self):

        return {
            "min": self.bounds_min.copy(),
            "max": self.bounds_max.copy(),
            "size": self.bounds_max - self.bounds_min,
            "center": (self.bounds_min + self.bounds_max) / 2
        }

    def get_bounding_box_corners(self):

        return np.array([
            [
                x * self.half,
                y * self.half,
                z * self.half
            ]
            for x, y, z in product([-1, 1], repeat=3)
        ])

    def get_bounding_box_visual(self, color=YELLOW, width=2):

        return Cube(
            side_length=self.side_length,
            fill_opacity=0,
            stroke_color=color,
            stroke_width=width
        )

    # ======================================================
    # PROPRIEDADES
    # ======================================================

    def get_center(self):
        return super().get_center()

    def get_dimensions(self):
        return self.dimensions.copy()

    def get_volume(self):
        return self.side_length ** 3

    def get_surface_area(self):
        return 6 * self.side_length ** 2

    def get_diagonal(self):
        return self.circumscribed_radius * 2

    # ======================================================
    # TRANSFORMAÇÕES / COORDENADAS
    # ======================================================
    
    def get_world_vertices(self):
    
        return np.array([
            self.get_center() + p
            for p in self.vertex_positions
        ])

    def get_world_bounding_box(self):

        vertices = self.get_world_vertices()

        return {
            "min": np.min(vertices, axis=0),
            "max": np.max(vertices, axis=0),
            "size": np.max(vertices, axis=0) -
                    np.min(vertices, axis=0),
            "center": (
                np.min(vertices, axis=0) +
                np.max(vertices, axis=0)
            ) / 2
        }


    def get_orthographic_projection(
        self,
        plane_point=np.array([0., 0., -1.5]),
        plane_normal=np.array([0., 0., 1.]),
        edge_color="#E6E6E6",
        edge_width=3,
        vertex_color="#E6E6E6",
        vertex_radius=0.05,
        show_projection_lines=True,
        projection_line_color="#E6E6E6"
    ):

        # Normalização do vetor normal
        normal = np.array(plane_normal, dtype=float)
        normal = normal / np.linalg.norm(normal)

        plane_point = np.array(plane_point, dtype=float)

        # Vértices em coordenadas globais
        world_vertices = self.get_world_vertices()

        # Projeção ortográfica dos vértices
        projected_vertices = []

        for vertex in world_vertices:

            distance = np.dot(
                vertex - plane_point,
                normal
            )

            projected = vertex - distance * normal

            projected_vertices.append(projected)

        projected_vertices = np.array(projected_vertices)

        # Arestas projetadas
        projected_edges = VGroup(*[
            Line(
                projected_vertices[a],
                projected_vertices[b],
                color=edge_color,
                stroke_width=edge_width
            )
            for a, b in self.edge_indices
        ])

        # Vértices projetados
        projected_dots = VGroup(*[
            Dot3D(
                point=p,
                radius=vertex_radius,
                color=vertex_color
            )
            for p in projected_vertices
        ])

        # Linhas entre vértices originais e projetados
        projection_lines = VGroup()

        if show_projection_lines:

            projection_lines = VGroup(*[
                DashedLine(
                    start=world_vertices[i],
                    end=projected_vertices[i],
                    color=projection_line_color,
                    stroke_width=1.5
                )
                for i in range(len(world_vertices))
            ])

        # Agrupamento
        projection = VGroup(
            projected_edges,
            projected_dots,
            projection_lines
        )

        # Dados geométricos para consultas posteriores
        projection.vertices = projected_vertices
        projection.edges = projected_edges
        projection.dots = projected_dots
        projection.projection_lines = projection_lines

        return projection



    def get_perspective_projection(
        self,
        camera_position=np.array([5.0, 5.0, 5.0]),
        plane_point=np.array([0.0, 0.0, 0.0]),
        plane_normal=np.array([0.0, 0.0, 1.0]),
        edge_color=YELLOW,
        edge_width=3,
        vertex_color="#E6E6E6",
        vertex_radius=0.05,
        show_projection_lines=True,
        projection_line_color=GRAY,
    ):
        camera_position = np.array(camera_position, dtype=float)
        plane_point = np.array(plane_point, dtype=float)
        plane_normal = np.array(plane_normal, dtype=float)

        plane_normal /= np.linalg.norm(plane_normal)

        world_vertices = self.get_world_vertices()
        projected_vertices = []

        for vertex in world_vertices:
            direction = vertex - camera_position

            denominator = np.dot(direction, plane_normal)

            if abs(denominator) < 1e-8:
                raise ValueError("Raio paralelo ao plano de projeção.")

            t = np.dot(plane_point - camera_position, plane_normal) / denominator

            if t <= 0:
                raise ValueError(
                    "O plano de projeção precisa estar entre a câmera e os vértices."
                )

            projected = camera_position + t * direction
            projected_vertices.append(projected)

        projected_vertices = np.array(projected_vertices)

        edges = VGroup()
        for a, b in self.edge_indices:
            edges.add(
                Line(
                    projected_vertices[a],
                    projected_vertices[b],
                    color=edge_color,
                    stroke_width=edge_width,
                )
            )

        dots = VGroup()
        for vertex in projected_vertices:
            dots.add(
                Dot3D(
                    point=vertex,
                    radius=vertex_radius,
                    color=vertex_color,
                )
            )

        projection_lines = VGroup()
        if show_projection_lines:
            for original, projected in zip(world_vertices, projected_vertices):
                projection_lines.add(
                    DashedLine(
                        camera_position,
                        projected,
                        color=projection_line_color,
                        stroke_width=1.5,
                        dash_length=0.08,
                    )
                )

        projection = VGroup(projection_lines, edges, dots)
        projection.vertices = projected_vertices
        projection.edges = edges
        projection.dots = dots
        projection.projection_lines = projection_lines

        return projection

    
    def get_screen_projection(self, projection, width=3.0, height=3.0):
        """
        Converte os vértices do plano de projeção em coordenadas
        2D para exibição fixa na tela.
        """
    
        vertices = projection.vertices
    
        # Eixos do plano de projeção
        center = vertices.mean(axis=0)
    
        # Base local do plano
        right = vertices[1] - vertices[0]
        right /= np.linalg.norm(right)
    
        up = vertices[3] - vertices[0]
        up /= np.linalg.norm(up)
    
        # Coordenadas locais dos vértices
        local = np.array([
            [
                np.dot(vertex - center, right),
                np.dot(vertex - center, up),
            ]
            for vertex in vertices
        ])
    
        # Normalização para o tamanho desejado na tela
        max_x = max(np.max(np.abs(local[:, 0])), 1e-8)
        max_y = max(np.max(np.abs(local[:, 1])), 1e-8)
    
        screen_vertices = np.array([
            [
                (x / max_x) * width / 2,
                (y / max_y) * height / 2,
                0,
            ]
            for x, y in local
        ])
    
        screen_vertices[:, 0] += 4.0
    
        screen_edges = VGroup()
    
        for a, b in self.edge_indices:
            screen_edges.add(
                Line(
                    screen_vertices[a],
                    screen_vertices[b],
                    color=YELLOW,
                    stroke_width=3,
                )
            )
    
        return screen_edges
    
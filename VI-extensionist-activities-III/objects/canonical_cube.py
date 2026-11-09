
from manim import *
from itertools import product
import numpy as np


class CanonicalCube(VGroup):

    def __init__(
        self,
        side_length=2,
        fill_color=WHITE,
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

    def get_vertices(self, color="#DC1A1A", radius=0.05):

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

    def get_highlighted_edges(self, color="#DC1A1A", width=5):

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

    def get_highlighted_faces(self, color="#DC1A1A", opacity=0.2):

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
        return self.center.copy()

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
            self.get_matrix() @ np.append(p, 1)
            for p in self.vertex_positions
        ])[:, :3]

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


from manim import *
from itertools import product


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

        s = self.half

        # Vértices
        self.vertices = {
            (x, y, z): np.array([x*s, y*s, z*s])
            for x, y, z in product([-1, 1], repeat=3)
        }

        # Arestas
        self.edges = []

        for vertex in self.vertices:
            for axis in range(3):

                neighbor = list(vertex)
                neighbor[axis] *= -1
                neighbor = tuple(neighbor)

                if vertex[axis] == -1:
                    self.edges.append(
                        Line(
                            self.vertices[vertex],
                            self.vertices[neighbor],
                            color=edge_color,
                            stroke_width=edge_width
                        )
                    )

        # Faces
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

        # Elementos do cubo
        self.add(self.faces, self.edge_group)

    def get_vertices(self, color="#DC1A1A", radius=0.05):

        return VGroup(*[
            Dot3D(
                point=position,
                radius=radius,
                color=color
            )
            for position in self.vertices.values()
        ])

    def get_highlighted_edges(
        self,
        color="#DC1A1A",
        width=5
    ):

        return VGroup(*[
            Line(
                edge.get_start(),
                edge.get_end(),
                color=color,
                stroke_width=width
            )
            for edge in self.edges
        ])

    def get_highlighted_faces(
        self,
        color="#DC1A1A",
        opacity=0.2
    ):

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

    def get_vertex_position(self, x, y, z):
        return self.vertices[(x, y, z)]

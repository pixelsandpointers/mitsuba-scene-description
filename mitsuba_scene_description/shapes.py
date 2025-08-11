from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List, Union
from .utils import Plugin, RGB, Ref, Transform

# Category: Shapes


@dataclass
class WavefrontObjMeshLoader(Plugin):
    """Wavefront OBJ mesh loader (obj)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#obj
        Params:
            - filename (string):  Filename of the OBJ file that should be loaded
            - face_normals (boolean):  When set to true , any existing or computed vertex normals are
    discarded and face normals will instead be used during rendering.
    This gives the rendered object a faceted appearance. (Default: false )
            - flip_tex_coords (boolean):  Treat the vertical component of the texture as inverted? Most OBJ files use this convention. (Default: true )
            - flip_normals (boolean):  Is the mesh inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform):  Specifies an optional linear object-to-world transformation.
    (Default: none, i.e. object space = world space)
            - vertex_count (integer): [P] Total number of vertices
            - face_count (integer): [P] Total number of faces
            - faces (uint32[]): [P] Face indices buffer (flatten)
            - vertex_positions (float[]): [P | ∂ | D] Vertex positions buffer (flatten) pre-multiplied by the object-to-world transformation.
            - vertex_normals (float[]): [P | ∂ | D] Vertex normals buffer (flatten)  pre-multiplied by the object-to-world transformation.
            - vertex_texcoords (float[]): [P | ∂] Vertex texcoords buffer (flatten)
            - (Mesh attribute) (float[]): [P | ∂] Mesh attribute buffer (flatten)
            - (Mesh attribute) (float[]): [[P | ∂]] Mesh attribute buffer (flatten)
    """

    filename: Optional[str] = None
    face_normals: Optional[bool] = None
    flip_tex_coords: Optional[bool] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    vertex_count: Optional[int] = None
    face_count: Optional[int] = None
    faces: Optional[Plugin] = None
    vertex_positions: Optional[float] = None
    vertex_normals: Optional[float] = None
    vertex_texcoords: Optional[float] = None
    mesh_attribute: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        face_normals: Optional[bool] = None,
        flip_tex_coords: Optional[bool] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        vertex_count: Optional[int] = None,
        face_count: Optional[int] = None,
        faces: Optional[Plugin] = None,
        vertex_positions: Optional[float] = None,
        vertex_normals: Optional[float] = None,
        vertex_texcoords: Optional[float] = None,
        mesh_attribute: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="obj", id=id)
        self.id = id
        self.filename = filename
        self.face_normals = face_normals
        self.flip_tex_coords = flip_tex_coords
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.vertex_count = vertex_count
        self.face_count = face_count
        self.faces = faces
        self.vertex_positions = vertex_positions
        self.vertex_normals = vertex_normals
        self.vertex_texcoords = vertex_texcoords
        self.mesh_attribute = mesh_attribute
        self.bsdf = bsdf


@dataclass
class WavefrontObjMeshLoader(Plugin):
    """Wavefront OBJ mesh loader (obj)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#obj
        Params:
            - filename (string):  Filename of the OBJ file that should be loaded
            - face_normals (boolean):  When set to true , any existing or computed vertex normals are
    discarded and face normals will instead be used during rendering.
    This gives the rendered object a faceted appearance. (Default: false )
            - flip_tex_coords (boolean):  Treat the vertical component of the texture as inverted? Most OBJ files use this convention. (Default: true )
            - flip_normals (boolean):  Is the mesh inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform):  Specifies an optional linear object-to-world transformation.
    (Default: none, i.e. object space = world space)
            - vertex_count (integer): [P] Total number of vertices
            - face_count (integer): [P] Total number of faces
            - faces (uint32[]): [P] Face indices buffer (flatten)
            - vertex_positions (float[]): [P | ∂ | D] Vertex positions buffer (flatten) pre-multiplied by the object-to-world transformation.
            - vertex_normals (float[]): [P | ∂ | D] Vertex normals buffer (flatten)  pre-multiplied by the object-to-world transformation.
            - vertex_texcoords (float[]): [P | ∂] Vertex texcoords buffer (flatten)
            - (Mesh attribute) (float[]): [P | ∂] Mesh attribute buffer (flatten)
            - (Mesh attribute) (float[]): [[P | ∂]] Mesh attribute buffer (flatten)
    """

    filename: Optional[str] = None
    face_normals: Optional[bool] = None
    flip_tex_coords: Optional[bool] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    vertex_count: Optional[int] = None
    face_count: Optional[int] = None
    faces: Optional[Plugin] = None
    vertex_positions: Optional[float] = None
    vertex_normals: Optional[float] = None
    vertex_texcoords: Optional[float] = None
    mesh_attribute: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        face_normals: Optional[bool] = None,
        flip_tex_coords: Optional[bool] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        vertex_count: Optional[int] = None,
        face_count: Optional[int] = None,
        faces: Optional[Plugin] = None,
        vertex_positions: Optional[float] = None,
        vertex_normals: Optional[float] = None,
        vertex_texcoords: Optional[float] = None,
        mesh_attribute: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="obj", id=id)
        self.id = id
        self.filename = filename
        self.face_normals = face_normals
        self.flip_tex_coords = flip_tex_coords
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.vertex_count = vertex_count
        self.face_count = face_count
        self.faces = faces
        self.vertex_positions = vertex_positions
        self.vertex_normals = vertex_normals
        self.vertex_texcoords = vertex_texcoords
        self.mesh_attribute = mesh_attribute
        self.bsdf = bsdf


@dataclass
class Ply(Plugin):
    """PLY (Stanford Triangle Format)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#Stanford Triangle Format
        Params:
            - filename (string):  Filename of the PLY file that should be loaded
            - face_normals (boolean):  When set to true , any existing or computed vertex normals are
    discarded and face normals will instead be used during rendering.
    This gives the rendered object a faceted appearance. (Default: false )
            - flip_tex_coords (boolean):  Treat the vertical component of the texture as inverted? (Default: false )
            - flip_normals (boolean):  Is the mesh inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform):  Specifies an optional linear object-to-world transformation.
    (Default: none, i.e. object space = world space)
            - vertex_count (integer): [P] Total number of vertices
            - face_count (integer): [P] Total number of faces
            - faces (uint32[]): [P] Face indices buffer (flatten)
            - vertex_positions (float[]): [P | ∂ | D] Vertex positions buffer (flatten) pre-multiplied by the object-to-world transformation.
            - vertex_normals (float[]): [P | ∂ | D] Vertex normals buffer (flatten)  pre-multiplied by the object-to-world transformation.
            - vertex_texcoords (float[]): [P | ∂] Vertex texcoords buffer (flatten)
            - (Mesh attribute) (float[]): [P | ∂] Mesh attribute buffer (flatten)
            - (Mesh attribute) (float[]): [[P | ∂]] Mesh attribute buffer (flatten)
    """

    filename: Optional[str] = None
    face_normals: Optional[bool] = None
    flip_tex_coords: Optional[bool] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    vertex_count: Optional[int] = None
    face_count: Optional[int] = None
    faces: Optional[Plugin] = None
    vertex_positions: Optional[float] = None
    vertex_normals: Optional[float] = None
    vertex_texcoords: Optional[float] = None
    mesh_attribute: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        face_normals: Optional[bool] = None,
        flip_tex_coords: Optional[bool] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        vertex_count: Optional[int] = None,
        face_count: Optional[int] = None,
        faces: Optional[Plugin] = None,
        vertex_positions: Optional[float] = None,
        vertex_normals: Optional[float] = None,
        vertex_texcoords: Optional[float] = None,
        mesh_attribute: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="Stanford Triangle Format", id=id)
        self.id = id
        self.filename = filename
        self.face_normals = face_normals
        self.flip_tex_coords = flip_tex_coords
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.vertex_count = vertex_count
        self.face_count = face_count
        self.faces = faces
        self.vertex_positions = vertex_positions
        self.vertex_normals = vertex_normals
        self.vertex_texcoords = vertex_texcoords
        self.mesh_attribute = mesh_attribute
        self.bsdf = bsdf


@dataclass
class SerializedMeshLoader(Plugin):
    """Serialized mesh loader (serialized)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#serialized
        Params:
            - filename (string):  Filename of the serialized file that should be loaded
            - shape_index (integer):  A .serialized file may contain several separate meshes. This parameter
    specifies which one should be loaded. (Default: 0, i.e. the first one)
            - face_normals (boolean):  When set to true , any existing or computed vertex normals are
    discarded and emph{face normals} will instead be used during rendering.
    This gives the rendered object a faceted appearance. (Default: false )
            - flip_normals (boolean):  Is the mesh inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform):  Specifies an optional linear object-to-world transformation.
    (Default: none, i.e. object space = world space)
            - vertex_count (integer): [P] Total number of vertices
            - face_count (integer): [P] Total number of faces
            - faces (uint32[]): [P] Face indices buffer (flatten)
            - vertex_positions (float[]): [P | ∂ | D] Vertex positions buffer (flatten) pre-multiplied by the object-to-world transformation.
            - vertex_normals (float[]): [P | ∂ | D] Vertex normals buffer (flatten)  pre-multiplied by the object-to-world transformation.
            - vertex_texcoords (float[]): [P | ∂] Vertex texcoords buffer (flatten)
            - (Mesh attribute) (float[]): [P | ∂] Mesh attribute buffer (flatten)
            - (Mesh attribute) (float[]): [[P | ∂]] Mesh attribute buffer (flatten)
    """

    filename: Optional[str] = None
    shape_index: Optional[int] = None
    face_normals: Optional[bool] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    vertex_count: Optional[int] = None
    face_count: Optional[int] = None
    faces: Optional[Plugin] = None
    vertex_positions: Optional[float] = None
    vertex_normals: Optional[float] = None
    vertex_texcoords: Optional[float] = None
    mesh_attribute: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        shape_index: Optional[int] = None,
        face_normals: Optional[bool] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        vertex_count: Optional[int] = None,
        face_count: Optional[int] = None,
        faces: Optional[Plugin] = None,
        vertex_positions: Optional[float] = None,
        vertex_normals: Optional[float] = None,
        vertex_texcoords: Optional[float] = None,
        mesh_attribute: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="serialized", id=id)
        self.id = id
        self.filename = filename
        self.shape_index = shape_index
        self.face_normals = face_normals
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.vertex_count = vertex_count
        self.face_count = face_count
        self.faces = faces
        self.vertex_positions = vertex_positions
        self.vertex_normals = vertex_normals
        self.vertex_texcoords = vertex_texcoords
        self.mesh_attribute = mesh_attribute
        self.bsdf = bsdf


@dataclass
class Cube(Plugin):
    """Cube (cube)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#cube
        Params:
            - flip_normals (boolean):  Is the cube inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform):  Specifies an optional linear object-to-world transformation.
    (Default: none (i.e. object space = world space))
            - vertex_count (integer): [P] Total number of vertices
            - face_count (integer): [P] Total number of faces
            - faces (uint32[]): [P] Face indices buffer (flatten)
            - vertex_positions (float[]): [P | ∂ | D] Vertex positions buffer (flatten) pre-multiplied by the object-to-world transformation.
            - vertex_normals (float[]): [P | ∂ | D] Vertex normals buffer (flatten)  pre-multiplied by the object-to-world transformation.
            - vertex_texcoords (float[]): [P | ∂] Vertex texcoords buffer (flatten)
            - (Mesh attribute) (float[]): [P | ∂] Mesh attribute buffer (flatten)
            - (Mesh attribute) (float[]): [[P | ∂]] Mesh attribute buffer (flatten)
    """

    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    vertex_count: Optional[int] = None
    face_count: Optional[int] = None
    faces: Optional[Plugin] = None
    vertex_positions: Optional[float] = None
    vertex_normals: Optional[float] = None
    vertex_texcoords: Optional[float] = None
    mesh_attribute: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        vertex_count: Optional[int] = None,
        face_count: Optional[int] = None,
        faces: Optional[Plugin] = None,
        vertex_positions: Optional[float] = None,
        vertex_normals: Optional[float] = None,
        vertex_texcoords: Optional[float] = None,
        mesh_attribute: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="cube", id=id)
        self.id = id
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.vertex_count = vertex_count
        self.face_count = face_count
        self.faces = faces
        self.vertex_positions = vertex_positions
        self.vertex_normals = vertex_normals
        self.vertex_texcoords = vertex_texcoords
        self.mesh_attribute = mesh_attribute
        self.bsdf = bsdf


@dataclass
class Sphere(Plugin):
    """Sphere (sphere)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#sphere
        Params:
            - center (point):  Center of the sphere (Default: (0, 0, 0))
            - radius (float):  Radius of the sphere (Default: 1)
            - flip_normals (boolean):  Is the sphere inverted, i.e. should the normal vectors be flipped? (Default: false , i.e.
    the normals point outside)
            - to_world (transform): [P | ∂ | D] Specifies an optional linear object-to-world transformation.
    Note that non-uniform scales and shears are not permitted!
    (Default: none, i.e. object space = world space)
            - silhouette_sampling_weight (float): [P] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
            - silhouette_sampling_weight (float): [[P]] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
    """

    center: Optional[Plugin] = None
    radius: Optional[float] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    silhouette_sampling_weight: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        center: Optional[Plugin] = None,
        radius: Optional[float] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        silhouette_sampling_weight: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="sphere", id=id)
        self.id = id
        self.center = center
        self.radius = radius
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.silhouette_sampling_weight = silhouette_sampling_weight
        self.bsdf = bsdf


@dataclass
class Rectangle(Plugin):
    """Rectangle (rectangle)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#rectangle
    Params:
        - flip_normals (boolean):  Is the rectangle inverted, i.e. should the normal vectors be flipped? (Default: false )
        - to_world (transform): [P | ∂ | D] Specifies a linear object-to-world transformation. (Default: none (i.e. object space = world space))
        - silhouette_sampling_weight (float): [P] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
        - silhouette_sampling_weight (float): [[P]] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
    """

    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    silhouette_sampling_weight: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        silhouette_sampling_weight: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="rectangle", id=id)
        self.id = id
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.silhouette_sampling_weight = silhouette_sampling_weight
        self.bsdf = bsdf


@dataclass
class Disk(Plugin):
    """Disk (disk)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#disk
        Params:
            - flip_normals (boolean):  Is the disk inverted, i.e. should the normal vectors be flipped? (Default: false )
            - to_world (transform): [P | ∂ | D] Specifies a linear object-to-world transformation. Note that non-uniform scales are not
    permitted! (Default: none, i.e. object space = world space)
            - silhouette_sampling_weight (float): [P] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
            - silhouette_sampling_weight (float): [[P]] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
    """

    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    silhouette_sampling_weight: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        silhouette_sampling_weight: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="disk", id=id)
        self.id = id
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.silhouette_sampling_weight = silhouette_sampling_weight
        self.bsdf = bsdf


@dataclass
class Cylinder(Plugin):
    """Cylinder (cylinder)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#cylinder
        Params:
            - p0 (point):  Object-space starting point of the cylinder’s centerline.
    (Default: (0, 0, 0))
            - p1 (point):  Object-space endpoint of the cylinder’s centerline (Default: (0, 0, 1))
            - radius (float):  Radius of the cylinder in object-space units (Default: 1)
            - flip_normals (boolean):  Is the cylinder inverted, i.e. should the normal vectors
    be flipped? (Default: false , i.e. the normals point outside)
            - to_world (transform): [P | ∂ | D] Specifies an optional linear object-to-world transformation. Note that non-uniform scales are
    not permitted! (Default: none, i.e. object space = world space)
            - silhouette_sampling_weight (float): [P] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
            - silhouette_sampling_weight (float): [[P]] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
    """

    p0: Optional[Plugin] = None
    p1: Optional[Plugin] = None
    radius: Optional[float] = None
    flip_normals: Optional[bool] = None
    to_world: Optional[Transform] = None
    silhouette_sampling_weight: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        p0: Optional[Plugin] = None,
        p1: Optional[Plugin] = None,
        radius: Optional[float] = None,
        flip_normals: Optional[bool] = None,
        to_world: Optional[Transform] = None,
        silhouette_sampling_weight: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="cylinder", id=id)
        self.id = id
        self.p0 = p0
        self.p1 = p1
        self.radius = radius
        self.flip_normals = flip_normals
        self.to_world = to_world
        self.silhouette_sampling_weight = silhouette_sampling_weight
        self.bsdf = bsdf


@dataclass
class BSplineCurve(Plugin):
    """B-spline curve (bsplinecurve)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#bsplinecurve
        Params:
            - filename (string):  Filename of the curves to be loaded
            - to_world (transform):  Specifies a linear object-to-world transformation. Note that the control
    points’ raddii are invariant to this transformation!
            - silhouette_sampling_weight (float): [P] Weight associated with this shape when sampling silhoeuttes in the scene. (Default: 1)
            - control_point_count (integer): [P] Total number of control points
            - segment_indices (uint32[]): [P] Starting indices of a B-Spline segment
            - control_points (float[]): [P | ∂ | D] Flattened control points buffer pre-multiplied by the object-to-world transformation.
    Each control point in the buffer is structured as follows: position_x, position_y, position_z, radius
            - control_points (float[]): [[P | ∂ | D]] Flattened control points buffer pre-multiplied by the object-to-world transformation.
    Each control point in the buffer is structured as follows: position_x, position_y, position_z, radius
    """

    filename: Optional[str] = None
    to_world: Optional[Transform] = None
    silhouette_sampling_weight: Optional[float] = None
    control_point_count: Optional[int] = None
    segment_indices: Optional[Plugin] = None
    control_points: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        to_world: Optional[Transform] = None,
        silhouette_sampling_weight: Optional[float] = None,
        control_point_count: Optional[int] = None,
        segment_indices: Optional[Plugin] = None,
        control_points: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="bsplinecurve", id=id)
        self.id = id
        self.filename = filename
        self.to_world = to_world
        self.silhouette_sampling_weight = silhouette_sampling_weight
        self.control_point_count = control_point_count
        self.segment_indices = segment_indices
        self.control_points = control_points
        self.bsdf = bsdf


@dataclass
class LinearCurve(Plugin):
    """Linear curve (linearcurve)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#linearcurve
        Params:
            - filename (string):  Filename of the curves to be loaded
            - to_world (transform):  Specifies a linear object-to-world transformation. Note that the control
    points’ raddii are invariant to this transformation!
            - control_point_count (integer): [P] Total number of control points
            - segment_indices (uint32[]): [P] Starting indices of a linear segment
            - control_points (float[]): [P] Flattened control points buffer pre-multiplied by the object-to-world transformation.
    Each control point in the buffer is structured as follows: position_x, position_y, position_z, radius
            - control_points (float[]): [[P]] Flattened control points buffer pre-multiplied by the object-to-world transformation.
    Each control point in the buffer is structured as follows: position_x, position_y, position_z, radius
    """

    filename: Optional[str] = None
    to_world: Optional[Transform] = None
    control_point_count: Optional[int] = None
    segment_indices: Optional[Plugin] = None
    control_points: Optional[float] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        to_world: Optional[Transform] = None,
        control_point_count: Optional[int] = None,
        segment_indices: Optional[Plugin] = None,
        control_points: Optional[float] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="linearcurve", id=id)
        self.id = id
        self.filename = filename
        self.to_world = to_world
        self.control_point_count = control_point_count
        self.segment_indices = segment_indices
        self.control_points = control_points
        self.bsdf = bsdf


@dataclass
class SdfGrid(Plugin):
    """SDF Grid (sdfgrid)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#sdfgrid
        Params:
            - filename (string):  Filename of the SDF grid data to be loaded. The expected file format
    aligns with a single-channel grid-based volume data source .
    If no filename is provided, the shape is initialised as an empty 2x2x2 grid.
            - grid (tensor): [P | ∂ | D] Tensor array containing the grid data. This parameter can only be specified
    when building this plugin at runtime from Python or C++ and cannot be
    specified in the XML scene description.
            - normals (string):  Specifies the method for computing shading normals. The options are analytic or smooth . (Default: smooth )
            - to_world (transform): [P | ∂ | D] Specifies a linear object-to-world transformation. (Default: none (i.e. object space = world space))
            - to_world (transform): [[P | ∂ | D]] Specifies a linear object-to-world transformation. (Default: none (i.e. object space = world space))
    """

    filename: Optional[str] = None
    grid: Optional[Plugin] = None
    normals: Optional[str] = None
    to_world: Optional[Transform] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        grid: Optional[Plugin] = None,
        normals: Optional[str] = None,
        to_world: Optional[Transform] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="sdfgrid", id=id)
        self.id = id
        self.filename = filename
        self.grid = grid
        self.normals = normals
        self.to_world = to_world
        self.bsdf = bsdf


@dataclass
class ShapeGroup(Plugin):
    """Shape group (shapegroup)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#shapegroup
    Params:
        - (Nested plugin) (shape):  One or more shapes that should be made available for geometry instancing
        - (Nested plugin) (shape): [] One or more shapes that should be made available for geometry instancing
    """

    nested_plugin: Optional[Plugin] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        nested_plugin: Optional[Plugin] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="shapegroup", id=id)
        self.id = id
        self.nested_plugin = nested_plugin
        self.bsdf = bsdf


@dataclass
class Instance(Plugin):
    """Instance (instance)
    https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#instance
    Params:
        - (Nested plugin) (shapegroup):  A reference to a shape group that should be instantiated.
        - to_world (transform): [P | ∂ | D] Specifies a linear object-to-world transformation. (Default: none (i.e. object space = world space))
        - to_world (transform): [[P | ∂ | D]] Specifies a linear object-to-world transformation. (Default: none (i.e. object space = world space))
    """

    nested_plugin: Optional[Plugin] = None
    to_world: Optional[Transform] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        nested_plugin: Optional[Plugin] = None,
        to_world: Optional[Transform] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="instance", id=id)
        self.id = id
        self.nested_plugin = nested_plugin
        self.to_world = to_world
        self.bsdf = bsdf


@dataclass
class Ellipsoids(Plugin):
    """Ellipsoids (ellipsoids)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#ellipsoids
        Params:
            - filename (string):  Specifies the PLY file containing the ellipsoid centers, scales, and quaternions.
    This parameter cannot be used if data or centers are provided.
            - data (tensor):  A tensor of shape (N, 10) or (N * 10) that defines the ellipsoid centers, scales, and quaternions.
    This parameter cannot be used if filename or centers are provided.
            - centers (tensor):  A tensor of shape (N, 3) specifying the ellipsoid centers.
    This parameter cannot be used if filename or data are provided.
            - scales (tensor):  A tensor of shape (N, 3) specifying the ellipsoid scales.
    This parameter cannot be used if filename or data are provided.
            - quaternions (tensor):  A tensor of shape (N, 3) specifying the ellipsoid quaternions.
    This parameter cannot be used if filename or data are provided.
            - scale_factor (float):  A scaling factor applied to all ellipsoids when loading from a PLY file. (Default: 1.0)
            - extent (float):  Specifies the extent of the ellipsoid. This effectively acts as an
    extra scaling factor on the ellipsoid, without having to alter the scale
    parameters. (Default: 3.0)
            - extent_adaptive_clamping (float):  If True, use adaptive extent values based on the opacities attribute of
    the volumetric primitives. (Default: False)
            - to_world (transform): [P | ∂ | D] Specifies an optional linear object-to-world transformation to apply to
    all ellipsoids.
            - (Nested plugin) (tensor):  Specifies arbitrary ellipsoids attribute as a tensor of shape (N, D) with D
    the dimensionality of the attribute. For instance this can be used to define
    an opacity value for each ellipsoids, or a set of spherical harmonic coefficients
    as used in the volprim_rf_basic integrator.
            - (Nested plugin) (tensor): [] Specifies arbitrary ellipsoids attribute as a tensor of shape (N, D) with D
    the dimensionality of the attribute. For instance this can be used to define
    an opacity value for each ellipsoids, or a set of spherical harmonic coefficients
    as used in the volprim_rf_basic integrator.
    """

    filename: Optional[str] = None
    data: Optional[Plugin] = None
    centers: Optional[Plugin] = None
    scales: Optional[Plugin] = None
    quaternions: Optional[Plugin] = None
    scale_factor: Optional[float] = None
    extent: Optional[float] = None
    extent_adaptive_clamping: Optional[float] = None
    to_world: Optional[Transform] = None
    nested_plugin: Optional[Plugin] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        data: Optional[Plugin] = None,
        centers: Optional[Plugin] = None,
        scales: Optional[Plugin] = None,
        quaternions: Optional[Plugin] = None,
        scale_factor: Optional[float] = None,
        extent: Optional[float] = None,
        extent_adaptive_clamping: Optional[float] = None,
        to_world: Optional[Transform] = None,
        nested_plugin: Optional[Plugin] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="ellipsoids", id=id)
        self.id = id
        self.filename = filename
        self.data = data
        self.centers = centers
        self.scales = scales
        self.quaternions = quaternions
        self.scale_factor = scale_factor
        self.extent = extent
        self.extent_adaptive_clamping = extent_adaptive_clamping
        self.to_world = to_world
        self.nested_plugin = nested_plugin
        self.bsdf = bsdf


@dataclass
class MeshEllipsoids(Plugin):
    """Mesh ellipsoids (ellipsoidsmesh)
        https://mitsuba.readthedocs.io/en/latest/src/generated/plugins_shapes.html#ellipsoidsmesh
        Params:
            - filename (string):  Specifies the PLY file containing the ellipsoid centers, scales, and quaternions.
    This parameter cannot be used if data or centers are provided.
            - data (tensor):  A tensor of shape (N, 10) or (N * 10) that defines the ellipsoid centers, scales, and quaternions.
    This parameter cannot be used if filename or centers are provided.
            - centers (tensor):  A tensor of shape (N, 3) specifying the ellipsoid centers.
    This parameter cannot be used if filename or data are provided.
            - scales (tensor):  A tensor of shape (N, 3) specifying the ellipsoid scales.
    This parameter cannot be used if filename or data are provided.
            - quaternions (tensor):  A tensor of shape (N, 3) specifying the ellipsoid quaternions.
    This parameter cannot be used if filename or data are provided.
            - scale_factor (float):  A scaling factor applied to all ellipsoids when loading from a PLY file. (Default: 1.0)
            - extent (float):  Specifies the extent of the ellipsoid. This effectively acts as an
    extra scaling factor on the ellipsoid, without having to alter the scale
    parameters. (Default: 3.0)
            - extent_adaptive_clamping (float):  If True, use adaptive extent values based on the opacities attribute of the volumetric primitives. (Default: False)
            - shell (string or |mesh|):  Specifies the shell type. Could be one of box , ico_sphere ,
    or uv_sphere , as well as a custom child mesh object. (Default: ico_sphere )
            - to_world (transform): [P | ∂ | D] Specifies an optional linear object-to-world transformation to apply to all ellipsoids.
            - (Nested plugin) (tensor):  Specifies arbitrary ellipsoids attribute as a tensor of shape (N, D) with D
    the dimensionality of the attribute. For instance this can be used to define
    an opacity value for each ellipsoids, or a set of spherical harmonic coefficients
    as used in the volprim_rf_basic integrator.
            - (Nested plugin) (tensor): [] Specifies arbitrary ellipsoids attribute as a tensor of shape (N, D) with D
    the dimensionality of the attribute. For instance this can be used to define
    an opacity value for each ellipsoids, or a set of spherical harmonic coefficients
    as used in the volprim_rf_basic integrator.
    """

    filename: Optional[str] = None
    data: Optional[Plugin] = None
    centers: Optional[Plugin] = None
    scales: Optional[Plugin] = None
    quaternions: Optional[Plugin] = None
    scale_factor: Optional[float] = None
    extent: Optional[float] = None
    extent_adaptive_clamping: Optional[float] = None
    shell: Optional[str] = None
    to_world: Optional[Transform] = None
    nested_plugin: Optional[Plugin] = None
    bsdf: Optional[Plugin] = None

    def __init__(
        self,
        id: Optional[str] = None,
        filename: Optional[str] = None,
        data: Optional[Plugin] = None,
        centers: Optional[Plugin] = None,
        scales: Optional[Plugin] = None,
        quaternions: Optional[Plugin] = None,
        scale_factor: Optional[float] = None,
        extent: Optional[float] = None,
        extent_adaptive_clamping: Optional[float] = None,
        shell: Optional[str] = None,
        to_world: Optional[Transform] = None,
        nested_plugin: Optional[Plugin] = None,
        bsdf: Optional[Plugin] = None,
    ):
        super().__init__(type="ellipsoidsmesh", id=id)
        self.id = id
        self.filename = filename
        self.data = data
        self.centers = centers
        self.scales = scales
        self.quaternions = quaternions
        self.scale_factor = scale_factor
        self.extent = extent
        self.extent_adaptive_clamping = extent_adaptive_clamping
        self.shell = shell
        self.to_world = to_world
        self.nested_plugin = nested_plugin
        self.bsdf = bsdf

"""Derive a display-only 3MF without changing the downloadable source assembly."""
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as ET

import fast_simplification
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CORE = 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
NS = {'c': CORE}
TAG = '{' + CORE + '}'
RECIPE = 'weld-0.0001mm-material-groups-adaptive-min64-bounds-v3'


def build_browser_model():
    source = ROOT / 'assets/models/artorius/artorius.3mf'
    target = source.with_name('artorius-preview.3mf')
    manifest = source.with_name('preview-manifest.json')
    digest = sha256(source.read_bytes()).hexdigest()
    if target.exists() and manifest.exists():
        old = json.loads(manifest.read_text())
        if old.get('source_sha256') == digest and old.get('recipe') == RECIPE and old.get('preview_sha256') == sha256(target.read_bytes()).hexdigest():
            print('Browser model is current')
            return
    counts = dict(meshes=0, source_triangles=0, preview_triangles=0, retained_groups=0)
    with ZipFile(source) as archive:
        with archive.open('3D/3dmodel.model') as header:
            if next(ET.iterparse(header, events=('start',)))[1].get('unit', 'millimeter') != 'millimeter':
                raise ValueError('Preview tolerances require a millimeter source export')
        with archive.open('3D/3dmodel.model') as stream:
            context = ET.iterparse(stream, events=('end', 'start-ns'))
            for event, element in context:
                if event == 'start-ns':
                    prefix, uri = element
                    ET.register_namespace(prefix, uri)
                    continue
                if element.tag != TAG + 'object':
                    continue
                mesh = element.find('c:mesh', NS)
                if mesh is None:
                    continue
                points = np.array([[float(v.get(k)) for k in ('x','y','z')] for v in mesh.find('c:vertices', NS)])
                groups = defaultdict(list)
                for face in mesh.find('c:triangles', NS):
                    material = tuple(sorted((k,v) for k,v in face.attrib.items() if k not in ('v1','v2','v3')))
                    groups[material].append([int(face.get(k)) for k in ('v1','v2','v3')])
                mesh.clear()
                vertices = ET.SubElement(mesh, TAG + 'vertices')
                triangles = ET.SubElement(mesh, TAG + 'triangles')
                offset = 0
                for material, rows in groups.items():
                    faces = np.array(rows, dtype=np.int32)
                    used, inverse = np.unique(faces, return_inverse=True)
                    local_points = points[used]
                    local_faces = inverse.reshape((-1,3)).astype(np.int32)
                    counts['source_triangles'] += len(faces)
                    # CAD tessellation repeats coincident vertices along face seams.
                    # Weld only within one material group, at 0.0001 mm precision,
                    # so the decimator can follow connected surfaces.
                    welded_points, welded_inverse = np.unique(np.round(local_points, 4), axis=0, return_inverse=True)
                    welded_faces = welded_inverse[local_faces].astype(np.int32)
                    valid = (welded_faces[:,0] != welded_faces[:,1]) & (welded_faces[:,1] != welded_faces[:,2]) & (welded_faces[:,0] != welded_faces[:,2])
                    if valid.any():
                        local_points, local_faces = welded_points, welded_faces[valid]
                    out_points, out_faces = local_points, local_faces
                    if len(local_faces) > 64:
                        tolerance = max(0.25, float(np.linalg.norm(np.ptp(local_points,axis=0))) * 0.01)
                        # Back off when a coarse version changes a part's extents too much.
                        for fraction in (0.04, 0.1, 0.25, 0.5):
                            candidate_points, candidate_faces = fast_simplification.simplify(local_points, local_faces, target_count=max(64, int(len(local_faces)*fraction)), agg=5)
                            bounds_error = max(np.max(np.abs(candidate_points.min(axis=0)-local_points.min(axis=0))), np.max(np.abs(candidate_points.max(axis=0)-local_points.max(axis=0)))) if len(candidate_points) else np.inf
                            if len(candidate_faces) and np.isfinite(candidate_points).all() and bounds_error <= tolerance:
                                out_points, out_faces = candidate_points, candidate_faces
                                break
                        else:
                            counts['retained_groups'] += 1
                    for point in out_points:
                        ET.SubElement(vertices, TAG + 'vertex', {k: f'{value:.4f}' for k,value in zip(('x','y','z'),point)})
                    for face in out_faces:
                        attrs = dict(material)
                        attrs.update({k: str(int(value)+offset) for k,value in zip(('v1','v2','v3'),face)})
                        ET.SubElement(triangles, TAG + 'triangle', attrs)
                    offset += len(out_points)
                    counts['preview_triangles'] += len(out_faces)
                counts['meshes'] += 1
        with ZipFile(target, 'w', ZIP_DEFLATED, compresslevel=9) as output:
            for name in archive.namelist():
                output.writestr(name, ET.tostring(context.root, encoding='utf-8', xml_declaration=True) if name == '3D/3dmodel.model' else archive.read(name))
    report = dict(recipe=RECIPE, source_sha256=digest, preview_sha256=sha256(target.read_bytes()).hexdigest(), source_bytes=source.stat().st_size, preview_bytes=target.stat().st_size, **counts)
    if report['preview_bytes'] >= report['source_bytes'] or not counts['meshes']:
        raise ValueError('Expected a smaller, nonempty browser assembly')
    manifest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    build_browser_model()

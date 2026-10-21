# Artorius model exports

`artorius.3mf` is the original, full-resolution assembly download. It is never overwritten by the preview generator.

`python scripts/build_portfolio.py` generates `artorius-preview.3mf` and `preview-manifest.json` before Jekyll. Both generated files are ignored by Git and included in the built website. Install `requirements-portfolio.txt` first. Preview and deployment workflows run this command automatically.

The display export simplifies each mesh in separate material groups, preserving object identities, assembly transforms, resource references, and material assignments. An adaptive triangle target backs off when a component's bounds change beyond the generation tolerance. Every mesh remains represented. Fine geometric details are approximate; the preview is not a manufacturing file.

The manifest records source/preview checksums, byte sizes, triangle counts, and mesh count. Generation reuses a matching local output; replacing the source or changing the recipe regenerates it. The site checker verifies hashes, size reduction, mesh/triangle counts, and valid finite indexed geometry.

## Export from Fusion

1. Select the assembly/root component and choose **Save As Mesh**.
2. Choose **3MF**, millimeters, and **One File**. Start with medium refinement.
3. Export the complete assembly in its assembled position, with the intended bodies visible.
4. Upload the file with the exact name above. Check that all expected parts appear in the viewer.

The viewer provides orbit, pan, zoom, and reset controls. It does not recreate Fusion's feature history. The full source assembly remains publicly downloadable; keep editable CAD in the separate Artorius repository. Only the lightweight preview loads when a visitor clicks **Load 3D preview**. Three.js and its loader are pinned to 0.160.0 on jsDelivr; an internet connection and WebGL are required.

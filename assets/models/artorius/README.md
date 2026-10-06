# Artorius browser model

Upload the assembly as `artorius.3mf` in this folder:

`assets/models/artorius/artorius.3mf`

The Artorius project page detects this file at build time. Until it exists, the viewer displays a placeholder. GitHub Pages must rebuild after upload.

## Export from Fusion

1. Select the assembly/root component and choose **Save As Mesh**.
2. Choose **3MF**, millimeters, and **One File**. Start with medium refinement.
3. Export the complete assembly in its assembled position, with the intended bodies visible.
4. Upload the file with the exact name above. Check that all expected parts appear in the viewer.

The viewer lists separate mesh objects from the exported file. It supports visibility checkboxes, isolating one mesh, showing all, and resetting the camera. It does not recreate Fusion's feature history or guarantee the original component hierarchy/names. If the export combines bodies, it cannot separate them afterward. Exporting finer meshes increases load time and memory usage. There is no automatic simplification.

The file is publicly downloadable. Keep your editable CAD in the separate Artorius repository; this folder is for the display export. Models load only when visitors click **Load 3D model**. Three.js and its loader are pinned to 0.160.0 on jsDelivr; an internet connection and WebGL are required.

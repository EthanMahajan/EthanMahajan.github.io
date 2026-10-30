const root = document.querySelector("[data-cad-viewer]");
const loadButton = root?.querySelector("[data-cad-load]");
if (loadButton) {
  const status = root.querySelector("[data-cad-status]");
  loadButton.addEventListener("click", async () => {
    loadButton.disabled = true;
    status.textContent = "Loading viewer and model";
    let webglUnavailable = false;
    let renderer;
    let controls;
    let observer;
    let model;
    const dispose = () => {
      observer?.disconnect();
      controls?.dispose();
      model?.traverse((object) => {
        object.geometry?.dispose();
        const materials = Array.isArray(object.material) ? object.material : [object.material];
        materials.forEach((material) => material?.dispose());
      });
      renderer?.dispose();
      renderer?.domElement.remove();
    };
    try {
      const probe = document.createElement("canvas");
      const context = probe.getContext("webgl2") || probe.getContext("webgl");
      if (!context) {
        webglUnavailable = true;
        throw new Error("WebGL unavailable");
      }
      context.getExtension("WEBGL_lose_context")?.loseContext();
      const [THREE, { OrbitControls }, { ThreeMFLoader }] = await Promise.all([
        import("three"),
        import("three/addons/controls/OrbitControls.js"),
        import("three/addons/loaders/3MFLoader.js"),
      ]);
      const response = await fetch(root.dataset.modelUrl);
      if (!response.ok) throw new Error("Model download failed");
      const buffer = await response.arrayBuffer();
      status.textContent = "Preparing assembly geometry";
      await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      model = new ThreeMFLoader().parse(buffer);
      const meshes = [];
      model.traverse((object) => {
        if (object.isMesh) meshes.push(object);
      });
      if (!meshes.length) throw new Error("No visible mesh geometry");
      const box = new THREE.Box3().setFromObject(model);
      if (box.isEmpty()) throw new Error("Empty assembly");
      const center = box.getCenter(new THREE.Vector3());
      const radius = Math.max(box.getSize(new THREE.Vector3()).length() / 2, 0.001);
      renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.setClearColor(0xedf1f4);
      const canvas = root.querySelector("[data-cad-canvas]");
      canvas.append(renderer.domElement);
      renderer.domElement.tabIndex = 0;
      renderer.domElement.setAttribute("aria-label", "Artorius 3D assembly. Drag to orbit; arrow keys pan.");
      const scene = new THREE.Scene();
      scene.add(model);
      scene.add(new THREE.HemisphereLight(0xffffff, 0x526174, 2));
      const light = new THREE.DirectionalLight(0xffffff, 3);
      light.position.set(1, -1, 2);
      scene.add(light);
      const camera = new THREE.PerspectiveCamera(45, 1, radius / 1000, radius * 1000);
      camera.up.set(0, 0, 1);
      controls = new OrbitControls(camera, renderer.domElement);
      controls.target.copy(center);
      controls.minDistance = radius * 0.05;
      controls.maxDistance = radius * 100;
      controls.listenToKeyEvents(renderer.domElement);
      const render = () => renderer.render(scene, camera);
      const reset = () => {
        const halfFov = THREE.MathUtils.degToRad(camera.fov / 2);
        const fitAngle = Math.min(halfFov, Math.atan(Math.tan(halfFov) * camera.aspect));
        const distance = (radius / Math.sin(fitAngle)) * 1.15;
        camera.position.copy(center).add(new THREE.Vector3(1, -1, 0.7).normalize().multiplyScalar(distance));
        controls.target.copy(center);
        controls.update();
        render();
      };
      const resize = () => {
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        if (!width || !height) return;
        renderer.setSize(width, height, false);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        render();
      };
      controls.addEventListener("change", render);
      root.querySelector("[data-cad-reset]").addEventListener("click", reset);
      const zoom = (factor) => {
        const offset = camera.position.clone().sub(controls.target);
        const distance = THREE.MathUtils.clamp(offset.length() * factor, controls.minDistance, controls.maxDistance);
        camera.position.copy(controls.target).add(offset.setLength(distance));
        controls.update();
      };
      root.querySelector("[data-cad-zoom-in]").addEventListener("click", () => zoom(0.8));
      root.querySelector("[data-cad-zoom-out]").addEventListener("click", () => zoom(1.25));
      root.querySelector("[data-cad-interface]").hidden = false;
      resize();
      reset();
      observer = new ResizeObserver(resize);
      observer.observe(canvas);
      window.addEventListener(
        "pagehide",
        (event) => {
          if (!event.persisted) dispose();
        },
        { once: true }
      );
      root.querySelector("[data-cad-static]").hidden = true;
      loadButton.hidden = true;
      status.textContent = "Assembly loaded. Drag to orbit, or use zoom and reset.";
    } catch (error) {
      dispose();
      root.querySelector("[data-cad-interface]").hidden = true;
      root.querySelector("[data-cad-static]").hidden = false;
      status.textContent = webglUnavailable
        ? "This browser cannot display the interactive model because WebGL is unavailable. Use the static view or download the assembly meshes."
        : "The model could not be downloaded or read. Use the static view, download the assembly meshes, or try loading again.";
      loadButton.disabled = false;
      console.error("Artorius viewer:", error);
    }
  });
}

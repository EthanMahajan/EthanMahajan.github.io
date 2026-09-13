const THREE_MODULE_URL = 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
const GLTF_LOADER_URL = 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/GLTFLoader.js';
const FONT_LOADER_URL = 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/FontLoader.js';
const TEXT_GEOMETRY_URL = 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/geometries/TextGeometry.js';
const FONT_URL = 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/fonts/helvetiker_regular.typeface.json';

const BED_SIZE = 235;
const MAX_TEXT_WIDTH = 198;
const MAX_TEXT_HEIGHT = 165;
const PRIME_DURATION = 1000;
const PRINT_DURATION = 12000;
const POST_PRINT_DURATION = 3000;
const NOZZLE_Z = 3;

const animationRoot = document.querySelector('[data-printer-animation]');
const aboutCopy = document.querySelector('#about-copy');

if (animationRoot && aboutCopy) {
  window.addEventListener('pageshow', (event) => {
    if (event.persisted) {
      window.location.reload();
    }
  });

  const canvas = animationRoot.querySelector('[data-printer-canvas]');
  const status = animationRoot.querySelector('[data-printer-status]');
  const skipButton = animationRoot.querySelector('[data-printer-skip]');
  const aboutLink = document.querySelector('[data-about-link]');
  const modelUrl = animationRoot.dataset.modelUrl;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (aboutLink) {
    aboutLink.addEventListener('click', (event) => {
      const destination = new URL(aboutLink.href, window.location.href);
      if (destination.pathname === window.location.pathname && destination.search === window.location.search) {
        event.preventDefault();
        window.location.reload();
      }
    });
  }

  let stopped = false;
  let stopAnimation = () => {};

  const revealCopy = () => {
    stopped = true;
    aboutCopy.classList.remove('is-printing');
    animationRoot.dataset.state = 'complete';
    if (status) {
      status.textContent = 'Ready';
    }
    if (skipButton) {
      skipButton.hidden = true;
    }
  };

  const updateStatus = (message) => {
    if (status) {
      status.textContent = message;
    }
  };

  if (reducedMotion) {
    animationRoot.hidden = true;
    revealCopy();
  } else {
    aboutCopy.classList.add('is-printing');

    if (skipButton) {
      skipButton.addEventListener('click', () => {
        stopAnimation();
        revealCopy();
      });
    }

    const loadModules = async () => {
      const [THREE, { GLTFLoader }, { FontLoader }, { TextGeometry }] = await Promise.all([
        import(THREE_MODULE_URL),
        import(GLTF_LOADER_URL),
        import(FONT_LOADER_URL),
        import(TEXT_GEOMETRY_URL),
      ]);

      return { THREE, GLTFLoader, FontLoader, TextGeometry };
    };

    const addBox = (THREE, scene, size, position, material, castShadow = true) => {
      const mesh = new THREE.Mesh(new THREE.BoxGeometry(...size), material);
      mesh.position.set(...position);
      mesh.castShadow = castShadow;
      mesh.receiveShadow = true;
      scene.add(mesh);
      return mesh;
    };

    const makeScene = (THREE) => {
      const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.05;
      renderer.shadowMap.enabled = true;
      renderer.shadowMap.type = THREE.PCFSoftShadowMap;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(30, 1, 1, 1200);
      camera.up.set(0, 0, 1);
      camera.position.set(0, -330, 190);
      camera.lookAt(0, 0, 35);

      const darkMode = document.documentElement.dataset.theme === 'dark';
      const frameMaterial = new THREE.MeshStandardMaterial({
        color: darkMode ? 0x536270 : 0x71808b,
        metalness: 0.75,
        roughness: 0.3,
      });
      const bedMaterial = new THREE.MeshStandardMaterial({
        color: darkMode ? 0x26333d : 0xd6dee5,
        metalness: 0.45,
        roughness: 0.5,
      });
      const edgeMaterial = new THREE.MeshStandardMaterial({
        color: darkMode ? 0x8395a2 : 0x53636e,
        metalness: 0.8,
        roughness: 0.25,
      });

      scene.add(new THREE.HemisphereLight(0xeaf5ff, darkMode ? 0x15212a : 0x75818a, 1.8));
      const keyLight = new THREE.DirectionalLight(0xffffff, 3.2);
      keyLight.position.set(-220, -260, 380);
      keyLight.castShadow = true;
      keyLight.shadow.mapSize.set(1024, 1024);
      keyLight.shadow.camera.left = -300;
      keyLight.shadow.camera.right = 300;
      keyLight.shadow.camera.top = 300;
      keyLight.shadow.camera.bottom = -300;
      scene.add(keyLight);

      addBox(THREE, scene, [BED_SIZE, BED_SIZE, 4], [0, 0, -2], bedMaterial, false);

      const grid = new THREE.GridHelper(BED_SIZE, 16, darkMode ? 0x586b79 : 0x8fa0aa, darkMode ? 0x586b79 : 0x8fa0aa);
      grid.rotation.x = Math.PI / 2;
      grid.position.z = 0.15;
      grid.material.transparent = true;
      grid.material.opacity = 0.3;
      scene.add(grid);

      const frameOffset = 151;
      const frameHeight = 180;
      for (const x of [-frameOffset, frameOffset]) {
        for (const y of [-frameOffset, frameOffset]) {
          addBox(THREE, scene, [8, 8, frameHeight], [x, y, frameHeight / 2], frameMaterial);
        }
      }
      addBox(THREE, scene, [310, 8, 8], [0, -frameOffset, frameHeight], frameMaterial);
      addBox(THREE, scene, [310, 8, 8], [0, frameOffset, frameHeight], frameMaterial);
      addBox(THREE, scene, [8, 310, 8], [-frameOffset, 0, frameHeight], frameMaterial);
      addBox(THREE, scene, [8, 310, 8], [frameOffset, 0, frameHeight], frameMaterial);
      addBox(THREE, scene, [270, 8, 7], [0, 0, 145], edgeMaterial);

      const bedBorder = 120;
      addBox(THREE, scene, [BED_SIZE + 4, 3, 5], [0, -bedBorder, 2.5], edgeMaterial);
      addBox(THREE, scene, [BED_SIZE + 4, 3, 5], [0, bedBorder, 2.5], edgeMaterial);
      addBox(THREE, scene, [3, BED_SIZE + 4, 5], [-bedBorder, 0, 2.5], edgeMaterial);
      addBox(THREE, scene, [3, BED_SIZE + 4, 5], [bedBorder, 0, 2.5], edgeMaterial);

      const toolheadRig = new THREE.Group();
      scene.add(toolheadRig);

      const fallbackToolhead = new THREE.Group();
      fallbackToolhead.add(
        addBox(THREE, fallbackToolhead, [36, 28, 20], [0, 0, 8], edgeMaterial),
      );
      const fanMaterial = new THREE.MeshStandardMaterial({ color: 0x263b4c, metalness: 0.35, roughness: 0.45 });
      const fan = new THREE.Mesh(new THREE.CylinderGeometry(11, 11, 6, 24), fanMaterial);
      fan.rotation.x = Math.PI / 2;
      fan.position.set(0, -15, 9);
      fan.castShadow = true;
      fallbackToolhead.add(fan);
      toolheadRig.add(fallbackToolhead);

      const nozzleMaterial = new THREE.MeshStandardMaterial({ color: 0xe3a43b, metalness: 0.8, roughness: 0.25 });
      const nozzle = new THREE.Mesh(new THREE.ConeGeometry(2.8, 8, 12), nozzleMaterial);
      nozzle.position.z = -10;
      nozzle.castShadow = true;
      toolheadRig.add(nozzle);
      toolheadRig.userData.nozzleOffsetZ = -10;
      toolheadRig.position.z = NOZZLE_Z - toolheadRig.userData.nozzleOffsetZ;

      return { renderer, scene, camera, toolheadRig, fallbackToolhead, nozzle };
    };

    const loadToolhead = async (THREE, GLTFLoader, app) => {
      try {
        const gltf = await new GLTFLoader().loadAsync(modelUrl);
        const model = gltf.scene;
        model.updateMatrixWorld(true);
        const bounds = new THREE.Box3().setFromObject(model);
        const size = bounds.getSize(new THREE.Vector3());
        const center = bounds.getCenter(new THREE.Vector3());
        const scale = 58 / Math.max(size.x, size.y);
        model.scale.setScalar(scale);
        model.position.copy(center).multiplyScalar(-scale);
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
          }
        });
        app.toolheadRig.add(model);
        app.fallbackToolhead.visible = false;
        app.toolheadRig.userData.nozzleOffsetZ = -Math.max(size.z * scale * 0.5 + 2, 10);
        app.toolheadRig.position.z = NOZZLE_Z - app.toolheadRig.userData.nozzleOffsetZ;
      } catch (error) {
        updateStatus('Using lightweight printer head');
      }
    };

    const disposeLayout = (layout) => {
      layout.words.forEach(({ geometry }) => geometry.dispose());
    };

    const makeTextLayout = (THREE, TextGeometry, font, text) => {
      const words = text.replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
      let size = 7;

      for (let attempt = 0; attempt < 6; attempt += 1) {
        const spaceWidth = size * 0.5;
        const lineHeight = size * 1.55;
        const lines = [];
        let line = [];
        let lineWidth = 0;

        words.forEach((word) => {
          const geometry = new TextGeometry(word, {
            font,
            size,
            depth: 1.8,
            curveSegments: 2,
            bevelEnabled: false,
          });
          geometry.computeBoundingBox();
          const bounds = geometry.boundingBox;
          const width = bounds.max.x - bounds.min.x;
          geometry.translate(-(bounds.min.x + bounds.max.x) / 2, -bounds.min.y, 0);

          if (line.length > 0 && lineWidth + spaceWidth + width > MAX_TEXT_WIDTH) {
            lines.push({ words: line, width: lineWidth });
            line = [];
            lineWidth = 0;
          }

          line.push({ word, geometry, width });
          lineWidth += (line.length === 1 ? 0 : spaceWidth) + width;
        });

        if (line.length > 0) {
          lines.push({ words: line, width: lineWidth });
        }

        const totalHeight = lines.length * lineHeight;
        if (totalHeight <= MAX_TEXT_HEIGHT) {
          const material = new THREE.MeshStandardMaterial({
            color: 0x2f8fe5,
            metalness: 0.2,
            roughness: 0.38,
          });
          const textMeshes = [];
          const topY = totalHeight / 2 - lineHeight;

          lines.forEach((currentLine, lineIndex) => {
            let x = -currentLine.width / 2;
            const y = topY - lineIndex * lineHeight;
            currentLine.words.forEach((entry, wordIndex) => {
              const mesh = new THREE.Mesh(entry.geometry, material);
              mesh.position.set(x + entry.width / 2, y, 0.8);
              mesh.scale.z = 0.02;
              mesh.visible = false;
              mesh.castShadow = true;
              mesh.receiveShadow = true;
              textMeshes.push(mesh);
              x += entry.width + (wordIndex === currentLine.words.length - 1 ? 0 : spaceWidth);
            });
          });

          return { words: textMeshes, lineHeight, fontSize: size };
        }

        lines.forEach((currentLine) => currentLine.words.forEach(({ geometry }) => geometry.dispose()));
        size -= 0.5;
      }

      return { words: [], lineHeight: 0, fontSize: size };
    };

    const makeSegment = (THREE, start, end, material) => {
      const direction = new THREE.Vector3().subVectors(end, start);
      const length = direction.length();
      const mesh = new THREE.Mesh(new THREE.CylinderGeometry(1.6, 1.6, length, 8), material);
      mesh.userData = { start, direction: direction.normalize(), length };
      mesh.castShadow = true;
      mesh.visible = false;
      return mesh;
    };

    const setSegmentProgress = (mesh, progress) => {
      const amount = Math.max(0, Math.min(1, progress));
      const { start, direction, length } = mesh.userData;
      mesh.visible = amount > 0;
      mesh.position.copy(start).addScaledVector(direction, length * amount * 0.5);
      mesh.quaternion.setFromUnitVectors(new mesh.position.constructor(0, 1, 0), direction);
      mesh.scale.y = amount;
    };

    const moveBetween = (THREE, rig, from, to, amount) => {
      rig.position.x = THREE.MathUtils.lerp(from.x, to.x, amount);
      rig.position.y = THREE.MathUtils.lerp(from.y, to.y, amount);
      const nozzleZ = THREE.MathUtils.lerp(from.z, to.z, amount);
      rig.position.z = nozzleZ - rig.userData.nozzleOffsetZ;
    };

    const run = async () => {
      try {
        const { THREE, GLTFLoader, FontLoader, TextGeometry } = await loadModules();
        if (stopped) return;

        const app = makeScene(THREE);
        const fontPromise = new FontLoader().loadAsync(FONT_URL);
        const toolheadPromise = loadToolhead(THREE, GLTFLoader, app);
        updateStatus('Loading printer head');
        const [font] = await Promise.all([fontPromise, toolheadPromise]);
        if (stopped) return;

        const text = aboutCopy.textContent;
        const layout = makeTextLayout(THREE, TextGeometry, font, text);
        if (layout.words.length === 0) {
          revealCopy();
          return;
        }

        const printedText = new THREE.Group();
        layout.words.forEach((word) => printedText.add(word));
        app.scene.add(printedText);

        const filamentMaterial = new THREE.MeshStandardMaterial({
          color: 0xe3a43b,
          metalness: 0.12,
          roughness: 0.45,
        });
        const primeEnd = new THREE.Vector3(-64, -84, 2);
        const primeSegments = [
          makeSegment(THREE, new THREE.Vector3(-108, -108, 2), new THREE.Vector3(-64, -108, 2), filamentMaterial),
          makeSegment(THREE, new THREE.Vector3(-64, -108, 2), primeEnd, filamentMaterial),
        ];
        primeSegments.forEach((segment) => app.scene.add(segment));

        const textTargets = layout.words.map((word) => new THREE.Vector3(word.position.x, word.position.y, NOZZLE_Z));
        const firstTarget = textTargets[0];
        const finalTarget = textTargets[textTargets.length - 1];
        const parkTarget = new THREE.Vector3(106, 106, NOZZLE_Z);
        const homeXTarget = new THREE.Vector3(-108, 106, NOZZLE_Z);
        const homeYTarget = new THREE.Vector3(-108, -108, NOZZLE_Z);
        const homeZTarget = new THREE.Vector3(-108, -108, 45);
        const finalParkTarget = new THREE.Vector3(106, 106, 45);

        const resize = () => {
          const width = animationRoot.clientWidth;
          const height = animationRoot.querySelector('.printer-animation__stage').clientHeight;
          app.renderer.setSize(width, height, false);
          app.camera.aspect = width / height;
          app.camera.updateProjectionMatrix();
        };
        resize();
        window.addEventListener('resize', resize, { passive: true });

        const setToolheadTarget = (target) => {
          app.toolheadRig.position.x = target.x;
          app.toolheadRig.position.y = target.y;
          app.toolheadRig.position.z = target.z - app.toolheadRig.userData.nozzleOffsetZ;
        };

        const updatePrintPath = (progress) => {
          const clamped = Math.max(0, Math.min(0.99999, progress));
          const scaled = clamped * textTargets.length;
          const segmentIndex = Math.floor(scaled);
          const segmentProgress = scaled - segmentIndex;
          const from = segmentIndex === 0 ? primeEnd : textTargets[segmentIndex - 1];
          const to = textTargets[segmentIndex];
          moveBetween(THREE, app.toolheadRig, from, to, segmentProgress);

          layout.words.forEach((word, index) => {
            const wordProgress = clamped * layout.words.length - index;
            if (wordProgress <= 0) return;
            word.visible = true;
            word.scale.z = Math.min(1, wordProgress * 1.8);
          });
        };

        let frameId;
        const start = performance.now();
        const tick = (now) => {
          if (stopped) {
            if (frameId) cancelAnimationFrame(frameId);
            return;
          }

          const elapsed = now - start;
          if (elapsed < PRIME_DURATION) {
            const primeProgress = elapsed / PRIME_DURATION;
            setSegmentProgress(primeSegments[0], Math.min(1, primeProgress * 2));
            setSegmentProgress(primeSegments[1], Math.max(0, primeProgress * 2 - 1));
            setToolheadTarget(
              primeProgress < 0.5
                ? new THREE.Vector3(-108 + primeProgress * 2 * 44, -108, NOZZLE_Z)
                : new THREE.Vector3(-64, -108 + (primeProgress * 2 - 1) * 24, NOZZLE_Z),
            );
            updateStatus('Priming bed');
          } else if (elapsed < PRIME_DURATION + PRINT_DURATION) {
            const printProgress = (elapsed - PRIME_DURATION) / PRINT_DURATION;
            updatePrintPath(printProgress);
            updateStatus('Printing About page');
          } else {
            const postProgress = Math.min(1, (elapsed - PRIME_DURATION - PRINT_DURATION) / POST_PRINT_DURATION);
            if (postProgress < 0.23) {
              moveBetween(THREE, app.toolheadRig, finalTarget, parkTarget, postProgress / 0.23);
              updateStatus('Parking toolhead');
            } else if (postProgress < 0.48) {
              moveBetween(THREE, app.toolheadRig, parkTarget, homeXTarget, (postProgress - 0.23) / 0.25);
              updateStatus('Homing X axis');
            } else if (postProgress < 0.73) {
              moveBetween(THREE, app.toolheadRig, homeXTarget, homeYTarget, (postProgress - 0.48) / 0.25);
              updateStatus('Homing Y axis');
            } else if (postProgress < 0.88) {
              moveBetween(THREE, app.toolheadRig, homeYTarget, homeZTarget, (postProgress - 0.73) / 0.15);
              updateStatus('Homing Z axis');
            } else if (postProgress < 1) {
              moveBetween(THREE, app.toolheadRig, homeZTarget, finalParkTarget, (postProgress - 0.88) / 0.12);
              updateStatus('Parking toolhead');
            } else {
              setToolheadTarget(finalParkTarget);
              app.renderer.render(app.scene, app.camera);
              updateStatus('Ready');
              revealCopy();
              return;
            }
          }

          app.renderer.render(app.scene, app.camera);
          frameId = requestAnimationFrame(tick);
        };

        stopAnimation = () => {
          stopped = true;
          if (frameId) cancelAnimationFrame(frameId);
          app.renderer.render(app.scene, app.camera);
        };

        setToolheadTarget(new THREE.Vector3(-108, -108, NOZZLE_Z));
        frameId = requestAnimationFrame(tick);
      } catch (error) {
        revealCopy();
        updateStatus('Animation unavailable');
      }
    };

    run();
  }
}

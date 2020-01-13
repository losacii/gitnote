let scene, camera, renderer, cube;

function init() {
    // Scene, Camera, Renderer
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight );

    document.body.appendChild(renderer.domElement);

    camera.position.x = 2;
    camera.position.y = 3;
    camera.position.z = 20;

        // show axes in the screen
        var axes = new THREE.AxisHelper(9);
        scene.add(axes);


        // create a sphere
        sphereGeometry = new THREE.SphereGeometry(4, 10, 10);
        sphereMaterial = new THREE.MeshBasicMaterial({color: 0x7777ff, wireframe: true});
        sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
        // position the sphere
        sphere.position.x = 1;
        sphere.position.y = 4;
        sphere.position.z = 2;
        // add the sphere to the scene
        scene.add(sphere);

        camera.lookAt(scene.position);
}

var step = 0;
// Animate Function
function animate() {
    step += 0.01;
    if (step > 3.1416 * 2) {
        step = 0;
    }
    sphere.position.y = 9 * Math.cos(3 * step);
    sphere.position.z = -10 + 15 * Math.sin(step);
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

// Window Resize Handler, Event Listener
function onWindowResize() {  
    // update renderer
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}
window.addEventListener('resize', onWindowResize, false);

// main
init();
animate();


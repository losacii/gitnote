let scene, camera, renderer, cube;

function init() {
    // Scene, Camera, Renderer
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight );

    document.body.appendChild(renderer.domElement);

    camera.position.x = 2;
    camera.position.y = 1;
    camera.position.z = 9;

        // show axes in the screen
        var axes = new THREE.AxisHelper(9);
        scene.add(axes);

        // create the ground plane
        var planeGeometry = new THREE.PlaneGeometry(4, 6);
        var planeMaterial = new THREE.MeshBasicMaterial({color: 0x994545});
        var plane = new THREE.Mesh(planeGeometry, planeMaterial);
        // rotate and position the plane
        plane.rotation.x = -0.5 * Math.PI;
        plane.position.x = 2;
        plane.position.y = 0;
        plane.position.z = 3;
        // add the plane to the scene
        scene.add(plane);
}

// Animate Function
function animate() {
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


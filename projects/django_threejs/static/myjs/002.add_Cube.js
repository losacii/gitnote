let scene, camera, renderer, cube;

function init() {
    // Scene, Camera, Renderer
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight );

    document.body.appendChild(renderer.domElement);

    camera.position.x = 1;
    camera.position.y = 1;
    camera.position.z = 9;

        // show axes in the screen
        var axes = new THREE.AxisHelper(8);
        scene.add(axes);


        // create the ground plane
        var planeGeometry = new THREE.PlaneGeometry(15, 10);
        var planeMaterial = new THREE.MeshBasicMaterial({color: 0x56855e});
        var plane = new THREE.Mesh(planeGeometry, planeMaterial);
        // rotate and position the plane
        plane.rotation.x = -0.5 * Math.PI;
        plane.position.x = 0;
        plane.position.y = -1.3;
        plane.position.z = -2.9;
        // add the plane to the scene
        scene.add(plane);


        // create a cube
        cubeGeometry = new THREE.BoxGeometry(4, 4, 4);
        cubeMaterial = new THREE.MeshBasicMaterial({color: 0xffff00, wireframe: false});
        cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
        scene.add(cube);

}

// Animate Function
function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x = 0.1;
    cube.rotation.y += 0.01;
    cube.rotation.z = 0.1;
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


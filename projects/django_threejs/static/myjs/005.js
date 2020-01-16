let scene, camera, renderer, cube;

function init() {

    // -------------- Scene, Camera, Renderer -----------------
    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight );
    renderer.setClearColor(new THREE.Color(0x000000, 1.0));
    renderer.shadowMapEnabled = true;

    document.body.appendChild(renderer.domElement);

        // position and point the camera to the center of the scene
        camera.position.x = -30;
        camera.position.y = 50;
        camera.position.z = 30;
        camera.lookAt(scene.position);

    // --------------- show axes in the screen --------------------
    var axes = new THREE.AxisHelper(20);
    scene.add(axes);

    // 
    // ------------------ create the ground plane --------------------
    var planeGeometry = new THREE.PlaneGeometry(60, 20, 1, 1);
    var planeMaterial = new THREE.MeshLambertMaterial({color: 0xffffff});
    var plane = new THREE.Mesh(planeGeometry, planeMaterial);
    plane.receiveShadow = true;

    // rotate and position the plane
    plane.rotation.x = -0.5 * Math.PI;
    plane.position.x = 15;
    plane.position.y = 0;
    plane.position.z = 0;

    // add the plane to the scene
    scene.add(plane);

        // ------------------------ add something ----------------------------
        // create a cube
        cubeGeometry = new THREE.BoxGeometry(9, 9, 9);
        cubeMaterial = new THREE.MeshLambertMaterial({color: 0xff0000});
        cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
        cube.castShadow = true;

        // position the cube
        cube.position.x = -4;
        cube.position.y = 3;
        cube.position.z = 1;

        // add the cube to the scene
        scene.add(cube);


        // ------------ sphere -----------------------
        sphereGeometry = new THREE.SphereGeometry(4, 20, 20);
        sphereMaterial = new THREE.MeshLambertMaterial({color: 0x7777ff});
        sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

        // position the sphere
        sphere.position.x = 20;
        sphere.position.y = 0;
        sphere.position.z = 2;
        sphere.castShadow = true;

        // add the sphere to the scene
        scene.add(sphere);

        // ------------- add subtle ambient lighting -------------
        ambientLight = new THREE.AmbientLight(0x0c0c0c);
        scene.add(ambientLight);

        // ----------- add spotlight for the shadows -------------
        var spotLight = new THREE.SpotLight(0xffffff);
        spotLight.position.set(-40, 60, -10);
        spotLight.castShadow = true;
        scene.add(spotLight);
}


// Animate Function
var step = 0;
function animate() {

    step += 0.02;
    cube.rotation.x += 0.02;
    cube.rotation.y += 0.02;
    cube.rotation.z += 0.02;
    sphere.position.x = 20 + ( 25 * (Math.cos(step)));
    sphere.position.y = 2 + ( 10 * Math.abs(Math.sin(step)));

    camera.position.x = 30 * Math.cos(step / 5);
    camera.position.z = 30 * Math.sin(step / 4);
    camera.lookAt(scene.position);

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


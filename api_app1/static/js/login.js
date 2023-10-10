const loginBox = document.querySelector(".login");
const registBox = document.querySelector(".regist");

function toggleAnimation(box1, box2, callback) {
    box1.classList.remove('animate');
    box2.classList.remove('animate');

    setTimeout(() => {
        box1.classList.add('animate');
        box2.classList.add('animate');
        callback();

    }, 10);

}

document.getElementById("loginLink").addEventListener('click', () => {
    loginBox.style.animationDirection = 'normal';
    loginBox.style.zIndex = "0";
    registBox.style.zIndex = "1";
    registBox.style.animationDirection = 'reverse';

    toggleAnimation(registBox, loginBox, () => {
    });

});

document.getElementById("registLink").addEventListener('click', () => {
    registBox.style.animationDirection = 'normal';
    loginBox.style.zIndex = "1";
    registBox.style.zIndex = "0";
    loginBox.style.animationDirection = 'reverse';
    loginBox.style.transform = "rotate(0deg)";
    registBox.style.transform = "rotate(-5deg)";

    toggleAnimation(registBox, loginBox, () => {
        registBox.style.transform = "rotate(0deg)";
        loginBox.style.transform = "rotate(5deg)";
    });


});

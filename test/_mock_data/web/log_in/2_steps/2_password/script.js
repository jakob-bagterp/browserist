function verifyPassword(password) {
    return password === 'password123';
}

function getFormInputPassword() {
    return document.getElementById('password').value;
}

function loginFlowStep2Controller() {
    var password = getFormInputPassword();
    var isValidPassword = verifyPassword(password);
    if (isValidPassword) {
        window.location.href = './../../homepage.html';
    } else {
        window.location.href = './../../error.html';
    }
}

document.getElementById('login-form').addEventListener('submit', function (event) {
    event.preventDefault();
    loginFlowStep2Controller();
});

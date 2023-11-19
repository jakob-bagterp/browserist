function verifyUsername(username) {
    return username === 'johndoe';
}

function getFormInputUsername() {
    return document.getElementById('username').value;
}

function loginFlowStep1Controller() {
    var username = getFormInputUsername();
    var isValidUsername = verifyUsername(username);
    if (isValidUsername) {
        window.location.href = './../2_password/login_form.html';
    } else {
        window.location.href = './../../error.html';
    }
}

document.getElementById('login-form').addEventListener('submit', function (event) {
    event.preventDefault();
    loginFlowStep1Controller();
});

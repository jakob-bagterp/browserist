function verifyLogin(username, password) {
    const usernameTest = 'johndoe';
    const passwordTest = 'password123';

    return username === usernameTest && passwordTest === password;
}

function getFormInputUsername() {
    return document.getElementById('username').value;
}

function getFormInputPassword() {
    return document.getElementById('password').value;
}

function loginFlow() {
    var username = getFormInputUsername();
    var password = getFormInputPassword();
    var isValidLogin = verifyLogin(username, password);
    if (isValidLogin) {
        window.location.href = './../homepage.html';
    } else {
        window.location.href = './../error.html';
    }
}

document.getElementById('login-form').addEventListener('submit', function (event) {
    event.preventDefault();
    loginFlow();
});

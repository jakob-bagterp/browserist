const cookieBanner = document.getElementById('cookie-banner');
const acceptCookiesButton = document.getElementById('accept-cookies');
const declineCookiesButton = document.getElementById('decline-cookies');

const hasAcceptedCookies = false; // Dynamic variation instead of false: localStorage.getItem('acceptedCookies');
const hasDeclinedCookies = false; // Dynamic variation instead of false: localStorage.getItem('declinedCookies');

if (!hasAcceptedCookies && !hasDeclinedCookies) {
    // Show the cookie banner if no choice has been made:
    cookieBanner.style.display = 'block';

    acceptCookiesButton.addEventListener('click', () => {
        // Dynamic variation: localStorage.setItem('acceptedCookies', 'true');
        cookieBanner.style.display = 'none';
    });

    declineCookiesButton.addEventListener('click', () => {
        // Dynamic variation: localStorage.setItem('declinedCookies', 'true');
        cookieBanner.style.display = 'none';
    });
}

// js/auth.js

// --- Login Page Logic ---
// This part of the script runs only on login.html
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form from submitting the traditional way

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const errorMessage = document.getElementById('errorMessage');

        // Check credentials
        if (username === 'admin' && password === 'admin123') {
            // On successful login, set a flag in sessionStorage
            sessionStorage.setItem('isLoggedIn', 'true');
            // Redirect to the main page
            window.location.href = 'index.html';
        } else {
            // On failed login, show an error message
            errorMessage.style.display = 'block';
        }
    });
}

// --- Protected Page Logic ---
// This function will be called from all other pages to check for authentication
function checkAuth() {
    const isLoggedIn = sessionStorage.getItem('isLoggedIn');
    // If the user is not logged in, redirect them to the login page
    // The check `!window.location.pathname.endsWith('login.html')` prevents a redirect loop
    if (isLoggedIn !== 'true' && !window.location.pathname.endsWith('login.html')) {
        window.location.href = 'login.html';
    }
}

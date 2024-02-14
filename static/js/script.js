//Collapse navbar function

function collapseNavbar() {
    const togglebar = document.querySelector('.togglebar')
    togglebar.style.display = 'flex'
}

function hideNavbar() {
    const togglebar = document.querySelector('.togglebar')
    togglebar.style.display = 'none'
}

// Function to update and display the current year
function updateYear() {
    const now = new Date();
    const year = now.getFullYear();
    document.getElementById('year').innerText = year;
}
updateYear();
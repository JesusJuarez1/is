document.addEventListener('DOMContentLoaded', function() {
    var userDropdownDesktop = document.getElementById('userDropdownDesktop');
    var userDropdownMobile = document.getElementById('userDropdownMobile');
    
    if (userDropdownDesktop) {
        userDropdownDesktop.addEventListener('click', function() {
            var arrow = userDropdownDesktop.querySelector('.arrow');
            
            if (arrow) {
                if (arrow.classList.contains('fa-chevron-down')) {
                    arrow.classList.remove('fa-chevron-down');
                    arrow.classList.add('fa-chevron-up');
                } else {
                    arrow.classList.remove('fa-chevron-up');
                    arrow.classList.add('fa-chevron-down');
                }
            }

            var adminButton = document.getElementById('adminButton');
            var logoutButton = document.getElementById('logoutButton');
            
            if (adminButton && logoutButton) {
                var adminButtonDisplay = window.getComputedStyle(adminButton).getPropertyValue('display');
                var logoutButtonDisplay = window.getComputedStyle(logoutButton).getPropertyValue('display');
                
                adminButton.style.display = adminButtonDisplay === 'none' ? 'block' : 'none';
                logoutButton.style.display = logoutButtonDisplay === 'none' ? 'block' : 'none';
            }
        });
    }

    if (userDropdownMobile) {
        userDropdownMobile.addEventListener('click', function() {
            var arrow = userDropdownMobile.querySelector('.arrow');
            
            if (arrow) {
                if (arrow.classList.contains('fa-chevron-down')) {
                    arrow.classList.remove('fa-chevron-down');
                    arrow.classList.add('fa-chevron-up');
                } else {
                    arrow.classList.remove('fa-chevron-up');
                    arrow.classList.add('fa-chevron-down');
                }
            }

            var adminButton = document.getElementById('adminButton-mobile');
            var logoutButton = document.getElementById('logoutButton-mobile');
            
            if (adminButton && logoutButton) {
                var adminButtonDisplay = window.getComputedStyle(adminButton).getPropertyValue('display');
                var logoutButtonDisplay = window.getComputedStyle(logoutButton).getPropertyValue('display');
                
                adminButton.style.display = adminButtonDisplay === 'none' ? 'block' : 'none';
                logoutButton.style.display = logoutButtonDisplay === 'none' ? 'block' : 'none';
            }
        });
    }
});

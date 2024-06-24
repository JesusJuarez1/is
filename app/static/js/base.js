function openNav() {
    document.getElementById("mySidenav").style.width = "70%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0%";
}

const btnToggle = document.querySelector('.toggle-btn');

btnToggle.addEventListener('click', function () {
  var sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('active');
  var menu = sidebar.querySelector('.menu');
  if(menu){
    if (menu.classList.contains('fa-bars')) {
      menu.classList.remove('fa-bars');
      menu.classList.add('fa-times');
    } else {
      menu.classList.remove('fa-times');
      menu.classList.add('fa-bars');
    }
  }
});
// DARK MODE
const darkModeBtn = document.getElementById('dark-mode-btn');

darkModeBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});

// PARA MINIMIZAR EL SIDEBAR
const sideBar = document.getElementById('sidebar');
const menuBtn = document.getElementById('menu-btn');
const sidebarBtn = document.getElementById('sidebar-btn');

menuBtn.addEventListener('click', () => {
  sideBar.classList.toggle('minimize');
});

sidebarBtn.addEventListener('click', () => {
  document.body.classList.toggle('sidebar-hidden');
});

// MENUS DESPLEGABLES DEL SLIDEBAR
const menusItemsDropDoqwn = document.querySelectorAll('.menu-item-dropdown');
const menusItemStatic = document.querySelectorAll('.menu-item-static');

menusItemsDropDoqwn.forEach((menuItem) => {
  menuItem.addEventListener('click', () => {
    const subMenu = menuItem.querySelector('.sub-menu');
    const isActive = menuItem.classList.toggle('sub-menu-toggle');
    if (subMenu) {
      if (isActive) {
        subMenu.style.height = `${subMenu.scrollHeight + 6}px`;
        subMenu.style.padding = '0.2rem 0';
      } else {
        subMenu.style.height = '0';
        subMenu.style.padding = '0';
      }
    }
    menusItemsDropDoqwn.forEach((item) => {
      if (item !== menuItem) {
        const otherSubmenu = item.querySelector('.sub-menu');
        if (otherSubmenu) {
          item.classList.remove('sub-menu-toggle');
          otherSubmenu.style.height = '0';
          otherSubmenu.style.padding = '0';
        }
      }
    });
  });
});

menusItemStatic.forEach((menuItem) => {
  menuItem.addEventListener('mouseenter', () => {
    if (!sideBar.classList.contains('minimize')) return;

    menusItemsDropDoqwn.forEach((item) => {
      const otherSubmenu = item.querySelector('.sub-menu');
      if (otherSubmenu) {
        item.classList.remove('sub-menu-toggle');
        otherSubmenu.style.height = '0';
        otherSubmenu.style.padding = '0';
      }
    });
  });
});

function checkWindowsSize() {
  sideBar.classList.remove('minimize');
}
checkWindowsSize();
window.addEventListener('resize', checkWindowsSize);

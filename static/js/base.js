document.addEventListener('DOMContentLoaded', () => {
  // Toggles
  const $toggles = document.querySelectorAll('.js-toggle');
  $toggles.forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const target = el.dataset.target;
      const $target = document.getElementById(target);
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');
    });
  });

  //Temas
  const STORAGE_KEY = 'sys-theme';
  const DEFAULT_THEME = 'light';

  const state = {
    chosenTheme: null,
    appliedTheme: DEFAULT_THEME,
    OSTheme: null,
  };

  const $theme_Cycle = document.getElementById('js-cycle');
  const $theme_Switchers = document.querySelectorAll('.js-themes button');

  const updateThemeUI = () => {
    if (state.appliedTheme === 'light') {
      $theme_Cycle.className = 'opt-cycle js-burger is-sun';
    } else {
      $theme_Cycle.className = 'opt-cycle js-burger is-moon';
    }

    $theme_Switchers.forEach((el) => {
      const swatchTheme = el.dataset.scheme;

      if (state.chosenTheme === swatchTheme) {
        el.classList.add('is-active');
      } else {
        el.classList.remove('is-active');
      }
    });
  };

  const setTheme = (theme, save = true) => {
    state.chosenTheme = theme;
    state.appliedTheme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    if (save) {
      window.localStorage.setItem(STORAGE_KEY, theme);
    }

    updateThemeUI();
  };

  const localTheme = window.localStorage.getItem(STORAGE_KEY);
  state.OSTheme = DEFAULT_THEME;

  if (localTheme) {
    setTheme(localTheme, false);
  } else {
    setTheme(DEFAULT_THEME);
  }

  //Event Listeners
  $theme_Switchers.forEach((el) => {
    el.addEventListener('click', () => {
      const theme = el.dataset.scheme;
      setTheme(theme);
    });
  });

  window
    .matchMedia('(prefers-color-scheme: dark)')
    .addEventListener('change', (event) => {
      const theme = event.matches ? 'dark' : 'light';
      state.OSTheme = theme;
      setTheme(theme);
    });

  // Burgers
  const $burgers = document.querySelectorAll('.js-burger');

  $burgers.forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const targetID = el.dataset.target;
      const $target = document.getElementById(targetID);
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');
      e.stopPropagation();
    });
  });

  const onClickOutside = (menuSelector) => {
    document.addEventListener('click', (e) => {
      const menus = document.querySelectorAll(menuSelector);

      menus.forEach((el) => {
        if (!el.contains(e.target) && el.classList.contains('is-active')) {
          el.classList.remove('is-active');
        }
      });
    });
  };

  onClickOutside('.js-menu');
});

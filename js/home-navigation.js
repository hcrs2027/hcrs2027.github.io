(function () {
    'use strict';

    var navigation = document.querySelector('.page-toc');
    if (!navigation) return;

    var toggle = navigation.querySelector('.page-toc__toggle');
    var links = Array.from(navigation.querySelectorAll('a[href^="#"]'));
    var sections = links.map(function (link) {
        return document.getElementById(link.hash.slice(1));
    });
    var desktop = window.matchMedia('(min-width: 1200px)');
    var scheduled = false;

    document.documentElement.classList.add('has-home-navigation');
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
        toggle.setAttribute('aria-expanded', toggle.getAttribute('aria-expanded') !== 'true');
    });

    links.forEach(function (link) {
        link.addEventListener('click', function () {
            toggle.setAttribute('aria-expanded', 'false');
        });
    });

    navigation.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !desktop.matches && toggle.getAttribute('aria-expanded') === 'true') {
            toggle.setAttribute('aria-expanded', 'false');
            toggle.focus();
        }
    });

    function updateCurrentSection() {
        scheduled = false;
        var current = 0;
        sections.forEach(function (section, index) {
            if (section.getBoundingClientRect().top <= 120) current = index;
        });
        links.forEach(function (link, index) {
            if (index === current) link.setAttribute('aria-current', 'location');
            else link.removeAttribute('aria-current');
        });
    }

    function scheduleUpdate() {
        if (scheduled) return;
        scheduled = true;
        window.requestAnimationFrame(updateCurrentSection);
    }

    window.addEventListener('scroll', scheduleUpdate, { passive: true });
    window.addEventListener('resize', scheduleUpdate);
    window.addEventListener('hashchange', scheduleUpdate);
    window.addEventListener('load', scheduleUpdate);
    desktop.addEventListener('change', function () {
        toggle.setAttribute('aria-expanded', 'false');
        scheduleUpdate();
    });
    updateCurrentSection();
}());

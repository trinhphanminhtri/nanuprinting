$(document).ready(function () {
    $('.partners-carousel').owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        autoplay: true,
        autoplayTimeout: 800,
        dots: false,
        responsive: {
            0: { items: 3 },
            600: { items: 6 },
            1000: { items: 8 }
        }
    });
});
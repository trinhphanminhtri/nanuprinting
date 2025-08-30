$(document).ready(function () {
    $('.partners-carousel').owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        autoplay: true,
        autoplayTimeout: 2000,
        dots: false,
        responsive: {
            0: { items: 2 },
            600: { items: 4 },
            1000: { items: 6 }
        }
    });
});
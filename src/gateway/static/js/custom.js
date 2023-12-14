
  (function ($) {
  
  "use strict";

    // // PRE LOADER
    // $(window).load(function(){
    //   $('.preloader').delay(50).slideUp('fast'); // set duration in brackets    
    // });

    // PRE LOADER
    $(window).load(function(){
      $('.preloader').delay(1).fadeOut('fast'); // Remove slideUp and use fadeOut
    });


    // NAVBAR
    $(".navbar").headroom();

    $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    $('.slick-slideshow').slick({
      autoplay: true,
      infinite: true,
      arrows: false,
      fade: true,
      dots: true,
    });

    $('.slick-testimonial').slick({
      arrows: false,
      dots: true,
    });
    
  })(window.jQuery);


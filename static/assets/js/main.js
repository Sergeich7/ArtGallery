(function ($) {
    "use strict";

    /*----------------------------------------
	   Sticky Menu Activation
	---------------------------------*/
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 350) {
			$('.header-sticky').addClass('sticky');
		} else {
			$('.header-sticky').removeClass('sticky');
		}
	});
	/*----------------------------------------
		Off Canvas Mobile Menu
	-------------------------------------------*/
	$(".mobile-menu-bar").on('click', function () {
		$("body").addClass('fix');
		$(".mobile-menu-wrapper").addClass('open');
	});

	$(".btn-close-bar,.body-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".mobile-menu-wrapper").removeClass('open');
	});
	/*----------------------------------------
		Off Canvas Search
	-------------------------------------------*/
	$(".header-search-icon").on('click', function () {
		$("body").addClass('fix');
		$(".offcanvas-search").addClass('open');
	});

	$(".btn-close-bar,.body-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".offcanvas-search").removeClass('open');
	});
    /*----------------------------------------
		Responsive Mobile Menu
	------------------------------------------*/
	//Variables
	var $offCanvasNav = $('.mobile-menu'),
	$offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');

	//Close Off Canvas Sub Menu
	$offCanvasNavSubMenu.slideUp();

	//Category Sub Menu Toggle
	$offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
	var $this = $(this);
		if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
			e.preventDefault();
			if ($this.siblings('ul:visible').length){
				$this.parent('li').removeClass('active');
				$this.siblings('ul').slideUp();
			} else {
				$this.parent('li').addClass('active');
				$this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
				$this.closest('li').siblings('li').find('ul:visible').slideUp();
				$this.siblings('ul').slideDown();
			}
		}
	});

	/*----------------------------------------
		Swiper Slider Activation
	------------------------------------------*/
    /*-- Home Slider --*/
    var introSlider = new Swiper('.hero-slider', {
        loop: true,
        speed: 750,
        spaceBetween: 30,
        slidesPerView: 1,
		effect: 'slide',
		parallax: true,
        navigation: {
            nextEl: '.home-slider-next',
            prevEl: '.home-slider-prev',
		},
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		},
        //autoplay: {},
	});

	/*-- Testimonial --*/
	var testimonialCarousel = new Swiper('.testimonial-carousel .swiper-container', {
		loop: true,
		speed: 750,
		spaceBetween: 30,
		slidesPerView: 2,
		effect: 'slide',
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		},
		//autoplay: {},

		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			slidesPerView: 1,
			spaceBetween: 20
			},
			// when window width is >= 767px
			768: {
			slidesPerView: 2,
			spaceBetween: 30
			}
		}
	});

	/*-- Brand Logo --*/
	var brandCarousel = new Swiper('.brand-logo-carousel .swiper-container', {
		loop: true,
		speed: 750,
		spaceBetween: 30,
		slidesPerView: 5,
		effect: 'slide',
		//autoplay: {},

		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
			slidesPerView: 2,
			spaceBetween: 20
			},
			// when window width is >= 480px
			480: {
			slidesPerView: 3,
			spaceBetween: 30
			},
			// when window width is >= 768px
			768: {
			slidesPerView: 4,
			spaceBetween: 30
			},
			// when window width is >= 992px
			992: {
			slidesPerView: 5,
			spaceBetween: 30
			}
		}
	});

	/*-- Project carousel --*/

	var projectCarousel = new Swiper('.project-carousel .swiper-container', {
        loop: true,
        slidesPerView: 4,
		spaceBetween: 30,
		observer: true,
		observeParents: true,			
		autoHeight: true,
		setWrapperSize: true,

        pagination: {
            el: '.project-carousel .swiper-pagination',
        },

        // Navigation arrows
        navigation: {
            nextEl: '.project-carousel .swiper-button-next',
            prevEl: '.project-carousel .swiper-button-prev',
		},		
		
		// Responsive breakpoints
		breakpoints: {
			// when window width is >= 320px
			320: {
				slidesPerView: 1,
				spaceBetween: 20
			},
			// when window width is >= 480px
			575: {
				slidesPerView: 2,
				spaceBetween: 30
			},
			// when window width is >= 768px
			768: {
				slidesPerView: 2,
				spaceBetween: 30
			},
			// when window width is >= 992px
			992: {
				slidesPerView: 3,
				spaceBetween: 30
			},
			// when window width is >= 1200px
			1200: {
				slidesPerView: 4,
				spaceBetween: 30
			},
		}
	});

	
	/* ----------------------------
        Portfolio Masonry Activation
    -------------------------------*/
    $(window).on('load', function () {
		// filter items on button click
		$('.project-tab').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$(this).siblings('.is-checked').removeClass('is-checked');
			$(this).addClass('is-checked');
			$grid.isotope({
				filter: filterValue
			});
		});

		// init Isotope
		var $grid = $('.mesonry-list').isotope({
			percentPosition: true,
			transitionDuration: '0.7s',
			layoutMode: 'masonry',
			masonry: {
				columnWidth: '.resizer',
			}
		});
	})

	/* ----------------------------
		Odometer Activation 
    -------------------------------*/
	if( $('.odometer').length ){

		var elemOffset = $('.odometer').offset().top;
		var winHeight = $(window).height();
		if(elemOffset < winHeight){
			$('.odometer').each(function(){
				$(this).html($(this).data('count-to'));
			});
		}
		$(window).on('scroll', function(){
			var elemOffset = $('.odometer').offset().top;
			function winScrollPosition() {
				var scrollPos = $(window).scrollTop(),
					winHeight = $(window).height();
				var scrollPosition = Math.round(scrollPos + (winHeight / 1.2));
				return scrollPosition;
			}
			if ( elemOffset < winScrollPosition()) {
				$('.odometer').each(function(){
					$(this).html($(this).data('count-to'));
				});
			}	
		});
	};
	
	/*----------------------------------------
		Aos Activation Js
	------------------------------------------*/
	$(window).on('scroll', function(){
		AOS.init({
			duration: 1200, // values from 0 to 3000, with step 50ms
			disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
			offset: 30, // offset (in px) from the original trigger point
			once: true,
			easing: 'ease',
		  });
	});

	AOS.init({
		duration: 1200, // values from 0 to 3000, with step 50ms
		disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
		offset: 30, // offset (in px) from the original trigger point
		once: true,
		easing: 'ease',
	});

	/*---------------------------------
        Scroll Up
    -----------------------------------*/
    function scrollToTop() {
        var $scrollUp = $('#scroll-top'),
            $lastScrollTop = 0,
            $window = $(window);

        $window.on('scroll', function () {
            var st = $(this).scrollTop();
            if (st > $lastScrollTop) {
                $scrollUp.removeClass('show');
            } else {
                if ($window.scrollTop() > 200) {
                    $scrollUp.addClass('show');
                } else {
                    $scrollUp.removeClass('show');
                }
            }
            $lastScrollTop = st;
        });

        $scrollUp.on('click', function (evt) {
            $('html, body').animate({scrollTop: 0}, 600);
            evt.preventDefault();
        });
    }
	scrollToTop();


	/*---------------------------------
	 	MailChimp
    -----------------------------------*/
    $('#mc-form').ajaxChimp({
        language: 'en',
        callback: mailChimpResponse,
        // ADD YOUR MAILCHIMP URL BELOW HERE!
        url: 'http://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef'
    });
    function mailChimpResponse(resp) {
        if (resp.result === 'success') {
            $('.mailchimp-success').html('' + resp.msg).fadeIn(900);
            $('.mailchimp-error').fadeOut(400);
        } else if (resp.result === 'error') {
            $('.mailchimp-error').html('' + resp.msg).fadeIn(900);
        }
	}
	/*-------------------------
        Ajax Contact Form 
    ---------------------------*/
    $(function() {

        // Get the form.
        var form = $('#contact-form');

        // Get the messages div.
        var formMessages = $('.form-messege');

        // Set up an event listener for the contact form.
        $(form).submit(function(e) {
            // Stop the browser from submitting the form.
            e.preventDefault();

            // Serialize the form data.
            var formData = $(form).serialize();

            // Submit the form using AJAX.
            $.ajax({
                type: 'POST',
                url: $(form).attr('action'),
                data: formData
            })
            .done(function(response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text(response);

                // Clear the form.
                $('#contact-form input,#contact-form textarea').val('');
            })
            .fail(function(data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            });
        });

    });
	

})(jQuery);


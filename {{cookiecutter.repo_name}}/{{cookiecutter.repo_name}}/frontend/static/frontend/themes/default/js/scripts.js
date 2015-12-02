$(document).ready(function() {

    /******************* Waypoints *******************/

    $(".wp1").waypoint(function() {
        $(".wp1").addClass("animated fadeInLeft");
    }, {
        offset: "75%"
    });
    $(".wp2").waypoint(function() {
        $(".wp2").addClass("animated fadeInUp");
    }, {
        offset: "75%"
    });
    $(".wp3").waypoint(function() {
        $(".wp3").addClass("animated fadeInDown");
    }, {
        offset: "55%"
    });
    $(".wp4").waypoint(function() {
        $(".wp4").addClass("animated fadeInDown");
    }, {
        offset: "75%"
    });
    $(".wp5").waypoint(function() {
        $(".wp5").addClass("animated fadeInUp");
    }, {
        offset: "75%"
    });
    $(".wp6").waypoint(function() {
        $(".wp6").addClass("animated fadeInDown");
    }, {
        offset: "75%"
    });

    /***************** Slide-In Nav ******************/

    $(".nav_slide_button").on("click", function(e) {
        e.preventDefault();
        $(".pull").slideToggle();
    });

    /*************** Smooth Scrolling ****************/

    var scroll_to_top = true;

    $("a[href*=#]:not([href=#])").on("click", function(e) {
        if (location.pathname.replace(/^\//, "") === this.pathname.replace(/^\//, "") && location.hostname === this.hostname) {
            var that = this;
            var target = $(this.hash);
            target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                e.preventDefault();
                $("html, body").animate({
                    scrollTop: target.offset().top
                }, 2000, function() {
                    scroll_to_top = true;
                    $(".nav li > a").removeClass("active");
                    $(".nav li > a[href='/" + that.hash + "']").addClass("active");
                });
            }
        }
    });

    /******************* Go to top *******************/


    if ($("#back-top").length) {

        // Updates menu and shows/hides Go to top button

        function update_menu(window_cur) {
            var window_with_nav_top = $(window_cur).scrollTop() + $("#navbar").height();
            $("section").each(function(i, el) {
                var $el = $(el);
                var el_top = $el.position().top;
                var el_bottom = el_top + $el.height();
                var el_id = $el.attr("id");
                // Detect which section user is seeing
                if (window_with_nav_top >= el_top && window_with_nav_top < el_bottom) {
                    $(".nav li > a[href='/#" + el_id + "']").addClass("active");
                    // TODO: setHashSilently(el_id);
                } else {
                    $(".nav li > a[href='/#" + el_id + "']").removeClass("active");
                }
            });
        }

        // Handle window scrolling (with throttling)

        function update_and_fade(window_cur) {
            // update menu
            if (scroll_to_top) {
                update_menu(window_cur);
            }
            // fade button
            if ($(window_cur).scrollTop() > 100) {
                $("#back-top").fadeIn("slow");
            } else {
                $("#back-top").fadeOut("fast");
                scroll_to_top = false;
            }
        }

        var time_to_go;
        $(window).on("scroll", function() {
            clearTimeout(time_to_go);
            time_to_go = setTimeout(function() {
                update_and_fade(this);
            }, 50);
        });

        // Handle Go to top clicks

        $("#back-top").on("click", function(e) {
            e.preventDefault();
            $("html, body").animate({scrollTop: 0}, 800);
            $(".nav li > a").removeClass("active");
        });

    }

    /******************* Overlays ********************/

    if (Modernizr.touch) {
        // show the close overlay button
        $(".close-overlay").removeClass("hidden");
        // handle the adding of hover class when clicked
        $(".img").on("click", function(e) {
            if (!$(this).hasClass("hover")) {
                $(this).addClass("hover");
            }
        });
        // handle the closing of the overlay
        $(".close-overlay").on("click", function(e){
            e.preventDefault();
            e.stopPropagation();
            if ($(this).closest(".img").hasClass("hover")) {
                $(this).closest(".img").removeClass("hover");
            }
        });
    } else {
        // handle the mouse enter/leave functionality
        $(".img").on("mouseenter", function() {
            $(this).addClass("hover");
        }).on("mouseleave", function() {
            $(this).removeClass("hover");
        });
    }

    /*************** Nav Transformicon ***************/

    // document.querySelector("#nav-toggle").addEventListener("click", function() {
    //  this.classList.toggle("active");
    // });

});

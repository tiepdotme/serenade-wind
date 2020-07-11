$(document).ready(function() {
  // main menu toggle
  var toggleButton = document.getElementById("menu-toggle");
  var menu = document.getElementById("primary-nav");

  if (toggleButton && menu) {
    toggleButton.addEventListener("click", function() {
      menu.classList.toggle("js-menu-is-open");
    });
  }

  // initialize smooth scroll
  $("a").smoothScroll({ offset: -20 });

  // add lightbox class to all image links
  $("a[href$='.jpg'], a[href$='.png'], a[href$='.gif']").attr("data-lity", "");

  var glideOptions = {
    // Mobile-first defaults
    slidesToShow: 1,
    slidesToScroll: 1,
    scrollLock: true,
    dots: '.dots',
    arrows: {
      prev: '.glider-prev',
      next: '.glider-next'
    },
    responsive: [
      {
        // screens greater than >= 775px
        breakpoint: 775,
        settings: {
          // Set to `auto` and provide item width to adjust to viewport
          slidesToShow: 'auto',
          slidesToScroll: 'auto',
          itemWidth: 250,
          duration: 0.25
        }
      },{
        // screens greater than >= 1024px
        breakpoint: 1024,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 1,
          itemWidth: 150,
          duration: 0.25
        }
      }
    ]
  };
  //check to see if the page has a gallery
  var gal = document.querySelectorAll(".gallery-slider");
  var galNums = gal.length;
  if(galNums > 0){
    var i=0, galleryId;
    for(;i < galNums;i++){
      galleryId = gal[i].classList[1];
      glideOptions.dots = ".dots-" + galleryId;
      glideOptions.arrows.prev = ".prev-" + galleryId;
      glideOptions.arrows.next = ".next-" + galleryId;
      new Glider(document.querySelector('.' + galleryId), glideOptions);
    }
  }
});


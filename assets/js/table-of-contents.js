function isScrolledIntoView(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}



let mainTocLinks = document.querySelectorAll("#markdown-toc li a");
let mainSections = document.querySelectorAll(".e-content h1, .e-content h2, .e-content h3, .e-content h4, .e-content h5, .e-content h6");
let tocMenu = document.getElementById("markdown-toc");
let tocWrapper = document.getElementsByClassName("toc-wrapper");
let isMobile = false;

if($(".toc-wrapper").css("display") !== 'none'){
    isMobile = true;
}
console.log(isMobile);

var elmTop = function(elem){
    var rect = elem.getBoundingClientRect();
    var win = elem.ownerDocument.defaultView;

    return rect.top;// + win.pageYOffset;
}

var outerPane = $("#primary-nav"),
    didScroll = false;

$(window).scroll(function() {
    didScroll = true;
});

setInterval(function() {
    if ( didScroll && isMobile === false ) {
        didScroll = false;

        let postHeaderTop = $(".page-header").offset().top;
        let windowTop = $(window).scrollTop();
        let myOffset = 10;
        if(postHeaderTop < (windowTop + myOffset)) {
            $(".toc-wrapper").css("display", "inline-block");
        } else {
            $(".toc-wrapper").css("display", "none");
        }
        // Check your page position and then
        // Load in more results
      let fromTop = window.scrollY;

        mainTocLinks.forEach(link => {
            let section = document.getElementById(link.hash.substring(1));
            
            
            if(isScrolledIntoView(section)) {
//             if ( section.offsetTop <= fromTop && section.offsetTop + section.offsetHeight > fromTop ) {
                link.classList.add("current");
            } else {
                link.classList.remove("current");
            }        
        });
    }    
}, 250);
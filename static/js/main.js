$(document).ready(function () {
  // Page scrolling function for the nav-links
  $(".nav-link").click(function () {
    $('html,body').animate({ scrollTop: $(this.hash).offset().top - 80 }, 1400);
    return false;
  });

  // Back to Top Link
  $(".top-link").click(function () {
    $('html,body').animate({ scrollTop: $("#topSection").offset().top }, 2000);
    return false;
  });

  // Function to change the nav-bar on scroll
  $(window).scroll(function () {
    $(window).scrollTop() >= 110 ?
    $('.nav-bar').addClass('scrolled') :
    $('.nav-bar').removeClass('scrolled');
  });

  const cards = document.getElementsByClassName("card");
  for (let card of cards) {
    card.addEventListener("click", () => {
      if (!card.classList.contains("active")) {
        for (let c of cards) {
          c.classList.remove("active");
          card.classList.add("active");
        }
      }
    });
  }
});



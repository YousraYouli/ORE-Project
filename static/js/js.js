let navbar = document.querySelector(".header .navbar");
// menu bnt active when we use phone mode

document.querySelector("#menu-btn").onclick = () => {
  navbar.classList.add("active");
};

document.querySelector("#close-navbar").onclick = () => {
  navbar.classList.remove("active");
};

let acountform = document.querySelector(".account-form");
//  swiper user reviews

var swiper = new Swiper(".reviews-slider", {
  loop: true,
  grabCursor: true,
  spaceBetween: 20,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    991: {
      slidesPerView: 3,
    },
  },
});

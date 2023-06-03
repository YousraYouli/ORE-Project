const editor = document.getElementById("editor");
const run = document.getElementById("run");
const result = document.getElementById("result");

run.addEventListener("click", () => {
  fetch("/execute", {
    method: "POST",
    body: JSON.stringify({ code: editor.value }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => res.json())
    .then((res) => (result.innerHTML = res.output));
});

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

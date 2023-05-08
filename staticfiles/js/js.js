let navbar = document.querySelector('.header .navbar')
// menu bnt active when we use phone mode

document.querySelector('#menu-btn').onclick = () => {
     navbar.classList.add('active');
}
    
document.querySelector('#close-navbar').onclick = () => {
        navbar.classList.remove('active');
}
// login and register btn

let registerBtn = document.querySelector('.account-form .register-btn');
let loginBtn = document.querySelector('.account-form .login-btn');

registerBtn.onclick = () =>{
    registerBtn.classList.add('active'); 
    loginBtn.classList.remove('active');
    document.querySelector('.account-form .login-form').classList.remove('active');
    document.querySelector('.account-form .register-form').classList.add('active');
}

loginBtn.onclick = () =>{
    registerBtn.classList.remove('active'); 
    loginBtn.classList.add('active');
    document.querySelector('.account-form .login-form').classList.add('active');
    document.querySelector('.account-form .register-form').classList.remove('active');
}

let acountform = document.querySelector('.account-form')
// menu bnt active when we use phone mode

document.querySelector('#account-btn').onclick = () => {
    acountform.classList.add('active');
}
    
document.querySelector('#close-form').onclick = () => {
    acountform.classList.remove('active');
}

// swiper home courses

var swiper = new Swiper(".home-cours-slider", {
    
    loop:true,
    grabCursor:true,
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
//  swiper user reviews 

var swiper = new Swiper(".reviews-slider", {
    
    loop:true,
    grabCursor:true,
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
    
// Menu

document.getElementById("menu-button").addEventListener("click", function () {
  var menu = document.getElementById("menu");
  var bars = document.getElementsByClassName("menu-icon");

  if (menu.style.display === "none" || menu.style.display === "") {
    menu.style.display = "block";
    bars[0].style.transform = "rotate(-45deg) translate(-5px, 6px)";
    bars[1].style.opacity = "0";
    bars[2].style.transform = "rotate(45deg) translate(-5px, -6px)";
  } else {
    menu.style.display = "none";
    bars[0].style.transform = "rotate(0)";
    bars[1].style.opacity = "1";
    bars[2].style.transform = "rotate(0)";
  }
});

// Slide show

let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.getElementsByClassName("slides");

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slideIndex++;

  if (slideIndex > slides.length) {
    slideIndex = 1;
  }

  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 20000);
}

// Feed column

const scrollingList = document.querySelector('.feed ul');

function stopAutoScroll() {
  scrollingList.style.animationPlayState = 'paused'; // Pause the animation on mouseover
}

function startAutoScroll() {
  scrollingList.style.animationPlayState = 'running'; // Resume the animation on mouseleave
}

scrollingList.addEventListener('mouseenter', stopAutoScroll);
scrollingList.addEventListener('mouseleave', startAutoScroll);

// Music Button

document.getElementById("music-button").addEventListener("click", function () {
  var iframe = document.querySelector("#sptfy-player iframe");
  iframe.contentWindow.postMessage({ command: 'toggle' }, '*');
});

// Bulba Chat

document.addEventListener("DOMContentLoaded", function() {
  const paragraph = document.getElementById("typed-text");
  const textToType = "What do you get when you cross Pikachu with porn? Pikascrew.";

  let currentIndex = 0;
  const typingSpeed = 80;

  function typeText() {
      if (currentIndex < textToType.length) {
          paragraph.textContent += textToType.charAt(currentIndex);
          currentIndex++;
          setTimeout(typeText, typingSpeed);
      }
  }

  typeText();
});
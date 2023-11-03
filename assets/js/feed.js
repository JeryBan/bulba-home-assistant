const scrollingList = document.querySelector('.feed-container');

function stopAutoScroll() {
  scrollingList.style.animationPlayState = 'paused'; // Pause the animation on mouseover
}

function startAutoScroll() {
  scrollingList.style.animationPlayState = 'running'; // Resume the animation on mouseleave
}

scrollingList.addEventListener('mouseenter', stopAutoScroll);
scrollingList.addEventListener('mouseleave', startAutoScroll);

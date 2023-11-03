document.getElementById("menu-button").addEventListener("click", function() {
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
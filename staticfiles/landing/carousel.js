// Select carousel elements
const carousel = document.querySelector('.carousel');
const carouselItems = document.querySelectorAll('.carousel-item');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

let counter = 0;
let autoSlideInterval;

// Update the carousel's position based on the current counter
function updateCarouselPosition() {
    carousel.style.transform = `translateX(${-counter * 100}%)`;
}

// Move to the next slide
function goToNextSlide() {
    counter = (counter + 1) % carouselItems.length;
    updateCarouselPosition();
}

// Move to the previous slide
function goToPrevSlide() {
    counter = (counter - 1 + carouselItems.length) % carouselItems.length;
    updateCarouselPosition();
}

// Start the auto-slide feature
function startAutoSlide() {
    autoSlideInterval = setInterval(goToNextSlide, 4200);
}

// Stop the auto-slide feature
function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

// Handle next button click
function handleNextButtonClick() {
    goToNextSlide();
    restartAutoSlide();
}

// Handle previous button click
function handlePrevButtonClick() {
    goToPrevSlide();
    restartAutoSlide();
}

// Restart auto-slide after manual navigation
function restartAutoSlide() {
    stopAutoSlide();
    startAutoSlide();
}

// Event listeners for navigation buttons
nextButton.addEventListener('click', handleNextButtonClick);
prevButton.addEventListener('click', handlePrevButtonClick);

// Start auto-slide initially
startAutoSlide();

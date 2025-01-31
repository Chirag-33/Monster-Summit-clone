document.addEventListener("mousemove", (event) => {
    const x = event.clientX / window.innerWidth;
    const y = event.clientY / window.innerHeight;

    document.body.style.backgroundPosition = `
        ${105 + x * 10}% ${0 + y * 10}%,
        ${4 + x * 10}% ${4 + y * 10}%,
        ${50 + x * 5}% ${7 + y * 5}%,
        ${100 + x * 5}% ${30 + y * 5}%,
        bottom
    `;
});


const commentDisplay = document.querySelector('.comment-display');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');

let currentIndex = 0;

const totalComments = document.querySelectorAll('.comment-container').length;

function updateSlide() {
    commentDisplay.style.transform = `translateX(-${currentIndex * 100}%)`;
}

leftArrow.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateSlide();
    }
});

rightArrow.addEventListener('click', () => {
    if (currentIndex < totalComments - 1) {
        currentIndex++;
        updateSlide();
    }
});

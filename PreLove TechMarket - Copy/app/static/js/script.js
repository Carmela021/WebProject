let count = 0;

function addToCart() {
    count++;
    document.getElementById("cart-count").innerText = count;
}

function searchProducts() {
    let input = document.getElementById("search-input").value.toLowerCase();
    let products = document.querySelectorAll(".product");

    products.forEach(product => {
        let title = product.querySelector("h3").innerText.toLowerCase();

        if (title.includes(input)) {
            product.style.display = "block";
        } else {
            product.style.display = "none";
        }
    });
}
function scrollSlider(amount) {
    const slider = document.getElementById('featured-slider');
    slider.scrollBy({
        left: amount,
        behavior: 'smooth'
    });
}
const scrollContainer = document.querySelector('.sale .product-grid');
let scrollInterval;

scrollContainer.addEventListener('mousemove', (e) => {
    const containerRect = scrollContainer.getBoundingClientRect();
    const mouseX = e.clientX - containerRect.left;
    const containerWidth = containerRect.width;
    clearInterval(scrollInterval);

    // If mouse is in the right 30% of the container, scroll right
    if (mouseX > containerWidth * 0.7) {
        startScrolling(5);
    }
    // If mouse is in the left 30% of the container, scroll left
    else if (mouseX < containerWidth * 0.3) {
        startScrolling(-5);
    }
});

scrollContainer.addEventListener('mouseleave', () => {
    clearInterval(scrollInterval);
});

function startScrolling(step) {
    scrollInterval = setInterval(() => {
        scrollContainer.scrollLeft += step;
    }, 10); 
}
//Countdown sale timer
function startCountdown() {
    // Set the end of the sale 
    const saleEnd = new Date();
    saleEnd.setHours(24, 0, 0, 0);

    const timerDisplay = document.getElementById('countdown');

    function updateTimer() {
        const now = new Date();
        const diff = saleEnd - now;

        if (diff <= 0) {
            timerDisplay.innerHTML = "EXPIRED";
            return;
        }

        // Math to convert milliseconds to Hours, Minutes, and Seconds
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        // Format to always show two digits (e.g., 05 instead of 5)
        timerDisplay.innerHTML =
            `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

   
    setInterval(updateTimer, 1000);
    updateTimer();
}

// Start the timer when the page loads
window.onload = startCountdown;



const follower = document.getElementById('follower');
const hero = document.querySelector('.shop-hero');

hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const mouseX = e.clientX - centerX;
    const mouseY = e.clientY - centerY;
    const damping = 20; 
    const moveX = mouseX / damping;
    const moveY = mouseY / damping;
    follower.style.transform = `translate(calc(-50% + ${moveX}px), calc(-50% + ${moveY}px))`;
});

hero.addEventListener('mouseleave', () => {
    follower.style.transform = `translate(-50%, -50%)`;
});

//button para tumaas agad 
const mybutton = document.getElementById("backToTop");


window.onscroll = function() {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
};


 mybutton.addEventListener("click", function() {
    window.scrollTo({
       top: 0,
       behavior: "smooth" // This makes the "upward" motion smooth 
    });
});
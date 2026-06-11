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
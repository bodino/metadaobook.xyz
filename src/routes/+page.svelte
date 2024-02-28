<script>
    import "../app.css";
    import { fade } from "svelte/transition";

    // Assuming you have 30 images named sequentially like page1.jpg, page2.jpg, etc.
    const images = Array.from({ length: 6 }).map(
        (_, index) => `/page${index + 1}.png`,
    );

    // Function to handle the mouse move event
    function handleMouseMove(event) {
        const card = event.currentTarget;
        const { width, height, left, top } = card.getBoundingClientRect();
        const centerX = left + width / 2;
        const centerY = top + height / 2;
        const mouseX = event.clientX - centerX;
        const mouseY = event.clientY - centerY;

        const rotateX = (mouseY / (height / 2)) * -15; // Tilts up or down
        const rotateY = (mouseX / (width / 2)) * 15; // Tilts left or right

        // Retrieve the base transform from data attribute or default to empty
        const baseTransform = card.dataset.baseTransform || "";

        card.style.transform = `${baseTransform} rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    }

    // Reset the transform when the mouse leaves the card
    // Reset the transform when the mouse leaves the card
    function handleMouseLeave(event) {
        const card = event.currentTarget;
        // Reset to the base transform stored in data attribute
        card.style.transform = card.dataset.baseTransform || "";
    }

    let parted = false;

    function toggleParting() {
        parted = !parted;
        document.querySelectorAll(".image-card").forEach((card, index) => {
            if (parted) {
                const translateXValue = index % 2 === 0 ? -50 : 50;
                const rotateYValue = index % 2 === 0 ? 30 : -30;
                const baseTransform = `translateX(${translateXValue}%) rotateY(${rotateYValue}deg)`;
                card.dataset.baseTransform = baseTransform;
                card.style.transform = baseTransform;
            } else {
                card.dataset.baseTransform = "";
                card.style.transform = "";
            }
        });
    }
</script>

<header class="site-title">
    Meta-DAO Book
    <button
        on:click={toggleParting}
        class:toggled={parted}
        class="part-button improved-part-button"
    >
        {parted ? "Close Text" : "View Text"}
    </button>
</header>

<div class="gallery">
    <div
        class="text-center"
        style:order={parted
            ? Math.floor(images.length / 2) + 1
            : images.length + 1}
    >
        {#if parted}
            <p class="text" in:fade={{ duration: 500 }}>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        {/if}
    </div>
    {#each images as image, index (image)}
        <div
            class={`image-card ${parted ? "parted" : ""}`}
            style={`order:${index + 1}; `}
            on:mousemove={handleMouseMove}
            on:mouseleave={handleMouseLeave}
        >
            <img src={image} alt={`Page ${index + 1}`} draggable="false" />
        </div>
    {/each}
</div>

<footer class="site-footer">
    <a href="your-twitter-link" target="_blank" rel="noopener noreferrer">
        <i class="fab fa-twitter"></i>
    </a>
    <a href="your-github-link" target="_blank" rel="noopener noreferrer">
        <i class="fab fa-github"></i>
    </a>
    <a href="your-website-link" target="_blank" rel="noopener noreferrer">
        <i class="fas fa-globe"></i>
        <!-- You can replace this with a custom icon if needed -->
    </a>
</footer>

<style>
    .part-button {
        /* Add your button styling here */
        padding: 10px 20px;
        cursor: pointer;
    }

    .gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Centers items in the main axis */
        gap: 1rem; /* Constant gap between items */
        position: relative;
        padding-top: 50px;
        max-width: 1600px; /* Maximum width of the gallery */
        margin-left: auto; /* Centers the gallery horizontally */
        margin-right: auto; /* Centers the gallery horizontally */
        perspective: 10000px; /* Adds depth to the 3D effect */
    }

    .image-card {
        transition:
            transform 0.5s ease,
            order 0.5s ease;
        transform-style: preserve-3d;
        display: flex; /* Apply flex properties to the image card */
        justify-content: center; /* Center the image within the card */
        align-items: center; /* Align the image vertically within the card */
        margin: 0.5rem; /* Half of the gap on all sides */
    }

    .image-card:hover {
        transition: transform 0.3s ease;
        transform: rotateY(2deg) rotateX(2deg); /* Adjust these angles to get your desired effect */
    }

    .parted:nth-child(odd) {
        /* Targets odd children, i.e., left column */
        transform: translateX(-50%) rotateY(30deg); /* Tilts left */
    }

    .parted:nth-child(even) {
        /* Targets even children, i.e., right column */
        transform: translateX(50%) rotateY(-30deg); /* Tilts right */
    }

    .text-center {
        transition: order 2s ease;
        position: absolute; /* Absolute position for the text */
        margin-top: 40px;
        width: 500px; /* The text should span the entire width of the gallery */
        height: 100%; /* The text should span the entire height of the gallery, if needed */
        /* display: flex; */
        justify-content: center;
        align-items: center;
        pointer-events: none; /* This ensures clicks pass through to elements below */
    }

    .text {
        transition: order 2s ease;
        font-size: 25px;
        color: antiquewhite;
    }

    img {
        max-height: 40rem; /* Adjust based on your images' size */
        height: auto;
        width: auto; /* Ensure the width is adjusted along with the height */
        max-width: 100%; /* Ensures the image doesn't exceed the card size */
        display: block; /* Ensures img element doesn't add extra space below */
        backface-visibility: hidden; /* Prevents flickering on rotation */
    }

    .site-footer {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
    }

    .site-footer a {
        color: #49a3fc; /* Twitter blue color, change it to match your design */
        font-size: 2rem; /* Icon size, adjust as needed */
        transition: color 0.3s ease;
    }

    .site-footer a:hover {
        color: #fc4949; /* Lighter blue for hover effect, adjust as needed */
    }

    /* If you have a specific custom icon for the website, use this */
    .custom-website-icon {
        font-size: 0; /* Hide the text for screen readers */
        background: url("path-to-your-custom-website-icon.png") no-repeat center
            center;
        background-size: contain;
        display: inline-block;
        width: 2rem; /* Match the font-size of other icons */
        height: 2rem; /* Match the font-size of other icons */
    }

    .site-footer {
        position: fixed; /* Fixed position to keep footer at the bottom */
        bottom: 10px; /* Aligns the footer at the bottom */
        left: 0; /* Aligns the footer to the left */
        width: 100%; /* Ensures the footer extends across the full width of the viewport */
        display: flex;
        justify-content: center; /* Centers the icons horizontally */
        align-items: center; /* Centers the icons vertically */
        gap: 20px; /* Adjust the space between icons as needed */
        padding: 10px 0; /* Adds some padding above and below the icons */
        background: transparent; /* No background for a floating effect */
        z-index: 1000; /* Ensures the footer is above other content */
    }

    .site-footer a {
        color: inherit; /* Inherits the color from the parent or you can set a specific color */
        text-decoration: none; /* Removes underline from links */
    }

    .site-footer i {
        font-size: 24px; /* Adjust icon size as needed */
        transition: transform 0.3s ease; /* Smooth transformation on hover */
    }

    .site-footer i:hover {
        transform: scale(1.1); /* Slightly enlarges the icon on hover */
    }

    /* Title styling */
    .site-title {
        position: fixed; /* Keeps the title and button visible */
        top: 20px; /* Adjust as needed */
        left: 20px; /* Adjust as needed */
        right: 20px; /* Extends the header across the top */
        display: flex; /* Aligns title and button in the same row */
        justify-content: space-between; /* Separates title and button */
        align-items: center; /* Centers items vertically */
        font-weight: bold; /* Makes the text bolder */
        text-transform: uppercase; /* Optional: Makes the text all uppercase for "better" look */

        font-size: 36px; /* Makes the text bigger */
        color: #fc4949; /* Adjust as needed */
        font-family: "Arial", sans-serif; /* Change the font-family to something "better" as per your preference */

        z-index: 1010; /* Ensures visibility over other elements */
    }

    /* Improved Part button styling */
    .improved-part-button {
        background-color: #49a3fc; /* A visually appealing color */
        color: #fff; /* Contrasting text color for readability */
        border: none; /* Removes default border */
        border-radius: 5px; /* Rounded corners for a modern look */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow for depth */
        font-weight: bold; /* Makes the button text stand out */
        font-size: 16px; /* Makes the text bigger */
        transition: background-color 0.3s ease;

        cursor: pointer; /* Changes cursor to pointer on hover over button */
        font-family: "Arial", sans-serif; /* Change the font-family to something "better" as per your preference */
    }

    .improved-part-button:hover {
        background-color: #fc4949; /* Color change on hover for interactive feel */
    }

    .improved-part-button:hover,
    .improved-part-button.toggled,
    .improved-part-button.toggled:hover {
        background-color: #fc4949; /* Red background */
        color: #fff; /* White text for better contrast */
    }

    .improved-part-button.toggled:hover {
        background-color: #007bff; /* Blue background */
        color: #fff; /* Adjust text color as needed */
    }
</style>

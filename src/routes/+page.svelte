<script>
    import "../app.css";

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

<button on:click={toggleParting} class="part-button"
    >{parted ? "Close" : "Part"}</button
>

<div class="gallery">
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
    <div
        class="text-center"
        style:order={parted
            ? Math.floor(images.length / 2) + 1
            : images.length + 1}
    >
        {#if parted}
            <p>Your text goes here</p>
        {/if}
    </div>
</div>

<style>
    .part-button {
        /* Add your button styling here */
        margin-bottom: 20px;
        padding: 10px 20px;
        cursor: pointer;
    }

    .gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Centers items in the main axis */
        gap: 1rem; /* Constant gap between items */
        position: relative;
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
        transition: order 0.5s ease;
        position: absolute; /* Absolute position for the text */
        top: 0; /* Align the top edge of the text with the top edge of the gallery */
        left: 0; /* Align the left edge of the text with the left edge of the gallery */
        width: 100%; /* The text should span the entire width of the gallery */
        height: 100%; /* The text should span the entire height of the gallery, if needed */
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none; /* This ensures clicks pass through to elements below */
    }

    img {
        max-height: 40rem; /* Adjust based on your images' size */
        height: auto;
        width: auto; /* Ensure the width is adjusted along with the height */
        max-width: 100%; /* Ensures the image doesn't exceed the card size */
        display: block; /* Ensures img element doesn't add extra space below */
        backface-visibility: hidden; /* Prevents flickering on rotation */
    }
</style>

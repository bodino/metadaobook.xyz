<script>
    import "../app.css";
    import { fade } from "svelte/transition";
    import { onMount } from "svelte";

    // Assuming you have 30 images named sequentially like page1.jpg, page2.jpg, etc.
    let images = Array.from({ length: 32 }).map((_, index) => ({
        id: index + 1,
        image: `/page${index + 1}.png`,
        placeholder: `/placeholder/page${index + 1}.png`, // Add a placeholder property
        flipped: false,
    }));

    function lazyLoad(node, { src, placeholder }) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        let img = entry.target;
                        img.src = src; // Load the actual image
                        observer.unobserve(img);
                    }
                });
            },
            {
                rootMargin: "200px", // Load images a bit before they enter the viewport
            },
        );

        node.src = placeholder; // Initially set to load the placeholder
        observer.observe(node);

        return {
            destroy() {
                observer.unobserve(node);
            },
        };
    }

    function toggleFlip(image) {
        image.flipped = !image.flipped;
        console.log("flipped ", image);
    }

    // Function to handle the mouse move event
    function handleMouseMove(event) {
        const card = event.currentTarget;
        const { width, height, left, top } = card.getBoundingClientRect();
        const centerX = left + width / 2;
        const centerY = top + height / 2;
        const mouseX = event.clientX - centerX;
        const mouseY = event.clientY - centerY;

        const rotateX = (mouseY / (height / 2)) * -5; // Tilts up or down
        const rotateY = (mouseX / (width / 2)) * 5; // Tilts left or right

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

    onMount(() => {
        // Place any code here that needs to access `window` or other browser-only globals
        function adjustForWindowSize() {
            if (window.innerWidth < 1100) {
                if (parted) {
                    // Check if parted is true before toggling
                    toggleParting();
                }
            }
        }

        // Add event listener for window resize
        window.addEventListener("resize", adjustForWindowSize);

        // Call adjustForWindowSize on initial load to ensure proper state
        adjustForWindowSize();

        // Optional: return a cleanup function to remove the event listener
        return () => {
            window.removeEventListener("resize", adjustForWindowSize);
        };
    });
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

<div class="viewing-experience-message">
    For the best viewing experience, please use a larger screen.
</div>

<div class="gallery">
    {#if parted}
        <div
            in:fade={{ duration: 500 }}
            class="text-center"
            style:order={parted
                ? Math.floor(images.length / 2) + 1
                : images.length + 1}
        >
            <h2>Futarchy: A New Dawn of Decision Making</h2>
            <p>
                First, there was autocracy. Those in power ruled selfishly to
                better their own interests, leaving their subjects helpless with
                no ability to enact any change. The ruling class faced zero
                accountability for the impact of their decisions on society.
                Then, there was democracy. For the first time, all members of
                society were empowered and granted an equal share in the
                steering of civilization. Yet the arrow of progress went in
                strange, confusing directions, and everyone held complaints
                about how so much low-hanging fruit was left unpicked. Why were
                the decisions being made so stupid? And so the empowered once
                again became the powerless, subject to a blackboxed emergent
                process that made decisions at random. They gave up and stopped
                even trying. Maybe the king was gone, but the tragedy of the
                commons was now the unofficial one. What difference would one
                vote make? Crypto foolishly copied this pattern, implementing a
                system of coin voting even more inefficient than democracy.
            </p>

            <p>
                In the distance, hope looms: futarchy. What if instead of just
                static votes, people could provide input with a sliding scale
                indicating how confident they were and how important they
                thought something was? Under futarchy, members of society can
                bet on their beliefs by betting on what they think certain
                decisions will lead to. Speculative markets powerfully harness
                the wisdom of society rather than leaving the bulk of it
                untouched. , Thus, serving as a nexus of all available
                information and accurately weighing people’s opinions by their
                profits?how informed they are. People have skin in the game
                Under futarchy, there are strong incentives to actually predict
                the future what is going to happen rather than succumbing to
                biases or bad priors--incentives aligned with the betterment of
                society. Under futarchy, there is individual accountability:
                individuals stake their own money on what outcomes will be good,
                and so the tragedy of the commons is defeated. Under futarchy,
                there is no dumb decision-making blackbox; it is a highly
                intelligent egregore fusing together the minds of every member
                of society. Under futarchy, there is hope.
            </p>

            <h3>Betting: A Tax on Bullshit</h3>
            <p>
                Betting is a tax on bullshit. Who would you trust more:
                political prediction markets with millions of dollars wagered on
                who will win the next election, or the political pundit spinning
                up a narrative on his talk show to the pleasure of his who knows
                his targeted political audience -and will willing to liesay
                whatever he can to keep their attention? Markets consistently
                beat polling and pundits because the bid-ask midpoint of a
                market is a forecast accurately weighing opinions by conviction
                and value. And over time, they become even smarter. because Tthe
                bullshitters lose their money asand the sharps fight to price
                the market as accurately as possible. The incentives of betting
                are great: the biases and narratives you might believe in
                disappear when you’re confronted with the task of betting real
                money on what you think will actually happen. Prediction markets
                are good proxies because the value of a share is directly pegged
                to the likelihood of an event. Decision markets under futarchy
                work because they’re pegged to the value of the token
                conditional on a policy change. Just like the incentives of
                betting, futarchy works because the better you are at judging
                the impact of policy changes whether policy changes will be
                good, the more money you make, leading you to have more sway and
                then the more control you have over future decisions.
                Furthermore, And when you’re betting real money, you can no
                longer get away with just having vague thoughts about whether
                something will be good or bad–you probably wouldn’t want to
                stake real money on opinions like that anyways. Futarchy
                replaces “idk I think Xxyz will maybe be good” with “conditional
                on Xxyz happening, I think my tokens will go up 65% in value”.
            </p>

            <h3>The Mechanics of Decision Markets</h3>
            <p>
                Decision markets under futarchy operate on the premise that the
                value of a policy can be measured by its impact on token value.
                This system rewards accurate policy judgment with financial
                gain, ensuring that only those with genuine insights can
                influence major decisions.
            </p>

            <h3>Accountability and Impact</h3>
            <p>
                Futarchy fosters immediate accountability and tightens the
                feedback loop in governance. It promises a system where
                individual accountability trumps the tragedy of the commons, and
                informed decisions shape the future.
            </p>

            <p>
                As we stand on the brink of adopting futarchy, it's clear: the
                path forward is not through louder voices or more votes, but
                through smarter, more informed decisions that benefit all.
            </p>
        </div>
    {/if}
    {#each images as image, index (image.id)}
        <div
            class={`image-card ${image.flipped ? "flipped" : ""} ${parted ? "parted" : ""}`}
            style={`order:${index + 1};`}
            on:click={() => toggleFlip(image)}
            on:mousemove={handleMouseMove}
            on:mouseleave={handleMouseLeave}
        >
            <img
                class="img"
                use:lazyLoad={{
                    src: image.image,
                    placeholder: image.placeholder,
                }}
                draggable="false"
            />
        </div>
    {/each}
</div>

<footer class="site-footer">
    <a
        href="https://twitter.com/MetaDAOProject"
        target="_blank"
        rel="noopener noreferrer"
    >
        <i class="fab fa-twitter"></i>
    </a>
    <a
        href="https://github.com/bodino/metadaoxyz"
        target="_blank"
        rel="noopener noreferrer"
    >
        <i class="fab fa-github"></i>
    </a>
    <a
        href="https://app.themetadao.org/"
        target="_blank"
        rel="noopener noreferrer"
    >
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
        overflow: hidden; /* This will cut off any part of the content that exceeds the gallery bounds */

        flex-wrap: wrap;
        justify-content: center; /* Centers items in the main axis */
        gap: 1rem; /* Constant gap between items */
        position: relative;
        padding-top: 100px;
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
        max-width: 517px;
        width: 100%; /* Scale width on smaller screens */

        max-height: 640px;
        height: auto; /* Adjust height automatically to maintain aspect ratio */
        aspect-ratio: 517 / 640; /* Maintain aspect ratio based on your max dimensions */

        object-fit: cover;
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
        max-width: 500px; /* The text should span the entire width of the gallery */
        height: 100%; /* The text should span the entire height of the gallery, if needed */
        /* display: flex; */
        font-size: 25px; /* Increases the base font size */

        justify-content: center;
        align-items: center;
        color: antiquewhite; /* Makes text color white */
    }

    .text-center h2,
    .text-center h3 {
        font-size: 30px; /* Larger font size for headings */
        margin-top: 20px; /* Adds spacing above headings */
    }

    .text-center p {
        margin-top: 10px; /* Adds spacing above paragraphs */
    }

    .text {
        transition: order 2s ease;
        font-size: 25px;
        color: antiquewhite;
    }

    .img {
        max-height: 40rem; /* Adjust based on your images' size */
        height: 100%;
        object-fit: cover;

        width: auto; /* Ensure the width is adjusted along with the height */
        max-width: 100%; /* Ensures the image doesn't exceed the card size */
        display: block; /* Ensures img element doesn't add extra space below */
        backface-visibility: hidden; /* Prevents flickering on rotation */
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
        position: fixed;
        bottom: 10px;
        left: 50%; /* Adjust to center the footer */
        transform: translateX(-50%); /* Centers the footer horizontally */
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        padding: 8px 20px; /* Adjusted padding for pill shape */
        background-color: #201f23; /* Adds the black pill-shaped background */
        border-radius: 50px; /* Adjust as needed to fine-tune the pill shape */
        z-index: 1000;
        /* box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Optional: Adds shadow for depth */
        color: #fc4949; /* Keeps your specified icon color */
    }

    .site-footer a {
        color: #fc4949; /* Ensures link color matches your design */
        font-size: 2rem; /* Maintains icon size */
        transition: color 0.3s ease;
    }

    .site-footer i {
        font-size: 24px; /* Adjust icon size as needed */
        transition: transform 0.3s ease; /* Smooth transformation on hover */
    }

    .site-footer i:hover {
        transform: scale(1.1); /* Slightly enlarges the icon on hover */
        color: #49a3fc; /* Lighter blue for hover effect, adjust as needed */
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

    .viewing-experience-message {
        display: none; /* Hide by default */
        text-align: center;
        padding: 1rem;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        border-radius: 5px;
        font-size: 1rem;
        position: fixed; /* Position the message fixed on the screen */
        top: 100px; /* Distance from the bottom of the viewport */
        left: 50%; /* Center the message horizontally */
        transform: translateX(
            -50%
        ); /* Adjust horizontal positioning to truly center */
        width: calc(
            100% - 40px
        ); /* Ensure it doesn't stretch beyond viewport width, considering padding */
        max-width: 500px; /* Maximum width of the message */
        z-index: 1000; /* Ensure it's above other content */
    }

    /* This media query applies styles when the window width is less than 1100 pixels */
    @media (max-width: 1099px) {
        .improved-part-button {
            display: none; /* Hides the button */
        }
        .viewing-experience-message {
            /* display: block; /* Show only when window width is under 1099px */
        }

        .site-title {
            justify-content: center;
        }
    }

    .image-card.flipped {
        /* transform: rotateY(180deg); */
    }
</style>

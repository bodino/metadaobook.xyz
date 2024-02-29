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
    <div
        class="text-center"
        style:order={parted
            ? Math.floor(images.length / 2) + 1
            : images.length + 1}
    >
        {#if parted}
            <p class="text" in:fade={{ duration: 500 }}>
                Current governance structures are broken. In a country, a
                politician will run on the policies that are most likely to get
                him re-elected, not the ones that are truly best for the people
                he represents. In a company, a manager has little incentive to
                bet on moonshot product lines that could 10x the value of the
                company, if it also means he could lose his job. In a DAO,
                getting people to vote is hard and direct democracy makes for
                mediocre products. They have been a failure in crypto for the
                most part. Often, what works best is having a benevolent
                dictator in charge, where one person makes the final decision,
                as in many founder-led startups and open source projects. The
                risk here is that the organization rests on the shoulders of a
                single person. If the person loses their mind, it's hard for the
                organization to succeed. Enter Futarchy Markets do a much better
                job than humans at getting to the most accurate information.
                Information is decentralized. No expert can hold that much
                information in his head. It's dispersed across the brains of
                millions of humans and markets are the mechanism through which
                that information can be gathered and communicated in one place.
                This was Friedrich Hayek's brilliant insight. We have proof that
                markets work in practice, not just theory. Orange futures
                predict the weather better than forecasters. The Iowa Electronic
                markets predict the US Presidential elections winner better than
                polls or political analysts. And Wall Street traders predicted
                who would be held responsible for the Challenger explosion four
                months before a presidential committee did. Markets applied to
                organizations is called futarchy, an idea invented by Robin
                Hanson in 2000. You can apply market-led governance in anything
                from small groups of people to public companies and governments.
                You just need an agreed upon desired outcome and a metric that
                represents that outcome. An example would be wealth and GDP for
                countries. I'll use an experimental new project called Meta-DAO
                to show how decision markets work. MetaDAO's goal is to increase
                the value of the project. A investment fund comes along and puts
                up a proposal to acquire $10,000 worth of the native token,
                $META. Alongside the capital, the fund offers MetaDAO
                legitimacy, attracting more attention to the project. The
                proposal gains enough traction and a market is created. There
                are two options: pass or fail. Market participants have five
                days to trade to signal their decision whether the fund adds
                enough value to the project to warrant a sweetheart deal on the
                tokens. At the expire date, the average price across all days is
                taken. If the pass market is greater than 5 percent of the fail
                market, the proposal passes. Otherwise it fails. Why now Before
                a technology is widely adopted, the idea has been around for a
                long time and it has been tried many times before. Before there
                was Instacart, there was WebVan. So you have to ask, why
                futarchy now and why MetaDAO? Past experiments of futarchy have
                failed because the organization in question didn't start out
                using markets to make decisions. If you don't start out with
                markets you are at the mercy of asking humans to act against
                their own interests. Hanson uses the example of deadlines. Take
                a manager whose job it is to ship some piece of software on
                time. If he adds a market to have everyone vote on whether the
                software will ship on time and the market concludes no, he'll
                have time to figure out what needs to happen to make sure the
                team meets the deadline. If he still fails to meet the deadline,
                he'll have no one to blame. There was nothing that came out of
                left field. Decision markets make managers look bad. MetaDAO on
                the otherhand, started making decisions almost right from the
                outset. It launched on November 8, 2023. After one week, it
                decentralized. All big decisions from then on would be made
                using markets. There is no team or foundation token allocation.
                10,000 $META were distributed to early participants with the
                remainder going to the DAO's treasury. It's founded by an
                anonymous character named Prophet and has managed to attract a
                group of talented free thinkers. Unlike most crypto projects, it
                plans to create products that generate cash flow. An example of
                one is a futarchy-as-a-service software product for other DAOs
                to easily adopt its same governance structure. How to
                participate With crypto projects, people often think that you
                have to code to drive the most value. In reality, marketing is
                just as important as product. If users don't hear about your
                project, it's as if it didn't exist. Great marketing is the
                ability to tell a project's story: what it is and where it's
                going. This can be written content, videos, tweets, even art. If
                you're not a storyteller, you can trade, code, design, scheme,
                make deals happen. There's something you're especially suited
                for, anon. — Thanks to Isaac Yonemoto for reading drafts and
                giving feedback. E
            </p>
        {/if}
    </div>
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
        justify-content: center;
        align-items: center;
        pointer-events: none; /* This ensures clicks pass through to elements below */
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

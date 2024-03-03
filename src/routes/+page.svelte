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
        {parted ? "Close the Curtains" : "See the light"}
    </button>
</header>

<div class="gallery">
    {#if parted}
        <div
            in:fade={{ duration: 500 }}
            class="text-center"
            style:order={parted
                ? Math.floor(images.length / 2) + 1
                : images.length + 1}
        >
            <h3>~Autocracy~ First, the people had no voice</h3>
            <p>
                Autocracy meant those in power ruled selfishly to further their
                own interests, leaving their subjects helpless with no ability
                to enact any change. The ruling class faced zero accountability
                for the impact of their decisions on society. Multisigs ruled
                the world. A circle of 8 royals held all the power. If 5 agreed,
                the law was changed. Still, today, they rule much of
                cyberspace–but the dissenters who yearned for freedom left and
                started anew.
            </p>

            <h3>
                ~Democracy~ Then, the voice of the people became the voice of
                God
            </h3>
            <p>
                The dissenters built democracy. They empowered all members of
                society with a voice. For the first time, everyone held equal
                access to the steering wheel of civilization. Yet the wheel
                seemed to turn in random, stupid directions. A million coin
                voters cried out at once, finally free to speak up with their
                voice–and all anyone could hear was noise.
            </p>
            <p>
                Those who couldn’t yell loud enough–those without enough
                coins–were the first to give up, realizing their votes meant
                nothing on the margin. Society fell to the tragedy of the
                commons. What could possibly affect society enough to affect me?
                became an unspoken mind virus. Sometimes they voted carelessly,
                sometimes they didn’t vote at all.
            </p>
            <p>
                The empowered once again became the powerless. Those same
                dissenters who yearned for a purer cyberspace set out, hopeless,
                and they have been stateless since.
            </p>

            <h3>~Futarchy~ Let there be <s>light markets</s></h3>
            <p>
                But now, for the first time in memory, there is hope once again:
                futarchy.
            </p>
            <p>
                Imagine a democracy built on top of markets. Votes become bets,
                and bets express predictions about two divergent future worlds:
                one where a policy is implemented, one where it isn’t. Betting
                gives people skin in the game. Keeping them individually
                accountable where they might otherwise dismiss decisions due to
                not being directly affected. Markets mean everyone is listened
                to at the volume they speak at.
            </p>
            <p>
                Crucially, futarchic markets must be explicitly tethered to the
                real world so they accurately reflect what they’re trying to
                measure. Meta-DAO’s implementation is centered around the price
                of $META conditional on a proposal passing or failing, in the
                form of conditional tokens: pMeta and fMeta. The time-weighted
                average prices (TWAPs) in the two corresponding conditional
                orderbooks extract invaluable insights from the market. If the
                Pass TWAP exceeds the Fail’s by 5%, traders have conviction that
                $META will be more valuable in worlds where the proposal passes.
            </p>
            <p>
                Futarchy wins. Markets powerfully harness the wisdom of the
                crowds by effectively synthesizing the perspectives and
                knowledge of the masses, rewarding truth-seeking, and giving
                participants skin in the game.
            </p>

            <h3>The people have created their God: futarchic markets</h3>
            <p>
                Futarchy is the best we can do short of figuring out
                omniscience. Millions of people equals millions of opinions and
                insights–a ton of them are extremely valuable, but even more are
                actively a waste of time to listen to.
            </p>
            <p>
                Governance requires listening to the people, but they’ll just
                give up even if they think they have a lot to contribute if it’s
                a waste of time for them to participate. With markets, people
                are rewarded even more if they are right when others are wrong.
                First, they’ll decide for themselves how valuable they think
                their opinions are–and over time, as they win or lose money, the
                market will tell them whether or not they are right.
            </p>
            <p>
                Dumb bettors will pay the bullshit tax and slowly lose all their
                money as it flows to sharps who seek the truth rather than what
                they want to be true. The market recursively self-improves and
                becomes more and more attuned to reality.
            </p>

            <h3>Betting is a tax on bullshit</h3>
            <p>
                Major elections are coming up this year. What would you trust
                more: a narrative fine-tuned by a pundit to get as much
                attention as possible, or the pricing of a political prediction
                market with millions of dollars wagered?
            </p>
            <p>
                The pundit makes money if he gets views; he doesn’t need to be
                right. The bettors in the market only care about being right.
                Show the pundit the market and he’ll be exposed as a bullshitter
                when he refuses to bet on the things he claims to be certain
                about even at longshot odds.
            </p>
            <p>
                Futarchy revolves around this same idea. Traders who are good at
                judging whether policies will be good or bad make more money,
                while those who suck gradually let go of the reins of
                society–whether because they realize they’re just bad at
                predicting or because they lose all their money.
            </p>
            <p>
                Crucially, they care a lot about being right when they have
                money on the line, and this means they have to think hard about
                whether policy changes will be good or bad.
            </p>

            <h3>Skin in the game</h3>
            <p>
                Unlike how the tragedy of the commons plagues democratic systems
                like coin voting because an individual actor may vote in a way
                that is optimal for them, ignoring what’s best for society
                because it doesn’t affect them as much, those who choose to
                become involved in futarchic governance are immediately rewarded
                or punished. They are held individually accountable rather than
                just being a small speck in a massive society with merely
                collective accountability.
            </p>

            <h3>The people are God. They speak to us through the markets</h3>
            <p>
                Today there exists Meta-DAO, an organization which has no bosses
                or corporate hierarchies. It exists in the truest form of
                futarchy. It is but a nascent child. But all things start small,
                before they appear to us as the institutions which are o so
                important. Meta-DAO is experimenting on the most important part
                of society: coordination. For that alone its existence is
                justified. It is a potential future, where we work together
                better and in a more fair manner.
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
        overflow-x: hidden;
        overflow-y: auto; /* Adjusts to allow vertical scrolling */
        scrollbar-width: none; /* Hides scrollbars in Firefox */

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
        overflow-y: hidden; /* Allows scrolling within this element */
        overflow-x: hidden;
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
        max-height: 100%; /* Adjust based on your layout */
        overflow-y: visible; /* Allows scrolling within this element */
        max-width: 500px; /* The text should span the entire width of the gallery */
        /* display: flex; */
        font-size: 30px; /* Increases the base font size */

        justify-content: center;
        align-items: center;
        color: #faf4eb; /* Makes text color white */
    }

    .text-center h2 {
        font-size: 40px; /* Adjusted font size for h2 */
        margin-top: 20px; /* Keeps spacing above headings */
    }

    p {
        line-height: 50px;
    }

    .text-center h3 {
        font-size: 45px; /* Smaller font size for h3 */
        margin-top: 20px; /* Keeps spacing above headings */
        font-style: italic; /* Italics for h3 */
    }

    .text-center p {
        margin-top: 10px; /* Adds spacing above paragraphs */
    }

    .text {
        transition: order 2s ease;
        font-size: 25px;
        /* color: #faf4eb; */
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

    /* This media query applies styles when the window width is less than 1100 pixels */
    @media (max-width: 1099px) {
        .improved-part-button {
            display: none; /* Hides the button */
        }
        .site-title {
            justify-content: center;
        }
    }
</style>

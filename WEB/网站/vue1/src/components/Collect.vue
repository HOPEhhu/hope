<template>
    <div class="page-wrap">
        <header class="page-header">

        </header>
        <main class="page-main">
            <h1>Bigfoot</h1>
            <article>
                <section class="left-side">
                    <h2>Fact or fiction? </h2>
                    <div>
                        <div>
                            <p>Illo numquam, sapiente neque repellendus facere amet doloribus asperiores quia eum? Sunt
                                vero amet neque vel? Tempora, nulla voluptatum amet autem culpa magnam debitis! Dolores
                                esse quam amet nobis ut.</p>
                            <p>Sunt excepturi in nostrum, fugiat veritatis ab sit sequi nemo aperiam deserunt
                                temporibus, dolorem ex adipisci autem. Quasi, iure fugiat! Nulla amet doloribus velit
                                nam tempora, soluta consequatur doloremque omnis?</p>
                            <p> Aenean iaculis odio et eleifend elementum. Pellentesque porta lacus sit amet ligula
                                tristique ornare. Ut euismod suscipit enim. Morbi eu molestie odio. Nullam pellentesque
                                bibendum magna non aliquet. Praesent commodo metus ut dapibus sollicitudin. Etiam
                                tristique arcu et risus venenatis egestas. Mauris quis feugiat leo. Mauris scelerisque
                                eleifend risus a suscipit. Praesent commodo pharetra vehicula. Praesent imperdiet luctus
                                ex eget consectetur. Sed facilisis lobortis dolor quis scelerisque. Pellentesque porta
                                orci nec viverra semper.</p>
                        </div>
                        <div>
                            <p>In nec ornare mauris. Ut bibendum libero sit amet leo finibus ornare. Donec vel ultrices
                                velit, vel congue elit. Class aptent taciti sociosqu ad litora torquent per conubia
                                nostra, per inceptos himenaeos. Etiam blandit sem nisi, eget fringilla risus tristique
                                sit amet. Ut quis dictum massa, nec tincidunt urna. Aliquam dignissim mi at eros egestas
                                elementum. Phasellus tempor lectus id consectetur finibus. Etiam felis augue,
                                ullamcorper sed pretium dictum, interdum sed nulla. Morbi eu ante ac tortor suscipit
                                posuere. Praesent feugiat, dolor sed condimentum tincidunt, massa tortor congue lorem,
                                eget sollicitudin nulla nibh sit amet justo. Pellentesque erat quam, iaculis
                                pellentesque eros non, accumsan laoreet quam.</p>
                            <p>Praesent nec lacus urna. Pellentesque hendrerit turpis sed dictum vehicula. Ut in sapien
                                odio. Sed vitae finibus nisl. Pellentesque dui nisl, condimentum facilisis feugiat nec,
                                dictum quis nisi. Donec pellentesque ornare mauris non congue. Integer consequat nulla
                                at odio congue luctus.</p>
                            <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
                                egestas. Quisque lobortis mattis turpis eu commodo. Donec diam massa, convallis at ex
                                non, finibus lacinia ipsum. Vestibulum rutrum nunc mollis condimentum mollis. Nunc at
                                nunc mauris. Proin magna nisl, imperdiet imperdiet malesuada a, gravida ac dolor.
                                Vivamus ex ipsum, convallis vitae egestas in, dignissim eu augue. Nullam euismod orci
                                lectus, ut tempor mauris malesuada sit amet.</p>
                        </div>
                    </div>
                </section>
                <section class="right-side">
                    <figure>
                        <img src="https://assets.codepen.io/t-1/john-moeses-bauan-sx6n_hgSmOc-unsplash.jpg"
                            alt="a small part of a redwood forest with the sun beaming through the trees.">
                        <figcaption>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dignissimos laborum cumque
                            incidunt, enim ipsa dicta? Porro illo doloribus, consectetur eum exercitationem sit ipsam,
                            est nesciunt maxime, eius animi dolor? Harum.</figcaption>
                    </figure>
                    <!-- photo by John Moeses Bauan for Unsplash.  https://unsplash.com/photos/sx6n_hgSmOc -->
                </section>
            </article>
        </main>
        <footer class="page-footer">
            <h3>More Resources</h3>
            <div>
                <nav>
                    <h4>Sightings</h4>
                    <ul>
                        <li><a href="#">West Coast</a></li>
                        <li><a href="#">Great Lakes Region</a></li>
                        <li><a href="#">Southeastern US</a></li>
                        <li><a href="#">East Coast</a></li>
                    </ul>
                </nav>
                <nav>
                    <h4>Formal Studies</h4>
                    <ul>
                        <li><a href="#">Studies in the 1970s</a></li>
                        <li><a href="#">Studies in the 1990s - 2000s</a></li>
                        <li><a href="#">Contemporary Studies</a></li>
                    </ul>
                </nav>
                <nav>
                    <h4>Bigfoot in Popular Culture</h4>
                    <ul>
                        <li><a href="#">Bigfoot in Movies & TV</a></li>
                        <li><a href="#">Laws about Bigfoot</a></li>
                        <li><a href="#">Share Your Story</a></li>
                    </ul>
                </nav>
            </div>
        </footer>
    </div>

</template>

<script>
    export default {
        name: "Collect",
        props: [],
        data() {
            return {

            }
        },
        methods: {

        },
        mounted() {

        },
        computed: {
        }

    };
</script>

<style scoped>
    @import url("https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&family=Lato:wght@300&display=swap");

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    img,
    picture,
    video,
    canvas,
    svg {
        max-width: 100%;
        display: block;
    }

    ol,
    ul {
        list-style: none;
    }

    a {
        text-decoration: none;
        color: #777;
    }

    figure {
        box-shadow: 3px 3px 4px 0px #00000044;
        border: 1px solid lightgray;
    }

    figcaption {
        text-align: center;
        padding: 0.6rem 0.2rem;
    }

    body {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgb(50, 50, 50);
        font-size: 62.5%;
        font-family: "Lato", sans-serif;
    }

    .page-wrap {
        max-width: 1200px;
        width: 100%;
        border: 1px solid black;
        background: white;
        padding: 10px;
    }

    article {
        display: flex;
        justify-content: space-between;
    }

    h1,
    h2,
    h3,
    h4 {
        font-family: "Comfortaa", cursive;
    }

    .page-main {
        padding-bottom: 2rem;
    }

    .page-main h1 {
        text-align: center;
        font-size: 4rem;
        padding: 2rem 0;
    }

    .left-side {
        width: 60%;
    }

    .left-side div:only-of-type {
        display: flex;
        justify-content: space-between;
        font-size: 0.8rem;
    }

    .left-side h2 {
        border-top: 1px solid black;
        border-bottom: 1px solid black;
        font-size: 2rem;
        padding: 1rem;
        text-align: center;
    }

    .left-side div p {
        padding: 1rem;
    }

    .right-side {
        padding-left: 2rem;
        padding-right: 1rem;
        width: 40%;
    }

    footer {
        background-color: rgb(38, 38, 38);
        padding-bottom: 3rem;
    }

    footer div:only-of-type {
        display: flex;
        justify-content: space-around;
        font-size: 0.8rem;
    }

    footer h4,
    footer h3 {
        color: #fff;
    }

    footer h3 {
        text-align: center;
        font-size: 2rem;
        padding: 2rem;
    }

    nav {
        position: relative;
        z-index: 3;
    }

    nav::after {
        content: "P";
        position: absolute;
        top: -1rem;
        left: 4rem;
        font-size: 8rem;
        color: #fff;
        opacity: 0.1;
        z-index: -1;
    }

    nav li {
        padding: 0.4rem 1rem;
    }

    nav li a {
        color: rgb(224, 224, 224);
    }

    nav li a:hover {
        opacity: 0.7;
    }

    footer nav:nth-of-type(1)::after {
        content: "S";
    }

    footer nav:nth-of-type(2)::after {
        content: "F";
        left: 7rem;
    }

    footer nav:nth-of-type(3)::after {
        content: "B";
        left: 7rem;
    }

    /*hasta 640px de anchura se aplica esta media query*/
    @media (max-width: 640px) {
        footer div:only-of-type {
            flex-direction: column;
        }

        .left-side div:only-of-type {
            flex-direction: column;
        }

        nav {
            display: flex;
            padding-top: 3rem;
            padding-bottom: 3rem;
        }

        nav ul {
            display: flex;
        }

        article {
            flex-direction: column;
        }

        .right-side {
            width: 100%;
        }

        .left-side {
            width: 100%;
        }
    }
</style>
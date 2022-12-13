<script lang="typescript">
    import Accordion from "./components/Accordion.svelte";
    import Editor from "./components/Editor.svelte";
    import Ribbon from "./components/Ribbon.svelte";
</script>

<main>
    <Accordion />
    <div class="document">
        <Ribbon />
        <Editor />
    </div>
</main>

<style lang="scss">
    main {
        display: flex;
        height: 100vh;
        width: 100vw;
        padding: 1rem;
        gap: 1rem;

        .document {
            display: flex;
            flex-direction: column;
            flex-grow: 1;
            gap: 1rem;
        }
    }
</style>

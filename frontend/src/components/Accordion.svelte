<script lang="typescript">
    import Menu from "./menus/Menu.svelte";
</script>

<section class="accordion">
    <Menu />
    <Menu />
    <Menu />
    <Menu />
</section>

<style lang="scss">
    .accordion {
        flex-grow: 0.15;
    }
</style>

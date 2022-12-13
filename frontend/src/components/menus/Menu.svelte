<script lang="typescript">
    let active: boolean = false;

    const toggleMenu = () => {
        active = !active;
    };
</script>

<div class="title" class:active on:click={toggleMenu}>awd</div>
<div class="content">awd</div>

<style lang="scss">
</style>

<template>
<div/>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
    name: 'ChatPage',
    setup() {
        const slide = ref('style')
        return {
            slide,
            lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
        }
    },
    props: {
        
    }
})

</script>
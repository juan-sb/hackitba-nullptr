<template>
<div class="column justify-center items-center content-center vertical-middle" >
    <div id="A" class=".col-3"/>
    <q-carousel
        v-model="slide"
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        padding
        arrows
        height="80vh"
        width="50vw"
        class="bg-primary text-white shadow-1 rounded-borders .col-6"
    >

        <q-carousel-slide 
            v-for="project in projects" 
            v-bind:key="project.name" 
            :name="project.name"
        >
            <div class="full">
                <q-video class="full" :src="project.video_profile" />
            </div>
        </q-carousel-slide>
    </q-carousel>
    <div class=".col-3"/>
</div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
    name: 'PioneerSearch',
    setup() {
        const slide = ref('')
        const projects = ref([{}])
        return {
            slide,
            projects,
        }
    },
    async mounted() {
        const res = await Proxy.get('api/dj-rest-auth/user')
        const projectsResponse = await Proxy.get('projects/')
        this.projects = projectsResponse.data
        this.slide = this.projects[0].name
    }
})

</script>
<template>
<div class="q-pa-md justify-center column" style="width: 100%">
    <div class=".col-2 self-center">
        <q-list bordered padding class="q-mx-xl">
            <q-item v-for="project in projects" v-bind:key="project.name">
                <q-item-section>
                    <q-item-label overline>{{ project.name }}</q-item-label>
                        <q-item-label caption>Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
                    </q-item-section>

                    <q-item-section side>
                        <q-icon name="favorite" color="red" />
                        <span class="self-center">{{ project.like_count }} </span>
                    </q-item-section>
            </q-item>
        </q-list>
    </div>
</div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
    name: 'PioneerProjects',
    setup() {
        const projects = ref([{}])
        
        return {
            projects    
        }
    },
    async mounted() {
        const res = await Proxy.get('api/dj-rest-auth/user')
        const projectsResponse = await Proxy.get('projects/')
        this.projects = projectsResponse.data
    }
})

</script>
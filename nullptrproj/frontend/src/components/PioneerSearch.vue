<template>
<div class="column justify-start items-start content-start full-height full-width fixed">

    <div class="gt-sm col-2 full-width"/>
    <div class="row col-grow full-width">
        <div class="gt-sm col-4"/>
        <div class="col-grow" 
                style="max-width: 500px;">

            <q-card v-if="projects.length > 0" v-touch-swipe.mouse="handleSwipe"
                class="full-height full-width"
                draggable="false"
                style="user-select: none;"
                selectable="false"
                >
                <q-card-section>
                    <div class="row">
                        <div class="text-h6" >{{ projects[0].name }}</div>
                        <q-space />
                        <q-btn @click="swapProjectLike" :icon="likeIcon" color="red">
                            {{ "  " + projects[0].like_count }}
                        </q-btn>
                    </div>
                </q-card-section>

                <q-scroll-area class="q-pt-none full-width" style="height:83%">
                    <q-video style="height: 40%" src="https://www.youtube.com/embed/VGaTBZ51YDM"/>

                    <q-separator inset/>
                    
                    <q-video style="height: 40%" src="https://www.youtube.com/embed/VGaTBZ51YDM"/>

                    <q-card-section>
                        <div class="text-h6">{{ projects[0].description }}</div>
                    </q-card-section>
                </q-scroll-area>
            </q-card>
            <div v-else>No quedan más pioneros!</div>
        </div>
        <div class="gt-sm col-4"/>
    </div>
    <div class="gt-sm col-2 full-width"/>

</div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'


export default defineComponent({
    name: 'PioneerSearch',
    setup() {
        const user = {}
        const projects = ref([{}])
        const likeIcon = ref('favorite_border')
        return {
            user,
            projects,
            likeIcon,
            async updateProjects() {
                const projectsResponse = await Proxy.get('projects/')
                this.projects = projectsResponse.data
            }
        }
    },
    async mounted() {
        const res = await Proxy.get('api/dj-rest-auth/user')
        this.user = res.data
        await this.updateProjects()
        console.log(this.projects[0].description)
        this.swapProjectLike()
        this.swapProjectLike()
    },
    methods: {
        async handleSwipe({ evt, ...newInfo }) {
            if(newInfo.direction != 'left' && newInfo.direction != 'right') return;
            const positiveMatch = newInfo.direction == 'right' ? 1 : 0;
            const res = await Proxy.post('/matches/', {
                'investor': this.user.pk,
                'project': this.projects[0].pk,
                'hasEnded': !positiveMatch
            })
            this.updateProjects()
        },
        async swapProjectLike(evt, nvt) {
            const res = await Proxy.get('/swaplike/' + this.projects[0].pk)
            this.likeIcon = res.data == 'created' ? 'favorite' : 'favorite_border'
            this.updateProjects()
        }
    }
})

</script>

<template>
  <div class="text-center">
    <h1>{{project.name}}</h1>
  </div>
<div 
    class="q-pa-md justify-center column content--container" 
    style="width: 100%;"
  >
    <div class=".col-2 self-center" style="width: 100%;">
      <div class="q-pa-md">
        <div class="row q-my-md justify-start">
          <div class="col col-12-xs col-12-sm self-end">Presentación personal:</div>
          <div class="col-12-sm col-6 col-12-xl  ">
            <a :href="project.video_profile"> {{project.video_profile}}</a>
          </div>
        </div>
        <div class="row q-my-md">
          <div class="col">Presentación de tu idea:</div>
          <div class="col-6">
            <a :href="project.video_description"> {{project.video_description}}</a>
          </div>
        </div>
        <div class="row q-my-md">
          <div class="col">Descripción:</div>
          <div class="col-6">{{project.description}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
    name: 'PioneerProjectDetails',
    setup() {
        const project = ref({})
        return {
          project
        }
    },
    async mounted() {
      const res = await Proxy.get('projects/?name=' + this.$route.query.name)
      this.project = res.data[0]
    }
})

</script>

<style lang="scss">
  // $

  // @import "../css/components/pioneerprojects.scss"
</style>
<template>
  <div class="text-center">
    <h1>Proyecto XXX</h1>
  </div>
  <div 
    class="q-pa-md justify-center column content--container" 
    style="width: 100%;"
  >
    <div class="q-pa-md">
      <div class="row">
        <div class="col">Presentación personal:</div>
        <div class="col-6"></div>
      </div>
      <div class="row">
        <div class="col">Presentación de tu idea:</div>
        <div class="col-6"></div>
      </div>
      <div class="row">
        <div class="col">Descripción:</div>
        <div class="col-6"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
    name: 'PioneerProjects',
    setup() {
        const project = ref([{}])
        // console.log(this.$route.query.pageqq)
        
        return {
            project
        }
    },
    async mounted() {
        const res = await Proxy.get('projects/?name=')
        const projectsResponse = await Proxy.get('projects/')
        this.projects = projectsResponse.data
    }
})

</script>

<style lang="scss">
  // $

  // @import "../css/components/pioneerprojects.scss"
</style>
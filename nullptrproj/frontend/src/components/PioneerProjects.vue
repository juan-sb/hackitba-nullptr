<template>
<div class="text-center">
  <h1>Mis proyectos</h1>
</div>
<div class="q-pa-md justify-center column content--container" style="width: 100%;">
  <div class=".col-2 self-center q-my-lg q-mb-xl">
    <q-btn
    round
    icon="add_circle"
    type="a" 
    label=""
    aria-label="Agregar"
    color="primary" 
    style="margin: auto;"
    to="/myprojects/form"
    />
  <p class="text-center q-my-xs">Agregar</p>
  </div>
  <div class=".col-2 self-center" style="width: 100%;">
    <q-list bordered padding class="q-mx-xl">
      <q-item clickable v-ripple
        v-for="project in projects" v-bind:key="project.name"
        :to="'/projects/?name=' + project.name"
      >
        <q-item-section>
          <q-item-label overline>{{ project.name }}</q-item-label>
            <q-item-label caption lines="1">
              {{ project.description }}
            </q-item-label>
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

<style lang="scss">
  // $

  @import "../css/components/pioneerprojects.scss"
</style>
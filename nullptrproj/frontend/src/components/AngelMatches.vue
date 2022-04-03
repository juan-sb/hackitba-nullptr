<template>
  <div class="q-my-xl .col-2 self-center" style="width: 100%;">
    <q-list bordered padding class="q-mx-xl">
      <q-item clickable v-ripple
        v-for="match in matches" v-bind:key="match.id"
      >
        <q-item-section>
          <q-item-label overline>{{ match.project.name }}</q-item-label>
            <q-item-label caption lines="1">
              {{ match.project.description }}
            </q-item-label>
            
        </q-item-section>
        
        <q-item-label overline>
          <p v-if="match.hasEnded" style="color: #C10015;">Finalizado</p>
          <p v-else style="color: #21BA45;">Activo</p>
        </q-item-label>

        <q-item-section side>
          <q-icon name="favorite" color="red" />
          <span class="self-center">{{ match.project.like_count }} </span>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
  name: 'AngelMatches',
  setup() {
    const matches = ref([{}])

  return {
      matches
    }
  },
  async mounted() {
    const res = await Proxy.get('api/dj-rest-auth/user')
    const matchesResponse = await Proxy.get('matches/')
    this.matches = matchesResponse.data
  }
})

</script>
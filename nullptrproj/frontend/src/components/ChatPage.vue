<template>

<div class="column full-width fixed full-height justify-center align-center items-center">
  
  <q-list bordered class="rounded-borders" style="max-width: 600px">
      <q-item-label header>Comunicaciones</q-item-label>

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar2.jpg">
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">Instalación fotovoltáica en San Luis</q-item-label>
          <q-item-label caption lines="2">
            <span class="text-weight-bold">Martina M.</span>
            -- Quedamos el martes a las 18.30 como hicimos la semana pasada, por el mismo link de meet. Saludos.
          </q-item-label>
        </q-item-section>

        <q-item-section side top>
          15:21
        </q-item-section>
      </q-item>

      <q-separator inset="item" />

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar4.jpg">
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">Soluciones IoT para cines</q-item-label>
          <q-item-label caption lines="4">
            <span class="text-weight-bold">Edward McCluskey</span>
            -- Ansioso por el siguiente checkpoint en Mayo, esperemos que todo se mantenga encaminado!

          </q-item-label>
        </q-item-section>

        <q-item-section side top>
          8:56
        </q-item-section>
      </q-item>

      <q-separator inset="item" />

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar1.jpg">
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">AVIS Simulador de Vuelo</q-item-label>
          <q-item-label caption lines="2">
            <span class="text-weight-bold">Matias Arado</span>
            -- El mayor problema del prototipo es el acople eléctrico entre el
              interior de la cabina y el exterior, ya que hay que pasar por los dos ejes
              de rotación.
          </q-item-label>
        </q-item-section>

        <q-item-section side top>
          Ayer
        </q-item-section>
      </q-item>

      <q-separator inset="item" />

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar3.jpg">
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">Helafree</q-item-label>
          <q-item-label caption lines="2">
            <span class="text-weight-bold">Camila Estevez</span>
            -- No llegué a un acuerdo con la gente del centro de distribuición,
              con el sobrante que hay puedo mantenerme 15 días pero necesitaríamos
              encontrar una solución urgente.
          </q-item-label>
        </q-item-section>

        <q-item-section side top>
          Ayer
        </q-item-section>
      </q-item>
    </q-list>
</div>


</template>



<script>

import { defineComponent, ref } from 'vue'
import options from '../options/config';
import Proxy from '../Proxy'


export default defineComponent({
    name: 'ChatPage',
    setup() {
      const matches = ref([{}])
      return {
        matches
      }
    },
    async mounted() {
      const res = await Proxy.get('matches/')
      this.matches = res.data
      console.log(res.data)

    },
    props: {
        
    }
})

</script>
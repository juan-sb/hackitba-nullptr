<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          <q-avatar>
            <img src="/assets/logo.png">
          </q-avatar>
          MatchFunding
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      side="left"
    >
      <q-list>
        <q-item-label header>Menú</q-item-label>

        <q-item v-if="user.user_type == 'IN'" to="/pioneers">
          <q-item-section avatar>
            <q-icon name="travel_explore" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Búsqueda de pioneros</q-item-label>
          </q-item-section>
        </q-item>

        <q-item v-else to="/myprojects">
          <q-item-section avatar>
            <q-icon name="assignment" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Mis proyectos</q-item-label>
          </q-item-section>
        </q-item>

        <q-item v-if="user.user_type == 'IN'" to="/angel/matches">
          <q-item-section avatar>
            <q-icon name="psychology" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Proyectos que seguís</q-item-label>
          </q-item-section>
        </q-item>

        <q-item to="/chat">
          <q-item-section avatar>
            <q-icon name="question_answer" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Chat</q-item-label>
          </q-item-section>
        </q-item>

        <q-space/>  
        
        <q-item clickable @click="logout">
          <q-item-section avatar>
            <q-icon name="exit_to_app" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Cerrar sesión </q-item-label>
          </q-item-section>
        </q-item>

      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

export default defineComponent({
  name: 'MainLayout',

  setup () {
    const leftDrawerOpen = ref(false)
    const user = ref({
      username: '',
      user_type: ''
    })
    return {
      leftDrawerOpen,
      user,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
  methods:
  {
    async logout() {
      try {
        const res = await Proxy.post("/api/dj-rest-auth/logout/", {});
        this.$router.go(0);
      } catch (error) {
        this.$q.notify("Error en las credenciales.");
        console.log(error.response);
      }
    }
  },
  async mounted () {
    this.leftDrawerOpen = false
    const res = await Proxy.get("/api/dj-rest-auth/user/", {
      headers: { "Content-Type": "application/json" }
    });
    this.user.username = res.data.username
    this.user.user_type = res.data.user_type
  }

})
</script>

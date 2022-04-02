<template>
  <div class="fullscreen">
    <div
      style="width: 80%; height: 100%"
      class="column fixed-center justify-around items-center"
    >
      <img style="width: 50%" src="logotemp.png" />

      <q-form @submit="onSubmit" class="q-gutter-md q-mb-xl" style="width:80%">
        <q-input
          color="primary"
          dense
          rounded
          outlined
          class="full-width"
          v-model="username"
          label="Usuario"
          :rules="[val => (val && val.length > 0) || 'Ingrese su nombre de usuario']"
        >
          <template v-slot:before>
            <q-icon name="person" />
          </template>
        </q-input>

        <q-input
          dense
          rounded
          outlined
          :type="isPasswordHidden ? 'password' : 'text'"
          v-model="password"
          label="Contraseña"
          class="full-width"
          lazy-rules
          :rules="[val => (val && val.length > 0) || 'Ingrese su contraseña']"
        >
          <template v-slot:before>
            <q-icon name="lock" />
          </template>
          <template v-slot:append>
            <q-icon
              :name="isPasswordHidden ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPasswordHidden = !isPasswordHidden"
            />
          </template>
        </q-input>

        <q-btn
          unelevated
          rounded
          padding="sm"
          type="submit"
          color="secondary"
          label="INGRESAR"
          class="full-width"
        />
      </q-form>

      <div class="q-mb-xl">
        <router-link to="/jodita" class="justify-center" />He olvidado mi
        contraseña
      </div>
    </div>
  </div>
</template>

<script>
//import { Component, Vue, Model } from "vue-property-decorator";
import { defineComponent, ref } from 'vue'
import Proxy from '../Proxy'

// @Component({
//   metaInfo(){
//     return {
//       title: "Iniciar sesión"
//     }
//   }
// })

export default defineComponent({
  name: 'LoginPage',

  setup() {
    const password = ref('')
    const username = ref('')
    const isPasswordHidden = ref('true')

    return {
      password,
      username,
      isPasswordHidden
    }
  },
  methods: {
    async onSubmit() {
      try {
        const res = await Proxy.post("/api/dj-rest-auth/login/", {
          username: this.username,
          password: this.password,
          '["remember_me"]': true
        });
        console.log("ME PUEDO LOGEAR")
        this.$router.push({ name: "index" });
      } catch (error) {
        this.$q.notify("Error en las credenciales.");
        console.log(error.response);
      }
    }
  },

  async mounted() {
    const res = await Proxy.get("/api/dj-rest-auth/user/", {
      data: null,
      headers: { "Content-Type": "application/json" }
    });
    if (res.data.response.user?.id) this.$router.push("/");
  },

})
</script>

<style></style>

<template>
  <div class="text-center">
    <h1>¡Compartí tu proyecto!</h1>
  </div>
  <div class="project-form--container">
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="project-form"
    >
      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Nombre del desarrollo"
        hint="Breve y conciso"
        lazy-rules
        :rules="briefRules"
      />
      <q-input
        ref="cvRef"
        filled
        v-model="url_cv"
        label="Presentación personal (máximo 1 minuto)"
        hint="* URL de tu video en YouTube"
        lazy-rules
        :rules="urlRules"
      />

      <q-input
        ref="ideaRef"
        filled
        v-model="url_idea"
        label="Presentación de tu idea (máximo 3 minutos)"
        hint="* URL de tu video subido a YouTube"
        lazy-rules
        :rules="urlRules"
      />

      <q-input
        ref="briefRef"
        filled
        v-model="brief_description"
        type="textarea"
        label="Describí tu idea"
        hint="* En menos de 256 caractéres"
        counter
        lazy-rules
        :rules="briefRules"
      />

      <q-checkbox
        v-model="accept"
        label="Acepto los términos y condiciones."
      />

      <div class="project-form-button--container">
        <q-btn label="Submit" type="submit" color="primary" @onClick="submitProject" />
      </div>
    </form>
  </div>
</template>

<script>
import { useQuasar } from 'quasar'
import { ref } from 'vue'
import Proxy from '../Proxy'

export default {
  setup () {
    const $q = useQuasar()

    const name = ref(null)
    const nameRef = ref(null)

    const url_cv = ref(null)
    const cvRef = ref(null)

    const url_idea = ref(null)
    const ideaRef = ref(null)

    const brief_description = ref(null)
    const briefRef = ref(null)

    const accept = ref(false)

    return {
      url_cv,
      cvRef,
      urlRules: [
        val => (val && val.length > 0) || 'Este campo es obligatorio.',
        val => (val.match(/^(http(s)?:\/\/)?(www\.)?(youtube\.com\/watch\?v\=|youtu.be\/)(\w)+$/) 
                || 'La dirección provista no es válida')
      ],

      url_idea,
      ideaRef,

      name,
      nameRef,

      brief_description,
      briefRef,
      briefRules: [
        val => (val && val.length > 0) || 'Este campo es obligatorio.',
        val => (val.length < 256) || '¡Demasiados caracteres!'
      ],

      accept,

      onSubmit () {
        cvRef.value.validate()
        ideaRef.value.validate()
        briefRef.value.validate()
        nameRef.value.validate()

        if (cvRef.value.hasError || ideaRef.value.hasError) {
          // form has error
        }
        else if (accept.value !== true) {
          $q.notify({
            color: 'negative',
            message: 'Por favor asegurate de leer y aceptar nuestros términos y condiciones.'
          })
        }
        else {
          Proxy.get('api/dj-rest-auth/user/').then(res => {
            Proxy.post('projects/', {
              "pioneer": res.data.pk,
              "video_profile": url_cv.value,
              "video_description": url_idea.value,
              "description": brief_description.value,
              "name": name.value
            }).then(res => {
              $q.notify({
                icon: 'done',
                color: 'positive',
                message: 'Submitted'
              })
            })
          })
        }
      }
    }
  }
}
</script>


<style lang="scss">
  // $
  @import "../css/components/projectform.scss"
</style>
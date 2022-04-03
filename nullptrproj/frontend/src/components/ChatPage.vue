<template>

<div/>

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
      const res = Proxy.get('matches/')

    }
    props: {
        
    }
})

</script>
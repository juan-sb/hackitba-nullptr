<template>

<div/>

</template>



<script>
import JitsiMeetJS from '@lyno/lib-jitsi-meet';
import { defineComponent, ref } from 'vue'
import options from '../options/config';

JitsiMeetJS.init();
JitsiMeetJS.setLogLevel(JitsiMeetJS.logLevels.INFO);
const connection = new JitsiMeetJS.JitsiConnection(null, null, options);
function onConnectionSuccess() {
  console.log("onConnectionSuccess", arguments);
}
function onConnectionFailed() {
  console.log("onConnectionFailed", arguments);
}
function disconnect() {
  console.log("disconnect", arguments);
}
connection.addEventListener(JitsiMeetJS.events.connection.CONNECTION_ESTABLISHED, onConnectionSuccess);
connection.addEventListener(JitsiMeetJS.events.connection.CONNECTION_FAILED, onConnectionFailed);
connection.addEventListener(JitsiMeetJS.events.connection.CONNECTION_DISCONNECTED, disconnect);
connection.connect();


export default defineComponent({
    name: 'ChatPage',
    setup() {
        return {
        }
    },
    props: {
        
    }
})

</script>
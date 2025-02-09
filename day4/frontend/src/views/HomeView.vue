<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="hello anchit"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  created(){
    if(localStorage.getItem('authToken') === null){
      alert('You are not logged in');
      this.$router.push({name: 'login'});
    }
    if (localStorage.getItem('role') != 'admin'){
        alert('You are not authorized to view this page');
        this.$router.push({name: 'about'});
    }
  }
}
</script>

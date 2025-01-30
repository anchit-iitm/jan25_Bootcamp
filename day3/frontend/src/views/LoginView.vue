<template>
    <div name="loginpage">
        <h1>Login Page</h1>
        <form>
            <label for="username">Email:</label>
            <input type="text" id="username" name="username" v-model="this.email" >
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="this.password">
            <button type="button" @click="this.login()">Login</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    name: 'LoginView',
    data(){
        return{
            email: '',
            password: ''
        }
    },
    methods:{
        login(){
            axios
            .post('http://localhost:5000/api/login',
            {
                email: this.email,
                password: this.password
            }
            )
            .then(response => {
                if(response.status === 202);
                {
                    this.$router.push({name: 'home'});
                }
            })
            .catch(error => {
                alert(error.response.data.msg);
            });
        }
    }
}
</script>
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
                console.log(response);
                if(response.status === 202);
                {
                    localStorage.setItem('authToken', response.data.authToken);
                    localStorage.setItem('role', response.data.role);
                    if(response.data.role === 'admin'){
                        this.$router.push({name: 'home'});
                    }
                    if(response.data.role === 'manager'){
                        this.$router.push({name: 'about'});
                    }
                }
            })
            .catch(error => {
                alert(error.response.data.msg);
            });
        }
    }
}
</script>
<template>
    <div name="firstPage">
        <h1 v-if="this.name">hello world from {{ this.name }}</h1>
        <table>
            <thead>
                <tr>
                    <th>name</th>
                    <th>age</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="json in this.data">
                    <td><router-link :to="{name: 'redirect', params: {name1: json.name}}">{{ json.name }}</router-link></td>
                    <td>{{ json.age }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import axios from 'axios';
export default{
    name: 'firstPage',
    data(){
        return{
            name: null,
            token: null,
            data: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken'); 
        if(this.token === null){
            alert('You are not logged in');
            this.$router.push({name: 'login'});
        }
        this.fetchData();
        this.fetchTable();
    },
    methods:{
        fetchData(){
            axios.get('http://localhost:5000/firstApi',
                {
                    headers:{
                        "Authorization": `${this.token}`
                    }
                }
            )
            .then(response => {
                if(response.status === 200){
                    this.name = response.data.data;
                }
            })
            .catch(error => {
                if(error.response.status === 404){
                    alert(error.response.data.msg);
                }
                if(error.response.status === 401){
                    alert(error.response.data.response.errors[0]);
                    this.$router.push({name: 'login'});
                }
                if(error.response.status === 403){
                    alert(error.response.data.response.errors[0]);
                }
            });
        },
        fetchTable(){
            axios.get('http://localhost:5000/secondApi',
                {
                    headers:{
                        "Authorization": `${this.token}`
                    }
                }
            )
            .then(response => {
                if(response.status === 200){
                    this.data = response.data
                }
            })
            .catch(error => {
                if(error.response.status === 404){
                    alert(error.response.data.msg);
                }
                if(error.response.status === 401){
                    alert(error.response.data.response.errors[0]);
                    this.$router.push({name: 'login'});
                }
                if(error.response.status === 403){
                    alert(error.response.data.response.errors[0]);
                }
            });
        }
    }
}
</script>

<style></style>
<template>
    <div>
        <h1>Category Create</h1>
        <div class="container-sm">
            <div class="form-group" >
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" v-model="this.name">
            </div>
            <div class="form-group">
                <label for="description">Description</label>
                <textarea class="form-control" id="description" v-model="this.description"></textarea>
            </div>
            <button type="submit" class="btn btn-primary" @click="this.createCategory()">Submit</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { routeLocationKey } from 'vue-router';
export default {
    name: 'CategoryCreate',
    data(){
        return{
            name: null,
            description: null,
            token: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken');
        if (this.token == null){
            this.$router.push({name: 'login'});
        }
        if (this.$route.params.id != null){
            
        }
    },
    methods:{
        createCategory(){
            axios.post('http://localhost:5000/api/categories',
            {
                name: this.name,
                description: this.description
            },{
                headers: {  
                    Authorization: this.token
                }
            },
            ).then(response => {
                if (response.status == 201){
                    this.$router.push({name: 'home'});
                }
            }).catch(error => {
                if (error.response.status == 401){
                    this.$router.push({name: 'login'});
                }
                else if (error.response.status == 404){
                    alert(error.response.data.msg);
                }
                else if (error.response.status == 407){
                    alert(error.response.data.msg);
                }
                else if(error.response.status == 500){
                    alert('Internal server error');
                }
                else{
                    alert(error.response.data.msg);
                }
            });
        }
    }
}
</script>
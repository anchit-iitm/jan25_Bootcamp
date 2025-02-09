<template>
    <div>
        <h1>Dashboard</h1>
        <p v-if="!data">Welcome to {{this.user}} dashboard</p>
        <div class="container" >
            <table>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>description</th>
                        <th>action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in data" :key="item.id">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.description }}</td>
                        <td><router-link :to="{name: 'category_update', params: {id: item.id}}"><button class="btn btn-outline">update</button></router-link> | <button class="btn btn-outline">delete</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'Dashboard',
    data() {
        return {
            user: null,
            data: null,
            token: null
        }
    },
    created() {
        this.user = localStorage.getItem('role')
        this.token = localStorage.getItem('authToken')
        if (!this.token) {
            this.$router.push({name: 'login'})
        }
        this.fetchData()
    },
    methods: {
        fetchData() {
            axios.get('http://localhost:5000/api/categories', {
                headers: {
                    Authorization: this.token
                }
            })
            .then(response => {
                this.data = response.data.data
            })
            .catch(error => {
                alert(error.response.data.msg)
            })
        }
    }
}
</script>
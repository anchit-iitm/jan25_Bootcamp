<template>
    <h1>hi, {{ var1 }}</h1>
</template>
<script>
export default{
    data(){
        return{
            var1: null
        }
    },
    mounted(){
        this.var1 = this.$route.params.name1;
    }
}
</script>
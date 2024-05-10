<script setup lang="ts">
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import InputNumber from "primevue/inputnumber";
import Password from 'primevue/password';
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
const router = useRouter()

const username =ref()
const pass =ref()
const confirmedPass =ref()
const city =ref()
const missingInfo =ref(false)
const differentPassword =ref(false)

function signup(){
    if(!username.value || !pass.value || !confirmedPass.value || !city.value){
        missingInfo.value=true
    }
    else if (pass.value != confirmedPass.value){
        differentPassword.value=true
    }
    else{
        axios.post("http://127.0.0.1:8000/signup",{
            user:{
            username:username.value,
            password:pass.value,
            type:'customer',
            city_name:city.value
        }

        },{}).then(res=>{router.push('login');console.log(res)})
    }
}


</script>

<template>
  <main>
    <div class="container">
      <div class="left">
        <h1>Welcome To CoffeeTeria, Your daily dose of happiness</h1>
      </div>
      <div class="right">
        
        <h2>Signup</h2>
        <h4 v-if="missingInfo">Some Data Is Missing</h4>
        <h4 v-if="differentPassword">Different Password</h4>
        <div class="wrapper">

            <InputText v-model="username" placeholder="Username"/>
            <Password v-model="pass"  :feedback="false" placeholder="Password"/>
            <Password v-model="confirmedPass" :feedback="false" placeholder="Confirm Password"/>
            <InputText v-model="city" placeholder="City" />
        </div>
        <div class="button">

        <Button @click="signup" label="Signup"/>

        </div>
    
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  min-height: 100%;
  width: 100%;
  background-color: var(--primary);
  padding-top: 5rem;
}
.container {
  margin-inline: auto;
  width: 60rem;
  aspect-ratio: 1.6/1;
  background-color: var(--secondary);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  color: var(--MyText);
  display: grid;
  grid-template-columns: 40% 60%;
}
.left {
  padding: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--MySecondary);
  background-color: var(--accent2);
}
.wrapper{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    flex-direction: column;
}
h2{
    text-align: center;
    margin-bottom: 2rem;
}
button{
    padding: 0.5rem 2rem;
}
.button{
    margin-top: 4rem;
    display: flex;
    justify-content: end;
    padding-right: 4rem;
    
}
h4{
    text-align: center;
    color: red;
    margin: 0;
}
h1{
    color: var(--secondary);
    text-transform: capitalize;
}
@media screen and (max-width: 800px) {
  
  
  .container {
    width: 80%;
    aspect-ratio:auto;
    height: fit-content;
    grid-template-columns: 1fr;
    grid-template-rows: 20% 80%;
  }
  .button{
    margin-bottom: 2rem;
  }
}
</style>

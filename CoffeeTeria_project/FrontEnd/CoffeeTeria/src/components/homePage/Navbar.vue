<script lang="ts" setup>
import { useRouter } from "vue-router";
import Button from "primevue/button";
import "primeicons/primeicons.css";
import { ref } from "vue";
import { useToken, usePersonalInfo } from "@/stores/counter";
const info = usePersonalInfo();
const token = useToken();
const router = useRouter();
let logout = () => {
  token.logout();
  router.push("/");
};

const role = ref();
const name = ref();
const balacne = ref();

function personalInformation() {
  if (token.getIsAuthorized) {
    balacne.value = info.getBalance;
    role.value = info.getRole;
    name.value = info.getName;
  }
}

const viewLogout = ref(false);

personalInformation();
</script>

<template>
  <main>
    <div class="container">
      <img src="/images/coffeelogo.png" alt="" />

      <div class="profile" v-if="token.getIsAuthorized">
        <i class="pi pi-user" @click="viewLogout = !viewLogout"></i>
        <div class="logout" v-if="viewLogout">
          <p @click="logout">Log Out</p>
        </div>
        <div class="info">
          <p>{{ name }} | {{ role }}</p>
          <p>BALANCE: {{ balacne }} L.E</p>
        </div>
      </div>
      <div class="profile" v-if="!token.getIsAuthorized">
        <Button @click="router.push('/login')" label="Login"/>
        <Button @click="router.push('/signup')" label="Signup"/>
      </div>
    </div>
  </main>
</template>

<style scoped>
.container {
  height: 4rem;
  background-color: var(--secondary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-inline: 2rem;
}
img {
  height: 61.75%;
}
button{
    margin-inline:1rem ;
}
p{
  line-height: 0.5rem;
  color: var(--primary);
}
i {
  background-color: var(--accent1);
  color: var(--primary);
  border-radius: 100%;
  font-size: 1rem;
  padding: 0.5rem;
  cursor: pointer;
}
.profile {
  justify-self: end;
  position: relative;
  color: var(--accent1);
  display: flex;
  justify-content: center;
  align-items: center;
  display: flex;
  gap: 0.5rem;
  height: 100%;
}
.logo {
  display: flex;
  align-items: center;
}
p{
  line-height: 0.5rem;
}
i {
  background-color: var(--accent1);
  color: var(--primary);
  border-radius: 100%;
  font-size: 1rem;
  padding: 0.5rem;
  cursor: pointer;
}
.selected {
  color: var(--MyAccent1);
  border-bottom: 2px solid;
}
.logout {
  position: absolute;
  top: 100%;
  left: 0;
  border-radius: 8px;
  background-color: var(--accent1);
  color: var(--MyText);
  width: max-content;
  margin-top: 0.5rem;
  padding: 0rem 2rem;
  z-index: 2;
}
.logout::before {
  content: "";
  width: 1rem;
  height: 1rem;
  background-color: var(--accent1);
  position: absolute;
  top: 0;
  left: 0.5rem;
  transform: rotate(45deg);
}
.logout > p {
  cursor: pointer;
}
.logout > p:hover {
  opacity: 0.5;
}
</style>

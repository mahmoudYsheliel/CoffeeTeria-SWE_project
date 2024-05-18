<script setup lang="ts">
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import { useRouter } from "vue-router";
import { ref } from "vue";

import axios from "axios";
import { useToken, usePersonalInfo } from "../../stores/counter";

const userName = ref("");
const pass = ref("");
const router = useRouter();
const token = useToken();
const info = usePersonalInfo();
const userNotFound = ref(false);

function login() {
  axios
    .post(
      "/token",
      `grant_type=&username=${userName.value}&password=${pass.value}&scope=&client_id=&client_secret=`
    )
    .then((res: any) => {
      console.log(res);
      if (res.data["access_token"]) {
        token.addToken(res.data["access_token"]);

        axios
          .post(
            "/personal_info",
            {},
            {
              headers: {
                Authorization: `Bearer ${token.getToken}`,
              },
            }
          )
          .then((res: any) => {
            console.log(res);
            let data = res.data.data.info;
            if (data) {
              info.addInfo(data["balance"], data["username"], data["type"]);
              info.saveToLocalStorage();
              if (data["type"] === "customer") {
                router.push("/");
              } else if (data["type"] === "owner") {
                router.push("/");
              }
            }
          });
      }
    });
}
</script>
<template>
  <main>
    <div class="container">
      <div class="login">
        <div class="wrapper">
          <h2 v-if="userNotFound">user not found</h2>
          <img src="/images/coffeelogo.png" alt="" />
          <div class="inputs">
            <InputText placeholder="Username" type="text" v-model="userName" />
            <InputText placeholder="Password" type="text" v-model="pass" />
          </div>
          <Button @click="login" label="LOGIN" />
        </div>
      </div>
      <img src="/images/image 1.png" alt="image" class="side-image" />
    </div>
  </main>
</template>

<style scoped>
main {
  background-color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5rem;
}
.container {
  width: 800px;
  aspect-ratio: 1.6/1;
  background-color: var(--secondary);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  color: var(--MyText);
}
.login {
  height: 100%;
  width: 38.75%;
}
.side-image {
  height: 100%;
  width: 61.75%;
}
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  height: 100%;
  position: relative;
}
.inputs {
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
button {
  padding-inline: 2rem;
}

@media screen and (max-width: 800px) {
  img {
    display: none;
  }
  .login {
    width: 100%;
  }
  .container {
    width: 61.75%;
    aspect-ratio: 1/1;
  }
}
</style>

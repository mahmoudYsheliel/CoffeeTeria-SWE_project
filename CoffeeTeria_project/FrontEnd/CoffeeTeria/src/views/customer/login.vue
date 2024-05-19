<script lang="ts" setup>
// Importing necessary components and utilities
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import { useRouter } from "vue-router";
import { ref } from "vue";
import axios from "axios";
import { useToken, usePersonalInfo } from "../../stores/counter";

// Initializing variables and hooks
const userName = ref("");
const pass = ref("");
const router = useRouter();
const token = useToken();
const info = usePersonalInfo();
const userNotFound = ref(false);

// Function to handle login process
function login() {
  axios
    .post(
      "/token",
      `grant_type=&username=${userName.value}&password=${pass.value}&scope=&client_id=&client_secret=`
    )
    .then((res: any) => {
      // Logging the response
      console.log(res);
      if (res.data["access_token"]) {
        // Adding token to store
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
              // Adding personal info to store
              info.addInfo(data["balance"], data["username"], data["type"]);
              info.saveToLocalStorage();
              // Redirecting based on user type
              if (data["type"] === "customer" || data["type"] === "owner") {
                router.push("/");
              } else {
                userNotFound.value = true;
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
          <!-- Display error message if user not found -->
          <h2 v-if="userNotFound">User not found</h2>
          <img src="/images/coffeelogo.png" alt="" />
          <div class="inputs">
            <!-- Input fields for username and password -->
            <InputText placeholder="Username" type="text" v-model="userName" />
            <InputText placeholder="Password" type="text" v-model="pass" />
          </div>
          <!-- Button to initiate login process -->
          <Button @click="login" label="LOGIN" />
        </div>
      </div>
      <!-- Side image -->
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

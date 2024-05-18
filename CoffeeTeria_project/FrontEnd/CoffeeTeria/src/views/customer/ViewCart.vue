<script lang="ts" setup>
import Navbar from "@/components/homePage/Navbar.vue";
import { useCart, usePersonalInfo, useOrder } from "@/stores/counter";
import { useToken } from "@/stores/counter";
import Dialog from "primevue/dialog";
import Button from "primevue/button";
import { useRouter } from "vue-router";
import axios from "axios";
import { ref, computed } from "vue";
import Dropdown from "primevue/dropdown";
import InputText from "primevue/inputtext";
import InputNumber from "primevue/inputnumber";
import Calendar from "primevue/calendar";
import { useRoute } from "vue-router";

const info = usePersonalInfo();

const token = useToken();
const route = useRoute();
const orderType = ["Delivery", "Pick Up", "Book A Seat"];
const selectedOrderType = ref();

const location = ref();
const pickTime = ref();
const bookTime = ref();
const bookSeatCount = ref();
const cart = useCart();
const order = useOrder();
const personalInfo = usePersonalInfo();
const notEnoughMoney = ref(false);
const missingInfo = ref(false);
interface productCounnt {
  product: any;
  count: number;
}
interface ItemCount {
  product_id: string;
  count: number;
}
const itemsCounts = ref<ItemCount[]>([]);
const productsCounts = ref<productCounnt[]>([]);
const router = useRouter();
const orderSuccess = ref(false);
const total = computed(() => {
  let total = 0;
  for (let productCount of productsCounts.value) {
    total += productCount.count * productCount.product.price;
  }
  return total;
});
for (let productId of cart.getProducts) {
  axios.post("/get_product", { product_id: productId }).then((res) => {
    if (res.data.data.product) {
      productsCounts.value.push({ product: res.data.data.product, count: 1 });
    }
  });
}
const proceed = () => {
  for (let product of productsCounts.value) {
    itemsCounts.value.push({
      product_id: product.product.id,
      count: product.count,
    });
  }
  console.log(itemsCounts.value);
  if (total.value > personalInfo.getBalance) {
    notEnoughMoney.value = true;
  } else {
    for (let productCount of productsCounts.value) {
      order.addProductCount(
        productCount.product.id,
        productCount.product.price,
        productCount.count
      );
    }
    let order_info = {};
    if (total.value == 0 || !selectedOrderType.value) {
      missingInfo.value = true;
    } else if (selectedOrderType.value == orderType[0]) {
      if (!location.value) {
        missingInfo.value = true;
      } else {
        order_info = { location: location.value };
        sendOrder(order_info, orderType[0]);
      }
    } else if (selectedOrderType.value == orderType[1]) {
      if (!pickTime.value) {
        missingInfo.value = true;
      } else {
        order_info = {
          time:
            pickTime.value.toDateString() +
            " " +
            pickTime.value.toLocaleTimeString(),
        };
        sendOrder(order_info, orderType[1]);
      }
    } else if (selectedOrderType.value == orderType[2]) {
      if (!bookSeatCount.value || !bookTime) {
        missingInfo.value = true;
      } else {
        order_info = {
          time:
            bookTime.value.toDateString() +
            " " +
            bookTime.value.toLocaleTimeString(),
          number_of_seats: bookSeatCount.value,
        };
        sendOrder(order_info, orderType[2]);
      }
    }
  }
};

function sendOrder(order_info: any, type: string) {
  axios
    .post(
      "/create_order",
      {
        order: {
          coffee_shop_id: route.params.shopId,
          customer_id: "",
          type: type,
          created_at: new Date().toISOString(),
          details: itemsCounts.value,
          order_info: order_info,
        },
      },
      {
        headers: {
          Authorization: `Bearer ${token.getToken}`,
        },
      }
    )
    .then((res) => {
      if (res.data.data.order_id) {
        orderSuccess.value = true;
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
            }
          });
      }
    });
}
</script>

<template>
  <main>
    <Navbar />
    <h1 v-if="notEnoughMoney">Not Enough Money</h1>
    <h1 v-if="missingInfo">Some data is missing or you didn't order</h1>
    <div class="container">
      <Dialog
        v-model:visible="orderSuccess"
        modal
        header="Order Success"
        :style="{ width: '40rem' }"
      >
        <h1 style="color: rgb(100, 200, 50)">Order Done Successfuly</h1>
        <p v-if="selectedOrderType == orderType[0]">
          time to deliver is: 20 minutes
        </p>
        <Button @click="router.push('/')" label="Return Home Page" />
      </Dialog>

      <div
        v-for="(productCount, i) in productsCounts"
        :key="productCount.product.id"
        class="product"
      >
        <div class="image">
          <img :src="productCount.product.image" alt="" />
          <div class="info">
            <p>{{ productCount.product.name }}</p>
            <p>{{ productCount.product.price }}</p>
          </div>
        </div>
        <div class="product-count-price">
          <input
            type="number"
            placeholder="count"
            v-model="productCount.count"
          />
          <div class="total">
            total {{ productCount.count * productCount.product.price }}
          </div>
        </div>
      </div>
      <div class="container2">
        <Dropdown
          @change="console.log(selectedOrderType)"
          style="width: 100%"
          v-model="selectedOrderType"
          :options="orderType"
          placeholder="Order Type"
        />
        <hr />
        <div v-if="selectedOrderType == orderType[0]" class="option">
          <span>Location To Deliver The Order</span>
          <InputText class="input" v-model="location" />
        </div>
        <div v-if="selectedOrderType == orderType[1]" class="option">
          <span>Time To Pick Up The Order</span>
          <Calendar
            class="input"
            showIcon
            iconDisplay="button"
            showTime
            hourFormat="24"
            v-model="pickTime"
          />
        </div>
        <div v-if="selectedOrderType == orderType[2]" class="option">
          <span>Number Of Seats</span>
          <InputNumber class="input" v-model="bookSeatCount" />
        </div>
        <div v-if="selectedOrderType == orderType[2]" class="option">
          <span>Time To Book</span>
          <Calendar
            class="input"
            showIcon
            iconDisplay="button"
            showTime
            hourFormat="24"
            v-model="bookTime"
          />
        </div>
      </div>
    </div>
    <div class="botom">
      <div class="total-price">Total Price: {{ total }}</div>
      <Button label="Proceed" @click="proceed" />
    </div>
  </main>
</template>

<style scoped>
img,
p {
  margin: 0;
}
h1 {
  color: orange;
  text-align: center;
}
img {
  width: 100px;
  aspect-ratio: 1.6/1;
  border-radius: 8px;
}
.info {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.image {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 8px;
  justify-content: center;
  gap: 0.5rem;
  width: 90%;
}
.product {
  background-color: var(--secondary);
  width: 200px;
  height: 150px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 8px;
  justify-content: center;
  gap: 0.5rem;
}
.container {
  width: 80%;
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  min-height: 40vh;
  margin-top: 10vh;
}
.product-count-price {
  display: flex;
  justify-content: space-between;
  width: 95%;
}
input {
  width: 5rem;
  border-radius: 4px;
}
.botom {
  width: 80%;
  margin-inline: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.5rem;
  color: var(--accent1);
}
button {
  padding: 0.5rem 2rem;
}
.container2 {
  width: 100%;
  margin-inline: auto;
  min-height: 40vh;
}
.option {
  margin-inline: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--secondary);
  font-size: 1.25rem;
  font-weight: bolder;
  margin-top: 2rem;
}
.input {
  width: 20rem;
}
</style>

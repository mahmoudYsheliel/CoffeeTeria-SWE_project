
import { defineStore } from "pinia";

export const useToken = defineStore("token", {
  state: () => ({
    token: null as string | null,
    isAuthorized: false,
  }),
  actions: {
    addToken(token: string) {
      this.token = token;
      this.isAuthorized = true;
      this.saveToLocalStorage();
    },
    saveToLocalStorage() {
      localStorage.setItem("token", JSON.stringify(this.token));
      localStorage.setItem("isAuthorized", JSON.stringify(this.isAuthorized));
    },
    logout() {
      this.token = null;
      this.isAuthorized = false;
      localStorage.clear();
    },
  },
  getters: {
    getToken(state) {
      const data = localStorage.getItem("token");

      if (data) {
        this.token = JSON.parse(data);
      }
      return state.token;
    },
    getIsAuthorized(state) {
      const data = localStorage.getItem("isAuthorized");
      if (data != null) {
        this.isAuthorized = JSON.parse(data);
      }
      return state.isAuthorized;
    },
  },
});


export const usePersonalInfo = defineStore("personalInfo", {
  state: () => ({
    balance: 0,
    name: "",
    role: null as string | null,
  }),
  actions: {
    addInfo(balance: number, name: string, role: string) {
      this.balance = balance;
      this.name = name;
      this.role = role;
    },
    saveToLocalStorage() {
      localStorage.setItem("balance", JSON.stringify(this.balance));
      localStorage.setItem("role", JSON.stringify(this.role));
      localStorage.setItem("name", JSON.stringify(this.name));
    },
    delete() {
      this.balance = 0;
      this.name = '';
      this.role=null
      localStorage.removeItem('balance');
      localStorage.removeItem('role');
      localStorage.removeItem('name');
    },
  },
  getters: {
    getBalance(state) {
      const data = localStorage.getItem("balance");

      if (data) {
        this.balance = JSON.parse(data);
      }
      return state.balance;
    },
    getRole(state) {
      const data = localStorage.getItem("role");

      if (data) {
        this.role = JSON.parse(data);
      }
      return state.role;
    },
    getName(state) {
      const data = localStorage.getItem("name");

      if (data) {
        this.name = JSON.parse(data);
      }
      return state.name;
    },
  },
});



export const useCart = defineStore("cart", {
  state: () => ({
    products:[] as string[]
  }),
  actions: {
    addProduct(Id: string,) {
      if(!this.products.includes(Id)){

        this.products.push(Id);
      }
    },
    delete() {
      this.products = [];
    },
  },
  getters: {
    getProducts(state) {
     
      return state.products;
    },
  },
});

interface productCount{
  productId:string
  price:number
  count:number
}

export const useOrder = defineStore("order", {
  state: () => ({
    productsCounts:[] as productCount[]
  }),
  actions: {
    addProductCount( productId:string,price:number,count:number) {
        this.productsCounts.push({productId:productId,price:price,count:count});
    
    },
    delete() {
      this.productsCounts = [];
    },
  },
  getters: {
    getProducts(state) {
     
      return state.productsCounts;
    },
  },
});



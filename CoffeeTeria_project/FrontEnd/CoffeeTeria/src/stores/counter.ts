import { defineStore } from "pinia";

// Store for managing user token and authorization status
export const useToken = defineStore("token", {
  state: () => ({
    token: null as string | null,
    isAuthorized: false,
  }),
  actions: {
    // Adds token and updates authorization status
    addToken(token: string) {
      this.token = token;
      this.isAuthorized = true;
      this.saveToLocalStorage();
    },
    // Saves token and authorization status to local storage
    saveToLocalStorage() {
      localStorage.setItem("token", JSON.stringify(this.token));
      localStorage.setItem("isAuthorized", JSON.stringify(this.isAuthorized));
    },
    // Clears token and authorization status
    logout() {
      this.token = null;
      this.isAuthorized = false;
      localStorage.clear();
    },
  },
  getters: {
    // Retrieves token from local storage
    getToken(state) {
      const data = localStorage.getItem("token");
      if (data) {
        this.token = JSON.parse(data);
      }
      return state.token;
    },
    // Retrieves authorization status from local storage
    getIsAuthorized(state) {
      const data = localStorage.getItem("isAuthorized");
      if (data != null) {
        this.isAuthorized = JSON.parse(data);
      }
      return state.isAuthorized;
    },
  },
});

// Store for managing user's personal information
export const usePersonalInfo = defineStore("personalInfo", {
  state: () => ({
    balance: 0,
    name: "",
    role: null as string | null,
  }),
  actions: {
    // Sets user's personal information
    addInfo(balance: number, name: string, role: string) {
      this.balance = balance;
      this.name = name;
      this.role = role;
    },
    // Saves personal information to local storage
    saveToLocalStorage() {
      localStorage.setItem("balance", JSON.stringify(this.balance));
      localStorage.setItem("role", JSON.stringify(this.role));
      localStorage.setItem("name", JSON.stringify(this.name));
    },
    // Clears personal information
    delete() {
      this.balance = 0;
      this.name = '';
      this.role = null;
      localStorage.removeItem('balance');
      localStorage.removeItem('role');
      localStorage.removeItem('name');
    },
  },
  getters: {
    // Retrieves balance from local storage
    getBalance(state) {
      const data = localStorage.getItem("balance");
      if (data) {
        this.balance = JSON.parse(data);
      }
      return state.balance;
    },
    // Retrieves role from local storage
    getRole(state) {
      const data = localStorage.getItem("role");
      if (data) {
        this.role = JSON.parse(data);
      }
      return state.role;
    },
    // Retrieves name from local storage
    getName(state) {
      const data = localStorage.getItem("name");
      if (data) {
        this.name = JSON.parse(data);
      }
      return state.name;
    },
  },
});

// Store for managing user's shopping cart
export const useCart = defineStore("cart", {
  state: () => ({
    products: [] as string[],
  }),
  actions: {
    // Adds product to the cart
    addProduct(Id: string) {
      if (!this.products.includes(Id)) {
        this.products.push(Id);
      }
    },
    // Clears the cart
    delete() {
      this.products = [];
    },
  },
  getters: {
    // Retrieves products from the cart
    getProducts(state) {
      return state.products;
    },
  },
});

// Interface for product count in order
interface productCount {
  productId: string;
  price: number;
  count: number;
}

// Store for managing user's order information
export const useOrder = defineStore("order", {
  state: () => ({
    productsCounts: [] as productCount[],
  }),
  actions: {
    // Adds product information to the order
    addProductCount(productId: string, price: number, count: number) {
      this.productsCounts.push({ productId: productId, price: price, count: count });
    },
    // Clears the order
    delete() {
      this.productsCounts = [];
    },
  },
  getters: {
    // Retrieves products from the order
    getProducts(state) {
      return state.productsCounts;
    },
  },
});

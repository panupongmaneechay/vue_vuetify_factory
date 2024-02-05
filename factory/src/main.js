import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router';
import Login from './components/Login.vue';
// import HelloPage from './components/HelloWorld.vue';
import DataTable from './components/DataTable.vue';
import 'vuetify/dist/vuetify.min.css';

Vue.config.productionTip = false;

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Login },
  { path: '/index', name: 'index', component: DataTable },
  // Add other routes as needed
];

const router = new VueRouter({
  routes,
});

new Vue({
  render: (h) => h(App),
  vuetify,
  router,
}).$mount('#app');

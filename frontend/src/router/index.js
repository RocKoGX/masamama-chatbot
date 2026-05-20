import { createRouter, createWebHistory } from 'vue-router'

import InicioView from '../views/InicioView.vue'
import ProductosView from '../views/ProductosView.vue'
import CarritoView from '../views/CarritoView.vue'
import NosotrosView from '../views/NosotrosView.vue'
import LocalesView from '../views/LocalesView.vue'

const routes = [
  { path: '/', component: InicioView },
  { path: '/productos', component: ProductosView },
  { path: '/carrito', component: CarritoView },
  { path: '/nosotros', component: NosotrosView },
  { path: '/locales', component: LocalesView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router   
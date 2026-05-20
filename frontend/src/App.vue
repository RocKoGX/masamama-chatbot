<template>
  <Navbar :cantidad-carrito="cantidadCarrito" />

  <router-view
    :carrito="carrito"
    @agregar="agregarAlCarrito"
    @aumentar="aumentarCantidad"
    @disminuir="disminuirCantidad"
    @eliminar="eliminarProducto"
    @vaciar="vaciarCarrito"
  />

  <ChatbotFlotante />

  <Footer />
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import ChatbotFlotante from './components/ChatbotFlotante.vue'

const carrito = ref(JSON.parse(localStorage.getItem('carritoMasamama')) || [])

const cantidadCarrito = computed(() =>
  carrito.value.reduce((total, item) => total + item.cantidad, 0)
)

watch(
  carrito,
  () => {
    localStorage.setItem('carritoMasamama', JSON.stringify(carrito.value))
  },
  { deep: true }
)

function agregarAlCarrito(producto) {
  const item = carrito.value.find(p => p.id === producto.id)

  if (item) {
    item.cantidad++
  } else {
    carrito.value.push({ ...producto, cantidad: 1 })
  }

  alert(`${producto.nombre} fue agregado al carrito.`)
}

function aumentarCantidad(id) {
  const item = carrito.value.find(p => p.id === id)
  if (item) item.cantidad++
}

function disminuirCantidad(id) {
  const item = carrito.value.find(p => p.id === id)
  if (item && item.cantidad > 1) item.cantidad--
  else eliminarProducto(id)
}

function eliminarProducto(id) {
  carrito.value = carrito.value.filter(p => p.id !== id)
}

function vaciarCarrito() {
  carrito.value = []
}
</script>
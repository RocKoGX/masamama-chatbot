<template>
  <section class="carrito">
    <h1>Carrito de compras</h1>

    <p v-if="carrito.length === 0">
      No hay productos en el carrito.
    </p>

    <div
      v-for="item in carrito"
      :key="item.id"
      class="item"
    >
      <img :src="item.imagen" :alt="item.nombre">

      <div>
        <h3>{{ item.nombre }}</h3>
        <p>S/ {{ item.precio.toFixed(2) }} x {{ item.cantidad }}</p>
      </div>

      <div>
        <button @click="$emit('disminuir', item.id)">-</button>
        <button @click="$emit('aumentar', item.id)">+</button>
        <button @click="$emit('eliminar', item.id)">Eliminar</button>
      </div>
    </div>

    <div v-if="carrito.length > 0" class="total">
      <h2>Total: S/ {{ total.toFixed(2) }}</h2>
      <button @click="finalizarCompra">Finalizar compra</button>
      <button @click="$emit('vaciar')">Vaciar carrito</button>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  carrito: Array
})

defineEmits(['aumentar', 'disminuir', 'eliminar', 'vaciar'])

const total = computed(() =>
  props.carrito.reduce((suma, item) => suma + item.precio * item.cantidad, 0)
)

function finalizarCompra() {
  alert('Compra simulada realizada correctamente.')
}
</script>

<style scoped>
.carrito {
  padding: 60px 8%;
  min-height: 70vh;
}

.item {
  background: white;
  padding: 16px;
  margin-bottom: 14px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 14px rgba(0,0,0,0.1);
}

img {
  width: 90px;
  height: 70px;
  object-fit: cover;
  border-radius: 10px;
}

button {
  margin: 5px;
  padding: 9px 13px;
  border: none;
  background: #6b3f22;
  color: white;
  border-radius: 8px;
}

.total {
  margin-top: 30px;
  text-align: center;
}
</style>
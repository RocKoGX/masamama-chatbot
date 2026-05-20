<template>
  <section id="carrito" class="carrito">
    <h2>Carrito de compras</h2>

    <p v-if="carrito.length === 0">
      Aún no agregaste productos.
    </p>

    <div
      v-for="item in carrito"
      :key="item.id"
      class="item"
    >
      <div>
        <h3>{{ item.nombre }}</h3>
        <p>S/ {{ item.precio.toFixed(2) }} x {{ item.cantidad }}</p>
      </div>

      <div class="acciones">
        <button @click="$emit('disminuir', item.id)">-</button>
        <button @click="$emit('aumentar', item.id)">+</button>
        <button @click="$emit('eliminar', item.id)">Eliminar</button>
      </div>
    </div>

    <div v-if="carrito.length > 0" class="total">
      <h3>Total: S/ {{ total.toFixed(2) }}</h3>
      <button @click="finalizarCompra">Finalizar compra</button>
      <button class="vaciar" @click="$emit('vaciar')">Vaciar carrito</button>
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
  alert('Compra simulada registrada correctamente. Gracias por comprar en Masamama.')
}
</script>

<style scoped>
.carrito {
  background: #f3e1c8;
}

h2 {
  text-align: center;
  font-size: 34px;
}

.item {
  background: white;
  margin: 12px auto;
  max-width: 700px;
  padding: 16px;
  border-radius: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.acciones button {
  margin-left: 8px;
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
  background: #6b3f22;
  color: white;
}

.total {
  text-align: center;
  margin-top: 24px;
}

.total button {
  margin: 8px;
  padding: 12px 18px;
  border: none;
  background: #6b3f22;
  color: white;
  border-radius: 8px;
}

.vaciar {
  background: #9b2f2f !important;
}
</style>
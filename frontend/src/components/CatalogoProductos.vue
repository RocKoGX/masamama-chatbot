<template>
  <section id="productos">
    <h2>Productos disponibles</h2>

    <div class="filtros">
      <button
        v-for="cat in categorias"
        :key="cat"
        @click="categoriaSeleccionada = cat"
      >
        {{ cat }}
      </button>
    </div>

    <div class="grid">
      <div
        class="card"
        v-for="producto in productosFiltrados"
        :key="producto.id"
      >
        <img :src="producto.imagen" :alt="producto.nombre">
        <span>{{ producto.categoria }}</span>
        <h3>{{ producto.nombre }}</h3>
        <p>{{ producto.descripcion }}</p>
        <strong>S/ {{ producto.precio.toFixed(2) }}</strong>
        <button @click="$emit('agregar', producto)">Agregar</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  productos: Array
})

defineEmits(['agregar'])

const categoriaSeleccionada = ref('Todos')

const categorias = computed(() => [
  'Todos',
  ...new Set(props.productos.map(p => p.categoria))
])

const productosFiltrados = computed(() => {
  if (categoriaSeleccionada.value === 'Todos') {
    return props.productos
  }

  return props.productos.filter(
    p => p.categoria === categoriaSeleccionada.value
  )
})
</script>

<style scoped>
h2 {
  text-align: center;
  font-size: 34px;
}

.filtros {
  text-align: center;
  margin-bottom: 30px;
}

.filtros button {
  margin: 6px;
  padding: 10px 16px;
  border: none;
  background: #d6a15d;
  border-radius: 20px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 24px;
}

.card {
  background: white;
  border-radius: 16px;
  padding: 16px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.1);
}

img {
  width: 100%;
  height: 170px;
  object-fit: cover;
  border-radius: 12px;
}

span {
  display: inline-block;
  margin-top: 10px;
  color: #8b5a2b;
  font-weight: bold;
}

.card button {
  width: 100%;
  margin-top: 12px;
  padding: 10px;
  border: none;
  background: #6b3f22;
  color: white;
  border-radius: 8px;
}
</style>
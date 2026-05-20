<template>
  <section>
    <h2>Productos destacados</h2>
    <p class="subtitulo">Los favoritos de nuestros clientes.</p>

    <div class="grid">
      <div
        class="card"
        v-for="producto in productos"
        :key="producto.id"
      >
        <img :src="producto.imagen" :alt="producto.nombre">
        <h3>{{ producto.nombre }}</h3>
        <p>{{ producto.descripcion }}</p>
        <strong>S/ {{ producto.precio.toFixed(2) }}</strong>
        <button @click="$emit('agregar', producto)">Agregar al carrito</button>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  productos: Array
})

defineEmits(['agregar'])
</script>

<style scoped>
h2 {
  font-size: 34px;
  text-align: center;
}

.subtitulo {
  text-align: center;
  margin-bottom: 32px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
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
  height: 180px;
  object-fit: cover;
  border-radius: 12px;
}

button {
  width: 100%;
  margin-top: 12px;
  padding: 10px;
  border: none;
  background: #6b3f22;
  color: white;
  border-radius: 8px;
}
</style>
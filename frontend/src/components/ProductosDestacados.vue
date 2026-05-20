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
  margin: 45px;
}

.subtitulo {
  text-align: center;
  margin-bottom: 32px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 24px;
  margin: 10px;
}

.card {
  background: -webkit-gradient(linear, right bottom, left top, from(#f3f3f3), to(#fff));
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.1);
  border: solid 1px #e4e4e4;
  display: flex;
  flex-direction: column;
}

img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 12px;
}

button {
  width: 100%;
  margin-top: auto;
  padding: 8px;
  border: none;
  background: linear-gradient(#855536, #6b3f22, #402412);
  box-shadow: inset 0 0 1px 2px rgb(94 62 33 / 59%);
  color: white;
  border-radius: 8px;
  
}

strong {
  display: inline-block;
  margin-top: 10px;
  margin-bottom: 10px;
  color: #be1111;
  font-weight: bold;
}
</style>
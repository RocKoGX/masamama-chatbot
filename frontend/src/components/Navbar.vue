<template>
  <nav class="navbar">
    <router-link to="/" class="logo">Masamama</router-link>

    <div>
      <router-link to="/">Inicio</router-link>
      <router-link to="/productos">Productos</router-link>
      <router-link to="/nosotros">Nosotros</router-link>
      <router-link to="/locales">Locales</router-link>
      <router-link to="/carrito">
        Carrito 🛒 {{ cantidadCarrito }}
      </router-link>
    </div>
  </nav>
</template>

<script setup>
defineProps({
  cantidadCarrito: Number
})
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: #6b3f22;
  color: white;
  padding: 18px 8%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

a {
  color: white;
  margin-left: 18px;
  text-decoration: none;
  font-weight: bold;
}

.router-link-active {
  color: #d6a15d;
}
</style>
<template>
  <section class="hero">
    <div class="hero-texto">
      <h1>Panadería y cafetería artesanal Masamama</h1>
      <p>
        Productos elaborados con masa madre, fermentación lenta,
        trigo molido en piedra e insumos locales.
      </p>

      <router-link to="/productos">
        Ver productos
      </router-link>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 420px;
  background:
    linear-gradient(rgba(60, 35, 18, 0.65), rgba(60, 35, 18, 0.65)),
    url("https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1200");
  background-size: cover;
  background-position: center;
  color: white;
  display: flex;
  align-items: center;
  padding: 60px 8%;
}

.hero-texto {
  max-width: 600px;
}

h1 {
  font-size: 48px;
}

p {
  font-size: 18px;
  line-height: 1.6;
}

a {
  display: inline-block;
  margin-top: 20px;
  background: #d6a15d;
  color: #3b2415;
  padding: 12px 22px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
}
</style>
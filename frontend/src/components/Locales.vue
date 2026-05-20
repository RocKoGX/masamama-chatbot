<template>
  <section id="locales">
    <h2>Nuestros locales</h2>

    <div class="grid">
      <div class="local">
        <h3>Masamama Cercado</h3>
        <p>Local ubicado en el centro de Arequipa.</p>
        <p><strong>Horario:</strong> 8:00 a.m. - 9:00 p.m.</p>
      </div>

      <div class="local">
        <h3>Masamama Yanahuara</h3>
        <p>Local ubicado en una zona tradicional de Arequipa.</p>
        <p><strong>Horario:</strong> 8:00 a.m. - 9:00 p.m.</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
h2 {
  text-align: center;
  font-size: 34px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}

.local {
  background: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.1);
}
</style>
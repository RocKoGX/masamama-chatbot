<template>
  <Hero />

  <ProductosDestacados
    :productos="productosDestacados"
    @agregar="$emit('agregar', $event)"
  />
</template>

<script setup>
import { computed } from 'vue'
import { productos } from '../data/productos'
import Hero from '../components/Hero.vue'
import ProductosDestacados from '../components/ProductosDestacados.vue'

defineEmits(['agregar'])

const productosDestacados = computed(() =>
  productos.filter(p => p.destacado)
)
</script>
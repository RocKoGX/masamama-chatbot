<template>
  <CatalogoProductos
    :productos="productos"
    @agregar="$emit('agregar', $event)"
  />
</template>

<script setup>
import { productos } from '../data/productos'
import CatalogoProductos from '../components/CatalogoProductos.vue'

defineEmits(['agregar'])
</script>
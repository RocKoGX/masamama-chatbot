<template>
  <div>
    <button class="boton-chat" @click="abierto = !abierto">
      🤖
    </button>

    <div v-if="abierto" class="chatbox">
      <div class="header">
        <strong>Asistente Masamama</strong>
        <button @click="abierto = false">x</button>
      </div>

      <div class="mensajes">
        <div class="mensaje bot">
          Hola, soy el asistente de ventas de Masamama. Puedes preguntarme sobre productos, ventas o locales.
        </div>

        <div
          v-for="(msg, index) in mensajes"
          :key="index"
          :class="['mensaje', msg.tipo]"
        >
          {{ msg.texto }}
        </div>
      </div>

      <div class="input">
        <input
          v-model="pregunta"
          @keyup.enter="enviarPregunta"
          placeholder="Escribe tu pregunta..."
        >

        <button @click="enviarPregunta">
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const abierto = ref(false)
const pregunta = ref('')
const mensajes = ref([])

async function enviarPregunta() {
  if (!pregunta.value.trim()) return

  const textoUsuario = pregunta.value

  mensajes.value.push({
    tipo: 'usuario',
    texto: textoUsuario
  })

  pregunta.value = ''

  try {
    const res = await fetch('http://127.0.0.1:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pregunta: textoUsuario })
    })
    console.log('Status', res.status)
    const text = await res.text()
    console.log('Response text:', text)
    let data = {}
    try{
      data = JSON.parse(text)
    } catch (e) {
      throw new Error("El backend no devolvió un JSON válido: " + text);
    }
    mensajes.value.push({
      tipo: 'bot',
      texto: data.respuesta || 'El chatbot no respondió.'
    })
  } catch (error) {
    console.error(
      'Error frontend', error
    )

    mensajes.value.push({
      tipo: 'bot',
      texto: 'No pude conectarme con el backend. Verifica que FastAPI esté ejecutándose.'+error.message
  });
      
    }
  }

</script>

<style scoped>
.boton-chat {
  position: fixed;
  right: 24px;
  bottom: 24px;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  border: none;
  background: #6b3f22;
  color: white;
  font-size: 28px;
  z-index: 50;
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
}

.chatbox {
  position: fixed;
  right: 24px;
  bottom: 96px;
  width: 340px;
  height: 470px;
  background: white;
  border-radius: 18px;
  overflow: hidden;
  z-index: 50;
  box-shadow: 0 6px 24px rgba(0,0,0,0.25);
  display: flex;
  flex-direction: column;
}

.header {
  background: #6b3f22;
  color: white;
  padding: 14px;
  display: flex;
  justify-content: space-between;
}

.header button {
  background: transparent;
  color: white;
  border: none;
  font-size: 18px;
}

.mensajes {
  flex: 1;
  padding: 14px;
  overflow-y: auto;
  background: #fffaf3;
}

.mensaje {
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 12px;
  font-size: 14px;
}

.bot {
  background: #ead7bd;
  color: #3b2415;
}

.usuario {
  background: #6b3f22;
  color: white;
  margin-left: 40px;
}

.input {
  display: flex;
  padding: 10px;
  gap: 8px;
  background: #f3e1c8;
}

.input input {
  flex: 1;
  padding: 10px;
  border: 1px solid #c9a27e;
  border-radius: 8px;
}

.input button {
  background: #6b3f22;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px;
}
</style>
<template>
  <div class="container">
    <div class="header-buscar">
      <input
        class="text-buscar"
        v-model="termoBusca"
        placeholder="Digite o nome da operadora"
      />
      <button class="button" @click="buscarOperadora">Buscar</button>
    </div>

    <ul class="resultados" v-if="resultados.length">
      <li v-for="operadora in resultados" :key="operadora['Registro_ANS']">
        {{ operadora["Nome_Fantasia"] }} - {{ operadora["Logradouro"] }} -
        {{ operadora["Numero"] }}, {{ operadora["Bairro"] }},
        {{ operadora["Cidade"] }} - {{ operadora["UF"] }} - ({{
          operadora["DDD"]
        }}) {{ operadora["Telefone"] }} - {{ operadora["Endereco_eletronico"] }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const termoBusca = ref("");
const resultados = ref([]);

const buscarOperadora = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/buscar", {
      params: { nome: termoBusca.value },
    });
    console.log("Dados recebidos:", response.data);
    resultados.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar operadora:", error);
  }
};
</script>

<script setup lang="ts">
import { getLivro } from "~/services/livros";
import { type Livro } from "~/models/livros";
import { type Ref, ref } from "vue";
import { useToast } from "primevue/usetoast";
const toast = useToast();

const show = ()=> {
  toast.add({ severity: 'success', summary: 'Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 30000 });
};

const livros: Ref<Array<Livro>> = ref([])  

const atualizarLivros = () => {
  getLivro()
  .then((livrosEcontrados) => {
    console.log("Livros Encontrados: ", livrosEcontrados?.results[0].nome);
    livros.value = livrosEcontrados?.results ?? [];
  });
};

atualizarLivros();


</script>

<template>
  <main class="home-container flex flex-column align-items-center">
    <Toast/>
    <div class="LivroContainer grid align-items-center justify-content-center">
      <div v-for="(livro,index) in livros">
        <LivroItem :key="index" class="col-4" :livro="livro" />
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
  .home-container{
      margin: 0;
      width: 100vw;
      min-height: calc(100vh - var(--altura-header));
      background-color: #f6f6f6;
  }
</style>
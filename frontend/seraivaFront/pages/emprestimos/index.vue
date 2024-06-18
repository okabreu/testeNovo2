<script setup lang="ts">
import { ref } from 'vue';
import type { Ref } from 'vue';
import { getEmprestimos } from '~/services/emprestimos';
import type { Emprestimo } from '~/models/emprestimo';
import { useToast } from 'primevue/usetoast';
import EmprestimoItem from '~/components/EmprestimoItem.vue';

const toast = useToast();

const show = () => {
  toast.add({ severity: 'success', summary: 'Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 30000 });
};

const emprestimos: Ref<Array<Emprestimo>> = ref([]);

const atualizarEmprestimo = () => {
  getEmprestimos()
    .then((emprestimoEncontrados?) => {
      console.log("emprestimos Encontrados: ", emprestimoEncontrados?.results[0].usuarioFK);
      emprestimos.value = emprestimoEncontrados?.results ?? [];
    });
};

const handleStatusChanged = () => {
  atualizarEmprestimo();
};

atualizarEmprestimo();
</script>

<template>
  <main class="home-container flex flex-column align-items-center">
    <Toast/>
    <div class="LivroContainer grid align-items-center justify-content-center">
      <div v-for="(emprestimo, index) in emprestimos" :key="index">
        <EmprestimoItem :emprestimo="emprestimo" @statusChanged="handleStatusChanged" />
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
  .home-container {
    margin: 0;
    width: 100vw;
    min-height: calc(100vh - var(--altura-header));
    background-color: #f6f6f6;
  }
</style>

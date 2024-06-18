<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import { type Emprestimo, STATUS_PAGAMENTO } from '~/models/emprestimo';
import { updateEmprestimoStatus } from '~/services/emprestimos';

type propType = {
  emprestimo: Emprestimo;
}
const props = defineProps<propType>();

const status = ref(props.emprestimo.status);
const emit = defineEmits(['statusChanged']);

const handleStatusChange = () => {
  if (!props.emprestimo.id) return;

  updateEmprestimoStatus(props.emprestimo.id, status.value)
    .then((updatedEmprestimo) => {
      if (updatedEmprestimo) {
        alert('Status atualizado com sucesso!');
        emit('statusChanged');
      } else {
        alert('Erro ao atualizar status!');
      }
    })
    .catch((error) => {
      console.error("Erro ao atualizar status: ", error);
      alert('Erro ao atualizar status!');
    });
};
</script>

<template>
  <section class="cartao flex flex-column align-items-center justify-content-center" v-if="props.emprestimo">
    <div>
      <h4 class="emprestimoNome">{{ props.emprestimo.usuarioFK }}</h4>
    </div>
    <div>
      <h4 class="emprestimoData">{{ props.emprestimo.data_emprestimo }}</h4>
    </div>
    <div>
      <h4 class="emprestimoStatus">{{ props.emprestimo.status }}</h4>
    </div>
    <div>
      <select v-model="status">
        <option v-for="(label, key) in STATUS_PAGAMENTO" :key="key" :value="key">{{ label }}</option>
      </select>
    </div>
    <div>
      <button @click="handleStatusChange">Alterar</button>
    </div>
  </section>
</template>

<style scoped lang="scss">
.cartao {
  width: 300px;
  height: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  margin-top: 5rem;
  margin-left: 1rem;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.318);

  .emprestimoNome,
  .emprestimoData,
  .emprestimoStatus {
    color: #000000;
    text-align: center;
    margin: 0.5rem 0;
  }
}
</style>

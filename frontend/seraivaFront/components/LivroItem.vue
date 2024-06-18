<script setup lang="ts">
import { type Livro } from '~/models/livros';
import { computed } from "#imports";
import { carrinho } from "#imports";

const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = carrinho();

type propType = {
  livro: Livro;
}
const props = defineProps<propType>();

const emit = defineEmits(['eventoAdicionado']);

const adicionarItem = () => {
  adicionarNoCarrinho(props.livro);
  emit('eventoAdicionado');
  console.log("CARRINHO ATUAL: ", getCarrinho());
}

const livroNoCarrinho = computed(()=>{
  return estaNoCarrinho(props.livro);   
});

</script>

<template>
  <section class="cartao flex flex-column align-items-center justify-content-center" v-if="props.livro">
    <div class="check text right">
      <Checkbox v-model="livroNoCarrinho" :binary="true" :readonly="true"/>
    </div>
    <div class="LivroImagem">
      <img :src="props.livro.foto">
    </div>
    <div>
      <h4 class="LivroNome">{{ props.livro.nome }}</h4>
    </div>
    <div class="flex flex-row">
      <span>R${{ props.livro.valor_emprestimo }} </span>
    </div>
    <Button @click="adicionarItem" class="botaoAdd" label="FAZER EMPRÉSTIMO"/>
  </section>
</template>

<style scoped lang="scss">
  .cartao{
    width: 300px;
    height: 500px;
    background-color:rgb(255, 255, 255);
    border-radius: 8px;
    margin-top: 4rem;
    margin-left: 2rem;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.318);

    .LivroImagem img{
      width: 200px;
      height: 280px;
      margin-top: 1rem;
      box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.318);
    }

    .botaoAdd{
      background-color: #034C8C;
      border: 3px solid #fff;
      width: 80%;
      height: 5vh;
      border-radius: 3vh;

      &:hover{
        background-color: #5B9ED9;
      }
    }

    .LivroNome{
      color: #000000;
      text-align: center;
    }

    .check{
      width: 95%;
    }
  }
</style>
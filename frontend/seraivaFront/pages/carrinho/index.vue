<script setup lang="ts">
import { computed } from "#imports";
import { carrinho, type CarrinhoItem } from "#imports";
const { getCarrinho, removerDoCarinho, getValorTotalDoCarrinho, esvaziarCarrinho } = carrinho();
import { salvarEmprestimo, salvarItemLivro } from "~/services/emprestimo";
const { data } = useAuth();
import { STATUS_PAGAMENTO, type ItemLivroBody } from "~/models/emprestimo";
import { type UsuarioCustomizado } from "~/models/usuario";

definePageMeta({
  middleware: "auth",
});


const UsuarioLogado = computed<any>(() => {
    if (data.value) {
        return data.value ? data.value?.results[0] as UsuarioCustomizado : null;
    }
    return null;
})

const itensNoCarrinho = computed<Array<CarrinhoItem>>(()=>getCarrinho());
const valorTotal = computed(() => getValorTotalDoCarrinho().toPrecision(5));

const carregando = ref(false);
const salvo = ref(false);

console.log("itens No carrinho.....", itensNoCarrinho);

const deletarDoCarrinho = (itemParaRemover: CarrinhoItem) => {
  removerDoCarinho({
    livro: itemParaRemover.livro,
    qtd_estoque: 0
  });
}

const salvarPedido = () => {
  if (getCarrinho().length) {
    carregando.value = true;
    console.log("data", data.value)
    salvarEmprestimo({
      status: STATUS_PAGAMENTO.P,
      usuarioFK: UsuarioLogado.value ? `${UsuarioLogado.value.id}` : ''
     }).then(salvarEmprestimo => {
      console.log("venda salva: ", salvarEmprestimo);
      let payload: Array<ItemLivroBody> = [];
      getCarrinho().forEach(item => {
        payload.push({
          emprestimoFK: salvarEmprestimo?.id ?? 0,
          livroFK: item.livro.id ?? 0,
          qtd_livro: item.qtd_estoque ?? 0,
        })
      });

      salvarItemLivro(payload).then(resposta => {
        console.log("ITENS DE VENDA SALVOS!", resposta);
        setTimeout(() => {
          salvo.value = true;
          
          esvaziarCarrinho();
        }, 3000);
      }).catch(error => {
        console.error("Erro ao salvar venda! ", error);
      });

    }).catch(error => {
      console.error("Erro ao salvar venda! ", error);
    })
      .finally(() => {
        setTimeout(() => {
          carregando.value = false;
        }, 3000);
      });
  }
}

</script>

<template>
  <main class="carrinho-container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4">Seu Carrinho</h2>
    <div class="card flex justify-content-center" v-if="carregando">
      <ProgressSpinner />
    </div>
    <table v-if="!carregando">
      <tbody>
        <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
          <td>
            <div class="item-carrinho">
              <div><img class="fotolivro" :src="itemCarrinho.livro.foto" alt="foto livro" /></div>
              <div>{{ itemCarrinho.livro.nome }}</div>
              <div>{{ itemCarrinho.livro.formato.nome }}</div>
              <div>R$ {{ itemCarrinho.livro.valor_emprestimo }}</div>
              <div>{{ itemCarrinho.qtd_estoque }}</div>
              <div>R$ {{ itemCarrinho.qtd_estoque * itemCarrinho.livro.valor_emprestimo }}</div>
              <div>
                <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
              </div>
            </div>
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr class="text-center">
          <td class="valor-total" colspan="7">Valor Total: R${{ valorTotal }}</td>
        </tr>
      </tfoot>
    </table>
    <Button :disabled="salvo" v-if="!carregando" @click="salvarPedido" class="mt-2 botao-pedido " label="Fechar pedido" />
    <Message v-if="salvo" severity="success">
      <p>Pedido realizado com sucesso!</p>
      <p>Consulte seus itens em <NuxtLink to="/pedidos">Meus Pedidos</NuxtLink> </p>
    </Message>

  </main>
</template>

<style scoped lang="scss">

$largura-tabela: 90vw;
.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: #f6f6f6;
}

table {
  width: $largura-tabela;
  background-color: white;
  border-radius: 1rem;
}

.item-carrinho {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  border-bottom: 2px solid black;
}

.fotolivro {
  width: 50px;
  height: 50px;
}

.valor-total {
  font-weight: bold;
  width: 900px
}

.botao-pedido {
  background-color: #034C8C;
  border: 0px;
  width: 200px;
  height: 50px;

  &:hover {
    background-color: #5B9ED9;
  }
}
</style>
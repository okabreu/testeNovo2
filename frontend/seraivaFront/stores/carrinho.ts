import { defineStore } from "pinia";
import type { Livro } from "~/models/livros";

export type CarrinhoItem = {
    livro: Livro;
    qtd_estoque: number;
}

export type Carrinho = {
    livros: Array<CarrinhoItem>;    
}

export const carrinho = defineStore('carrinhoStore', {
    state: (): Carrinho => ({
        livros: []
    }),
    actions: {
      adicionarNoCarrinho(novoLivro: Livro){
            const LivroJaExiste = this.getLivroDoCarrinho(novoLivro);
            if(LivroJaExiste){
                LivroJaExiste.qtd_estoque += 1;
                this.livros = [
                    ...this.livros.filter(item=>item.livro.id !== LivroJaExiste.livro.id),
                    LivroJaExiste
                ];
            }
            else{
                this.livros.push({
                    qtd_estoque: 1,
                    livro: novoLivro
                });
            }
      },
      removerDoCarinho(carrinhoItem: CarrinhoItem){
        const posicaoNoCarrinho = this.getLivroDoCarrinhoIndex(carrinhoItem.livro);
        this.livros.splice(posicaoNoCarrinho,1);

        if(carrinhoItem.qtd_estoque){
            this.livros = [
                ...this.livros,
                carrinhoItem
            ];
        }
      },
      esvaziarCarrinho(){
        this.livros = [];
      }
    },
    getters: {
        estaNoCarrinho: (carrinho:Carrinho) => (LivroParaEncontrar: Livro): boolean =>{
            return carrinho.livros.findIndex(item=>item.livro.id === LivroParaEncontrar.id) !== -1;
        },
        getLivroDoCarrinho: (carrinho:Carrinho) => (LivroParaEncontrar: Livro)=>{
            return carrinho.livros.find(item=>item.livro.id === LivroParaEncontrar.id);
        },
        getLivroDoCarrinhoIndex: (carrinho:Carrinho) => (LivroParaEncontrar: Livro)=>{
            return carrinho.livros.findIndex(item=>item.livro.id === LivroParaEncontrar.id);
        },
        getCarrinho: (carrinho: Carrinho) => () : Array<CarrinhoItem> => {
            return carrinho.livros;
        },
        getValorTotalDoCarrinho: (carrinho: Carrinho) => () : Number => {
            let soma = 0;
            carrinho.livros.forEach(item=>{
                soma += (item.livro.valor_emprestimo * item.qtd_estoque)
            })
            return soma;
        }
    }
  })
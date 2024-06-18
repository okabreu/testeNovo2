import type { Livro } from "./livros";
import type { UsuarioCustomizado } from "./usuario";

export enum STATUS_PAGAMENTO {
    'P' = "P",
    'A' = "A",
    'C' = "C",
    'R' = "R",
}

export type Emprestimo = {
    id?: number;
    usuarioFK: string;
    data_emprestimo?: string;
    status: STATUS_PAGAMENTO;
} 

export type ItemLivro = {
    livroFK: Livro;
    emprestimoFK: Emprestimo;
    qtd_livro: number;
}

export type ItemLivroBody = {
    livroFK: number;
    emprestimoFK: number;
    qtd_livro: number;
}
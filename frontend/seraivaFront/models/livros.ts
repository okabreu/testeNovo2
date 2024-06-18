export type Formato = {
    id: number;
    nome: string;
}

export type Genero = {
    id: number;
    nome: string;
}

export type Autor = {
    id: number;
    nome: string;
    biografia: string;
    foto: string;
}

export type Livro = {
    id: number;
    nome: string;
    autor: Autor;
    ano: number;
    genero: Genero;
    qtd_paginas: number;
    formato: Formato;
    numero_edicao: number;
    descricao: string;
    valor_emprestimo: number;
    qtd_estoque: number;
    estrelas: number;
    foto: string;
}


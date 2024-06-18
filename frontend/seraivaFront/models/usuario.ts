export type Groups = {
    id: number;
    nome: string;

}

export type UsuarioCustomizado ={
    id: number;
    nome: string;
    email: string;
    endereco: string;
    cpf: number;
    Groups: Groups;
}
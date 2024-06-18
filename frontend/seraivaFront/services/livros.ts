import { BACKEND_URL } from "~/models/app";
import type { Pagination } from "~/models/pagination";
import type { Livro } from "~/models/livros";

export const getLivro = (numeroPagina: number = 0): Promise<Pagination<Livro>|null>  => {
  return useFetch<Pagination<Livro>>(`${BACKEND_URL}/livro?page=${numeroPagina}`)
    .then(resposta=> {
      return Promise.resolve(resposta.data.value);      
    })
    .catch(error=>{
      console.log("error", error);
      return Promise.resolve(null);
    })  
};
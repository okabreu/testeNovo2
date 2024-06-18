import { BACKEND_URL } from "~/models/app";
import type { Emprestimo,ItemLivro,ItemLivroBody } from "~/models/emprestimo";

export const salvarEmprestimo = (emprestimo: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimo/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};

export const salvarItemLivro = (emprestimo: Array<ItemLivroBody>): Promise<ItemLivro | null> => {
  return useFetch<ItemLivro>(`${BACKEND_URL}/itemLivro/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};
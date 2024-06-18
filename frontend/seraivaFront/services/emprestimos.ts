import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, STATUS_PAGAMENTO } from "~/models/emprestimo";
import type { Pagination } from "~/models/pagination";

// Função para obter empréstimos
export const getEmprestimos = (numeroPagina: number = 0): Promise<Pagination<Emprestimo> | null> => {
  return fetch(`${BACKEND_URL}/emprestimo?page=${numeroPagina}`)
    .then((resposta: Response) => resposta.json())
    .then((data: Pagination<Emprestimo>) => {
      return Promise.resolve(data);
    })
    .catch((error: Error) => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};

// Função para atualizar o status do empréstimo
export const updateEmprestimoStatus = (id: number, status: STATUS_PAGAMENTO): Promise<Emprestimo | null> => {
  return fetch(`${BACKEND_URL}/emprestimo/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ status })
  })
    .then((response: Response) => {
      if (!response.ok) {
        throw new Error('Erro ao atualizar o status');
      }
      return response.json();
    })
    .then((data: Emprestimo) => {
      return Promise.resolve(data);
    })
    .catch((error: Error) => {
      console.log("error", error);
      return Promise.resolve(null);
    });
};

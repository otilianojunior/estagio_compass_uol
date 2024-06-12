### Desafio Etapa 2:

Para responder esta etapa do desafio, é necessário responder a alguns questionamentos.

1. **É possível reutilizar containers?**

   Sim, é possível reutilizar um container que já foi utilizado antes, desde que saibamos seu nome ou ID. Para listar todos os containers executados recentemente, utilize o comando abaixo:

   ```bash
   docker ps -a
   ```

2. **Comando necessário para reiniciar um container que esteja parado:**

   Para reiniciar o container desejado, que apareceu na lista gerada pelo comando anterior, utilize o comando a seguir:

   ```bash
   docker start <nome_ou_id>
   ```

3. **Visualização dos logs de um container:**

   Para ver todos os resultados da execução daquele container, utilize o comando:

   ```bash
   docker logs <nome_ou_id>
   ```

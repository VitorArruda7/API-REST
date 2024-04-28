Pré-requisitos:
Docker instalado e configurado no sistema.

Passo 1: Clone o repositório

Passo 2: Navegue até o diretório do projeto
```
cd <nome_do_diretório>
```

Passo 3: Construa e inicie os contêineres
Use o Docker Compose para construir e iniciar os contêineres definidos no arquivo docker-compose.yml

Execute o comando:
```
docker-compose up -d
```

Este comando irá construir as imagens necessárias e iniciar os contêineres em segundo plano.

Passo 4: Acesse a API Flask
Depois que os contêineres estiverem em execução, você pode acessar a API Flask usando um navegador da web ou uma ferramenta de cliente HTTP

---

Para acessar todos os atendimentos acesse:

```
http://localhost:8001/api/v1/atendimentos
```

---

Para filtrar os atendimentos por data:

```
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01
```

Onde 2024-01-01 é o campo que deve ser inserida a data do atendimento que deseja pesquisar.

---

Para filtrar os atendimentos por condição de saúde:

```
http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao
```

Onde hipertensao é o campo que deve ser inserida a condição de saúde do paciente, podendo ser: hipertensao|diabetes|ferida vascular|dengue|tuberculose.

---

Para filtrar os atendimentos por unidade de saúde:

```
http://localhost:8001/api/v1/atendimentos?unidade=Unidade%20de%20saude%20Daniela
```

Onde Unidade%20de%20saude%20Daniela é o campo em que deve ser inserido o nome da unidade de saúde em que foi feito o atendimento.

---

Para filtrar mais de uma informação em uma única pesquisa também é possível combinar os filtros desejados.

```
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=hipertensao
```

Onde estariamos filtrando por atendimentos realizados em 2024-01-01 em que o paciente atendido tem hipertensão.

---

Passo 5: Parar e limpar os contêineres

Para isso você pode executar:
```
docker-compose down
```

Isso encerrará os contêineres e removerá todos os recursos associados a eles.

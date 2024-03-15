# Criando um Recurso no Azure AI Search e Azure AI Services

## Ideia do Projeto:

O projeto visa criar uma solução de pesquisa e análise de insights a partir de avaliações de clientes para a Fourth Coffee, uma cadeia nacional de café. Utilizando recursos do Azure AI Search e Azure AI Services, é possível extrair dados das avaliações dos clientes, enriquecer esses dados com informações geradas por IA e realizar pesquisas avançadas sobre os insights obtidos.

## Passo a Passo:

### 1. Criar um Recurso no Azure AI Search:

* Acesse o portal Azure (https://portal.azure.com).
* Clique no botão **+ Criar um recurso** e pesquise por "Azure AI Search".
* Selecione "Azure AI Search" na lista de resultados.
* Preencha as configurações necessárias:
    - **Assinatura:** Selecione sua assinatura do Azure.
    - **Grupo de recursos:** Escolha um grupo de recursos existente ou crie um novo.
    - **Nome do serviço:** Escolha um nome único para o serviço.
    - **Localização:** Selecione uma região disponível.
    - **Plano de Preços:** Escolha o plano de preços "Básico".
* Clique em **Revisar + criar** e, em seguida, em **Criar** após a validação ser concluída.

### 2. Criar um Recurso no Azure AI Services:

* No portal Azure, clique novamente no botão **+ Criar um recurso** e pesquise por "Azure AI Services".
* Selecione "Azure AI Services" na lista de resultados.
* Configure o recurso com as seguintes configurações:
    - **Assinatura:** Sua assinatura do Azure.
    - **Grupo de recursos:** O mesmo grupo de recursos do recurso Azure AI Search.
    - **Localização:** A mesma região do recurso Azure AI Search.
    - **Nome do recurso:** Escolha um nome único para o recurso.
    - **Plano de Preços:** Selecione o plano de preços "Padrão S0".
* Clique em **Revisar + criar** e, em seguida, em **Criar** após a validação ser concluída.

### 3. Criar uma Conta de Armazenamento:

* Novamente no portal Azure, clique em **+ Criar um recurso** e pesquise por "Conta de Armazenamento".
* Selecione "Conta de Armazenamento" na lista de resultados.
* Configure a conta de armazenamento com as seguintes configurações:
    - **Assinatura:** Sua assinatura do Azure.
    - **Grupo de recursos:** O mesmo grupo de recursos do recurso Azure AI Search.
    - **Nome da conta:** Escolha um nome único para a conta.
    - **Localização:** Escolha uma região disponível.
    - **Desempenho:** Padrão.
    - **Redundância:** Armazenamento com redundância local (LRS).
* Clique em **Revisar + criar** e, em seguida, em **Criar** após a validação ser concluída.

### 4. Carregar Documentos para o Armazenamento Azure:

* Acesse a conta de armazenamento criada no portal Azure.
* Na seção de Containers, crie um novo container com o nome "coffee-reviews" e configure o nível de acesso público como "Contêiner" (acesso anônimo para contêineres e blobs).
* Baixe os documentos de avaliações de café do link fornecido e extraia os arquivos para uma pasta local.
* Faça upload dos arquivos extraídos para o container "coffee-reviews" criado na conta de armazenamento.

### 5. Indexar os Documentos no Azure AI Search:

* No portal Azure, navegue até o recurso Azure AI Search criado.
* Na página Visão geral, selecione **Importar dados**.
* Siga o assistente de importação de dados para criar uma fonte de dados para o armazenamento Azure Blob e configurar o enriquecimento de dados com habilidades de IA.
* Crie um índice e um indexador para importar os documentos do armazenamento Azure Blob para o Azure AI Search.
* Aguarde até que o indexador seja executado com sucesso, garantindo que todos os documentos sejam indexados corretamente.

## Recursos Adicionais:

* Documentação do Azure AI Search: [Link](https://docs.microsoft.com/pt-br/azure/search/)
* Documentação do Azure AI Services: [Link](https://docs.microsoft.com/pt-br/azure/cognitive-services/)
* Tutorial de introdução ao Azure AI Search: [Link](https://docs.microsoft.com/pt-br/azure/search/search-what-is-azure-search)
* Tutorial de introdução ao Azure AI Services: [Link](https://docs.microsoft.com/pt-br/azure/cognitive-services/cognitive-services-apis-create-account)

## Rodar o projeto:

* clonar o projeto
* rodar pip install -r requirements.txt
* entrar na pasta src
* rodar o comando python app.py

![Projeto](https://raw.githubusercontent.com/VicLira/coffee-review-document-analysis/main/src/imgs-readme/project.png)


**Este foi o guia passo a passo para criar e configurar os recursos necessários no Azure para o projeto de pesquisa e análise de insights da Fourth Coffee usando Azure AI Search + Azure AI Services e storage account.**

**Obrigado pela atenção! Se tiver dúvidas, entre em contato através do meu e-mail: victor.liracarlos@gmail.com**
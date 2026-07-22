# Portal AEFP

## Visão Geral

O **Portal AEFP** é uma plataforma institucional para consolidação, exploração e visualização de dados relacionados às atividades da Assessoria de Ensino e Fomento à Pesquisa (AEFP).

O sistema foi concebido para transformar bases de dados dispersas em um **atlas digital integrado**, permitindo navegação por:

- Países;
- Continentes;
- Programas;
- Projetos;
- Instituições;
- Bolsas;
- Indicadores;
- Séries históricas;
- Dados consolidados para download.

O portal utiliza visualizações interativas, mapas geográficos e painéis analíticos para ampliar a transparência, rastreabilidade e capacidade de análise das informações institucionais.

---

# Objetivos

O Portal AEFP busca responder perguntas como:

- Em quais países existem projetos ativos?
- Quais instituições estão vinculadas aos programas?
- Como a cooperação internacional evoluiu ao longo do tempo?
- Quantas bolsas foram concedidas por modalidade?
- Quais programas concentram mais recursos?
- Como os indicadores se distribuem geograficamente?

---

# Arquitetura Geral

```text
Frontend (Next.js)
        │
        ▼
Backend (FastAPI)
        │
        ▼
PostgreSQL + PostGIS
        │
        ▼
Bases de Dados AEFP
```

---

# Tecnologias Utilizadas

## Frontend

### Next.js

Responsável pela interface web.

Utilizado para:

- Páginas do portal;
- Roteamento;
- Renderização híbrida;
- Otimização de desempenho.

Exemplos de módulos:

- Home
- Atlas
- Projetos
- Programas
- Indicadores
- Downloads

### TypeScript

Utilizado para tipagem estática.

Benefícios:

- Menor incidência de erros;
- Melhor manutenção;
- Documentação implícita do sistema.

### TailwindCSS

Framework de estilização.

Benefícios:

- Desenvolvimento rápido;
- Consistência visual;
- Redução de CSS repetitivo.

### TanStack Query

Gerenciamento de requisições.

Responsável por:

- Cache;
- Sincronização;
- Atualização automática dos dados.

### Leaflet

Biblioteca para mapas interativos.

Utilizada no Atlas Geográfico.

Permite:

- Zoom;
- Filtros por país;
- Exibição de projetos;
- Visualização de indicadores.

### Recharts

Biblioteca de gráficos.

Utilizada para:

- Séries temporais;
- Rankings;
- Comparações institucionais.

---

## Backend

### FastAPI

Framework principal da API.

Responsável por:

- Endpoints REST;
- Documentação automática;
- Integração com banco de dados.

Exemplos:

```http
GET /countries
GET /projects
GET /institutions
```

### SQLAlchemy

ORM utilizado para comunicação com o banco.

Benefícios:

- Abstração do SQL;
- Manutenção simplificada;
- Suporte a migrações.

### Alembic

Sistema de versionamento do banco.

Permite:

- Registrar alterações;
- Reproduzir ambientes;
- Manter histórico estrutural.

### Pydantic

Validação de dados.

Responsável por:

- Validar entradas;
- Validar saídas;
- Garantir consistência.

### GeoAlchemy2

Extensão espacial.

Permite operações geográficas utilizando PostGIS.

---

## Banco de Dados

### PostgreSQL

Banco relacional principal.

Armazena:

- Países;
- Instituições;
- Programas;
- Projetos;
- Bolsas;
- Indicadores.

### PostGIS

Extensão geográfica utilizada para:

- Coordenadas;
- Geometrias;
- Consultas espaciais.

---

# Estrutura do Repositório

```text
portal-aefp/
│
├── back/
├── front/
├── database/
├── docs/
├── docker-compose.yml
├── README.md
└── .env.example
```

---

# Estrutura de Dados

## Entidades Principais

```text
continents
countries
institutions
programs
projects
scholarships
indicators
```

## Relacionamentos

```text
project_countries
project_institutions
scholarship_institutions
```

---

# Configuração do Ambiente

## Clonar o Projeto

```bash
git clone <repositorio>

cd portal-aefp
```

---

# Configuração do Banco de Dados

Criar um arquivo `.env` ou utilizar as variáveis:

```env
POSTGRES_DB=aefp
POSTGRES_USER=aefp
POSTGRES_PASSWORD=aefp
```

Executar os containers:

```bash
docker compose up -d
```

Verificar execução:

```bash
docker ps
```

---

# Configuração do Backend

Entrar na pasta:

```bash
cd back
```

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente:

### Linux/Mac

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Criar o arquivo `.env`:

### Desenvolvimento Local

```env
DATABASE_URL=postgresql://aefp:aefp@localhost:5432/aefp

APP_NAME=Portal AEFP

DEBUG=True
```

### Docker Compose

Quando o backend estiver rodando dentro de um container Docker e o serviço PostgreSQL se chamar `db`:

```env
DATABASE_URL=postgresql://aefp:aefp@db:5432/aefp

APP_NAME=Portal AEFP

DEBUG=True
```

Executar:

```bash
uvicorn app.main:app --reload
```

Abrir:

```text
http://localhost:8000/docs
```

---

# Configuração do Frontend

Entrar na pasta:

```bash
cd front
```

Instalar dependências:

```bash
npm install
```

Criar arquivo `.env.local`:

### Desenvolvimento Local

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Executar:

```bash
npm run dev
```

Abrir:

```text
http://localhost:3000
```

---

# Uso com GitHub Codespaces

## Backend

Quando utilizado junto com Docker Compose:

```env
DATABASE_URL=postgresql://aefp:aefp@db:5432/aefp
```

O hostname `db` funciona porque os containers compartilham a mesma rede Docker.

Caso o FastAPI esteja sendo executado fora do container:

```env
DATABASE_URL=postgresql://aefp:aefp@localhost:5432/aefp
```

ou

```env
DATABASE_URL=postgresql://aefp:aefp@127.0.0.1:5432/aefp
```

dependendo da configuração da porta.

---

## Frontend

Durante o desenvolvimento normalmente é utilizado:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Entretanto, ao expor portas no GitHub Codespaces, o endereço pode assumir o formato:

```text
https://SEU-CODESPACE-8000.app.github.dev
```

Exemplo:

```env
NEXT_PUBLIC_API_URL=https://SEU-CODESPACE-8000.app.github.dev
```

---

# Fluxo de Funcionamento

```text
Usuário
   │
   ▼
Interface Next.js
   │
   ▼
Axios
   │
   ▼
FastAPI
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL/PostGIS
   │
   ▼
Retorno dos Dados
   │
   ▼
Mapas e Gráficos
```

---

# Boas Práticas Implementadas

- Arquitetura modular;
- Separação entre frontend e backend;
- Banco de dados espacial;
- Versionamento de banco de dados;
- Uso de variáveis de ambiente;
- Estrutura orientada a domínio;
- API documentada automaticamente;
- Componentização da interface;
- Escalabilidade para novos módulos.

---

# Segurança

O portal deve observar:

- Proteção de dados pessoais;
- Minimização de exposição pública;
- Validação de entradas;
- Controle de acesso administrativo;
- Auditoria de alterações de dados.

> Nenhum dado sensível deve ser disponibilizado publicamente sem avaliação prévia de sua necessidade institucional e conformidade normativa.

---

# Roadmap de Desenvolvimento

## Fase 1

- Estrutura do projeto;
- Banco de dados;
- API inicial.

## Fase 2

- Atlas Geográfico;
- Importação de dados;
- Rotas institucionais.

## Fase 3

- Indicadores;
- Dashboards;
- Downloads.

## Fase 4

- Otimização;
- Testes;
- Publicação.

---

# Documentação Complementar

A documentação técnica deverá ser mantida em:

```text
docs/
│
├── arquitetura/
├── metodologia/
├── dicionario-dados/
└── wireframes/
```

Objetivos:

- Garantir rastreabilidade das decisões arquiteturais;
- Registrar metodologias adotadas;
- Manter o dicionário de dados atualizado;
- Preservar wireframes e protótipos da interface.

---

# Créditos

## Desenvolvimento e Arquitetura do Portal AEFP

**Marcelo Vaz Oliveira**

Responsável pela concepção, implementação, modelagem de dados, integração dos componentes e evolução do sistema.

## Suporte Técnico e Apoio Arquitetural

**M365 Copilot (GPT-5)**

Utilizado como ferramenta de apoio para discussão de arquitetura, organização do projeto, revisão técnica, documentação, modelagem e sugestões de implementação.

Todas as decisões finais de arquitetura, código, modelagem de dados, infraestrutura e publicação são de responsabilidade do desenvolvedor do projeto, que conduziu e implementou a solução.

---

# Licença

Definir conforme orientação institucional e requisitos de publicação do projeto.
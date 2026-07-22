# 1. Estrutura Geral

```bash
HOME
│
├── Visão Geral
│
├── Atlas Geográfico
│   ├── Mundo
│   ├── Continentes
│   ├── Países
│   └── Instituições
│
├── Programas
│   ├── Programa AEFP
│   ├── Cooperação Internacional
│   ├── Capacitação
│   └── Bolsas
│
├── Projetos
│   ├── Todos os Projetos
│   ├── Em execução
│   ├── Concluídos
│   └── Por área temática
│
├── Instituições
│   ├── Nacionais
│   ├── Internacionais
│   └── Redes de Cooperação
│
├── Bolsas
│   ├── Por modalidade
│   ├── Por país
│   ├── Por ano
│   └── Por instituição
│
├── Indicadores
│   ├── Cooperação
│   ├── Formação
│   ├── Produção
│   └── Investimento
│
├── Metodologia
│
└── Download de Dados
```

--- 

# 2. Estrutura de Pastas

```bash
portal-aefp/
│
├── back/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── migrations/
│   ├── tests/
│   ├── .env
│   ├── requirements.txt
│   └── Dockerfile
│
├── front/
│   │
│   ├── public/
│   │   ├── images/
│   │   ├── icons/
│   │   └── maps/
│   │
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx
│   │   │   ├── atlas/
│   │   │   ├── programas/
│   │   │   ├── projetos/
│   │   │   ├── instituicoes/
│   │   │   ├── bolsas/
│   │   │   ├── indicadores/
│   │   │   ├── metodologia/
│   │   │   └── downloads/
│   │   │
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   ├── charts/
│   │   │   ├── maps/
│   │   │   ├── tables/
│   │   │   └── ui/
│   │   │
│   │   ├── features/
│   │   │   ├── atlas/
│   │   │   ├── programas/
│   │   │   ├── projetos/
│   │   │   ├── instituicoes/
│   │   │   ├── bolsas/
│   │   │   └── indicadores/
│   │   │
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── atlas.service.ts
│   │   │   ├── projetos.service.ts
│   │   │   ├── bolsas.service.ts
│   │   │   └── indicadores.service.ts
│   │   │
│   │   ├── hooks/
│   │   │   ├── useAtlas.ts
│   │   │   ├── useProjetos.ts
│   │   │   └── useIndicadores.ts
│   │   │
│   │   ├── lib/
│   │   │   ├── utils.ts
│   │   │   ├── constants.ts
│   │   │   └── validations.ts
│   │   │
│   │   └── types/
│   │       ├── country.ts
│   │       ├── institution.ts
│   │       ├── project.ts
│   │       ├── scholarship.ts
│   │       └── indicator.ts
│   │
│   ├── .env.local
│   ├── next.config.ts
│   ├── tsconfig.json
│   ├── package.json
│   ├── package-lock.json
│   └── Dockerfile
│
├── database/
│   ├── raw/
│   ├── processed/
│   ├── seeds/
│   └── scripts/
│
├── docs/
│   ├── arquitetura/
│   ├── metodologia/
│   ├── dicionario-dados/
│   └── wireframes/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── .devcontainer/
    ├── devcontainer.json
    └── Dockerfile
```

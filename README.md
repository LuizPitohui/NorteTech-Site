# ⚡ Norte Tech - Portal Corporativo & Sistema de Admissão Digital

Este projeto é uma solução web integrada desenvolvida com **Django** que une um **Site Institucional Moderno** a um **Portal de Recrutamento e Seleção (ATS)** completo.

O sistema permite que a empresa gerencie sua presença digital (notícias, serviços, banners) e todo o fluxo de contratação (vagas, banco de talentos, recebimento de currículos e validação de documentos) através de um painel administrativo personalizado.

---

## 🚀 Tecnologias Utilizadas

* **Backend:** Python 3.13 + Django 6.0
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5 (Responsivo)
* **Gerenciador de Pacotes:** Poetry
* **Banco de Dados:** SQLite (Dev) / PostgreSQL (Prod - Recomendado)
* **Ícones:** FontAwesome 6

---

## 🛠 Funcionalidades Principais

### 🌐 Módulo Institucional (Site)
* **Home Dinâmica:**
    * **Carrossel de Banners:** Gerenciável via Admin (Imagem + Título + Texto Justificado).
    * **Seção Sobre Nós:** Vídeo institucional e texto descritivo lado a lado.
    * **Últimas Notícias:** Feed automático das postagens recentes.
* **A Empresa:**
    * **Estatísticas Editáveis:** Números de Colaboradores e Frota editáveis via Admin (`CompanySettings`).
    * **Cultura:** Exibição de Missão e Valores (Campo "Visão" removido conforme diretriz 12/2025).
    * **Bases Operacionais:** Mapa e lista de endereços.
* **Serviços:** Catálogo de serviços prestados pela Norte Tech.
* **LGPD:** Página de Privacidade e Termos de Uso.

### 💼 Módulo Carreiras (Candidato)
* **Portal do Candidato:**
    * Cadastro e Login seguro.
    * **Perfil Completo:** Dados pessoais, currículo (PDF), formação e experiências.
    * **Minhas Candidaturas:** Dashboard visual com barra de progresso (timeline) do status de cada vaga.
* **Vagas & Banco de Talentos:**
    * Busca de vagas abertas.
    * **Aplicação Unificada:** Fluxo para aplicar em vaga específica ou deixar currículo no Banco de Talentos.
    * **Checkbox LGPD:** Aceite obrigatório dos termos antes de aplicar.
* **Onboarding Digital:**
    * Upload de documentos admissionais (RG, CPF, Comprovante de Residência).
    * Feedback visual de status (Em análise, Aprovado, Rejeitado).

### 📊 Módulo Gestão (RH & Admin)
* **Dashboard RH (`/rh/`):**
    * Painel exclusivo separado do Admin técnico.
    * Métricas em tempo real: Funil de contratação, Vagas abertas, Total de candidatos.
* **Gestão de Candidatos:**
    * Visualização de currículos.
    * Mudança de status (Novo -> Entrevista -> Contratado).
    * Validação de documentos (Aprovar/Rejeitar com motivo).
* **Gestão de Conteúdo (CMS):**
    * Controle total de textos, banners, vídeos e configurações da empresa sem tocar em código.

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
* Python 3.10+
* Poetry (Recomendado)

### 1. Clonar e Instalar Dependências

```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/norte-tech-portal.git](https://github.com/seu-usuario/norte-tech-portal.git)
cd norte-tech-portal

# Instale as dependências via Poetry
poetry install
poetry shell

2. Configurar o Banco de Dados
Bash

# Crie as migrações iniciais
python manage.py makemigrations
python manage.py migrate
3. Criar Superusuário (Admin)
Bash

python manage.py createsuperuser
# Siga as instruções para criar login e senha
4. Rodar o Servidor
Bash

python manage.py runserver
Acesse em: http://127.0.0.1:8000/

🔐 Acesso aos Painéis
O sistema possui duas áreas administrativas distintas:

Super Admin (TI/Desenvolvimento):

URL: /admin/

Acesso total a usuários, grupos, permissões e configurações técnicas.

Painel do RH (Gestores):

URL: /rh/

Interface limpa focada em Vagas, Candidatos e Dashboard de Métricas.

📂 Estrutura do Projeto
Plaintext

norte-tech-site/
├── config/             # Configurações globais (settings, urls)
├── core/               # App Institucional (Home, Sobre, Notícias, Contato)
├── careers/            # App de Recrutamento (Vagas, Candidatos, RH)
├── accounts/           # App de Usuários (Login, Registro, Perfil)
├── services/           # App de Serviços
├── templates/          # Arquivos HTML
│   ├── admin/          # Customizações do Dashboard RH
│   ├── accounts/       # Telas de Login/Perfil
│   └── ...
├── static/             # CSS, JS, Imagens do sistema
└── media/              # Uploads de usuários (Currículos, Fotos, Vídeos)
✅ Histórico de Atualizações Recentes
Refatoração da Home: Implementação de carrossel Bootstrap 5 e Player de vídeo com overlay removido para layout em Grid.

Sistema de Métricas: Criação do Dashboard visual para o RH.

Ajuste Corporativo: Remoção do campo "Visão" e dinamização dos dados de Frota e Colaboradores via CompanySettings.

Banco de Talentos: Implementação de rota para candidatura espontânea sem vínculo com vaga específica.

Desenvolvido por Luiz Fernando da Silva Guedes.
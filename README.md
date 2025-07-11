# 🧪 Sprint 8 – Testes Automatizados com Selenium e POM | Urban Routes

Este repositório contém os testes automatizados desenvolvidos durante o **8º sprint** do bootcamp de QA da TripleTen. O objetivo deste sprint foi aplicar o conhecimento recém-adquirido em **Selenium WebDriver** e no padrão **Page Object Model (POM)** para automatizar o fluxo completo de solicitação de um táxi no aplicativo **Urban Routes**.

## 🎯 Objetivo do Sprint

Durante os sprints anteriores, os testes eram executados manualmente ou com scripts mais simples. Neste sprint, foi proposto refatorar e finalizar o teste completo do aplicativo, agora utilizando Selenium, boas práticas com POM e localizadores eficientes.

## ✅ Funcionalidades testadas

O fluxo de teste contempla todo o processo de solicitação de um táxi, incluindo:

- Definir endereço de partida
- Selecionar o plano **Comfort** (com verificação condicional)
- Preencher o número de telefone com código SMS recuperado via `retrieve_phone_code()`
- Adicionar cartão de crédito (com manipulação de foco no campo CVV)
- Escrever comentário para o motorista
- Solicitar **cobertor e lenços** com verificação de estado
- Solicitar **2 sorvetes**
- Finalizar o pedido de táxi com a tarifa Comfort e exibir a modal de busca de carros
- 
## 🧱 Estrutura

O projeto segue a arquitetura baseada em POM

## 🧩 Detalhes técnicos

- Uso de `setup_class()` e `teardown_class()` para controle do ciclo de vida dos testes
- Localizadores utilizando `By.ID`, `By.CLASS_NAME`, `By.XPATH`, entre outros
- Separação de responsabilidades: métodos de interação com a UI ficam em `pages.py`
- Execução via **Pytest**

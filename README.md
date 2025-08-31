# PointCounter

## Descrição

PointCounter é um projeto simples feito em Flask que permite aos usuários contar pontos em qualquer jogo.  
O objetivo é praticar desenvolvimento web com Python e Flask, além de criar uma interface web simples usando HTML e CSS.

---

## Tecnologias utilizadas

- Python  
- Flask  
- HTML  
- CSS  

---

## Como executar

1. Baixe ou clone este repositório.  
2. Instale a biblioteca Flask.  
3. Execute o arquivo `manage.py` e acesse o endereço que será mostrado no terminal.

---

## Estrutura do Projeto

- PointCounter/
- ├── static/ ← Pasta com arquivos estáticos:
- │ └── css/ ← CSS usado no projeto
- ├── templates/ ← Templates HTML 
- │      ├── empate.html(aparece caso o jogo empate em pontos)
- │      ├── pontos.html(interface onde os pontos sao digitados)
- │      ├── time1.html(aparece caso o time 1 tenha mais pontos que o time 2)
- │      └── time2.html(aparece caso o time 2 faca mais pontos que o time 1)
- ├── manage.py ← Arquivo principal com a lógica do Flask (rotas, lógica de contagem)
- └── README.md ← Documentação do projeto (este arquivo)
  

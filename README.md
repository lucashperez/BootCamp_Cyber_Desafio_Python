
# Desafio Python — Keylogger & Ransomware

Este repositório contém dois projetos desenvolvidos com foco no estudo de criptografia, segurança da informação e captura de eventos de teclado.  
---

## 📁 Estrutura do Projeto

```
Desafio_python/
├── Keylogger/
│   ├── keylogger.py
│   ├── keylogger_email.py
│   ├── log.txt
│   └── images/
│       └── (prints do processo funcionando)
│
└── Ransomware/
    ├── ransoware.py
    ├── descriptografar.py
    ├── chave.key
    ├── LEIA ISSO.txt
    ├── imagens/
    └── test_files/
```

## 🔐 1. Keylogger

O módulo **Keylogger** captura teclas pressionadas e registra em `log.txt`.  
Também inclui uma versão que envia o log por e-mail (**keylogger_email.py**).

### Recursos:
- Registro de teclas pressionadas  
- Print demonstrando captura  
- Envio automático por e‑mail (para testes locais)

## 🕵️ 2. Ransomware (Simulação)

O módulo **Ransomware** realiza uma simulação de criptografia de arquivos em um diretório.  
Inclui:
- `ransoware.py` → criptografa arquivos  
- `descriptografar.py` → restaura os arquivos  
- `chave.key` → chave gerada automaticamente  
- Pasta `test_files/` com arquivos de exemplo


## 📸 Imagens

As pastas `images/` incluem capturas demonstrativas:
- Arquivos criptografados  
- Arquivos descriptografados  
- Prints do keylogger funcionando  
- Exemplo de recebimento de e-mail

## 🛡 Técnicas de Proteção
Arquivo com algumas das técnicas que podem fazer a diferença em um ambiente de segunra
- Orientação de usuários
- Firewall
- Antivírus 



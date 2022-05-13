# Freelaway
Freelaway - PSW 3.0 (Pystack Week) Projeto de site freelancer utilizando DJANGO.

Desenvolvida uma aplicação completa para conectar empresas e freelances.

# Live Demo
https://otavio-freelaway.herokuapp.com
<br>

## Descrição
O projeto conta com as seguintes **Funcionalidades**:

- Autenticação, Recuperação de senha e Cadastro de Usuário:
<img alt="autenticação" src="img/auth.png">

- Listagem, Filtragem de busca, Detalhes e Aceite de Jobs:
<img alt="encontrar jobs" src="img/encontrar_jobs.png">
<img alt="detalhes" src="img/detalhes.png">
- Atualização de Perfil, Listagem de Jobs Aceitos e Envio de Arquivos:
<img alt="perfil" src="img/perfil.png">
<img alt="enviar" src="img/enviar.png">



## Para instalar

1 - Primeiro clone o repositório e entre na pasta do projeto.

```bash
# Clone este repositório
$ git clone https://github.com/navegantes/freelaway

# Entre na pasta
$ cd freelaway
```

2 - Segundo inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv

#Ativar
  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3 - Instale as dependências

```bash
# Instale as dependências
# Linux
$ pip3 install -r requirements.txt
# Windows
$ pip install -r requirements.txt
```

4 - Faça as migrações.

```bash
# Linux
python3 manage.py migrate
# Windows
python manage.py migrate
```

5 - Crie um super usuário

```bash
$ python3 .\manage.py createsuperuser
$ python .\manage.py createsuperuser
```

6 - Inicie a aplicação

```bash
# Para iniciar o projeto
# Linux
$ python3 manage.py runserver
# Windows
$ python manage.py runserver

# O app vai inicializar em <http://127.0.0.1:8000/>

# Para iniciar o projeto em uma porta especifica
$ python manage.py runserver <porta>

# O app vai inicializar em <http://127.0.0.1:<porta>/>

```
## Próximos passos:
- Criar botão para cancelar o job selecionado ✔
- Criar página inicial
- Adicionar o logout na barra de navegação


# Base do projeto

Projeto utilizando Django e Pillow desenvolvido com base no projeto proposto na PYSTACK WEEK 3.0 promovida pelo
Pythonando de 04 a 10 de abril de 2022.

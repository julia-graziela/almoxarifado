### 👉 Configurações via `Windows` 

> Instale os modulos via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Inicializar

```bash
$ python manage.py runserver
```

Irá rodar na porta: `http://127.0.0.1:8000/`. 

<br />

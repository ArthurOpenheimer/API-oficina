# API-oficina


## Sobre a API
Este projeto é uma API dedicada a uma oficina de veículos, suas features são:<br />
• Realizar CRUD de veículos.<br />
• Realizar CRUD de clientes.<br />
• Realizar CRUD de funcionários.<br />
• Realizar CRUD de serviços.<br />

A API possui rotas para listar todos os dados citados, além de também listar:<br />
• Veículos de um cliente.<br />
• Serviços realizados em um veículo.<br />
• Servicos realizados por um funcionário.<br />


O projeto conta com um export do Insomnia, localizado [r2h]https://github.com/ArthurOpenheimer/API-oficina/tree/main/documentos<br />


## Instalação
Antes de começar, você deve ter instalado o [Git](https://git-scm.com) em seu computador, além disso é bom ter um editor para trabalhar com o código como por exemplo, o [VSCode](https://code.visualstudio.com/)

1- Clone este repositório
```bash
$ git clone https://github.com/ArthurOpenheimer/API-oficina.git
```

2- Abra a pasta "API-oficina" em um terminal

3- Instale os requerimentos(requirements.txt) usando o seguinte comando:
```bash
$ pip install -U -r requirements.txt
```

4- No terminal, rode o seguinte comando para inicializar o servidor:
```bash
$ python manage.py runserver
```

5- Acesse o site: <http://localhost:8000/> para testar a API
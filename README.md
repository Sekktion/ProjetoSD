ProjetoSD é um pequeno projeto prático dos conceitos aprendidos em aula durante o curso de Sistemas Distribuídos como parte do bacharelado em Ciência da Computação.
Seu propósito é exemplificar estratégias de comunicação entre diferentes instâncias de um servidor através de um _broker_, no caso, o MQTT e de implementação de _Middleware_ de comunicação entre Cliente e Servidor utilizando Remote Procedure Calls através do gRPC.
Possui capacidade de comunicar mudanças e atualizar outras instâncias do servidor em tempo real, armazenando os dados em memória volátil.

# Key-value store client

Implementação de KVS como conseguimos de acordo com [estas](https://paulo-coelho.github.io/ds_notes/projeto/) especificações. 


## Esclarecimentos

Nem todos os requisitos foram implementados, mas dentre os realizados estão:
* Portal e Cliente Administrativos.
* Comunicação entre Portais e Clientes por gRPC.
* Comunicação entre os Portais via MQTT.
* Armazenamento dos dados no cache local dos Portais.

Vale enfatizar então que o Portai e o Cliente de matrícula não foram implementados.
Para mais detalhes, [DIFICULDADES.md](https://github.com/Sekktion/ProjetoSD/blob/main/DIFICULDADES.md#descrição-das-dificuldades-com-indicação-do-que-não-foi-implementado).

## Utilização
### Instalando Dependências

* Execute ```compile.sh``` para instalação das dependências do projeto.

### Mosquitto

* Para comunicação entre Portais foi utilizada a biblioteca ```paho-mqtt``` na versão 1.5.1 e, para seu funcionamento, o MQTT deve estar em execução na porta 1883.
* Obtenha o software do broker MQTT [aqui](https://mosquitto.org/download/).

### Servidores (Seus próprios servidores)

* Execute ao menos uma instância do portal Administrativo através do ```admin_server.sh```.
* Informe, no terminal, uma porta diferente para cada instância quando solicitada.

### Clientes

* Execute ao menos uma instância do cliente Administrativo (até 10 conexões simultâneas em um servidor) através de ```admin_client.sh```.
* Siga as instruções conforme dito pela interface no terminal.

## Exemplos de uso do Cliente

Exemplos de criação e listagem de Alunos, Professores e Disciplinas.

```bash
#!/bin/bash

pipenv shell

# cria alguns alunos
python3 admin_client.py
1010
1
11811BCC009
Vinicius

python3 admin_client.py
2020
1
11911BCC021
Gabriel

#cria alguns professores
python3 admin_client.py
1010
6
11111
Gina

python3 admin_client.py
2020
6
22222
Paulo

#cria algumas disciplinas com nome e código
python3 admin_client.py
1010
11
GBC074
SistemasDistribuidos

python3 admin_client.py
1010
11
GBC204
ComputacaoGrafica

#lista alunos cadastrados nos portais administrativos
python3 admin_client.py
1010
5

#lista professores cadastrados nos portais administrativos
python3 admin_client.py
2020
10

#lista disciplinas cadastrados nos portais administrativos
python3 admin_client.py
1010
15
```

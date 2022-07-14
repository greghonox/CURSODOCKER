# docker swarm

## Onde rodar ?

### Da para rodar local, mas a impressão de ver as orquestração dos serviços fica ruim. Para isso abaixo tem um local gratuito para testar.
[doker labs](https://labs.play-with-docker.com/)

## Oque é ?

### Para começar o *docker swarm* é um orquestrador de container.

## Onde começar:

### O docker swarm já vem instalado no docker. Para inicializar faça:

``` python
docker swarm init --advertise-addr [IP_HOST]
```

## Ele ira gerar algo semelhante a isso:

``` python
docker swarm join --token SWMTKN-1-1ctz5yc53a78862trhglawc86fuaz1y1xj95xnxovo388qwa25-bu7enogqr4jem8ev1t9z8nhrb 192.168.0.18:2377
```

## Para conectar em outras maquinas e tornalas *nodes* só utilizar o comando acima. Sua sintaxe:

``` python
docker swarm join --token TOKE IP:2377
```

## Para listar os *nodes* conectados

``` python
docker node ls
```

## Para *criar serviços* por exemplo vamos inicializar o nginx
## Apenas o *Manager* __pode executar os comandos que vem abaixo__

``` python
docker service create --name nginx -p 80:80 nginx
```

## Para *listar os serviços* que estão rodando

``` python
docker service ls
```

## Para *remover os serviços* que estão rodando

``` python
docker service rm id
```

## Criando *container swarm*
### A idéia é utilizar um arquivo *docker-compose.yaml* para gerar seus containers.

``` python
docker stack deploy -c docker-compose.yaml nome_servicos
docker stack deploy -c docker-compose.yaml flask_service
```

## *Scalando nos outros nodes*
### Agora que temos um manager. Podemos *orquestrar para outros nodes executar* os container

``` python
docker service scale nome_servicos=quantidade
docker service scale flask_servic=10
```
## Para *recuperar o token do manager* faça:

```
docker swarm join-token manager
docker info
```

## Para *um node  sair do projeto* faça:
### Com o comando abaixo você poderá listar os node e services e ira perceber uma lista atualizada da situação

```
docker swarm leave
```

## Para *remover um node do projeto* faça:
### Com o comando abaixo você poderá listar os node e services e ira perceber uma lista atualizada da situação

```
docker node rm id
```

## Para sair

```
docker swarm leave -f
```


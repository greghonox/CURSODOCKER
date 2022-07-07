# docker-compose
## Com docker compose pode ser levatar varias imagens com apenas o comando:

``` python
docker compose up
```

## Para se derrubar as imagens em execução:

``` python
docker compose down
```

## Quando se deseja criar um *build* dos *Dockerfile* não precisa expecifiar a imagem conforme abaixo:

``` python
services:
  db:
    image: flaskcompose
```

## Essa troca é necessário para não fazer o proesso manual de *build* em cada pasta separada e depois vir rodar o *up*. __Lembrando que a image mostrado acima é o nome que foi passado como parametro --name__.

## Com a instrução abaixo, só precisa passar o nome da pasta e não o Dockerfile

``` python
services:
  flask:
    build: ./flask
```
## Passos para gerar um container executavel

### 1. rode o __comando para gerar o build__, depois de feito os arquivos com o Dockerfile
``` python
docker build . -t nods
```

### 2. Rodar o container
``` python
docker run -d -p 5001:5001 --name nods nods
```

### 3. Caso deseja rodar o container **nods**, já feito anteriormente, ele ira aproveitar todos os argumentos passado anteriormente
``` python
docker start ndos
```

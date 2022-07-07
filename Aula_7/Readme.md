# docker-compose com bind do diretorio

### O detalhe especial esta aqui:
1. O *Dockefile*  não deve ter ter o *COPY* para o container
2. No *docker-compose.yaml* deve ficar assim:

``` python
services:
  flask:
    volumes:
      - /Users/gregoriohonorato/Documents/PROJETOS/APRENDIZADOS/CursoDocker/Aula_7/flask:/app
```

### Veja que o caminho é host:container. 
### Do lado esquerdo você deve pensar no diretorio com os arquivos de scripts. No nosso caso os **.py*.
### Do lado direito você deve colocar o *WORKDIR*.

### No exemplo que estamos usando o flask, é legal utilizar ele como *debug=True* para perceber a atualização quando salvar.
## Como rodar o python isolado dos arquivos de desenvolvimento ?

### Essa é a ideia dessa aula.

### Para isso utilize o *Dockerfile* criado depois utilize o comando no terminal para gerar o container.

``` python
docker build . -t python_docker
```

### Para rodar o main.py junto com o docker:

``` python
docker run -v /Users/gregoriohonorato/Documents/PROJETOS/APRENDIZADOS/PYTHON/:/app -v /tmp/:/tmp/ python_docker
```

### Depois você pode aproveitar e chamar esse container sem gerar um novo utilizando run dessa forma. Ele ira aproveitar os parametros passado anteriormente.

``` python
docker start python_docker
```


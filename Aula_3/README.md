## Como ter um docker com ambiente grafico ? Muito louco em pensar nisso mas existe

### Para isso utilize o *Dockerfile* criado depois utilize o comando no terminal para gerar o container.

``` python
docker build . -t kasmweb
```

### Para rodar o main.py junto com o docker:

``` python
docker run --rm  -it --shm-size=512m -p 6901:6901 -e VNC_PW=password kasmweb
```

### Depois você pode aproveitar e chamar esse container sem gerar um novo utilizando run dessa forma. Ele ira aproveitar os parametros passado anteriormente.

``` python
docker start kasm
```

### USUARIO: *kasm_user*
### SENHA: *password*
# Curso de docker.

# Indice:
## __Aula_1__
### Introdução basica com *Dockerfile* básico para gerar a primeira imagem.
### Trabalhando aqui com *node*

## __Aula_2__
### Ainda trabalhando com *Dockerfile* básico.
### Aqui vemos como criar uma imagem para desenvolvimento, mapeando a pasta de trabalho com o container. Super importante para não ter briga para gerar um setup de desenvolvimento.

## __Aula_3__
### Curiosidades... Como gerar um ambiente gráfico para o docker? Essa aula eu trago essa curiosidade com *kasm*.

## __Aula_4__
### Hora de praticar

## __Aula_5__
### Introdução ao *docker compose*
### Aqui geramos um ambiente com *wordpress* + *mysql*. No final não dar certo. O banco de dados fica inacessivel.

## __Aula_6__
### Continuando com *docker compose*. Mas agora trabalhando com flask + mysql no mesmo *docker-compose.yaml*.
### Por se tratar de continuar a introdução do docker compose foi feito no mesmo arquivo yaml. Mas na proxima aula isso acaba melhorando(organização melhor).
### Uma coisa já explorando aqui é definir os arquivos de *environment* em uma pasta diferente. Mas poderia se declarar environment e abaixo colocar as variaveis de ambiente.

## __Aula_7__
### Pensando ainda na aula anterior. Porém separando os arquivos de desenvolvimento com o container pronto. Dessa forma não precisa se build sempre para trabalhar com a nova versão.
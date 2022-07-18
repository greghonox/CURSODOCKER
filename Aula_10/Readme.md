## Gerar um projeto docker para o kubernetes

### Para começar vamos criar um container rodando o flask. Ele apenas renderiza o index.html

### Vamos fazer os passos anteriores

## 1. Build

``` python
docker build . -t greghono/flask-kubernetes
```

## 2. Rodar o container adicionando um nome

``` python
docker run -d -p 5001:5001 --name flask-kub flask-kubernetes
```

## 3. Caso precise apenas rodar não esqueça de usar o *start* 

``` python
docker start flask-kub
```

## 4. Enviar para o docker hub Lembre-se de que deve estar logado

## 4.1 Caso não esteja logado:
``` python
docker login
```

## 4.2 Enviar para o docker hub

``` python
docker push greghono/flask-kubernets
```

# __Vamos voltar a faltar de Kubernetes__

## Se tudo estiver certo vamos gerar o *deployment*

### Casos de erros não esqueça de utlizar o *docker logs flask-kub* ou *docker inspect flask-kub* para ter certeza que esta tudo correto.

## *Para criar um deployment*

``` python
kubectl create deployment <nome> --image=<usuario/imagem>
kubectl create deployment flask-kub --image=greghono/flask-kubernetes
```
### Não esqueça de deixa o *minikube rodando*

``` python
minikube start --driver=docker
```

## Para *verificar se esta rodando tudo certo*

``` python
minikube daskboard
```

## OU 

``` python
kubectl get deployments 
kubectl describe deployments 
```

# Conceito do __Pods__

## *Pods* é aonde o container ira executar

## Para *verificar o estado dos pods*

``` python
kubectl get pods
kubectl describe pods
```

## Até aqui o container *ainda não esta disponibilizando os serviço* para acesso

## Para *verificar a configuração do minikube*

``` python
kubectl config view
```

# *Criação de serviço*

## __Services__ faz o papel de expor o *Pods* para executar o serviço

``` python
kubectl expose deployment flask-kub  --type=LoadBalancer --port=5001
```

## Para ver os *status do servico*

``` python
kubectl get service # lista os serviços
kubectl describe services # lista detalhes dos servicos
kubectl describe services/flask-kub # detalha o servio espeificado
```

# *Adicionando ip*

## Para acessar o servico diretamente precisa se adicionar um IP. Basicamente ele faz um bind para outra porta do servico

``` python
minikube service --all
minikube service flask-kub
```

# *Replicando os pods*

## Agora vamos ver como *escalar* a aplicação em outras maquinas

``` python
kubectl scale deployment/nome_servico --replicas=numero_replicas
kubectl scale deployment/flask-kub --replicas=4
```

## Verifique com os comandos *kubectl get service* e *kubectl describe services* como esta ficando

# *Verificando as replicas*

``` python
kubectl get rs
```

# *Reduzindo as replicas*

## Para ter ajuste de diminuir as replicas ou mesmo aumentar

``` python
kubectl scale deployment/nome_servico --replicas=numero_replicas_diferente
kubectl scale deployment/flask-kub --replicas=2
```

# *Atualizar á imagem*

## Com o processo de desenvolvimento devemos atualizar o container do nosso kubernetes. Precisa ser feito em etapas.

## 1. Atualizar a imagem. Pode ser no processo de desenvolvimento como o código do projeto. Depois realizar um novo *build*.

``` python
docker build . -t greghono/flask-kubernetes:1
docker push greghono/flask-kubernetes:1
```

## 2. Sabendo o nome do deployments vamos atualizar no *kuberneters*

### Caso não saiba o nome do deployments execute

``` python
kubectl get deployments
```

## *Para atualizar*

``` python
 kubectl set image deployment/flask-kub flask-kubernetes=greghono/flask-kubernetes:1
 kubectl set image deployment/nome_deployment containers_image=repositorio_remoto:versao_se_tiver
```

# *Voltando o que estava feito*

## Podde ser que estava rodando tudo certo até o momento que foi feito a atualização. Para realizar um *rollback* da operação:

``` python
kubectl rollout deployment/flask-kub
```

## Para verificar o rollback

``` python
kubectl rollout status flask-kub
```

## Testas o caso acima de *rollback* faça

``` python
kubectl set image deployment/flask-kub flask-kubernetes=naoexisto/nem_sei_quem_e:1
# Se fizer, vai ver as tentativas de atualizar seguido do erro de ErrImagePull
kubectl get pods
# Ou
kubectl rollout status deployment/flask-kub
# Rollback
kubectl rollout undo deployment/flask-hub
# Verificando os status apos executar rollback
kubectl get pods
kubectl rollout status deployment/flask-kub
```

# *Deletanddo os servicos*

``` python
kubectl delete service flask-kub
```

## Para verificar se excluiu

``` python
minikube service list
```

# *Deletando um deployment*

## Caso deseja remover os deployments feitos. Isso removera tantos os *pods* como os *deployments*. Faça a remoção da segunite forma.

``` python
kubectl delete deployment flask-kub
kubectl delete deployment nome_deployment
```

## Depois siga os comandos para verificar se removeu *kubectl get deployments* ou no dashboard
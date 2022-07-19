# Trabalhando de forma declarativa.

## Na aula anterior demonstrei os comandos para genereciar o kubernetes com *minikube* e *kubectl*.

## Vimos comandos para todos os fins. Mas a vida fica complicada com tantos comandos e dependencia do usuário ter que manipular tudo isso. A forma *declativa vem para automatizar* esse processo.


## Deve se fazer:

## 1. Criar o *Dockerfile* com a imagem desejada.

## 2. Criar o *yaml* com a imagem desejada.

## Gerar o deployment

``` python
kubectl apply -f flask.yaml
```

# *Caso o minikube não esteja em execução*

``` python
minikube start --driver=docker
```

## Para verificar o serviço rodando:

``` python
minikube dashboard --url
kubectl get deployments
kubectl get pods
```

## Para *Remover o deploy*

``` python
kubectl delete -f flask.yaml 
kubectl delete -f arquivo.yaml
```

# Gerando serviços para os deployments

## Cada deployment deve ter *services* para ter acesso ao mundo real. Para isso criamos o arquivo *flask-service.yaml*

## Para gerar um deployment do arquivo de services

``` python
kubectl apply -f flask-service.yaml
```

## Para *gerar ip e acessar*

``` python
minikube service flask-service
```

## Para *Remover os services*

``` python
kubectl delete -f flask-service.yaml 
kubectl delete -f arquivo.yaml
```

## *Atualizando as imagens*

## Para atualizar as imagens, siga o processo de

## 1. Edite seu código

## 2. Faça:

``` python
docker build . -t flask-kub:tag
docker push greghono/flask-kub:tag
```

## 3. Atualize o *yaml* na tag *imagem* adicionando a versão nova. Depois só executar o

``` python
kubectl apply -f flask-kub.yaml
```

# Juntar arquivos yaml

## Caso queira ter um arquivo yaml juntando *deployments + service*. Acompanhe abaixo um rascunho com os dois

``` yaml
---
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  name: flask-kub 
spec: 
  replicas: 4 
  selector:
    matchLabels:
      app: flask-app 
  template: 
    metadata:
      labels:
        app: flask-app 
    spec: 
        containers:
          - name: flask
            image: greghono/flask-kubernetes:2
---
apiVersion: v1
kind: Service 
metadata:
  name: flask-service
spec:
  selector:
    app: flask-app 
  ports: 
    - protocol: 'TCP'
      port: 5001
      targetPort: 5001
  type: LoadBalancer
```

## Perceba acima que o diferencial é utilizar o __---__ no inicio de cada objetivo.
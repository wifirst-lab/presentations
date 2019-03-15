# Service

## Création du service

```bash
kubectl apply -f 000_service.yaml
```

## Récupération de la ClusterIP

```bash
kubectl get service
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
my-service   ClusterIP   10.97.30.88   <none>        8081/TCP   2m57s

curl http://10.97.30.88:8081
```

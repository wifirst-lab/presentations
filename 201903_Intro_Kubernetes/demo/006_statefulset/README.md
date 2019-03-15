# Statefulset

## Création des volumes de stockage (for demo purpose only, don't use it in production)

```bash
mkdir /tmp/data1
mkdir /tmp/data2
kubectl apply -f 000_create_volume.yaml
kubectl get pv
```

## Création du statefulset

```bash
kubectl apply -f 001_base_stateful.yaml
kubectl describe statefulset  web
kubectl get pvc

kubectl exec -ti web-0 -c nginx /bin/sh
hostname > /usr/share/nginx/html/test.html
exit

kubectl exec -ti web-1 -c nginx /bin/sh
hostname > /usr/share/nginx/html/test.html
exit

kubectl get service
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
nginx        ClusterIP   10.102.131.159   <none>        8082/TCP   12m

curl http://10.102.131.159:8082/test.html
```

## Suppression d'un pod

```bash
kubectl delete pods web-0
curl http://10.102.131.159:8082/test.html
```

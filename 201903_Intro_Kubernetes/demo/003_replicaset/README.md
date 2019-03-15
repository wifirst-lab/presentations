# ReplicaSet

## Création d'un replicaset

```bash
kubectl apply -f 000_base_replicaset.yml
```

## Tuer un pod ou un container docker pour voir le comportement du RS

```bash
kubectl delete pods $(kubectl get pods | grep frontend | head -1  | awk '{print $1}')
# Regarder l'event log pour voir le RS a relancé un pod
kubectl get rs
[snip]
Events:
  Type    Reason            Age    From                   Message
  ----    ------            ----   ----                   -------
  Normal  SuccessfulCreate  2m26s  replicaset-controller  Created pod: frontend-gdfkg
  Normal  SuccessfulCreate  2m26s  replicaset-controller  Created pod: frontend-qmw65
  Normal  SuccessfulCreate  2m26s  replicaset-controller  Created pod: frontend-z7nh4
  Normal  SuccessfulCreate  35s    replicaset-controller  Created pod: frontend-gbqzx

```

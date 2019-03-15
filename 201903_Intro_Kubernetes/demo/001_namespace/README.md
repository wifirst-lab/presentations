# Simple demo pour créer un namespace dans un cluster Kubernetes

## Création du namespace

```bash
kubectl apply -f 000_demo_ns.yaml
```

## Pour utiliser le namespace comme namespace par défault

```bash
kubectl config set-context $(kubectl config current-context) --namespace=demo
# Validate it
kubectl config view | grep namespace:
```
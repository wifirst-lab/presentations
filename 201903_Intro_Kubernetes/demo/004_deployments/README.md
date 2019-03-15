# Deployments

## Création du deployment de base

```bash
kubectl apply -f 000_base_deployment.yaml
```

## Mise à jour de l'image du deployments

```bash
kubectl apply -f 001_update_deployment.yaml
kubectl rollout history deployment/nginx-deployment
# Rollback
kubectl rollout undo deployment/nginx-deployment
kubectl rollout history deployment/nginx-deployment
```

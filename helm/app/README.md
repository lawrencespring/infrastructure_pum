Ingress:
https://getbetterdevops.io/secure-k8s-nginx-ingress-with-lets-encrypt/



App
cd helm/app:
Prod
kubectl create namespace pum-prod
helm upgrade pum-prod-app . -i -n pum-prod -f values-prod.yaml
helm uninstall pum-prod-app -n pum-prod

Staging
kubectl create namespace pum-staging
helm upgrade pum-staging-app . -i -n pum-staging -f values-staging.yaml
helm uninstall pum-staging-app -n pum-staging
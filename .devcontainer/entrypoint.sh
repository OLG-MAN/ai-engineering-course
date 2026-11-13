#!/usr/bin/env bash
# Builds a container-local kubeconfig from the host one (mounted read-only):
# the host points at https://127.0.0.1:26443, which from inside a container is the container itself.
# OrbStack routes cluster DNS into containers, and the API cert is valid for this name.
set -euo pipefail

HOST_KUBECONFIG=/mnt/host-kube/config
if [[ -f "$HOST_KUBECONFIG" ]]; then
  mkdir -p "$HOME/.kube"
  cp "$HOST_KUBECONFIG" "$HOME/.kube/config"
  chmod 600 "$HOME/.kube/config"
  if kubectl config get-clusters | grep -qx orbstack; then
    kubectl config set-cluster orbstack --server=https://kubernetes.default.svc.cluster.local >/dev/null
  fi
fi

exec "$@"

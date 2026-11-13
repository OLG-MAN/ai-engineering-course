COMPOSE := docker compose -f .devcontainer/compose.yaml

.PHONY: help up sh down rebuild status nuke

help: ## Show targets
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-8s %s\n", $$1, $$2}'

up: ## Start the lab container (builds the image the first time)
	$(COMPOSE) up -d

sh: ## Open a shell in the lab (starts it if needed)
	@$(COMPOSE) up -d
	@$(COMPOSE) exec lab bash

down: ## Stop and remove the container (code and caches are kept)
	$(COMPOSE) down

rebuild: ## Rebuild the image after Dockerfile/requirements.txt changes, then restart
	$(COMPOSE) up -d --build --force-recreate

status: ## Container state + cluster reachability from inside
	$(COMPOSE) ps
	-$(COMPOSE) exec lab sh -c 'python --version; kubectl get nodes'

nuke: ## Remove container, image and download caches
	$(COMPOSE) down --rmi local -v

# API Configuration

API_ARTIFACTS_DIR ?= artifacts/api

.PHONY: api api-clean

api:
	@mkdir -p "$(API_ARTIFACTS_DIR)"
	@printf "No HTTP API surface is published in this release.\n" > "$(API_ARTIFACTS_DIR)/summary.txt"

api-clean:
	@rm -rf "$(API_ARTIFACTS_DIR)"

##@ API
api: ## Emit API summary artifacts
api-clean: ## Remove API artifacts

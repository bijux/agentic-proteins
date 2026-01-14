# Citation Configuration

CITATION_FILE ?= CITATION.cff

.PHONY: citation citation-clean ciattion

citation:
	@if [ ! -f "$(CITATION_FILE)" ]; then \
	  echo "✘ Missing $(CITATION_FILE)"; \
	  exit 1; \
	fi
	@echo "✔ $(CITATION_FILE) present"

ciattion: citation

citation-clean:
	@true

##@ Citation
citation: ## Validate CITATION.cff locally
ciattion: ## Alias for citation
citation-clean: ## No-op clean for citation

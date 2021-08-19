all: lint

lint:
	@echo "[ Flake8 ]"
	@$(PYTHON)/bin/flake8 --max-line-length=120

clean:
    git clean -dfx

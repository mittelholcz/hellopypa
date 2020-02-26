SHELL:=/bin/bash


all:
	@echo 'Choose a target:'
	@echo '    env: setup development environment'
	@echo '    test: run pytest'
	@echo '    release_patch: publish new patch version'
	@echo '    release_minor: publish new minor version'
	@echo '    release_major: publish new major version'
.PHONY: all


env:
	if "$$(which deactivate)" ] ; then \
		deactivate ; \
		rm -rf .venv/ ; \
		python3 -m venv .venv ; \
		. .venv/bin/activate ; \
		pip install -r requirements-dev.txt ; \
	else \
		echo -n ; \
	fi
.PHONY: env


clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
.PHONY: clean


test:
	@clear
	@. .venv/bin/activate && pytest --verbose test/
.PHONY: test


build: clean test
	. .venv/bin/activate && python3 setup.py sdist bdist_wheel
.PHONY: build


OLDVER:=$$(grep -P -o "(?<=__version__ = ')[^']+" hellopypa/version.py)

MAJOR:=$$(echo $(OLDVER) | sed -r s"/([0-9]+)\.([0-9]+)\.([0-9]+)/\1/")
MINOR:=$$(echo $(OLDVER) | sed -r s"/([0-9]+)\.([0-9]+)\.([0-9]+)/\2/")
PATCH:=$$(echo $(OLDVER) | sed -r s"/([0-9]+)\.([0-9]+)\.([0-9]+)/\3/")

NEWMAJORVER="$$(( $(MAJOR)+1 )).0.0"
NEWMINORVER="$(MAJOR).$$(( $(MINOR)+1 )).0" 
NEWPATCHVER="$(MAJOR).$(MINOR).$$(( $(PATCH)+1 ))"


release_major:
	@make -s __release NEWVER=$(NEWMAJORVER)
.PHONY: release_major


release_minor:
	@make -s __release NEWVER=$(NEWMINORVER)
.PHONY: release_minor


release_patch:
	@make -s __release NEWVER=$(NEWPATCHVER)
.PHONY: release_patch


__release:
	@if [[ -z "$(NEWVER)" ]] ; then \
		echo 'Do not call this target!' ; \
		echo 'Use "release_major", "release_minor" or "release_patch"!' ; \
		exit 1 ; \
		fi
	@if [[ $$(git status --porcelain) ]] ; then \
		echo 'Working dir is dirty!' ; \
		exit 1 ; \
		fi
	@echo "NEW VERSION: $(NEWVER)"
	@sed -i -r "s/pypi-$(OLDVER)/pypi-$(NEWVER)/" README.md
	# @sed -i -r "s/version = '$(OLDVER)'/version = '$(NEWVER)'/" hellopypa/version.py
	# @make -s build
	# @git add README.md hellopypa/version.py
	# @git commit -m'new release'
	# @git tag -a $(NEWVER) -m'release: $(NEWVER)'
	# git push origin $(NEWVER)
	# pipenv run python3 -m twine upload dist/*
.PHONY: __release

# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

# Use bash even on Windows
SHELL := /bin/bash

# On Windows the activate script is stored in a different location.
ACTIVATE_SCRIPT := venv/bin/activate
ifeq ($(OS),Windows_NT)
ACTIVATE_SCRIPT := venv/Scripts/activate
endif

ACTIVATE=[[ -e $(ACTIVATE_SCRIPT) ]] && source $(ACTIVATE_SCRIPT);

clean:
	rm -rf build dist pythondata_*.egg-info

.PHONY: clean

venv-clean:
	rm -rf venv

.PHONY: venv-clean

$(ACTIVATE_SCRIPT): requirements.txt setup.py Makefile
	make venv
	@ls -l $(ACTIVATE_SCRIPT)
	@touch $(ACTIVATE_SCRIPT)
	@ls -l $(ACTIVATE_SCRIPT)

venv:
	virtualenv --python=python3 --always-copy venv
	# Packaging tooling.
	${ACTIVATE} pip install -U pip twine build
	# Setup requirements.
	${ACTIVATE} pip install -r requirements.txt
	@${ACTIVATE} python -c "from rr_graph.version import version as v; print('Installed version:', v)"

.PHONY: venv

build: | $(ACTIVATE_SCRIPT)
	${ACTIVATE} python -m build --sdist
	${ACTIVATE} python -m build --wheel

.PHONY: build

# PYPI_TEST = --repository-url https://test.pypi.org/legacy/
PYPI_TEST = --repository testpypi

upload-test: build | $(ACTIVATE_SCRIPT)
	${ACTIVATE} twine upload ${PYPI_TEST} dist/*

.PHONY: upload-test

upload: build | $(ACTIVATE_SCRIPT)
	${ACTIVATE} twine upload --verbose dist/*

.PHONY: upload

check: build | $(ACTIVATE_SCRIPT)
	${ACTIVATE} twine check dist/*.whl

.PHONY: check

install: | $(ACTIVATE_SCRIPT)
	${ACTIVATE} python setup.py install

.PHONY: install

test: | $(ACTIVATE_SCRIPT)
	${ACTIVATE} python setup.py test

.PHONY: test

#!/usr/bin/env bash
set -euo pipefail

python -m test_tex_generator.cli \
  --config config/default.yaml \
  --state work/generator-state.json \
  --output work/generated-tests.yaml \
  --coverage-report work/coverage-report.json \
  --count 200 \
  --append

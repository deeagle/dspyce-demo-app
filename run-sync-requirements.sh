#!/bin/bash

DSPCYE_DEPENDENCIES="dspyce-requirements.txt"
DSPYCE_DEMO_DEPENDENCIES="dspyce-demo-app-requirements.txt"
REQUIREMENTS_RESULT_FILE="requirements.txt"

echo "Running requirements-update ..."

echo "Get DSpyce requirements ..."
curl https://raw.githubusercontent.com/dspace-unimr/dspyce/main/requirements.txt -o "${DSPCYE_DEPENDENCIES}"

echo "Merge "
pip-compile "--output-file=${REQUIREMENTS_RESULT_FILE}" "${DSPYCE_DEMO_DEPENDENCIES}" "${DSPCYE_DEPENDENCIES}"

echo "Finish requirements-update successfully."

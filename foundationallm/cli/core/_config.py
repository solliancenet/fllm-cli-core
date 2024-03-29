# --------------------------------------------------------------------------------------------
# Copyright (c) FoundationaLLM. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from foundationallm.cli.core._environment import get_config_dir

GLOBAL_CONFIG_DIR = get_config_dir()
CONFIG_FILE_NAME = 'config'
GLOBAL_CONFIG_PATH = os.path.join(GLOBAL_CONFIG_DIR, CONFIG_FILE_NAME)
ENV_VAR_PREFIX = 'AZURE'
ENV_VAR_TEST_LIVE = 'AZURE_TEST_RUN_LIVE'

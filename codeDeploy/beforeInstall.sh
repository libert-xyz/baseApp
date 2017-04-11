#!/bin/bash
set -e

sed -i '$ a export APP_SETTINGS=config.ProductionConfig' /etc/bash.bashrc
bash


# run from <project_dir> via bash scripts/prepare_data/preprocess_visual_poetry

source .local_env
echo $PROJECT_DIR

uv run \
python ${PROJECT_DIR}/src/prepare_data/visual_poetry.py \
    --config-path="${PROJECT_DIR}/xp_configs" \
    --config-name="defaults.yaml"

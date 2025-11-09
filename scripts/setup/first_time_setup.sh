
# cd <project_dir>
# run as:  bash scripts/setup.sh

source .local_env
echo $PROJECT_DIR


# setup tasks
# sudo snap install --classic astral-uv
brew install poppler  # using this for pdfseparate on mac
uv init --python 3.11   # warning: have you already init'd to an earlier python version

uv add omegaconf
uv add hydra-core

uv add pdf2image

# uv venv  # if you don't already have a venv
source .venv/bin/activate

##### one time data prep

# download directory of pdfs, than
bash scripts/prepare_data/split_pages_visual_poetry.sh


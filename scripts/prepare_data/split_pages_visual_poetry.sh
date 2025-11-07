#!/bin/bash
# Split multi-page PDFs into single-page PDFs

# Set directories
source .local_env
echo $PROJECT_DIR

# todo define these elsewhere
input_dir="${PROJECT_DIR}/data/incoming/visual_poetry/pdfs"
output_dir="${PROJECT_DIR}/data/intermediates/visual_poetry/pdfs_singlepage"

echo $input_dir

#############################################
# Create output directory
mkdir -p "$output_dir"

# Process each PDF
for pdf in "$input_dir"/*.pdf; do
  # Skip if no PDFs found
  [ -e "$pdf" ] || continue
  
  # Get filename without path and extension
  basename=$(basename "$pdf" .pdf)
  
  # Split PDF into single pages
  #   pdftk "$pdf" burst output "$output_dir/${basename}_p%04d.pdf"
  pdfseparate "$pdf" "$output_dir/${basename}_p%04d.pdf"


  
  # Remove doc_data.txt created by pdftk
  rm -f doc_data.txt
done

echo "PDF splitting complete"
#############################################



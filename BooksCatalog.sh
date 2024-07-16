#!/bin/bash

# Input PDF file
input_pdf=BOOKS_CATALOG.pdf

#make a new folder
folder=BooksCatalog
mkdir -p ${folder}

# Get the total number of pages
total_pages=$(pdftk "$input_pdf" dump_data | grep NumberOfPages | awk '{print $2}')

# Initialize page counter
start_page=1

# Loop through the PDF, splitting it into 2-page chunks
while [ $start_page -le $total_pages ]; do
  end_page=$((start_page + 1))
  if [ $end_page -gt $total_pages ]; then
    end_page=$total_pages
  fi
  output_pdf=${folder}/${start_page}_${end_page}.pdf
  pdftk "$input_pdf" cat ${start_page}-${end_page}south output "$output_pdf"
  echo "Created $output_pdf"
  start_page=$((end_page + 1))
done

#!/bin/bash

cd /home/myat/AdvComPro/wk03

# Loop through all Python files (assuming they have a .py extension) and execute them
for file in *.py; do
    echo ""
    echo "Running $file..."
    echo "=================================================================================================================================="
    python3 "$file"
    echo "=================================================================================================================================="
    echo "$file completed."
    echo ""
    echo ""
done

echo "All Python files executed."

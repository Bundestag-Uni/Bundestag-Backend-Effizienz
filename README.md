# Bundestags Backend: Efficiency Calculator

This repository provides an efficiency calculation pipeline for speeches of the German parliament (Deutscher Bundestag). It is built upon the LightRAG repository ([https://github.com/HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)), utilizing metadata from graph indexing such as the number of nodes and edges to determine a measurable content size of a speech.

## Requirements

To use this repository, you must have a connection to an LLM API service, such as OpenAI or a self-hosted service like Ollama.

## Setup

1. **Modify AI Endpoints**: Change the designated AI endpoints in the `lightrag_ollama_demo.py` file.
2. **Import Dataset**: Import your dataset of speeches into the `datasets` folder.
3. **Run the Pipeline**: Pass your dataset to the `iterate_over()` function in the `lightrag_ollama_demo.py` file.

## Output

- The outputs will be generated in an `outputs` folder.
- **Cleaning Outputs**: The `clean_empty.py` script deletes failed output directories.
- **Metadata Extraction**: The `output_folder_to_json.py` script sifts through the output directories of the graph, extracts the needed metadata, and writes it to a JSON file.
- **Efficiency Calculation**: The `eff_calc.py` script calculates the efficiency metric.

## Usage

1. Clone this repository.
2. Install necessary dependencies.
3. Follow the setup instructions above.
4. Run the scripts as needed to process your data and generate outputs.

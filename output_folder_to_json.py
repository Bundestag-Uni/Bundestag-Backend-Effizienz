import os
import xml.etree.ElementTree as ET
import shutil
import pandas as pd
import json

def count_nodes_edges(file_path):
    "counts nodes and edges"
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        ns = {'graphml': 'http://graphml.graphdrawing.org/xmlns'}
        
        nodes = len(root.findall('.//graphml:node', ns))
        edges = len(root.findall('.//graphml:edge', ns))
        
        return nodes, edges
    except Exception as e:
        return None, None


    

def extract_content_length(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Find the key that starts with "doc-"
    doc_key = next((key for key in data.keys() if key.startswith("doc-")), None)
    
    if doc_key:
        # Extract the content_length
        content_length = data[doc_key].get("content_length")
        return content_length
    else:
        return None




def itterate_over(root_folder):
    
    """itterates over all direcories in a folder and deletes all that dond fit the pattern and crates json"""
    results = []
    for dir_name in os.listdir(root_folder):
        dir_path = os.path.join(root_folder,dir_name)
        
        if dir_name.startswith("KG_ID") and os.path.isdir(dir_path):
            unique_id = dir_name.split("KG_ID")[-1]
            file_path = os.path.join(dir_path, "graph_chunk_entity_relation.graphml")

            token_file_path = os.path.join(dir_path, "kv_store_doc_status.json")
            num_tokens = extract_content_length(token_file_path)
            if os.path.exists(file_path):
                nodes, edges = count_nodes_edges(file_path)
                
                    
                if nodes is not None and edges is not None:
                    new_row = {
                        'ID': dir_name,
                        'Num_tokens': num_tokens,
                        'Num_Nodes': nodes,
                        'Num_edges': edges,
                        'Efficiency': 0
                    }  
                    results.append(new_row) 
                else:
                    print(f"KG_ID{unique_id}: Error processing file")
                if nodes ==  0 and edges == 0:
                    
                    print(f"deleted {dir_name}: Nodes and edges 0") 
            else:
                
                print(f"deleted {dir_name}: No .graphml file found")    
    
    with open('output_wo_eff.json', 'w') as f:
        json.dump(results, f, indent=2)

itterate_over("path to/WAB5_Lightrag/outputs")




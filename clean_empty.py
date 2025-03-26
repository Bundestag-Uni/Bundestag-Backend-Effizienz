import os
import xml.etree.ElementTree as ET
import shutil

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

def rm_dir(path_to_dir):
    """removes directory"""
    try:
        shutil.rmtree(path_to_dir)
    except FileNotFoundError:
        print(f"{path_to_dir} not found")
    except PermissionError:
        print(f"Can't delete {path_to_dir}: Permission denied")

def itterate_over(root_folder):
    "itterates over all direcories in a folder and deletes all that dond fit the pattern"
    results = []
    for dir_name in os.listdir(root_folder):
        dir_path = os.path.join(root_folder,dir_name)
        if dir_name.startswith("KG_ID") and os.path.isdir(dir_path):
            unique_id = dir_name.split("KG_ID")[-1]
            file_path = os.path.join(dir_path, "graph_chunk_entity_relation.graphml")
            
            if os.path.exists(file_path):
                nodes, edges = count_nodes_edges(file_path)
                 
                    
                if nodes is not None and edges is not None:
                    print(f"KG_ID{unique_id}: Nodes: {nodes}, Edges: {edges}")
                else:
                    print(f"KG_ID{unique_id}: Error processing file")
                if nodes < 5 and edges < 2:
                    rm_dir(dir_path)
                    print(f"deleted {dir_name}: Nodes and edges to to little, persumed error") 
            else:
                rm_dir(dir_path)
                print(f"deleted {dir_name}: No .graphml file found")    

    

itterate_over("path to/WAB5_Lightrag/outputs_llama")

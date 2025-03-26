import xml.etree.ElementTree as ET
import pandas as pd

def extract_graphml_info_to_dataframe(file_path):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Find the graph element
        graph = root.find('{http://graphml.graphdrawing.org/xmlns}graph')

        if graph is None:
            return pd.DataFrame()

        # Count nodes and edges
        num_nodes = len(graph.findall('{http://graphml.graphdrawing.org/xmlns}node'))
        num_edges = len(graph.findall('{http://graphml.graphdrawing.org/xmlns}edge'))

        # Create a pandas DataFrame
        data = {
            'Metric': ['Number of Nodes', 'Number of Relationships'],
            'Value': [num_nodes, num_edges]
        }
        df = pd.DataFrame(data)

        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return pd.DataFrame()

# Example usage
file_path = 'pathto  /outputs/KG_ID2011500300/graph_chunk_entity_relation.graphml'
result_df = extract_graphml_info_to_dataframe(file_path)
print(result_df)

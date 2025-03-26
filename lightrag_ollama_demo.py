import asyncio
import os
import inspect
import logging
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding, hf_embedding
from lightrag.utils import EmbeddingFunc
import pandas as pd
import xml.etree.ElementTree as ET
from transformers import AutoModel, AutoTokenizer
#from lightrag.llm.hf import hf_model_complete, hf_embed



import json
with open("pathto/WAB5_Lightrag/mydataset/YOUR_DATASET.json", "r", encoding="utf-16") as file:
    data = json.load(file)
df = pd.DataFrame(data)

text = df["inhalt"].iloc[0]






logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)



def itterate_over_dataset():
    for index, row in df.iterrows():

        WORKING_DIR = "path to/WAB5_Lightrag/outputs_llama/KG_" + row["id"]
        if not os.path.exists(WORKING_DIR):
            os.mkdir(WORKING_DIR)
            
            rag = LightRAG(
            working_dir=WORKING_DIR,     
            llm_model_func=ollama_model_complete,
            llm_model_name="phi4",
            llm_model_max_async=16,
            llm_model_max_token_size=32768,
            llm_model_kwargs={"host": "OLLAMA_CONNECTION", "options": {"num_ctx": 32768}},
            embedding_func=EmbeddingFunc(
                embedding_dim=1024,
                max_token_size=8192,
                func=lambda texts: hf_embedding(
                    texts,
                    tokenizer=AutoTokenizer.from_pretrained(
                        "EMBED MODEL"
                    ),
                    embed_model=AutoModel.from_pretrained(
                        "EMBED MODEL"
                    ),
                ),
            ),
        )

            text = row["inhalt"]

            rag.insert(text)
        else:
            print(WORKING_DIR + " allready exists")

    
    
#itterate_over_dataset()


def test_creation():
    WORKING_DIR = "path to/WAB5_Lightrag/outputs/test"
    if not os.path.exists(WORKING_DIR):
        os.mkdir(WORKING_DIR)
            
        rag = LightRAG(
            working_dir=WORKING_DIR,     
            llm_model_func=ollama_model_complete,
            llm_model_name="phi4",
            llm_model_max_async=4,
            llm_model_max_token_size=32768,
            llm_model_kwargs={"host": "OLLAMA CONNECTION", "options": {"num_ctx": 32768}},
            embedding_func=EmbeddingFunc(
                embedding_dim=1024,
                max_token_size=8192,
                func=lambda texts: hf_embedding(
                    texts,
                    tokenizer=AutoTokenizer.from_pretrained(
                        "EMBED MODEL"
                    ),
                    embed_model=AutoModel.from_pretrained(
                        "EMBED MODEL"
                    ),
                ),
            ),
        )

        text = df["inhalt"].iloc[0]

        rag.insert(text)
    else:
        print(WORKING_DIR + " allready exists")


itterate_over_dataset()
#test_creation()
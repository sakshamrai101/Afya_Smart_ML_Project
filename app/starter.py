import os
import logging
import sys
import openai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config

openai.api_key=Config.OPENAI_API_KEY
# os.environ["OPENAI_API_KEY"] = "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"


# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    print(1000)
    index = VectorStoreIndex.from_documents(documents)
    print(index)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    print(999)
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()
# response = query_engine.query("Where did author take art classes?")
# print(response)
# response = query_engine.query("What did the author do growing up?")
q = "Complains of forgetfulness"
response = query_engine.query(q)

print(response)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from pprint import pprint
import pickle
import ssl

#import nltk
#nltk.download('punkt')


loader = GenericLoader.from_filesystem(
    "/home/app/ChatGPT-Next-Web/app/components",
    glob="*.*",
    suffixes=[".tsx", ".ts"],
    parser=LanguageParser(),
)
docs = loader.load()
print(len(docs))

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)

js_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=1000, chunk_overlap=200
)

documents = js_splitter.split_documents(docs)

print(len(documents))
for doc in documents:
    pprint(doc)
# Load Data to vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)


# Save vectorstore
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)

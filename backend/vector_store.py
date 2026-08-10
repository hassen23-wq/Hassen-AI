import os
import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from document_loader import load_documents, split_documents


# =========================
# Embedding Model
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# Paths
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_PATH = os.path.join(
    BASE_DIR,
    "vector_data"
)

INDEX_FILE = os.path.join(
    VECTOR_PATH,
    "star_index.faiss"
)

DATA_FILE = os.path.join(
    VECTOR_PATH,
    "documents.pkl"
)


# =========================
# Create Vector Database
# =========================

def create_vector_store():

    print("Creating vector database...")

    documents = load_documents()

    if not documents:
        raise Exception(
            "No documents found"
        )


    chunks = split_documents(
        documents
    )


    if not chunks:
        raise Exception(
            "No chunks generated"
        )


    texts = [
        chunk["content"]
        for chunk in chunks
    ]


    vectors = embedding_model.encode(
        texts,
        show_progress_bar=True
    )


    vectors = np.asarray(
        vectors,
        dtype="float32"
    )


    dimension = vectors.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        vectors
    )


    os.makedirs(
        VECTOR_PATH,
        exist_ok=True
    )


    faiss.write_index(
        index,
        INDEX_FILE
    )


    with open(
        DATA_FILE,
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


    print(
        "Vector database created successfully"
    )

    return True



# =========================
# Load Vector Database
# =========================

def load_vector_store():

    if not os.path.exists(INDEX_FILE) or not os.path.exists(DATA_FILE):

        create_vector_store()


    index = faiss.read_index(
        INDEX_FILE
    )


    with open(
        DATA_FILE,
        "rb"
    ) as f:

        chunks = pickle.load(
            f
        )


    return index, chunks



# =========================
# Search
# =========================

def search_vectors(
    query,
    k=3
):

    index, chunks = load_vector_store()


    query_vector = embedding_model.encode(
        [query]
    )


    query_vector = np.asarray(
        query_vector,
        dtype="float32"
    )


    distances, results = index.search(
        query_vector,
        k
    )


    output = []


    for idx in results[0]:

        if idx == -1:
            continue


        if idx < len(chunks):

            output.append(
                chunks[idx]["content"]
            )


    if not output:

        return "No relevant information found."


    return "\n\n".join(output)
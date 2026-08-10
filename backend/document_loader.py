import os
import re


KNOWLEDGE_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "../knowledge/products"
)



# ---------------------------------
# Load Documents
# ---------------------------------

def load_documents():

    documents = []


    if not os.path.exists(KNOWLEDGE_FOLDER):
        return documents



    for file_name in os.listdir(KNOWLEDGE_FOLDER):


        if file_name.endswith(
            (".md", ".txt")
        ):


            file_path = os.path.join(
                KNOWLEDGE_FOLDER,
                file_name
            )


            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:


                content = file.read()



            documents.append({

                "filename": file_name,

                "content": clean_text(
                    content
                )

            })


    return documents




# ---------------------------------
# Text Cleaning
# ---------------------------------

def clean_text(text):


    text = re.sub(
        r"\n+",
        "\n",
        text
    )


    text = re.sub(
        r"[#*_]",
        "",
        text
    )


    return text.strip()




# ---------------------------------
# Smart Chunking
# ---------------------------------

def split_documents(
        documents,
        chunk_size=500,
        overlap=100
):


    chunks = []


    chunk_id = 0



    for document in documents:


        words = (
            document["content"]
            .split()
        )


        start = 0



        while start < len(words):


            end = start + chunk_size



            chunk_words = words[
                start:end
            ]



            chunk = " ".join(
                chunk_words
            )



            chunks.append({

                "chunk_id": chunk_id,

                "source":
                    document["filename"],


                "content":
                    chunk

            })


            chunk_id += 1


            start += (
                chunk_size -
                overlap
            )



    return chunks
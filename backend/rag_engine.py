import os
# from vector_store import search_vectors

KNOWLEDGE_PATH = os.path.join(
    os.path.dirname(__file__),
    "../knowledge/products"
)


def load_knowledge():

    knowledge = ""

    for file in os.listdir(KNOWLEDGE_PATH):

        if file.endswith(".md"):

            path = os.path.join(
                KNOWLEDGE_PATH,
                file
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                knowledge += f.read()
                knowledge += "\n\n"

    return knowledge



def retrieve_context(query, max_length=4000):

    documents = load_knowledge()


    # تحويل السؤال لكلمات
    keywords = query.lower().split()


    # تقسيم الوثيقة
    sections = documents.split("\n\n")


    results = []


    for section in sections:

        score = 0

        text = section.lower()


        for word in keywords:

            if word in text:
                score += 1


        if score > 0:
            results.append(
                (score, section)
            )


    # ترتيب حسب التشابه
    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )


    context = ""


    for score, text in results[:5]:

        context += text
        context += "\n\n"


    return context[:max_length]
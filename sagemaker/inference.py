from src.DocuDive import loadModel, getResult

def model_fn():
    return loadModel()

def predict(body: dict, llm):
    query = body["query"]
    answer, documents = getResult(query, llm)
    docsDictionary = []
    for doc in documents:
        docsDictionary.append({doc.metadata["source"], doc.page_content})

    return {
            "answer":answer,
            "Documents":docsDictionary
            }
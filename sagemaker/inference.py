from src.DocuDive import loadModel, getResult

def model_fn():
    return loadModel()

def predict(body: dict, llm):
    query = body["query"]
    answer, documents = getResult(query, llm)
    result = {
        "answer":answer,
        "Documents":{}
        }
    for doc in documents:
        result['Documents'][doc.metadata["source"]] = doc.page_content

    return result
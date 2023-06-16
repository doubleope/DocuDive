# DocuDive
GPT for your wiki pages

- Based off of PrivateGPT - https://github.com/imartinez/privateGPT

# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
pip3 install -r requirements.txt
```

Then, download the LLM model and place it in a directory of your choice:
- LLM: default to [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). If you prefer a different GPT4All-J compatible model, just download it and reference it in your `.env` file.

Copy the `example.env` template into `.env`
```shell
cp example.env .env
```

and edit the variables appropriately in the `.env` file.
```
MODEL_TYPE: supports LlamaCpp or GPT4All
PERSIST_DIRECTORY: is the folder you want your vectorstore in
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for the LLM model
MODEL_N_BATCH: Number of tokens in the prompt that are fed into the model at a time. Optimal value differs a lot depending on the model (8 works well for GPT4All, and 1024 is better for LlamaCpp)
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
SOURCE_DIRECTORY: Directory for the documents
```

Note: because of the way `langchain` loads the `SentenceTransformers` embeddings, the first time you run the script it will require internet connection to download the embeddings model itself.

## Test dataset
This repo contains within synthetically produced text files containing description of different projects. These files can be found under v1.0_fake_products.

## Instructions for ingesting your own dataset

Put any and all your files into the `source_documents` directory

The supported extensions are:

   - `.csv`: CSV,
   - `.docx`: Word Document,
   - `.doc`: Word Document,
   - `.enex`: EverNote,
   - `.eml`: Email,
   - `.epub`: EPub,
   - `.html`: HTML File,
   - `.md`: Markdown,
   - `.msg`: Outlook Message,
   - `.odt`: Open Document Text,
   - `.pdf`: Portable Document Format (PDF),
   - `.pptx` : PowerPoint Document,
   - `.ppt` : PowerPoint Document,
   - `.txt`: Text file (UTF-8),

Run the following command to ingest all the data.

```shell
python src/ingest.py
```

It will create a `db` folder containing the local vectorstore. Will take 20-30 seconds per document, depending on the size of the document.
You can ingest as many documents as you want, and all will be accumulated in the local embeddings database.
If you want to start from an empty database, delete the `db` folder.

Note: during the ingest process no data leaves your local environment. You could ingest without an internet connection, except for the first time you run the ingest script, when the embeddings model is downloaded.

## Ask questions to your documents, locally on CLI!
In order to ask a question, run a command like:

```shell
python localrun.py
```

And wait for the script to require your input.

```plaintext
> Enter a query:
```

Hit enter. You'll need to wait 20-30 seconds (depending on your machine) while the LLM model consumes the prompt and prepares the answer. Once done, it will print the answer and the 4 sources it used as context from your documents; you can then ask another question without re-running the script, just wait for the prompt again.

Note: you could turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

## Locally launch a webservice!
To launch a webservice that runs on local host port 8080, run the following command: 

```shell
python v1.1_microservice/server.py
```

The webserver has 2 requests that you can make. One is a GET request to /ping which will return the string "pong". This will be to do any healthchecks on the service. And lastly there is a POST request to /invocations that will take in a query in the body of the response and return the response from the large language model. Here is an example of the request body:

```js
{"query":"can you explain what the connectify project is?"}
```

and here is an example of the response:

```js
{
    "result": {
        "answer": " Connectify, also known as CN or UPd - it's a software solution that turns your computer into an efficient virtual router for seamless internet connectivity. It offers features like hotspot creation and network management to enhance productivity while enabling sharing of data with other devices on the same LAN/WAN network (HS).",
        "Documents": {
            "v1.0_fake_products\\connectify.txt": "Key Activities:\n- Continuous improvement and feature updates of Connectify (UPD)\n- Gathering user feedback for product enhancements (FB)\n- Providing comprehensive training and customer support (TS)\n\nValue Propositions:\n- Transform your computer into a virtual router with a simple interface (UI)\n- Share internet connections with other devices seamlessly (HS)\n- Ensure data security and privacy with advanced encryption (AS)"
        }
    },
    "timestamp": "15/06/2023 16:48:06",
    "isSuccess": true,
    "jobDurationSeconds": 99.0
}
```

# How does it work?
Selecting the right local models and the power of `LangChain` you can run the entire pipeline locally, without any data leaving your environment, and with reasonable performance.

- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `HuggingFaceEmbeddings` (`SentenceTransformers`). It then stores the result in a local vector database using `Chroma` vector store.
- `DocuDive.py` uses a local LLM based on `GPT4All-J` or `LlamaCpp` to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- `GPT4All-J` wrapper was introduced in LangChain 0.0.162.

# System Requirements

## Python Version
To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

## C++ Compiler
If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

### For Windows 10/11
To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
   * Universal Windows Platform development
   * C++ CMake tools for Windows
3. Download the MinGW installer from the [MinGW website](https://sourceforge.net/projects/mingw/).
4. Run the installer and select the `gcc` component.

## Mac Running Intel
When running a Mac with Intel hardware (not M1), you may run into _clang: error: the clang compiler does not support '-march=native'_ during pip install.

If so set your archflags during pip install. eg: _ARCHFLAGS="-arch x86_64" pip3 install -r requirements.txt_

## Contributors
- [c0demode](https://github.com/c0demode)
- [Larry Battle](https://github.com/LarryBattle)
- [Bryce Duncan](https://github.com/BryceDuncan)
- [na]()
- brayanpena530
- [Alexander Schulz](https://github.com/alxschlz98)

## Schedule
### v1.0 - Local: CLI 
* Due by June 15, 2023 1pm
- (B/P/Br) Pick a LLM / VectorStore project to use. (PrivateGPT, H2OGPT, LlamaIndex)
- (B/P/Br) Load models into LLM locally to have the demo work
- (B/P/Br) Upload the formatted data into the LLM locally
- (B/P) Launch the LLM locally
- (W) Create confluence page or wiki server
- (W) Create fake product pages
- (W) Import fake product pages into wiki / confluence
- (W) Export the confluence pages
- (W/L) Format the confluence exported data to work with the LLM
- (Br) Create architecture diagram
- (L) Update readme.md
- (L) Create queries to testing the LLM / VectorStore

### v1.1 - Local: Microservice
* Due by June 15, 2023 3pm
- (L) Create the architecture and API contracts for each main modules
- (B) Choose the microservice frameworks
- (B) Create a microservice to use for the LLM / VectorStore
- (Br) Create a setup document of have to integrate this with a existing confluence site
- (L/W) Create a report to show the data accuracy / confusion matrix of the LLM / VectorStore vs Confluence search
- (L) Have a e2e tests that hit the LLM microservice endpoints

### v1.2 - Local: UI
* Due by June 15, 2023 5pm
- (A) Choose the UI framework
- (A) Create UI microservice for querying the LLM / VectorStore
- (A) Launch UI locally

### v1.3 - AWS: Microservice
* Due by June 15, 2023 5pm
- (P) Upload the formatted data into the LLM in AWS
- (P) Launch the LLM in AWS
- (P) Load models into LLM in AWS to have the demo work


### v1.4 - AWS: UI
* Due June 16 9:30am
- (A) Launch UI in AWS

### Create presentation
* by June 15, 10pm
- (L) Create presentation
- (L) Create video of the hackathon 
- (L) Upload to Youtube

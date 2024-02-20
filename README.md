# Pharmaceutical Marketing Material Generator

## Intro

This tool will generate marketing materials for the pharmaceutical industry.

It consists of a Flask backend, that will generate prompts that are sent to an LLM, and return marketing copy;
and a Streamlit front end, that will accept user inputs and display results.

As this is just a POC the front end and back end are ran indepentently.

### Running Backend

```
>cd backend
>pipenv install
>pipenv run flask --app ./generate_email/index --debug run -h 0.0.0.0
```

### Running Front End

First install Streamlit: https://docs.streamlit.io/get-started/installation

```
>cd frontend
>streamlit run app.py
```

A notebook outlining the prompt and content generation process can be found here:
[Text_Generation_Notebook](https://github.com/quaneh/pharma-marketing-generator/tree/main/notebooks/TextGeneration.ipynb)
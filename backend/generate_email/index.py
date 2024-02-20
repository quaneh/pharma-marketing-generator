
import json
from six.moves.urllib.request import urlopen
from functools import wraps

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, request

# from flask.globals import request_ctx
# from flask_cors import cross_origin
# from jose import jwt


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

from model.params import Params, ParamsSchema

# Create an APISpec
spec = APISpec(
    title="Pharma Marketing Generator",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


app = Flask(__name__)


# initialize the model
model = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key='<ENTER_OPENAI_KEY>', max_tokens=1500)

pinecone.init(
    api_key='<ENTER_PINECONE_KEY',
    environment='gcp-starter'
)

model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key="<ENTER_OPENAI_KEY>"
)

index_name = 'email-template-embeddings'
text_field = "text"

# switch back to normal index for langchain
index = pinecone.Index(index_name)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)


template = """
You are an AI assistant that creates marketing materials for pharmaceutical products.

Write an edvertisement for the drug {product_name}.
The drug's active ingredient is {drug_name}.
The drug treats the following conditions: {indications}.
The dosing period is {dosing_period}.
The producer is {pharma_producer}
"""


prompt_template = PromptTemplate(
    template=template,
    input_variables=[]
)

@app.route("/")
# @cross_origin(headers=["Content-Type", "Authorization"])
def home():
    return "WELCOME"

@app.route("/generate")
# @cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def generate():

    input_params = ParamsSchema().load(request.get_json())

    formatted_prompt = prompt_template.format(
        product_name=input_params['product_name'],
        drug_name=input_params['drug_name'],
        indications=input_params['indications'],
        dosing_period=input_params['dosing_period'],
        pharma_producer=input_params['pharma_producer']
    )

    with get_openai_callback() as cb:
        ai_response = model(formatted_prompt)
        print(cb)
    return {
        'prompt': formatted_prompt,
        'ai_response': ai_response,
        'total_tokens': cb.total_tokens,
        'prompt_tokens': cb.prompt_tokens,
        'completion_tokens': cb.completion_tokens,
        'requests': cb.successful_requests,
        'cost': cb.total_cost
    }

# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=generate)
import json
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

app = Flask(__name__)

try:
    load_dotenv()
    # Configurações do Azure Search
    AZURE_SEARCH_SERVICE_NAME = os.environ.get('AZURE_SEARCH_SERVICE_NAME')
    AZURE_SEARCH_INDEX_NAME = os.environ.get('AZURE_SEARCH_INDEX_NAME')
    AZURE_ADMIN_KEY = os.environ.get('AZURE_ADMIN_KEY')

    AZURE_SEARCH_ENDPOINT = 'https://' + AZURE_SEARCH_SERVICE_NAME + '.search.windows.net/'
    credential = AzureKeyCredential(AZURE_ADMIN_KEY)
    search_client = SearchClient(endpoint=AZURE_SEARCH_ENDPOINT, index_name=AZURE_SEARCH_INDEX_NAME, credential=credential)
except Exception as err:
    print(f'As chaves não foram definidas: {err}')

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        response = search_client.search(search_text=query)
        for result in response:
            results.append(result)
    formatted_results = json.dumps(results, indent=4)
    return render_template('index.html', results=formatted_results)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, Response
import csv
from datetime import datetime
import json

app = Flask(__name__)

# Função para converter datas para o formato padrão 'YYYY-mm-dd'
def parse_date(date_str):
    formats_to_try = ['%Y-%m-%d', '%d %B, %Y', '%Y-%m-%d %H:%M:%S.%f']
    for fmt in formats_to_try:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            pass
    # Se nenhuma conversão for bem-sucedida, retornar None
    return None

# Carregar os dados do arquivo CSV para uma lista de dicionários
def load_data():
    data = []
    with open('atendimentos.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Aplicando a função para converter as datas ao formato padrão
            row['data_atendimento'] = parse_date(row['data_atendimento'])
            data.append(row)
    return data

# Endpoint para consultar os atendimentos
@app.route('/api/v1/atendimentos', methods=['GET'])
def get_atendimentos():
    data = load_data()

    # Aplicar os filtros
    filtered_data = data
    if 'data_atendimento' in request.args:
        filtered_data = [item for item in filtered_data if item['data_atendimento'] == request.args['data_atendimento']]
    if 'condicao_saude' in request.args:
        condicao_saude_query = request.args['condicao_saude'].lower()  # Converter para minúsculas
        filtered_data = [item for item in filtered_data if item['condicao_saude'].lower() == condicao_saude_query]
    if 'unidade' in request.args:
        unidade_query = request.args['unidade'].lower()  # Converter para minúsculas
        filtered_data = [item for item in filtered_data if item['UNIDADE'].lower() == unidade_query]

    # Tratamento para acentos
    json_data = json.dumps(filtered_data, ensure_ascii=False, indent=4).encode('utf-8')

    # Adicionar quebra de linha
    json_response = b''
    for chunk in json_data.split(b'\n'):
        json_response += chunk + b'\n'

    return Response(json_response, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True, port=8001)

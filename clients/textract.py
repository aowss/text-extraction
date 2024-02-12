import boto3


def extract_data(file_content):
    textract = boto3.client('textract', region_name='us-east-2')
    bytes = bytearray(file_content)
    result = textract.detect_document_text(Document={'Bytes': bytes})
    analyze_result = textract.analyze_document(Document={'Bytes': bytes}, FeatureTypes=['FORMS'])
    print('analyze result: ', process_analyze_response(analyze_result))
    return result

def process_analyze_response(response):
    blocks = response['Blocks']

    # get key and value maps
    key_map = {}
    value_map = {}
    block_map = {}
    for block in blocks:
        block_id = block['Id']
        block_map[block_id] = block
        if block['BlockType'] == "KEY_VALUE_SET":
            if 'KEY' in block['EntityTypes']:
                key_map[block_id] = block
            else:
                value_map[block_id] = block

    return key_map, value_map, block_map
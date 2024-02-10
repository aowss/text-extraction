import boto3


def extract_data(file_content):
    textract = boto3.client('textract')
    bytes = bytearray(file_content)
    result = textract.detect_document_text(Document={'Bytes': bytes})
    return result

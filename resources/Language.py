import langid
import pdfplumber
import docx
import os
from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource, fields, request, reqparse, marshal
from utils.jwt import check_premission

"""iso-639 中英文映射"""
LAN_MAPPER = {}
with open(
    file=os.path.abspath(path=os.path.join('static', 'language.txt')),
    mode='r',
    encoding='utf-8',
) as f:
    for item in f.readlines():
        lan_type, lan_name = str(item).split(' ')
        LAN_MAPPER[lan_type] = lan_name.replace('\n', '')

fields_dict = {
    'lg_type': fields.String,
    'lg_name': fields.String,
    'lg_text': fields.String,
}


class LanguageRec(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('text', type=str, location='form')
        self.parser.add_argument('file', type=str, location='files')

    def return_lg_type(self, ans, text):
        lg_name = ''
        if ans in LAN_MAPPER:
            lg_name = LAN_MAPPER[ans]
        dic = {'lg_type': ans, 'lg_name': lg_name, 'lg_text': text}
        return marshal(dic, fields_dict, envelope='data')

    def parse_pdf_file(self, file):
        content = ''
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                content += page.extract_text()

        return content 

    def parse_docx_file(self, file):
        content = ''
        doc = docx.Document(file)
        for paragraph in doc.paragraphs:
            print(paragraph)
            content += paragraph.text

        return content
    
    def parse_ordinary_file(self, file):
        """
        markdown. txt
        """
        return bytes(file.read()).decode().replace('\n', '').strip()

    def post(self):
        text = self.parser.parse_args()['text']
        if text is not None:
            return self.return_lg_type(langid.classify(text)[0], text)
        else:
            file = request.files['file']
            dir_name = file.filename.split('.')[1]
            if dir_name == 'pdf':
                content = self.parse_pdf_file(file)
            elif dir_name == 'docx':
                content = self.parse_docx_file(file)
            else:
                content = self.parse_ordinary_file(file)

            return self.return_lg_type(langid.classify(content[0:1000])[0], content)

langrc_blueprint = Blueprint('langrc', __name__, url_prefix='/api')
langrc_blueprint.before_app_request(check_premission)
langrc_api = Api(langrc_blueprint)
langrc_api.add_resource(LanguageRec, '/langrc')
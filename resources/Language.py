import langid
import pdfplumber
import docx
import os
from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource, fields, request, reqparse, marshal
from sqlalchemy import insert
from config.db import engine
from config.db.history import History
from utils.jwt import check_premission
from utils.json_response import make_success_response

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
        return dic

    def get_pdf_content(self, file):
        content = ''
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                content += page.extract_text()

        return content

    def get_docx_content(self, file):
        content = ''
        doc = docx.Document(file)
        for paragraph in doc.paragraphs:
            print(paragraph)
            content += paragraph.text

        return content

    def get_oridinary_content(self, file):
        """
        markdown. txt
        """
        return bytes(file.read()).decode().replace('\n', '').strip()

    # 存储用户操作历史
    def mark_history(self, id, type, text):
        with engine.connect() as conn:
            conn.execute(
                insert(History),
                [{'content': text, 'type': type, 'user_id': id}],
            )
            conn.commit()
    
    def parse_file(self, file):
        dir_name = file.filename.split('.')[1]
        if dir_name == 'pdf':
            content = self.get_pdf_content(file)
        elif dir_name == 'docx':
            content = self.get_docx_content(file)
        else:
            content = self.get_oridinary_content(file)
        lg_type = self.get_text_lg_type(content)
        return [lg_type, content]
    
    def get_text_lg_type(self, text):
        return langid.classify(text[0:1000])[0]

    @check_premission
    def post(self, info):
        ans = None
        text = self.parser.parse_args()['text']
        if text is not None:
            # 基于文本进行语种识别
            _type = self.get_text_lg_type(text)
            self.mark_history(info['user_id'], _type, text)
            return make_success_response(self.return_lg_type(_type, text))
        else:
            # 基于文件进行语种识别
            ans = []
            files = request.files.getlist('file')
            for file in files:
                lg_type, content = self.parse_file(file=file)
                ans.append(self.return_lg_type(lg_type, content))
            return make_success_response(ans[0])


langrc_blueprint = Blueprint('langrc', __name__, url_prefix='/api')
langrc_api = Api(langrc_blueprint)
langrc_api.add_resource(LanguageRec, '/langrc')

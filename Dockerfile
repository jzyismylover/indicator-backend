FROM python:3.7-slim as build

WORKDIR /build

COPY nltk_data /root/nltk_data
COPY requirements.txt .
RUN pip install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com && \
pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "setup:app", "-c", "./gunicorn.conf.py"]
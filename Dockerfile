FROM python:3.7 as build

WORKDIR /build

COPY requirements.txt ./
RUN pip install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com && \
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
CMD ["gunicorn", "setup:app", "-c", "./gunicorn.conf.py"]
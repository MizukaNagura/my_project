# ベースとなるイメージを指定
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# 依存関係をインストールする
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# アプリケーションのソースコードをコピーする
COPY ./app /app

# 使用官方 Python 3.11 slim 镜像作为基础
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制并安装依赖，以利用Docker层缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY ./app ./app

# 暴露应用运行的端口
EXPOSE 8000

# 运行应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
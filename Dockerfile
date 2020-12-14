FROM python:3.8.6
RUN python -m pip install --upgrade pip
COPY . /app.api
WORKDIR /app.api
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["app.py" ]
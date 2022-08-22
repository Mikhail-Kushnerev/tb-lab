FROM python
RUN pip3 install --upgrade pip

WORKDIR /src
COPY ./requirements.txt /src
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./ ./src/

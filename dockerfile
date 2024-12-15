FROM python:3.9

WORKDIR /root/Litellm

COPY . /root/Litellm

RUN pip install openai

RUN pip install python-dotenv

RUN pip install --upgrade pip

RUN pip install litellm

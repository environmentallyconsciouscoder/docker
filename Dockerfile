FROM python:3.8-slim


WORKDIR /heart_model

COPY . /heart_model/

RUN apt-get update && \
    apt-get install -y gcc

RUN pip install -r requirements.txt


## default port for streamlit is 8501

EXPOSE 8501


CMD ["streamlit", "run", "heart_model.py"]
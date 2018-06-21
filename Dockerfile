FROM python:2.7

# better pip
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python - "pip==8.1.1"

# working dir
RUN mkdir /code
WORKDIR /code

# python deps
RUN pip install pip-tools
ADD requirements.txt /code/
RUN pip-sync

# rest of the code
ADD . /code/

# many useful env variables
#ENV FOO=BAR

# run time!
EXPOSE 3000
CMD ["gunicorn", "app", "--bind", "0.0.0.0:8000"]

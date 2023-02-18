FROM uselagoon/python-3.10

WORKDIR '/git_hub_ui_docker'

COPY '.' '/git_hub_ui_docker'
RUN pip install PyInstaller
RUN apk  update && apk add gcc
CMD [ "python","./check_file.py" ]
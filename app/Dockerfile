FROM python:3
 
ENV APP_HOME /app
 
WORKDIR $APP
 
COPY run.py templates static

RUN   pip3 install flask && pip3 install pillow
# Uruchamianie jako aplikacja flask (z domyślnym portem 5000)
#CMD ["flask", "--app=imageops.py", "run", "--host=0.0.0.0"]
# Uruchamianie jako aplikacja pthon (z domyślnym portem 8080 określonym wewnątrz aplikacji)
# CMD ["python3", "imageops.py"]
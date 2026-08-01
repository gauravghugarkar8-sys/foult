#base image
FROM python:3.12

#workdirectory
WORKDIR /app

#copy
COPY . /app
#COPY . .


# run
RUN pip install -r requirement.txt

#port
EXPOSE 8000
#doker automaticaly run this file
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
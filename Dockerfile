FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5432

CMD ["python", "./src/concert_tickets/main.py"]
FROM python
WORKDIR /home/ipa2026-msapp/worker
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-u", "consumer.py"]
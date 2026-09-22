FROM python
WORKDIR /home/ipa2026-msapp/worker
COPY . .
RUN pip install -r requirements.txt
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh && \
    printf "Host *\n  KexAlgorithms +diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1\n  Ciphers +aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc\n  HostKeyAlgorithms +ssh-rsa,ssh-dss\n  StrictHostKeyChecking no\n  UserKnownHostsFile /dev/null\n" > /root/.ssh/config
CMD ["python", "-u", "consumer.py"]
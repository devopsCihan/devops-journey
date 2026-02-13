FROM alpine:latest
WORKDIR /app
COPY ajan.sh .
RUN chmod +x ajan.sh
CMD ["./ajan.sh"]

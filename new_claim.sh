HOST=http://127.0.0.1:8000

curl $HOST \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"TestingMessage"}'

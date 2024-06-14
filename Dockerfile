FROM ghcr.io/ggerganov/llama.cpp:server

COPY ./models/ models/

CMD ["-c", "2048", "-m", "models/7B/OLMo-1.7-7B.IQ3_M.gguf", "--port", "8080", "--host", "0.0.0.0"]
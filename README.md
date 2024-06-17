[[_TOC_]]

# Description

**Setup showcase for LLM's in docker for communication via HTTP requests**

*Setup for CPU. For GPU need to research llama.cpp options*

# Showcased models

- [OLMo-1.7-7B.IQ3_M](https://huggingface.co/nopperl/OLMo-1.7-7B-GGUF/blob/main/OLMo-1.7-7B.IQ3_M.gguf).
- [llama-2-7b-chat.Q4_K_M](https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q4_K_M.gguf)
- [qwen2-7b-instruct-q3_k_m](https://huggingface.co/Qwen/Qwen2-7B-Instruct-GGUF/blob/main/qwen2-7b-instruct-q3_k_m.gguf)
- [gpt2.Q6_K](https://huggingface.co/RichardErkhov/openai-community_-_gpt2-gguf/blob/main/gpt2.Q6_K.gguf)

# Requirements

- Docker, docker compose with at least 8GB memory allocated to them (and as much CPU as possible)

# Up and running

1. Download showcased models (See `Showcased models` section)
2. Place your models into `models` folder in the root of the project under `model` name folder:

```
models/<new_model>/<new_model>.gguf
```

3. Up project via docker compose

```sh
docker compose up <service_name>
```

Possible services:

- `olmo` for `OLMo-1.7-7B.IQ3_M`. Port: `8080`
- `llama` for `llama-2-7b-chat.Q4_K_M`. Port: `8081`
- `qwen2` for `qwen2-7b-instruct-q3_k_m`. Port: `8082`
- `gpt2` for `gpt2.Q6_K`. Port: `8083`

You can also up all services it once (be careful with CPU, memory usage):

```sh
docker compose up
```

# Usage example

[Example from llama-cpp docs](https://github.com/ggerganov/llama.cpp/tree/master/examples/server#testing-with-curl)

# How to add new model as a new service

1. Ensure `llama-cpp` [supports](https://github.com/ggerganov/llama.cpp/tree/master?tab=readme-ov-file#description) new model architecture
2. Download `gguf`-ed model to your `models` folder
3. Create dockerfile for new model:

```sh
touch Dockerfile.new_model
```
4. Set `<new_model_file_name>` in new dockerfile:

```dockerfile
FROM ghcr.io/ggerganov/llama.cpp:server

CMD ["-c", "2048", "-m", "models/<new_model_file_name>.gguf", "--port", "8080", "--host", "0.0.0.0"]
```

5. Add new service to `docker-compose.yml`:

```yml
services:
  olmo:
    ...
  <new_model>:
    build:
      dockerfile: Dockerfile.<new_model>
    ports:
      - 8084:8080
    volumes:
      - ./models/<new_model>/:/models/
```

**Ensure that port is available**

6. Update `Showcased models` and `Possible services` sections in `README.md`

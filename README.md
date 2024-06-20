# Description

**Setup showcase for running LLM's in docker**

*Setup for CPU. For GPU need to research llama.cpp options*

# Requirements

- Docker, docker compose with at least 8GB memory allocated to them (and as much CPU as possible)

# How to run OLMo

1. Pull and build llamacpp container:

```sh
docker compose up -d olmo
```

2. Attach to container shell:

```sh
docker exec -it loki-olmo-1 /bin/bash
```

3. Download model:

```sh
olmo_download
```

4. Run chat with model:

```sh
olmo_run
```

# OLD info

<details>

<summary>TODO: need update</summary>

## Showcased models

- [OLMo-1.7-7B.IQ3_M](https://huggingface.co/nopperl/OLMo-1.7-7B-GGUF/blob/main/OLMo-1.7-7B.IQ3_M.gguf).
- [llama-2-7b-chat.Q4_K_M](https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q4_K_M.gguf)
- [qwen2-7b-instruct-q3_k_m](https://huggingface.co/Qwen/Qwen2-7B-Instruct-GGUF/blob/main/qwen2-7b-instruct-q3_k_m.gguf)
- [gpt2.Q6_K](https://huggingface.co/RichardErkhov/openai-community_-_gpt2-gguf/blob/main/gpt2.Q6_K.gguf)
- [zephyr-7b-beta.Q3_K_M](https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/blob/main/zephyr-7b-beta.Q3_K_M.gguf)
- [Phi-3-mini-128k-instruct](https://huggingface.co/MoMonir/Phi-3-mini-128k-instruct-GGUF/blob/main/phi-3-mini-128k-instruct.Q6_K.gguf)
- [sdxl-flash](https://huggingface.co/sd-community/sdxl-flash/blob/main/SDXL-Flash.safetensors). [vae](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/blob/main/sdxl_vae.safetensors)
- [whisper](https://ggml.ggerganov.com/)

## Up and running

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
- `zephyr` for `zephyr-7b-beta.Q3_K_M`. Port: `8084`
- `phi3` for `Phi-3-mini-128k-instruct`. Port: `8085`
- `stable_diffusion` for `sdxl-flash`. Port: `8086`
- `whisper` for `whisper.cpp`. Port: `8087`

You can also up all services it once (be careful with CPU, memory usage):

```sh
docker compose up
```

## Usage example

[Example from llama-cpp docs](https://github.com/ggerganov/llama.cpp/tree/master/examples/server#testing-with-curl)

## How to add new model as a new service

1. Ensure `llama-cpp` [supports](https://github.com/ggerganov/llama.cpp/tree/master?tab=readme-ov-file#description) new model architecture
2. Download `gguf`-ed (or any other format) model to your `models` folder
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
      - 8088:8080
    volumes:
      - ./models/<new_model>/:/models/
```

**Ensure that port is available**

6. Update `Showcased models` and `Possible services` sections in `README.md`

## How to use stable diffusion model

CURL request to generate image: 

```sh
curl --location 'http://localhost:8086/api/v1/image' \
--header 'Content-Type: application/json' \
--data '{
    "text": "cat"
}'
```

Currently only one endpoint available and only `text` parameter supported.

</details>
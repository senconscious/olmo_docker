**Showcase of using OLMo in docker via HTTP requests**

*Using gguf-ed version of OLMo https://huggingface.co/nopperl (created during llama.cpp integration https://github.com/ggerganov/llama.cpp/pull/6741)*

## Requirements

- Docker, docker compose with at least 8GB memory allocated to them (and as much CPU as possible)

## Up and running

1. Goto [model page](https://huggingface.co/nopperl/OLMo-1.7-7B-GGUF/blob/main/OLMo-1.7-7B.IQ3_M.gguf) and download it.
2. Place your model into `models/7B` folder in the root of the project
3. Up project via docker compose

```sh
docker compose up
```

## How to add another model

1. Ensure `llama-cpp` [supports](https://github.com/ggerganov/llama.cpp/tree/master?tab=readme-ov-file#description) new model architecture
2. Download gguf-ed model to your `models` folder
3. Edit `CMD` model path:

Replace this:

```sh
"models/7B/OLMo-1.7-7B.IQ3_M.gguf"
```

with new model:

```sh
"models/7B/my_new_model.gguf"
```

## Usage example

[Example from llama-cpp docs](https://github.com/ggerganov/llama.cpp/tree/master/examples/server#testing-with-curl)

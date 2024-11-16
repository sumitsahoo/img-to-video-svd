# ℹ️ IMG2VID
Generate video from image using Stable Video Diffusion by StabilityAI and Replicate.<br>
Stable Video Diffusion: https://stability.ai/stable-video<br>
Replicate: https://replicate.com/

## 📖 Medium Article
Here is the Medium Article: https://medium.com/@sumitsahoo/stable-video-diffusion-with-replicate-7bdd3ff3879e

## 📦 Dependency Installation

You need `Python 3.12.7` or `3.13.0` installed in your system. If you are using `pyenv` then check the version using command: `pyenv version`

1. Install poetry
    ```bash
    # Using pip
    pip install poetry
    
    # Using brew (macOS), if you are using pyenv you should use `pip install poetry`
    brew install poetry
    ```
2. Set poetry to create virtual environment within project folder
    ```bash
    poetry config virtualenvs.in-project true
    ```
3. Install dependency and create the virtual environment
    ```bash
    poetry install
    ``` 
4. Run the app with poetry
    ```python
    poetry run python main.py
    ```
    or launch the app via VS Code debug menu. VS Code launch config file is also provided for easy debugging 🤓


To update dependencies use: `poetry update`<br>
If you want to update dependencies in `pyproject.toml`, then you need to install plugin `poetry-plugin-up`. Use command below:
```
poetry self add poetry-plugin-up
```
Once installed, use command `poetry up` to install updates and edit `pyproject.toml` automatically.<br>
To view virtual environment location, use: `poetry env info --path`<br>
To generate `requirements.txt` using poetry, you need to have export plugin installed.<br>

Install the plugin:
```bash
poetry self add poetry-plugin-export
```
Once the plugin is installed, use `export` command to generate `requirements.txt`
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```



## 🔑 Environment Variable
There are 2 environment variable you can specify.
1. REPLICATE_API_TOKEN: This is your Replicate API key.
2. GRADIO_SERVER_PORT: This is Gradio server port. This is optional if not specified in `launch` method.

## 🚢 Docker

If you are planning on deploying the app to cloud, you need a Docker image. To build the same use the `Dockerfile` provided. The multi-stage build makes sure the resulting image is smaller in size and only includes the libraries that is needed. Also the use of non-root user makes it more secure.<br>

Build arm64 image (Make sure cloud deployment supports arm64 images):
```bash
docker build --no-cache -t img2vid_latest .
```
For amd64 image (most common and widely supported):
```bash
docker buildx build --no-cache --platform linux/amd64 -t img2vid_latest .
```

Once image is built, you can push the same to any cloud provider and use a serverless service to deploy the same easily.

To run Docker image locally use below command:
```bash
docker run -it \
-e GRADIO_SERVER_PORT=8080 \
-e REPLICATE_API_TOKEN=your_key_here \
-p 8080:8080 \
--name img2vid \
img2vid_latest
```

## 🙏🏻 Attributions
<a href="https://www.gradio.app/" title="gradio ui">UI is built using Gradio</a><br>
<a href="https://www.flaticon.com/free-icons/video" title="video icons">Video icons created by Prosymbols Premium - Flaticon</a><br>
<a href="https://basicappleguy.com/basicappleblog/os-x-rancho-cucamonga" title="wallpaper">Rancho Cucamonga wallpaper by thebasicappleguy</a>

## 📜 License

MIT License

Copyright (c) 2024 Sumit Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

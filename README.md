# IMG2VID
Generate video from image using Stable Video Diffusion by StabilityAI and Replicate.<br>
Stable Video Diffusion: https://stability.ai/stable-video<br>
Replicate: https://replicate.com/

## Medium Article
Drafting ...

## Dependency Installation

You need `Python 3.12.0` installed in your system. If you are using `pyenv` then check the version using command: `pyenv version`

1. Install poetry
    ```bash
    # Using pip
    pip install poetry
    
    # Using brew (macOS), if you are using pyenv you should use `pip install poetry`
    brew install poetry
    ```
2. Install the dependencies and create virtual environment
    Make poetry create virtual environment within project folder
    ```bash
    poetry config virtualenvs.in-project true
    ```
    Now, install dependency and create the environment
    ```bash
    poetry install
    ```
3. Activate the virtual environment and enter into the shell
    ```bash
    poetry shell
    ```    
4. Run the app
    ```python
    python3 main.py
    ```
To update dependencies use: `poetry update`<br>
To view virtual environment location, use: `poetry env info --path`<br>
To generate `requirements.txt` using poetry, use below command:
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## Attributions
<a href="https://www.gradio.app/" title="gradio ui">UI is built using Gradio</a><br>
<a href="https://www.flaticon.com/free-icons/video" title="video icons">Video icons created by Prosymbols Premium - Flaticon</a><br>
<a href="https://basicappleguy.com/basicappleblog/os-x-rancho-cucamonga" title="wallpaper">Rancho Cucamonga wallpaper by thebasicappleguy</a>

## License

MIT License

Copyright (c) 2023 Sumit Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

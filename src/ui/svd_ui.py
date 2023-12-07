import gradio as gr
import os
from src.util.svd_util import SVDUtil
from src.util.log_util import LogUtil


class SVDUI:
    def __init__(self):
        self.svd_util = SVDUtil()
        self.log = LogUtil()
        self.theme = gr.themes.Base(
            primary_hue="red",
            secondary_hue="red",
        ).set(
            # button_primary_background_fill="*secondary_500",
            button_primary_background_fill="#2196F3",
            button_primary_background_fill_dark="*primary_500",
            button_primary_text_color="white",
            loader_color="#2196F3",
        )

    def upload_file(self, file_path):
        svd_response = self.svd_util.generate_video_from_image(file_path)
        return svd_response

    def launch_ui(self):
        # Check if index is built

        custom_css = """
            
            footer {visibility: hidden}
        """

        with gr.Blocks(
            title="Generate UI Code",
            theme=self.theme,
            # css=custom_css,
        ) as generate_code:
            gr.Image(
                "./images/logo.svg",
                height=80,
                width=400,
                interactive=False,
                container=False,
                show_download_button=False,
            )

            gr.Textbox(
                value="(SVD) Image-to-Video is a latent diffusion model trained to generate short video clips from an image conditioning. This model was trained to generate 14 frames at resolution 576x1024 given a context frame of the same size.",
                show_label=False,
                interactive=False,
                container=False,
            ),

            gr.Interface(
                fn=self.svd_util.generate_video_from_image,
                inputs=[
                    gr.Image(
                        sources=["upload"],
                        type="filepath",
                        height=400,
                    ),
                ],
                outputs=[
                    gr.Video(
                        autoplay=True,
                        height=400,
                    ),
                    gr.Textbox(
                        label="Video URL", info="URL will be valid for 24hrs only"
                    ),
                ],
                examples=[
                    "./images/example/example1.png",
                    "./images/example/example2.png",
                    "./images/example/example3.png",
                ],
                flagging_options=None,
                allow_flagging=False,
            )

        generate_code.queue().launch(
            favicon_path="./images/favicon.ico",
            debug=False,
            show_api=False,
            server_name="0.0.0.0",
            server_port=8080,
            share=False,
            allowed_paths=["./images/", "./outputs/"],
        )

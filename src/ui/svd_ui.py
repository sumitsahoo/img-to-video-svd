import gradio as gr

from src.util.log_util import LogUtil
from src.util.svd_util import SVDUtil


class SVDUI:
    def __init__(self):
        self.svd_util = SVDUtil()
        self.log = LogUtil()
        self.theme = gr.themes.Base(
            primary_hue="purple",
            secondary_hue="purple",
        ).set(
            # button_primary_background_fill="*secondary_500",
            button_primary_background_fill="#8D64A3",
            button_primary_background_fill_dark="*primary_500",
            button_primary_text_color="white",
            loader_color="#8D64A3",
        )

    def launch_ui(self):
        # Check if index is built

        custom_css = """
            
            footer {visibility: hidden}
        """

        with gr.Blocks(
            title="IMG2VID",
            theme=self.theme,
            # css=custom_css,
        ) as img_to_vid:
            gr.Image(
                "./images/logo.svg",
                height=80,
                width=400,
                interactive=False,
                container=False,
                show_download_button=False,
            )

            (
                gr.Textbox(
                    value="(SVD) Image-to-Video is a latent diffusion model trained to generate short video clips from an image conditioning. This model was trained to generate 14 frames at resolution 576x1024 given a context frame of the same size. The generated videos are rather short (<= 4sec), and the model may not achieve perfect photorealism.",
                    show_label=False,
                    interactive=False,
                    container=False,
                ),
            )

            gr.Interface(
                fn=self.svd_util.generate_video_from_image,
                inputs=[
                    gr.Image(
                        label="Select Image",
                        sources=["upload"],
                        type="filepath",
                        height=400,
                    ),
                ],
                outputs=[
                    gr.Video(
                        label="Generated Video",
                        autoplay=True,
                        height=400,
                    ),
                    gr.Textbox(
                        label="Video URL",
                        info="URL will be valid for 1 hour only and content will be deleted after this",
                        show_copy_button=True,
                    ),
                ],
                examples=[
                    "./images/example/example1.png",
                    "./images/example/example2.png",
                    "./images/example/example3.png",
                ],
                allow_flagging="never",
            )

        img_to_vid.queue().launch(
            favicon_path="./images/favicon.ico",
            debug=False,
            show_api=False,
            server_name="0.0.0.0",
            server_port=8080,
            share=False,
            allowed_paths=["./images/", "./outputs/"],
        )

from src.util.log_util import LogUtil
import replicate


class SVDUtil:
    def __init__(self):
        self.log = LogUtil()
        self.model = "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438"

        # Gradio UI can be customized to take below parameters as input

        # Use svd to generate 14 frames or svd_xt for 25 frames
        self.video_length = "14_frames_with_svd"  # Possible values: 14_frames_with_svd, 25_frames_with_svd_xt
        # Frames per second
        self.frames_per_second = 6
        # Decide how to resize the input image
        self.sizing_strategy = "maintain_aspect_ratio"  # Possible values: maintain_aspect_ratio, crop_to_16_9, use_image_dimensions
        # Increase overall motion in the generated video
        self.motion_bucket_id = 127
        # Amount of noise to add to input image
        self.cond_aug = 0.02
        # Number of frames to decode at a time
        self.decoding_t = 7
        # Random seed. Leave blank to randomize the seed
        self.seed = 0

    # Generate video from image using SVD
    def generate_video_from_image(self, image_path):
        self.log.info("Generating video from image ...")
        try:
            with open(image_path, "rb") as input_image:
                output = replicate.run(
                    self.model,
                    input={
                        "cond_aug": self.cond_aug,
                        "decoding_t": self.decoding_t,
                        "input_image": input_image,
                        "video_length": self.video_length,
                        "sizing_strategy": self.sizing_strategy,
                        "motion_bucket_id": self.motion_bucket_id,
                        "frames_per_second": self.frames_per_second,
                    },
                )
                self.log.info(f"Generated video link: {output}")
                return (output, output)
        except Exception as e:
            self.log.error(f"Error: {e}")
        return (None, "Unable to generate video from image")

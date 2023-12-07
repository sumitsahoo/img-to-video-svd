from src.util.log_util import LogUtil
import replicate


class SVDUtil:
    def __init__(self):
        self.log = LogUtil()

    def generate_video_from_image(self, image_path):
        return (
            "https://replicate.delivery/pbxt/OzIIy45oJqK3JNPt70iU9ZaLzSNjrasOOil5xUMERfWq87fRA/000031.mp4",
            "https://replicate.delivery/pbxt/OzIIy45oJqK3JNPt70iU9ZaLzSNjrasOOil5xUMERfWq87fRA/000031.mp4",
        )
        self.log.info("Generating video from image")
        with open(image_path, "rb") as input_image:
            output = replicate.run(
                "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
                input={
                    "cond_aug": 0.02,
                    "decoding_t": 7,
                    "input_image": input_image,
                    "video_length": "14_frames_with_svd",
                    "sizing_strategy": "maintain_aspect_ratio",
                    "motion_bucket_id": 127,
                    "frames_per_second": 6,
                },
            )
            self.log.info(f"Generated video link: {output}")

            return (output, output)

from serpent.game import Game

from .api.api import Va11HallAAPI

from serpent.utilities import Singleton


class SerpentVa11HallAGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "VA-11 Hall-A: Cyberpunk Bartender Action"

        kwargs["app_id"] = "447530"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = Va11HallAAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:1280x720|GRAYSCALE"

        self.frame_width = 1280
        self.frame_height = 720
        self.frame_channels = 0

    @property
    def screen_regions(self):
        regions = {
            "HP_AREA": (180, 730, 210, 850),
            "SCORE_AREA": (180, 730, 210, 850)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets

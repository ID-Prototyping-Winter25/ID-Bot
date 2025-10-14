from gradio.themes.base import Base


class CustomTheme(Base):
    def __init__(self):
        super().__init__()

        super().set(
            body_background_fill="orange",
            body_background_fill_dark="blue",
            input_background_fill="#1f8766",
            input_background_fill_dark="#f52fee"
        )
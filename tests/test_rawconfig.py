# External Packages
import pytest

# Internal Packages
from khoj.utils.rawconfig import TextContentConfig, ImageContentConfig


# Test
# ----------------------------------------------------------------------------------------------------
def test_input_filter_or_directories_required_in_image_content_config():
    # Act
    with pytest.raises(ValueError):
        ImageContentConfig(
            input_directories=None,
            input_filter=None,
            embeddings_file="note_embeddings.pt",
        )

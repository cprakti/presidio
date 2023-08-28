import logging
from typing import List

from presidio_analyzer.predefined_recognizers.spacy_recognizer import SpacyRecognizer
from presidio_analyzer import RecognizerResult

logger = logging.getLogger("presidio-analyzer")


class TransformersRecognizer(SpacyRecognizer):
    """
    Recognize entities using the spacy-huggingface-pipeline package.

    The recognizer doesn't run transformers models,
    but loads the output from the NlpArtifacts
    See:
     - https://huggingface.co/docs/transformers/main/en/index for transformer models
     - https://github.com/explosion/spacy-huggingface-pipelines on the spaCy wrapper to transformers
    """ # noqa E501

    ENTITIES = [
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "AGE",
        "ID",
        "EMAIL",
        "DATE_TIME",
        "PHONE_NUMBER",
    ]

    LOW_SCORE_ENTITY_NAMES = {"ID"}

    def __init__(self, **kwargs):
        self.DEFAULT_EXPLANATION = self.DEFAULT_EXPLANATION.replace(
            "Spacy", "Transfromers"
        )
        super().__init__(**kwargs)

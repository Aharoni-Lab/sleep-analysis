from pathlib import Path

from sleep_analysis.io.io import IO

class EEGLab(IO):
    """
    Import eeglab data!

    Args:
        directory (:class:`pathlib.Path`): Some path that we want to use
    """

    def __init__(
        self,
        directory: Path
    ):
        self.directory = directory

class EEGLab2(IO):
    """
    Import eeglab data! AGAIN

    Args:
        directory (:class:`pathlib.Path`): Some path that we want to use
    """

    def __init__(
        self,
        directory: Path
    ):
        self.directory = directory
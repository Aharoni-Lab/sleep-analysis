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

    def load(self, path:Path):
        """
        Given some directory, load the raw eeg files

        Args:
            path:

        Returns:

        """
        set_files = Path(path).glob('*.set')

        # TODO: Finish me





import shutil
from pathlib import Path

from data import DATA_DIR
from utils import read_json


class OrganizeDir:
    """Class to organize files in a given directory.

    Example:
    >>> organizer = OrganizeDir()
    >>> organizer.run(to_organize_directory)
    """
    suffix_dir = read_json(DATA_DIR / 'suffix_dir.json')

    def __call__(self, to_organize_dir: str):
        """Runs organizer job to move files to the specified destinations
        in suffix_dir.

        :param to_organize_dir: directory to run organization job
        """
        self.to_organize_dir = Path(to_organize_dir).resolve()
        assert self.to_organize_dir.exists(),\
            f'Directory "{self.to_organize_dir}" not found!'

        # iterate over files to organize
        for path in self.to_organize_dir.iterdir():

            if path.is_dir():
                # to avoid moving directories created by us
                if path.name in OrganizeDir.suffix_dir.values():
                    continue

                dest = 'dirs'
                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

            elif path.is_file():
                suffix = path.suffix
                dest = OrganizeDir.suffix_dir.get(suffix)

                # suffix is not supported yet
                # does not exist in suffix_dir
                if not dest:
                    continue

                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))


if __name__ == '__main__':
    HOME_DIR = Path.home()
    organizer = OrganizeDir()
    organizer(HOME_DIR / 'Downloads')

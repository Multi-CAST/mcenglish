import pathlib

from multicastpy.dataset import Dataset as BaseDataset


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "mcenglish"

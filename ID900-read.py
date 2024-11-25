import numpy as np
from pathlib import Path

wd = Path.home().joinpath("project/Correlation")
datapath_1 = wd / "timestamps_C1-10.bin"
data_1b = datapath_1.read_bytes()
datapath_3 = wd / "timestamps_C3-10.bin"
data_3b = datapath_3.read_bytes()
datapath_4 = wd / "timestamps_C4-10.bin"
data_4b = datapath_4.read_bytes()

data_1 = np.frombuffer(data_1b, dtype='uint64')
data_3 = np.frombuffer(data_3b, dtype='uint64')
data_4 = np.frombuffer(data_4b, dtype='uint64')
exit(0)



from hsi_moss.hsi_prepare import *
from hsi_moss.spectral_tiffs import *
from hsi_moss.spectral_envi import *
import numpy as np
from progress.bar import Bar

base_dir = PurePath(r"E:\moss_data\Austin moss 2023\Moss")
metadata = np.loadtxt(base_dir.joinpath(r"Codes\paths+coordinates.csv").as_posix(), delimiter=',', dtype=str)

bar = Bar('Converting ENVI images to TIFF', max=metadata.shape[0])
fails = []
for line in metadata:
    index = line[0]
    path_relative = line[1]
    filename = line[2]
    fullpath = base_dir.joinpath(path_relative).joinpath(filename)
    hdrfullpath = fullpath.with_suffix('.hdr')
    
    if (Path(fullpath).exists() and not Path(fullpath.with_suffix('.tif')).exists()):
        try:
            envi_to_stiff(hdrfullpath)
        except:
            fails.append(line)
    bar.next()
bar.finish()
    
[print(f'Failed to convert {line[1]}/{line[2]}') for line in fails]

import os
from collections import namedtuple
from pathlib import Path

# Dataset root directory
_DATASET_ROOT = Path(__file__).parent / '../data'

Dataset = namedtuple('Dataset', ['name', 'root', 'src', 'bug_repo'])

# Source codes and bug repositories
# aspectj = Dataset(
#     'aspectj',
#     _DATASET_ROOT / 'AspectJ',
#     _DATASET_ROOT / 'AspectJ/AspectJ-1.5',
#     _DATASET_ROOT / 'AspectJ/AspectJBugRepository.xml'
# )

swt = Dataset(
    'swt',
    _DATASET_ROOT / 'SWT',
    _DATASET_ROOT / 'SWT/SWT-3.1',
    _DATASET_ROOT / 'SWT/SWTBugRepository.xml'
)

zxing = Dataset(
    'zxing',
    _DATASET_ROOT / 'ZXing',
    _DATASET_ROOT / 'ZXing/ZXing-1.6',
    _DATASET_ROOT / 'ZXing/ZXingBugRepository.xml'
)

tomcat = Dataset(
    'tomcat',
    _DATASET_ROOT / 'Tomcat',
    _DATASET_ROOT / 'Tomcat/tomcat-7.0.51',
    _DATASET_ROOT / 'Tomcat/Tomcat.txt'
)
aspectj = Dataset(
    'aspectj',
    _DATASET_ROOT / 'AspectJ',
    _DATASET_ROOT / 'AspectJ/org.aspectj-bug433351',
    _DATASET_ROOT / 'AspectJ/AspectJ.txt'
)
ui = Dataset(
    'ui',
    _DATASET_ROOT / 'Eclipse_Platform_UI',
    _DATASET_ROOT / 'Eclipse_Platform_UI/eclipse.platform.ui-johna-402445',
    _DATASET_ROOT / 'Eclipse_Platform_UI/Eclipse_Platform_UI.txt'
)
FullAspecj = Dataset(
    'FullAspecj',
    _DATASET_ROOT / 'Full-AspectJ',
    _DATASET_ROOT / 'Full-AspectJ/org.aspectj-bug433351',
    _DATASET_ROOT / 'Full-AspectJ/AspectJ.txt'
)
Birt = Dataset(
    'Birt',
    _DATASET_ROOT / 'Birt',
    _DATASET_ROOT / 'Birt/birt-20140211-1400',
    _DATASET_ROOT / 'Birt/Birt.txt'
)
# Current dataset in use. (change this name to change the dataset)
DATASET = Birt

if __name__ == '__main__':
    print(DATASET.name, DATASET.root, DATASET.src, DATASET.bug_repo)

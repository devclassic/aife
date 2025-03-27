打包用到

from PyInstaller.utils.hooks import copy_metadata, collect_submodules

# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=copy_metadata('tortoise-orm'),
    hiddenimports=collect_submodules('tortoise'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
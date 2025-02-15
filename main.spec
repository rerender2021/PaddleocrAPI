# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[
        '.\\venv\\Lib\\site-packages\\paddleocr',
        '.\\venv\\Lib\\site-packages\\paddle\\libs'
    ],
    binaries=[
        ('.\\venv\\Lib\\site-packages\\paddle\\libs', '.')
    ],
    datas=[
        ('.\\venv\\Lib\\site-packages\\paddle\\fluid\\proto', 'paddle/fluid/proto'),
        ('.\\venv\\Lib\\site-packages\\paddleocr\\ppocr', 'ppocr')
    ],
    hiddenimports=[
        'main',
        'framework_pb2',
        'scipy.special.cython_special',
        'skimage',
        'skimage.feature._orb_descriptor_positions',
        'skimage.filters.edges',
        'setuptools'
    ],
    hookspath=['.\\hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PaddleocrAPI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PaddleocrAPI',
)

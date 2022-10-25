# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['window_pygame.py'],
    pathex=['C:/Users/trajt/programming/python_work/spider_invasion/git_practice'],
    binaries=[],
    datas=[('images/interceptor-ship.bmp', 'images'),
    ('images/mite-alt.png', 'images'),
    ('images/polar-star.png', 'images'),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Планета пауков',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

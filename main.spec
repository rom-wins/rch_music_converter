# -*- mode: python ; coding: utf-8 -*-

def get_ytmusicapi_locales_data():
    locales_data = []
    yt_music_locales_dir = './.venv/Lib/site-packages/ytmusicapi/locales'
    for locale in os.listdir(os.path.join(yt_music_locales_dir)):
        if not os.path.isdir(os.path.join(yt_music_locales_dir, locale)):
            continue
        locales_data.append((
            os.path.join(yt_music_locales_dir, locale, 'LC_MESSAGES/*.mo'),
            os.path.join('ytmusicapi/locales', locale, 'LC_MESSAGES')
        ))
    return locales_data

a = Analysis(
    [
        'main.py',
    ],
    pathex=[],
    binaries=[],
    datas=get_ytmusicapi_locales_data(),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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

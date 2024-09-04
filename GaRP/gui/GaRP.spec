# example.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'], # Hauptdatei
             pathex=['./'], # Pfad zu deinem Python-Projekt
             binaries=[],
             datas=[
                ('settings.py', '.'),  # Einstellungen werden mit gepackt
                ('except_words_window.py', '.'), # Weitere Module hinzufügen
                ('parser_settings_window.py', '.'),
                ('languagetool_settings_window.py', '.'),
             ],
             hiddenimports=['py4j', 'customtkinter', 'tkinter'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='DeineAnwendung',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='DeineAnwendung')

import PyInstaller.__main__

PyInstaller.__main__.run([
    'RetroBitMegaDriveVisualizer.py',
    '--onefile',
    '--noconsole',
    '--windowed',
    '-i=images/icon.ico',
    '--add-data=images;images',
    '--debug=imports'
])
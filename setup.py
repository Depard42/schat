from cx_Freeze import setup, Executable
import zmq.libzmq


build_exe_options = {
    # zmq.backend.cython seems to be left out by default
    'packages': ['zmq.backend.cython', ],
    # libzmq.pyd is a vital dependency
    'include_files': [zmq.libzmq.__file__,],
}

setup(
    name='Secret Chat',
    version='1.0',
    description='Small and simple is our slogan:)',
    options={'build_exe': build_exe_options},
    executables=[Executable('SChat.py')],
)

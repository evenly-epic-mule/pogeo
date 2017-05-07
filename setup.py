#!/usr/bin/env python3

from os import environ
from sys import platform

from setuptools import setup, Extension

libraries = None
macros = [('NDEBUG', None)]
include_dirs = ['geometry', 'geometry/s2', 'geometry/util/math', 'include']
MANY_LINUX = False

if platform == 'win32':
    libraries = ['pthreadVC2']
    macros.append(('PTW32_STATIC_LIB', None))
    c_args = cpp_args = None
elif platform == 'darwin':
    c_args = ['-O3']
    if 'TRAVIS' not in environ:
        c_args.append('-march=native')
    cpp_args = c_args + ['-std=c++11', '-stdlib=libc++']
else:
    c_args = ['-O3']

    if 'MANYLINUX' in environ:
        MANY_LINUX = True
        c_args.extend(['-static-libgcc', '-static-libstdc++'])
    elif 'TRAVIS' not in environ:
        c_args.append('-march=native')
    cpp_args = c_args + ['-std=c++11']

libs = [('s2', {
        'language': 'c++',
        'macros': macros,
        'include_dirs': include_dirs,
        'cflags': cpp_args,
        'libraries': libraries,
        'sources': [
            'geometry/base/int128.cc',
            'geometry/base/logging.cc',
            'geometry/base/stringprintf.cc',
            'geometry/base/strtoint.cc',
            'geometry/strings/split.cc',
            'geometry/strings/stringprintf.cc',
            'geometry/strings/strutil.cc',
            'geometry/util/coding/coder.cc',
            'geometry/util/coding/varint.cc',
            'geometry/util/math/mathlimits.cc',
            'geometry/util/math/mathutil.cc',
            'geometry/s1angle.cc',
            'geometry/s2.cc',
            'geometry/s2cellid.cc',
            'geometry/s2latlng.cc',
            'geometry/s1interval.cc',
            'geometry/s2cap.cc',
            'geometry/s2cell.cc',
            'geometry/s2cellunion.cc',
            'geometry/s2edgeindex.cc',
            'geometry/s2edgeutil.cc',
            'geometry/s2latlngrect.cc',
            'geometry/s2loop.cc',
            'geometry/s2pointregion.cc',
            'geometry/s2polygon.cc',
            'geometry/s2polygonbuilder.cc',
            'geometry/s2polyline.cc',
            'geometry/s2r2rect.cc',
            'geometry/s2region.cc',
            'geometry/s2regioncoverer.cc',
            'geometry/s2regionintersection.cc',
            'geometry/s2regionunion.cc']}),
        ('urlencode', {
            'language': 'c++',
            'cflags': cpp_args,
            'sources': ['lib/urlencode.cpp']}),
        ('bitscan', {
            'language': 'c++',
            'macros': macros,
            'cflags': cpp_args,
            'sources': ['lib/bitscan.cpp']}),
        ('json', {
            'language': 'c++',
            'include_dirs': ['include'],
            'cflags': cpp_args,
            'sources': ['lib/json11.cpp']}),
        ('zlib', {
            'language': 'c',
            'include_dirs': ['include/zlib'],
            'cflags': c_args if not MANY_LINUX else c_args + ['-static'],
            'sources': [
                'lib/zlib/adler32.c',
                'lib/zlib/compress.c',
                'lib/zlib/crc32.c',
                'lib/zlib/deflate.c',
                'lib/zlib/trees.c',
                'lib/zlib/zutil.c'
            ]}),
        ('gzip', {
            'language': 'cpp',
            'include_dirs': ['include', 'include/zlib'],
            'cflags': cpp_args,
            'sources': ['lib/gzip.cpp']})]

try:
    from Cython.Build import cythonize
    file_ext = 'pyx'
except ImportError:
    file_ext = 'cpp'

exts = [Extension('pogeo.altitude',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/altitude.' + file_ext],
                  language='c++'),
        Extension('pogeo.const',
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  sources=['pogeo/const.' + file_ext],
                  language='c++'),
        Extension('pogeo.cellcache',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/cellcache.' + file_ext],
                  language='c++'),
        Extension('pogeo.geocoder',
                  include_dirs=include_dirs,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  sources=['pogeo/geocoder.' + file_ext],
                  language='c++'),
        Extension('pogeo.location',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/location.' + file_ext],
                  language='c++'),
        Extension('pogeo.loop',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/loop.' + file_ext],
                  language='c++'),
        Extension('pogeo.polygon',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/polygon.' + file_ext],
                  language='c++'),
        Extension('pogeo.polyline',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/polyline.' + file_ext],
                  language='c++'),
        Extension('pogeo.rectangle',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/rectangle.' + file_ext],
                  language='c++'),
        Extension('pogeo.utils',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args,
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/utils.' + file_ext],
                  language='c++'),
        Extension('pogeo.webcache',
                  define_macros=macros,
                  extra_compile_args=cpp_args,
                  extra_link_args=cpp_args if not MANY_LINUX else cpp_args + ['-Wl,-Bstatic', '-lzlib'],
                  include_dirs=include_dirs,
                  libraries=libraries,
                  sources=['pogeo/webcache.' + file_ext],
                  language='c++')]

if file_ext == 'pyx':
    exts = cythonize(exts)

setup(name='pogeo',
      version='0.4.0',
      description='Fast geography package.',
      long_description='A fast C++ extension for calculating cell IDs and distances.',
      url="https://github.com/Noctem/pogeo",
      author='David Christenson',
      author_email='mail@noctem.xyz',
      license='Apache',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: C++',
          'Programming Language :: Cython',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: GIS'],
      keywords='pogeo geography S2 distance geo geometry',
      libraries=libs,
      packages=['pogeo', 'pogeo.geo'],
      package_data={'pogeo': ['altitude.pxd', 'cellcache.pxd', 'const.pxd', 'location.pxd', 'loop.pxd', 'polygon.pxd', 'polyline.pxd', 'rectangle.pxd', 'utils.pxd', 'webcache.pxd'],
                    'pogeo.geo': '*.pxd'},
      ext_modules=exts)

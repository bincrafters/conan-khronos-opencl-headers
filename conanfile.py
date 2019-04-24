# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class OpenCLHeadersConan(ConanFile):
    name = "opencl-headers"
    version = "20190412"
    description = "Khronos OpenCL-Headers"
    topics = ("opencl")
    url = "https://github.com/bincrafters/conan-opencl-headers"
    homepage = "https://github.com/KhronosGroup/OpenCL-Headers"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/KhronosGroup/OpenCL-Headers"
        commit = "745c724b4ac623b1c42044454cb867e537d3917e"
        checksum = "8e10fe83984899c5ad902f5c7a2b2517cc6f0f4615ff340093a1a06e785a22de"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, commit), sha256=checksum)
        extracted_dir = "OpenCL-Headers-" + commit

        os.rename(extracted_dir, self._source_subfolder)


    def package(self):
        include_folder = os.path.join(self._source_subfolder, "CL")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include/CL", src=include_folder)


    def package_id(self):
        self.info.header_only()

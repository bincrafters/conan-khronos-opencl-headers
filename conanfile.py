# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class KhronosOpenCLHeadersConan(ConanFile):
    name = "khronos-opencl-headers"
    version = "20190502"
    description = "C language headers for the OpenCL API"
    topics = ("conan", "opencl", "header-only", "opencl-headers", "api-headers")
    url = "https://github.com/bincrafters/conan-opencl-headers"
    homepage = "https://github.com/KhronosGroup/OpenCL-Headers"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    no_copy_source = True
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        commit = "c5a4bbeabb10d8ed3d1c651b93aa31737bc473dd"
        sha256 = "d0fc2e2aeab7051a87f71dec94c6559e68eb191e1c1394d2add2c5d6ac767ca4"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, commit), sha256=sha256)
        extracted_dir = "OpenCL-Headers-" + commit
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "CL")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst=os.path.join("include", "CL"), src=include_folder)

    def package_id(self):
        self.info.header_only()

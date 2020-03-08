from conans import ConanFile, tools
import os


class KhronosOpenCLHeadersConan(ConanFile):
    name = "khronos-opencl-headers"
    version = "20190806"
    description = "C language headers for the OpenCL API"
    topics = ("conan", "opencl", "header-only", "opencl-headers", "api-headers")
    url = "https://github.com/bincrafters/conan-opencl-headers"
    homepage = "https://github.com/KhronosGroup/OpenCL-Headers"
    license = "MIT"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def source(self):
        commit = "0d5f18c6e7196863bc1557a693f1509adfcee056"
        sha256 = "03cbc1fd449399be0422cdb021400f63958ef2c5a7c099a0d8f36a705b312f53"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, commit), sha256=sha256)
        extracted_dir = "OpenCL-Headers-" + commit
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "CL")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst=os.path.join("include", "CL"), src=include_folder)

    def package_id(self):
        self.info.header_only()

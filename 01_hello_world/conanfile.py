from conans import ConanFile, CMake, tools


class HelloWorldConan(ConanFile):
    # Removed a bunch of attributes that are not needed, but you might want to
    # Add them for a real project
    name = "HelloWorld"
    version = "0.1"
    generators = "cmake"
    # If the source code is going to be in the same repo as the Conan recipe,
    # there is no need to define a `source` method. The source folder can be
    # defined like this
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        # The CMakeLists.txt file must be in `source_folder`
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        # Copy headers to the include folder and libraries to the lib folder
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HelloWorld"]
from spack import *

class GslLite(CMakePackage):
    """
    A single-file header-only version of ISO C++ Guidelines Support Library (GSL) for C++98, C++11, and later.
    gsl-lite recognizes when it is compiled for the CUDA platform and decorates some functions with __host__ and __device__.
    """

    homepage = "https://github.com/gsl-lite/gsl-lite"
    git      = "https://github.com/gsl-lite/gsl-lite"
    url      = "https://github.com/gsl-lite/gsl-lite/archive/refs/tags/v0.40.0.tar.gz"
    list_url = "https://github.com/gsl-lite/gsl-lite/archive/"
    list_depth = 2

    version('master', branch='master')
    version('0.40.0', sha256='65af4ec8a1050dac4f1ca4622881bb02a9c3978a9baec289fb56e25412d6cac7')
    version('0.39.0', sha256='f80ec07d9f4946097a1e2554e19cee4b55b70b45d59e03a7d2b7f80d71e467e9')
    version('0.38.1', sha256='c2fa2315fff312f3897958903ed4d4e027f73fa44235459ecb467ad7b7d62b18')
    version('0.38.0', sha256='5d25fcd31ea66dac9e14da1cad501d95450ccfcb2768fffcd1a4170258fcbc81')
    version('0.37.0', sha256='a31d51b73742bb234acab8d2411223cf299e760ed713f0840ffed0dabe57ca38')
    version('0.36.0', sha256='c052cc4547b33cedee6f000393a7005915c45c6c06b35518d203db117f75c71c')
    version('0.34.0', sha256='a7d5b2672b78704ca03df9ef65bc274d8f8cacad3ca950365eef9e25b50324c5')
    version('0.33.0', sha256='ebbbfa28656fb43356dceec90663f8398d2cb0c583ebaf32c8a385d5efd0bbca')
    version('0.32.0', sha256='134c891b0b0f038d622554faa4040f6d419c534ed18c1b893f4f3ff788515d10')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('examples', default=False,
            description='Build examples')
    variant('compat', default=False,
            description='Install MS-GSL compatibility header <gsl/gsl>')
    variant('legacy', default=False,
            description='Install legacy headers <gsl.h>, <gsl.hpp> and <gsl/gsl-lite.h>')

    depends_on('cmake@3.5.0:', type='build')

    def cmake_args(self):
        spec = self.spec
        args = []
        args += ['-DGSL_LITE_OPT_BUILD_EXAMPLES=%s' % 
                 ('ON' if ('+examples' in spec) else 'OFF')]
        args += ['-DGSL_LITE_OPT_INSTALL_COMPAT_HEADERS=%s' % 
                 ('ON' if ('+compat' in spec) else 'OFF')]
        args += ['-DGSL_LITE_OPT_INSTALL_LEGACY_HEADERS=%s' % 
                 ('ON' if ('+legacy' in spec) else 'OFF')]
        return args

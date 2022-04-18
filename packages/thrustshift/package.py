from spack import *


class Thrustshift(CMakePackage, CudaPackage):
    """CUDA library about what I consider useful and generic functions."""

    homepage = "https://github.com/codecircuit/thrustshift"
    git      = "https://github.com/codecircuit/thrustshift"
    url      = "https://github.com/codecircuit/thrustshift/archive/refs/heads/master.zip"
    list_url      = "https://github.com/codecircuit/thrustshift/archive/"
    list_depth = 2

    maintainers = ['codecircuit']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('master', branch='master')

    variant('cuda', default=True, description='Build with CUDA')
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('apps', default=False,
            description='Build additional applications (e.g. benchmarks)')
    variant('apps_use_fast_math', default=True,
            description='Use "fast math" when compiling additional apps')
    variant('tests', default=False,
            description='Build tests')

    conflicts('~cuda')

    depends_on('cmake@3.18.0:', type='build')
    depends_on('cmakeshift')

    depends_on('gsl-lite')

    depends_on('makeshift')
    depends_on('sysmakeshift')

    depends_on('cuda-api-wrappers@0.4.5-rc1:')
    depends_on('cuda-kat')

    depends_on('eigen@3.0.0:')

    depends_on('boost +filesystem +program_options cxxstd=17', when='+apps')
    depends_on('boost +test +filesystem cxxstd=17', when='+tests')
    depends_on('matrixmarket-reader', when='+tests')

    def cmake_args(self):
        # Add arguments other than CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        spec = self.spec
        args = []
        # args += ['-DCMAKE_CUDA_SEPARABLE_COMPILATION=ON']

        args += ['-DBUILD_APPS=%s' % 
                 ('ON' if ('+apps' in spec) else 'OFF')]
        args += ['-DINSTALL_APPS=%s' % 
                 ('ON' if ('+apps' in spec) else 'OFF')]
        if '+apps' in spec:
            args += ['-DBUILD_APPS_WITH_FAST_MATH=%s' % 
                     ('ON' if ('+apps_use_fast_math' in spec) else 'OFF')]

        args += ['-DBUILD_TESTS=%s' % 
                 ('ON' if ('+tests' in spec) else 'OFF')]
        args += ['-DINSTALL_TESTS=%s' % 
                 ('ON' if ('+tests' in spec) else 'OFF')]

        archs = spec.variants['cuda_arch'].value
        if archs[0] != 'none':
            arch_str = ";".join(archs)
            args.append('-DCMAKE_CUDA_ARCHITECTURES=%s' % arch_str)

        return args

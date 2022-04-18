from spack import *


class Sysmakeshift(CMakePackage):
    """It's hard to come up with a short string describing the scope of this library."""

    homepage = "https://github.com/mbeutel/sysmakeshift"
    git      = "https://github.com/mbeutel/sysmakeshift"
    url      = "https://github.com/mbeutel/sysmakeshift/archive/1.0.0.zip"
    list_url = "https://github.com/mbeutel/sysmakeshift/archive/"
    list_depth = 2

    version('master', branch='master', preferred=True)
    version('0.1.1', sha256='e2978003781c615ed008456e716d9437f16cd55069a291eedf05c0538520998a')
    version('0.1.0', sha256='510fe155113be42066f29c07d5c2df1f311a5df0959d5dc40feaf4052f1931f1')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('benchmarks', default=False,
            description='Build benchmarks')
    variant('tests', default=False,
            description='Build tests')

    depends_on('cmake@3.14.0:', type='build')
    depends_on('cmakeshift@3.8.0:')
    depends_on('gsl-lite@0.36.0:')

    depends_on('catch2@2.9.0:', when='+benchmarks')

    depends_on('catch2@2.11.0:', when='+tests')

    def cmake_args(self):
        spec = self.spec
        args = []

        args += ['-DSYSMAKESHIFT_BUILD_BENCHMARKS=%s' % 
                 ('ON' if ('+benchmarks' in spec) else 'OFF')]

        args += ['-DSYSMAKESHIFT_BUILD_TESTS=%s' % 
                 ('ON' if ('+tests' in spec) else 'OFF')]

        return args

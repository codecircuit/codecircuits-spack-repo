from spack import *

class Makeshift(CMakePackage):
    """It's hard to come up with a short string describing the scope of this library."""

    homepage = "https://github.com/mbeutel/makeshift"
    git      = "https://github.com/mbeutel/makeshift"
    url      = "https://github.com/mbeutel/makeshift/archive/3.0.0.zip"
    list_url = "https://github.com/mbeutel/makeshift/archive/"
    list_depth = 2

    version('master', branch='master', preferred=True)
    version('2020-01-04', sha256='204217b549c3bfbae7b55ea599e8e942127fe02fe8eb7e063108e98e5c533ed8',
            url='https://github.com/mbeutel/makeshift/archive/75b039532f825900f2cd0e4958c0e4d06f5ecf58.zip')
    version('1.1.0', sha256='7a20a1f88cffa6eeebbdc689a3df2b41f3315a7ce9c9ce39a5bca2019be20b3f',
            url='https://mp-force.ziti.uni-heidelberg.de/kmbeutel/makeshift/-/archive/1.1.0/makeshift-1.1.0.zip')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    depends_on('cmake@3.14.0:', type='build')

    depends_on('cppgsl', when='@0:3')
    depends_on('gsl-lite@0.35.5:', when='@2019:')
    depends_on('gsl-lite@0.36.0:', when='@master')

    depends_on('cmakeshift@1.2.0', when='@:2')
    depends_on('cmakeshift@2.0.1', when='@2:3')
    depends_on('cmakeshift@3.7.3:', when='@2019:')
    depends_on('cmakeshift@3.8.0:', when='@master')

    def cmake_args(self):
        spec = self.spec
        args = []
        return args

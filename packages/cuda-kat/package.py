from spack import *

class CudaKat(CMakePackage, CudaPackage):
    """CUDA kernel author's tools"""

    homepage = "https://github.com/eyalroz/cuda-kat"
    git      = "https://github.com/eyalroz/cuda-kat"
    url      = "https://github.com/eyalroz/cuda-kat/archive/refs/tags/v0.2.tar.gz"
    list_url = "https://github.com/eyalroz/cuda-kat/archive/"
    list_depth = 2

    version('master', branch='master')
    version('0.2',   sha256='1d5fc1172663f1db0e98d000ea0b1ab4c033a974090024559199954fd1c6b63f')
    version('0.1.1', sha256='f85b238c91f61441639a096e88df615001837d26034dee157522dfa98c10004d')
    version('0.1.0', sha256='04eb8950945e9f9e4dad42273ba94896e7634c6d145b4397e036be8f6e1131fb')

    variant('cuda', default=True, description='Build with CUDA')
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    conflicts('~cuda')

    depends_on('cmake@3.8.2:', type='build')

    def cmake_args(self):
        # Add arguments other than CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        spec = self.spec
        args = []

        archs = spec.variants['cuda_arch'].value
        if archs[0] != 'none':
            arch_str = ";".join(archs)
            args.append('-DCMAKE_CUDA_ARCHITECTURES=%s' % arch_str)

        return args

from spack import *

class CudaApiWrappers(CMakePackage, CudaPackage):
    """Thin C++-flavored wrappers for the CUDA Runtime API"""

    homepage = "https://github.com/eyalroz/cuda-api-wrappers"
    git      = "https://github.com/eyalroz/cuda-api-wrappers"
    url      = "https://github.com/eyalroz/cuda-api-wrappers/archive/refs/tags/v0.5.0-alpha.tar.gz"
    list_url      = "https://github.com/eyalroz/cuda-api-wrappers/archive/"
    list_depth = 2

    version('master',      branch='master')
    version('0.5.0-alpha', sha256='e74bb19dfa2cdb3209461b892ac84a57237a8cc3d8902ff6327ba36892f8d795')
    version('0.4.5-rc2',   sha256='1380ed5213ba2ec8b4ec1e200edc6a0bef9f0435f98d4562fcf7b310ba66ec04',
            preferred=True)
    version('0.4.4',       sha256='9b3449953587cd3cf64dc23ed84758e3ad264df50c6fae85790d89cbe0c44886')
    version('0.4.3',       sha256='ea52db94e0eba661b21cee7dc501e3661a2a72f360afb0f63a24d3b63f72e2a4')
    version('0.4.2',       sha256='c64210b83927ebaac02b2c43d33cb24cda6f395092c83aa9ac56979b4aafbc12')
    version('0.4.1rc1',    sha256='554408ddae44959fc2bf574cf0f4298e5afba788e05eebb81d5b463042ebbb93')
    version('0.4',         sha256='557c611b12e773ead084eff2aeb89dc67453fa6e03aef6b8a06bcf4ed2d04307')
    version('0.3.3',       sha256='7ded1c9da899f926ca8f62248e6505140ed9507289d446f469455490cd6cdd1f')

    variant('cuda', default=True, description='Build with CUDA')
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('examples', default=False,
            description='Build examples')

    conflicts('~cuda')

    depends_on('cmake@3.17.0:', type='build')
    depends_on('cuda@8.0.0:')

    def cmake_args(self):
        spec = self.spec
        args = []

        args += ['-DBUILD_EXAMPLES=%s' % 
                 ('ON' if ('+examples' in spec) else 'OFF')]

        archs = spec.variants['cuda_arch'].value
        if archs[0] != 'none':
            arch_str = ";".join(archs)
            args.append('-DCMAKE_CUDA_ARCHITECTURES=%s' % arch_str)

        return args

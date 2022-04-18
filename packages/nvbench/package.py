from spack import *

class Nvbench(CMakePackage, CudaPackage):
    """CUDA Kernel Benchmarking Library"""

    homepage = "https://github.com/NVIDIA/nvbench"
    git      = "https://github.com/NVIDIA/nvbench.git"
    url      = "https://github.com/NVIDIA/nvbench/archive/refs/heads/main.zip"
    list_url = "https://github.com/NVIDIA/nvbench/archive/"
    list_depth = 2

    version('main',      branch='main')

    variant('cuda', default=True, description='Build with CUDA')
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('nvml', default=True, description='Build with NVML support from the Cuda Toolkit.')
    variant('cupti', default=True, description='Build NVBench with CUPTI.')

    conflicts('~cuda')

    depends_on('cmake@3.20.1:', type='build')
    depends_on('cuda@11.3.0:', when='+cupti')

    def cmake_args(self):
        spec = self.spec
        args = []

        args += ['-DNVBench_ENABLE_NVML=%s' % 
                 ('ON' if ('+nvml' in spec) else 'OFF')]
        args += ['-DNVBench_ENABLE_CUPTI=%s' % 
                 ('ON' if ('+cupti' in spec) else 'OFF')]

        archs = spec.variants['cuda_arch'].value
        if archs[0] != 'none':
            arch_str = ";".join(archs)
            args.append('-DCMAKE_CUDA_ARCHITECTURES=%s' % arch_str)

        return args



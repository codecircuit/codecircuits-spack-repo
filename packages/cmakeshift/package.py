from spack import *


class Cmakeshift(CMakePackage):
    """Common CMake routines and find modules."""

    homepage = "https://github.com/mbeutel/CMakeshift"
    git      = "https://github.com/mbeutel/CMakeshift"
    url      = "https://github.com/mbeutel/CMakeshift/archive/3.5.0.zip"
    list_url = "https://github.com/mbeutel/CMakeshift/archive"
    list_depth = 2

    version('master', branch='master', preferred=True)
    version('3.8.2', sha256='cf153c8b3dfe5781d95a26d4d5b77d4deeabcdd209af86a153e8dc82efe42d3d')
    version('3.8.0', sha256='96cd9e749ddf99c7ee7cf36642618bddbd633546606444c65ab5a6ce8284dd4b')
    version('3.7.3', sha256='827f2b6fb564cd310e87fe68868a544c18351018eaf03d5c02d89c3ce36b47d9')
    version('3.7.1', sha256='686868fd832c3db3e7d5c4cf04d916d8601f9c374258d4c425c482e0436e40bb')
    version('3.7.0', sha256='8c363b714e8c7ce77b2c5b04170e7788bfd49fdd0f2566a43e5eb3026135938e')
    version('3.6.0', sha256='13dd04996f830881ecf81d9ed3eb9e63e67e0b89f73a2783561cfca9d72b92f1')
    version('3.5.0', sha256='cf89c03b692e4e9d509473be9f60bf8b71be6ce0ce383d690859be959afe54aa')
    version('3.4.0', sha256='e998519391f10d71cae7883d813ddb711e645cc02dd3535256ac61b560beffb0')
    version('3.3.0', sha256='c05a989e45be4a077e4fdda803f09a2c2727e1908e97f00de112e23967c30ce0',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/3.3.0/CMakeshift-3.3.0.zip")
    version('3.2.0', sha256='f1e6e4463db1ea21aac758842e0a6015ddbe6384f59476e5505de4efb1f612d2',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/3.2.0/CMakeshift-3.2.0.zip")
    version('3.1.0', sha256='e1dcfe9c996c764b106a2aea4799f2850a46bc143093935cbd3a949072fbec09',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/3.1.0/CMakeshift-3.1.0.zip")
    version('3.0.0', sha256='b40ac7a774ff408a7d45660161de1198709027e40f8505a0ad7ea2765d0b8469',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/3.0.0/CMakeshift-3.0.0.zip")
    version('2.0.1', sha256='22317c0393c33ed03c36e549cafe41ced005f01af119df273895c06e452c5517',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/2.0.1/CMakeshift-2.0.1.zip")
    version('1.2.0', sha256='fcdf525d709137ba99085fbb93826e0f5cef3501fa71ee3442bc7cae318c32ac',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/1.2.0/CMakeshift-1.2.0.zip")
    version('1.1.0', sha256='5e668a89d45c3a46556b1a321f766946a7e95afe40e5324b45087ab3268b2619',
            url="https://mp-force.ziti.uni-heidelberg.de/asc/CMakeshift/-/archive/1.1.0/CMakeshift-1.1.0.zip")

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    depends_on('cmake@3.14.0:', type='build')

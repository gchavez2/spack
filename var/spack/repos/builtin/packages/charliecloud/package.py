##############################################################################
# Copyright (c) 2018, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Charliecloud(MakefilePackage):
    """Lightweight user-defined software stacks for HPC."""

    homepage = "https://hpc.github.io/charliecloud"
    url      = "https://github.com/hpc/charliecloud/archive/v0.2.4.tar.gz"

    version('0.9.3', sha256='f1bf032377b8845bc9a93b8a4fad6386161e35900223c0acc61d1f3aa3a87bc7')
    version('0.9.2', sha256='8d0e4804d412beef720a66f886a0a78bce42f3269e880ebf11f602581f8047d4')
    version('0.9.1', sha256='8e69150a271285da71ece7a09b48251ef6593f72207c5126741d9976aa737d95')
    version('0.9.0', sha256='7e74cb16e31fd9d502198f7509bab14d1049ec68ba90b15e277e76f805db9458')
    version('0.2.4', 'b112de661c2c360174b42c99022c1967')

    @property
    def install_targets(self):
        return ['install', 'PREFIX=%s' % self.prefix]

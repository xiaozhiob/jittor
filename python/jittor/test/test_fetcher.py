# ***************************************************************
# Copyright (c) 2020 Jittor. Authors: Dun Liang <randonlang@gmail.com>. All Rights Reserved.
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
# ***************************************************************
import unittest
import jittor as jt
import numpy as np
from jittor import compile_extern

class TestFetcher(unittest.TestCase):
    def test_fetch(self):
        a = jt.array([1,2,3])
        a = a*2
        v = []
        jt.fetch([a], lambda a: v.append(a))
        jt.sync_all(True)
        assert len(v)==1 and (v[0]==[2,4,6]).all()

@unittest.skipIf(not jt.has_cuda, "Cuda not found")
class TestFetcherCuda(TestFetcher):
    @classmethod
    def setUpClass(self):
        jt.flags.use_cuda = 1

    @classmethod
    def tearDownClass(self):
        jt.flags.use_cuda = 0

if __name__ == "__main__":
    unittest.main()
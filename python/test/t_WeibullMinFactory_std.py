#! /usr/bin/env python

from __future__ import print_function
from openturns import *
import openturns.testing as ott

TESTPREAMBLE()
RandomGenerator.SetSeed(0)

try:
    distribution = WeibullMin(1.0, 2.5, -1.0)
    size = 10000
    sample = distribution.getSample(size)
    factory = WeibullMinFactory()
    estimatedDistribution = factory.build(sample)
    print("distribution=", repr(distribution))
    print("Estimated distribution=", repr(estimatedDistribution))
    estimatedDistribution = factory.build()
    print("Default distribution=", estimatedDistribution)
    estimatedDistribution = factory.build(
        distribution.getParameter())
    print("Distribution from parameters=", estimatedDistribution)
    estimatedWeibull = factory.buildAsWeibullMin(sample)
    print("Estimated weibull=", estimatedWeibull)
    estimatedWeibull = factory.buildAsWeibullMin()
    print("Default weibull=", estimatedWeibull)
    estimatedWeibull = factory.buildAsWeibullMin(
        distribution.getParameter())
    print("WeibullMin from parameters=", estimatedWeibull)
    sample = [[0.0]] * size
    estimatedDistribution = factory.build(sample)
    print("Estimated distribution=", repr(estimatedDistribution))
    sample = [[1.0]] * size
    estimatedDistribution = factory.buildAsWeibullMin(sample)
    ott.assert_almost_equal(estimatedDistribution.getBeta(), 0.0, 0.0, 1e-4)
    ott.assert_almost_equal(estimatedDistribution.getAlpha(), 1.0, 0.0, 1e-6)
    ott.assert_almost_equal(estimatedDistribution.getGamma(), 1.0, 0.0, 1e-6)

except:
    import sys
    print("t_WeibullFactory_std.py", sys.exc_info()[0], sys.exc_info()[1])

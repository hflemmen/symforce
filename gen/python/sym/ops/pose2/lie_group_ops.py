# -----------------------------------------------------------------------------
# This file was autogenerated by symforce from template:
#     python_templates/geo_package/ops/CLASS/lie_group_ops.py.jinja
# Do NOT modify by hand.
# -----------------------------------------------------------------------------

import math
import numpy
import typing as T

import sym  # pylint: disable=unused-import


class LieGroupOps(object):
    """
    Python LieGroupOps implementation for <class 'symforce.geo.pose2.Pose2'>.
    """

    @staticmethod
    def from_tangent(vec, epsilon):
        # type: (T.Sequence[float], float) -> sym.Pose2

        # Total ops: 2

        # Input arrays

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 4
        _res[0] = math.cos(vec[2])
        _res[1] = math.sin(vec[2])
        _res[2] = vec[0]
        _res[3] = vec[1]
        return sym.Pose2.from_storage(_res)

    @staticmethod
    def to_tangent(a, epsilon):
        # type: (sym.Pose2, float) -> T.List[float]

        # Total ops: 5

        # Input arrays
        _a = a.data

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 3
        _res[0] = _a[2]
        _res[1] = _a[3]
        _res[2] = math.atan2(
            _a[1], _a[0] + epsilon * ((0.0 if _a[0] == 0 else math.copysign(1, _a[0])) + 0.5)
        )
        return _res

    @staticmethod
    def retract(a, vec, epsilon):
        # type: (sym.Pose2, T.Sequence[float], float) -> sym.Pose2

        # Total ops: 11

        # Input arrays
        _a = a.data

        # Intermediate terms (2)
        _tmp0 = math.sin(vec[2])
        _tmp1 = math.cos(vec[2])

        # Output terms
        _res = [0.0] * 4
        _res[0] = _a[0] * _tmp1 - _a[1] * _tmp0
        _res[1] = _a[0] * _tmp0 + _a[1] * _tmp1
        _res[2] = _a[2] + vec[0]
        _res[3] = _a[3] + vec[1]
        return sym.Pose2.from_storage(_res)

    @staticmethod
    def local_coordinates(a, b, epsilon):
        # type: (sym.Pose2, sym.Pose2, float) -> T.List[float]

        # Total ops: 16

        # Input arrays
        _a = a.data
        _b = b.data

        # Intermediate terms (1)
        _tmp0 = _a[0] * _b[0] + _a[1] * _b[1]

        # Output terms
        _res = [0.0] * 3
        _res[0] = -_a[2] + _b[2]
        _res[1] = -_a[3] + _b[3]
        _res[2] = math.atan2(
            _a[0] * _b[1] - _a[1] * _b[0],
            _tmp0 + epsilon * ((0.0 if _tmp0 == 0 else math.copysign(1, _tmp0)) + 0.5),
        )
        return _res

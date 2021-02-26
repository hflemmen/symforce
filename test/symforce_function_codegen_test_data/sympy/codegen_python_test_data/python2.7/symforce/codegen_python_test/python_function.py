import numpy
import typing as T

import geo  # pylint: disable=unused-import


import codegen_python_test


def python_function(
    x, y, rot, rot_vec, scalar_vec, list_of_lists, values_vec, values_vec_2D, constants, states
):
    # type: (float, float, geo.Rot3, T.Sequence[geo.Rot3], T.Sequence[float], T.Sequence[T.Sequence[geo.Rot3]], T.Sequence[T.Any], T.Sequence[T.Sequence[T.Any]], T.Any, T.Any) -> T.Tuple[float, float, T.List[float], T.List[float], T.List[float]]
    """
    This function was autogenerated. Do not modify by hand.

    Arg type(s): Symbol, Symbol, Rot3, list, list, list, list, list, Values, Values
    Return type(s): Add, Add, list, list, list

    """
    # Total ops: 748

    # Input arrays
    _rot = rot.data

    # Intermediate terms (66)
    _tmp0 = x ** 2
    _tmp1 = 2 * values_vec[0].rot[3]
    _tmp2 = 2 * values_vec[0].rot_vec[0][3]
    _tmp3 = 2 * values_vec[0].rot_vec[1][3]
    _tmp4 = 2 * values_vec[0].rot_vec[2][3]
    _tmp5 = 2 * values_vec[0].list_of_lists[0][0][3]
    _tmp6 = 2 * values_vec[0].list_of_lists[0][1][3]
    _tmp7 = 2 * values_vec[0].list_of_lists[0][2][3]
    _tmp8 = 2 * values_vec[0].list_of_lists[1][0][3]
    _tmp9 = 2 * values_vec[0].list_of_lists[1][1][3]
    _tmp10 = 2 * values_vec[0].list_of_lists[1][2][3]
    _tmp11 = 2 * values_vec[0].list_of_lists[2][0][3]
    _tmp12 = 2 * values_vec[0].list_of_lists[2][1][3]
    _tmp13 = 2 * values_vec[0].list_of_lists[2][2][3]
    _tmp14 = 2 * values_vec[1].rot[3]
    _tmp15 = 2 * values_vec[1].rot_vec[0][3]
    _tmp16 = 2 * values_vec[1].rot_vec[1][3]
    _tmp17 = 2 * values_vec[1].rot_vec[2][3]
    _tmp18 = 2 * values_vec[1].list_of_lists[0][0][3]
    _tmp19 = 2 * values_vec[1].list_of_lists[0][1][3]
    _tmp20 = 2 * values_vec[1].list_of_lists[0][2][3]
    _tmp21 = 2 * values_vec[1].list_of_lists[1][0][3]
    _tmp22 = 2 * values_vec[1].list_of_lists[1][1][3]
    _tmp23 = 2 * values_vec[1].list_of_lists[1][2][3]
    _tmp24 = 2 * values_vec[1].list_of_lists[2][0][3]
    _tmp25 = 2 * values_vec[1].list_of_lists[2][1][3]
    _tmp26 = 2 * values_vec[1].list_of_lists[2][2][3]
    _tmp27 = 2 * values_vec[2].rot[3]
    _tmp28 = 2 * values_vec[2].rot_vec[0][3]
    _tmp29 = 2 * values_vec[2].rot_vec[1][3]
    _tmp30 = 2 * values_vec[2].rot_vec[2][3]
    _tmp31 = 2 * values_vec[2].list_of_lists[0][0][3]
    _tmp32 = 2 * values_vec[2].list_of_lists[0][1][3]
    _tmp33 = 2 * values_vec[2].list_of_lists[0][2][3]
    _tmp34 = 2 * values_vec[2].list_of_lists[1][0][3]
    _tmp35 = 2 * values_vec[2].list_of_lists[1][1][3]
    _tmp36 = 2 * values_vec[2].list_of_lists[1][2][3]
    _tmp37 = 2 * values_vec[2].list_of_lists[2][0][3]
    _tmp38 = 2 * values_vec[2].list_of_lists[2][1][3]
    _tmp39 = 2 * values_vec[2].list_of_lists[2][2][3]
    _tmp40 = 2 * values_vec_2D[0][0].rot[3]
    _tmp41 = 2 * values_vec_2D[0][0].rot_vec[0][3]
    _tmp42 = 2 * values_vec_2D[0][0].rot_vec[1][3]
    _tmp43 = 2 * values_vec_2D[0][0].rot_vec[2][3]
    _tmp44 = 2 * values_vec_2D[0][0].list_of_lists[0][0][3]
    _tmp45 = 2 * values_vec_2D[0][0].list_of_lists[0][1][3]
    _tmp46 = 2 * values_vec_2D[0][0].list_of_lists[0][2][3]
    _tmp47 = 2 * values_vec_2D[0][0].list_of_lists[1][0][3]
    _tmp48 = 2 * values_vec_2D[0][0].list_of_lists[1][1][3]
    _tmp49 = 2 * values_vec_2D[0][0].list_of_lists[1][2][3]
    _tmp50 = 2 * values_vec_2D[0][0].list_of_lists[2][0][3]
    _tmp51 = 2 * values_vec_2D[0][0].list_of_lists[2][1][3]
    _tmp52 = 2 * values_vec_2D[0][0].list_of_lists[2][2][3]
    _tmp53 = 2 * values_vec_2D[1][0].rot[3]
    _tmp54 = 2 * values_vec_2D[1][0].rot_vec[0][3]
    _tmp55 = 2 * values_vec_2D[1][0].rot_vec[1][3]
    _tmp56 = 2 * values_vec_2D[1][0].rot_vec[2][3]
    _tmp57 = 2 * values_vec_2D[1][0].list_of_lists[0][0][3]
    _tmp58 = 2 * values_vec_2D[1][0].list_of_lists[0][1][3]
    _tmp59 = 2 * values_vec_2D[1][0].list_of_lists[0][2][3]
    _tmp60 = 2 * values_vec_2D[1][0].list_of_lists[1][0][3]
    _tmp61 = 2 * values_vec_2D[1][0].list_of_lists[1][1][3]
    _tmp62 = 2 * values_vec_2D[1][0].list_of_lists[1][2][3]
    _tmp63 = 2 * values_vec_2D[1][0].list_of_lists[2][0][3]
    _tmp64 = 2 * values_vec_2D[1][0].list_of_lists[2][1][3]
    _tmp65 = 2 * values_vec_2D[1][0].list_of_lists[2][2][3]

    # Output terms
    _foo = _rot[3] + _tmp0
    _bar = _tmp0 + constants.epsilon + numpy.sin(y)
    _scalar_vec_out = [0.0] * 3
    _scalar_vec_out[0] = 2 * scalar_vec[0]
    _scalar_vec_out[1] = 2 * scalar_vec[1]
    _scalar_vec_out[2] = 2 * scalar_vec[2]
    _values_vec_out = [0.0] * 171
    _values_vec_out[0] = 2 * values_vec[0].x
    _values_vec_out[1] = 2 * values_vec[0].y
    _values_vec_out[2] = _tmp1 * values_vec[0].rot[0]
    _values_vec_out[3] = _tmp1 * values_vec[0].rot[1]
    _values_vec_out[4] = _tmp1 * values_vec[0].rot[2]
    _values_vec_out[5] = (
        -values_vec[0].rot[0] ** 2
        - values_vec[0].rot[1] ** 2
        - values_vec[0].rot[2] ** 2
        + values_vec[0].rot[3] ** 2
    )
    _values_vec_out[6] = _tmp2 * values_vec[0].rot_vec[0][0]
    _values_vec_out[7] = _tmp2 * values_vec[0].rot_vec[0][1]
    _values_vec_out[8] = _tmp2 * values_vec[0].rot_vec[0][2]
    _values_vec_out[9] = (
        -values_vec[0].rot_vec[0][0] ** 2
        - values_vec[0].rot_vec[0][1] ** 2
        - values_vec[0].rot_vec[0][2] ** 2
        + values_vec[0].rot_vec[0][3] ** 2
    )
    _values_vec_out[10] = _tmp3 * values_vec[0].rot_vec[1][0]
    _values_vec_out[11] = _tmp3 * values_vec[0].rot_vec[1][1]
    _values_vec_out[12] = _tmp3 * values_vec[0].rot_vec[1][2]
    _values_vec_out[13] = (
        -values_vec[0].rot_vec[1][0] ** 2
        - values_vec[0].rot_vec[1][1] ** 2
        - values_vec[0].rot_vec[1][2] ** 2
        + values_vec[0].rot_vec[1][3] ** 2
    )
    _values_vec_out[14] = _tmp4 * values_vec[0].rot_vec[2][0]
    _values_vec_out[15] = _tmp4 * values_vec[0].rot_vec[2][1]
    _values_vec_out[16] = _tmp4 * values_vec[0].rot_vec[2][2]
    _values_vec_out[17] = (
        -values_vec[0].rot_vec[2][0] ** 2
        - values_vec[0].rot_vec[2][1] ** 2
        - values_vec[0].rot_vec[2][2] ** 2
        + values_vec[0].rot_vec[2][3] ** 2
    )
    _values_vec_out[18] = 2 * values_vec[0].scalar_vec[0]
    _values_vec_out[19] = 2 * values_vec[0].scalar_vec[1]
    _values_vec_out[20] = 2 * values_vec[0].scalar_vec[2]
    _values_vec_out[21] = _tmp5 * values_vec[0].list_of_lists[0][0][0]
    _values_vec_out[22] = _tmp5 * values_vec[0].list_of_lists[0][0][1]
    _values_vec_out[23] = _tmp5 * values_vec[0].list_of_lists[0][0][2]
    _values_vec_out[24] = (
        -values_vec[0].list_of_lists[0][0][0] ** 2
        - values_vec[0].list_of_lists[0][0][1] ** 2
        - values_vec[0].list_of_lists[0][0][2] ** 2
        + values_vec[0].list_of_lists[0][0][3] ** 2
    )
    _values_vec_out[25] = _tmp6 * values_vec[0].list_of_lists[0][1][0]
    _values_vec_out[26] = _tmp6 * values_vec[0].list_of_lists[0][1][1]
    _values_vec_out[27] = _tmp6 * values_vec[0].list_of_lists[0][1][2]
    _values_vec_out[28] = (
        -values_vec[0].list_of_lists[0][1][0] ** 2
        - values_vec[0].list_of_lists[0][1][1] ** 2
        - values_vec[0].list_of_lists[0][1][2] ** 2
        + values_vec[0].list_of_lists[0][1][3] ** 2
    )
    _values_vec_out[29] = _tmp7 * values_vec[0].list_of_lists[0][2][0]
    _values_vec_out[30] = _tmp7 * values_vec[0].list_of_lists[0][2][1]
    _values_vec_out[31] = _tmp7 * values_vec[0].list_of_lists[0][2][2]
    _values_vec_out[32] = (
        -values_vec[0].list_of_lists[0][2][0] ** 2
        - values_vec[0].list_of_lists[0][2][1] ** 2
        - values_vec[0].list_of_lists[0][2][2] ** 2
        + values_vec[0].list_of_lists[0][2][3] ** 2
    )
    _values_vec_out[33] = _tmp8 * values_vec[0].list_of_lists[1][0][0]
    _values_vec_out[34] = _tmp8 * values_vec[0].list_of_lists[1][0][1]
    _values_vec_out[35] = _tmp8 * values_vec[0].list_of_lists[1][0][2]
    _values_vec_out[36] = (
        -values_vec[0].list_of_lists[1][0][0] ** 2
        - values_vec[0].list_of_lists[1][0][1] ** 2
        - values_vec[0].list_of_lists[1][0][2] ** 2
        + values_vec[0].list_of_lists[1][0][3] ** 2
    )
    _values_vec_out[37] = _tmp9 * values_vec[0].list_of_lists[1][1][0]
    _values_vec_out[38] = _tmp9 * values_vec[0].list_of_lists[1][1][1]
    _values_vec_out[39] = _tmp9 * values_vec[0].list_of_lists[1][1][2]
    _values_vec_out[40] = (
        -values_vec[0].list_of_lists[1][1][0] ** 2
        - values_vec[0].list_of_lists[1][1][1] ** 2
        - values_vec[0].list_of_lists[1][1][2] ** 2
        + values_vec[0].list_of_lists[1][1][3] ** 2
    )
    _values_vec_out[41] = _tmp10 * values_vec[0].list_of_lists[1][2][0]
    _values_vec_out[42] = _tmp10 * values_vec[0].list_of_lists[1][2][1]
    _values_vec_out[43] = _tmp10 * values_vec[0].list_of_lists[1][2][2]
    _values_vec_out[44] = (
        -values_vec[0].list_of_lists[1][2][0] ** 2
        - values_vec[0].list_of_lists[1][2][1] ** 2
        - values_vec[0].list_of_lists[1][2][2] ** 2
        + values_vec[0].list_of_lists[1][2][3] ** 2
    )
    _values_vec_out[45] = _tmp11 * values_vec[0].list_of_lists[2][0][0]
    _values_vec_out[46] = _tmp11 * values_vec[0].list_of_lists[2][0][1]
    _values_vec_out[47] = _tmp11 * values_vec[0].list_of_lists[2][0][2]
    _values_vec_out[48] = (
        -values_vec[0].list_of_lists[2][0][0] ** 2
        - values_vec[0].list_of_lists[2][0][1] ** 2
        - values_vec[0].list_of_lists[2][0][2] ** 2
        + values_vec[0].list_of_lists[2][0][3] ** 2
    )
    _values_vec_out[49] = _tmp12 * values_vec[0].list_of_lists[2][1][0]
    _values_vec_out[50] = _tmp12 * values_vec[0].list_of_lists[2][1][1]
    _values_vec_out[51] = _tmp12 * values_vec[0].list_of_lists[2][1][2]
    _values_vec_out[52] = (
        -values_vec[0].list_of_lists[2][1][0] ** 2
        - values_vec[0].list_of_lists[2][1][1] ** 2
        - values_vec[0].list_of_lists[2][1][2] ** 2
        + values_vec[0].list_of_lists[2][1][3] ** 2
    )
    _values_vec_out[53] = _tmp13 * values_vec[0].list_of_lists[2][2][0]
    _values_vec_out[54] = _tmp13 * values_vec[0].list_of_lists[2][2][1]
    _values_vec_out[55] = _tmp13 * values_vec[0].list_of_lists[2][2][2]
    _values_vec_out[56] = (
        -values_vec[0].list_of_lists[2][2][0] ** 2
        - values_vec[0].list_of_lists[2][2][1] ** 2
        - values_vec[0].list_of_lists[2][2][2] ** 2
        + values_vec[0].list_of_lists[2][2][3] ** 2
    )
    _values_vec_out[57] = 2 * values_vec[1].x
    _values_vec_out[58] = 2 * values_vec[1].y
    _values_vec_out[59] = _tmp14 * values_vec[1].rot[0]
    _values_vec_out[60] = _tmp14 * values_vec[1].rot[1]
    _values_vec_out[61] = _tmp14 * values_vec[1].rot[2]
    _values_vec_out[62] = (
        -values_vec[1].rot[0] ** 2
        - values_vec[1].rot[1] ** 2
        - values_vec[1].rot[2] ** 2
        + values_vec[1].rot[3] ** 2
    )
    _values_vec_out[63] = _tmp15 * values_vec[1].rot_vec[0][0]
    _values_vec_out[64] = _tmp15 * values_vec[1].rot_vec[0][1]
    _values_vec_out[65] = _tmp15 * values_vec[1].rot_vec[0][2]
    _values_vec_out[66] = (
        -values_vec[1].rot_vec[0][0] ** 2
        - values_vec[1].rot_vec[0][1] ** 2
        - values_vec[1].rot_vec[0][2] ** 2
        + values_vec[1].rot_vec[0][3] ** 2
    )
    _values_vec_out[67] = _tmp16 * values_vec[1].rot_vec[1][0]
    _values_vec_out[68] = _tmp16 * values_vec[1].rot_vec[1][1]
    _values_vec_out[69] = _tmp16 * values_vec[1].rot_vec[1][2]
    _values_vec_out[70] = (
        -values_vec[1].rot_vec[1][0] ** 2
        - values_vec[1].rot_vec[1][1] ** 2
        - values_vec[1].rot_vec[1][2] ** 2
        + values_vec[1].rot_vec[1][3] ** 2
    )
    _values_vec_out[71] = _tmp17 * values_vec[1].rot_vec[2][0]
    _values_vec_out[72] = _tmp17 * values_vec[1].rot_vec[2][1]
    _values_vec_out[73] = _tmp17 * values_vec[1].rot_vec[2][2]
    _values_vec_out[74] = (
        -values_vec[1].rot_vec[2][0] ** 2
        - values_vec[1].rot_vec[2][1] ** 2
        - values_vec[1].rot_vec[2][2] ** 2
        + values_vec[1].rot_vec[2][3] ** 2
    )
    _values_vec_out[75] = 2 * values_vec[1].scalar_vec[0]
    _values_vec_out[76] = 2 * values_vec[1].scalar_vec[1]
    _values_vec_out[77] = 2 * values_vec[1].scalar_vec[2]
    _values_vec_out[78] = _tmp18 * values_vec[1].list_of_lists[0][0][0]
    _values_vec_out[79] = _tmp18 * values_vec[1].list_of_lists[0][0][1]
    _values_vec_out[80] = _tmp18 * values_vec[1].list_of_lists[0][0][2]
    _values_vec_out[81] = (
        -values_vec[1].list_of_lists[0][0][0] ** 2
        - values_vec[1].list_of_lists[0][0][1] ** 2
        - values_vec[1].list_of_lists[0][0][2] ** 2
        + values_vec[1].list_of_lists[0][0][3] ** 2
    )
    _values_vec_out[82] = _tmp19 * values_vec[1].list_of_lists[0][1][0]
    _values_vec_out[83] = _tmp19 * values_vec[1].list_of_lists[0][1][1]
    _values_vec_out[84] = _tmp19 * values_vec[1].list_of_lists[0][1][2]
    _values_vec_out[85] = (
        -values_vec[1].list_of_lists[0][1][0] ** 2
        - values_vec[1].list_of_lists[0][1][1] ** 2
        - values_vec[1].list_of_lists[0][1][2] ** 2
        + values_vec[1].list_of_lists[0][1][3] ** 2
    )
    _values_vec_out[86] = _tmp20 * values_vec[1].list_of_lists[0][2][0]
    _values_vec_out[87] = _tmp20 * values_vec[1].list_of_lists[0][2][1]
    _values_vec_out[88] = _tmp20 * values_vec[1].list_of_lists[0][2][2]
    _values_vec_out[89] = (
        -values_vec[1].list_of_lists[0][2][0] ** 2
        - values_vec[1].list_of_lists[0][2][1] ** 2
        - values_vec[1].list_of_lists[0][2][2] ** 2
        + values_vec[1].list_of_lists[0][2][3] ** 2
    )
    _values_vec_out[90] = _tmp21 * values_vec[1].list_of_lists[1][0][0]
    _values_vec_out[91] = _tmp21 * values_vec[1].list_of_lists[1][0][1]
    _values_vec_out[92] = _tmp21 * values_vec[1].list_of_lists[1][0][2]
    _values_vec_out[93] = (
        -values_vec[1].list_of_lists[1][0][0] ** 2
        - values_vec[1].list_of_lists[1][0][1] ** 2
        - values_vec[1].list_of_lists[1][0][2] ** 2
        + values_vec[1].list_of_lists[1][0][3] ** 2
    )
    _values_vec_out[94] = _tmp22 * values_vec[1].list_of_lists[1][1][0]
    _values_vec_out[95] = _tmp22 * values_vec[1].list_of_lists[1][1][1]
    _values_vec_out[96] = _tmp22 * values_vec[1].list_of_lists[1][1][2]
    _values_vec_out[97] = (
        -values_vec[1].list_of_lists[1][1][0] ** 2
        - values_vec[1].list_of_lists[1][1][1] ** 2
        - values_vec[1].list_of_lists[1][1][2] ** 2
        + values_vec[1].list_of_lists[1][1][3] ** 2
    )
    _values_vec_out[98] = _tmp23 * values_vec[1].list_of_lists[1][2][0]
    _values_vec_out[99] = _tmp23 * values_vec[1].list_of_lists[1][2][1]
    _values_vec_out[100] = _tmp23 * values_vec[1].list_of_lists[1][2][2]
    _values_vec_out[101] = (
        -values_vec[1].list_of_lists[1][2][0] ** 2
        - values_vec[1].list_of_lists[1][2][1] ** 2
        - values_vec[1].list_of_lists[1][2][2] ** 2
        + values_vec[1].list_of_lists[1][2][3] ** 2
    )
    _values_vec_out[102] = _tmp24 * values_vec[1].list_of_lists[2][0][0]
    _values_vec_out[103] = _tmp24 * values_vec[1].list_of_lists[2][0][1]
    _values_vec_out[104] = _tmp24 * values_vec[1].list_of_lists[2][0][2]
    _values_vec_out[105] = (
        -values_vec[1].list_of_lists[2][0][0] ** 2
        - values_vec[1].list_of_lists[2][0][1] ** 2
        - values_vec[1].list_of_lists[2][0][2] ** 2
        + values_vec[1].list_of_lists[2][0][3] ** 2
    )
    _values_vec_out[106] = _tmp25 * values_vec[1].list_of_lists[2][1][0]
    _values_vec_out[107] = _tmp25 * values_vec[1].list_of_lists[2][1][1]
    _values_vec_out[108] = _tmp25 * values_vec[1].list_of_lists[2][1][2]
    _values_vec_out[109] = (
        -values_vec[1].list_of_lists[2][1][0] ** 2
        - values_vec[1].list_of_lists[2][1][1] ** 2
        - values_vec[1].list_of_lists[2][1][2] ** 2
        + values_vec[1].list_of_lists[2][1][3] ** 2
    )
    _values_vec_out[110] = _tmp26 * values_vec[1].list_of_lists[2][2][0]
    _values_vec_out[111] = _tmp26 * values_vec[1].list_of_lists[2][2][1]
    _values_vec_out[112] = _tmp26 * values_vec[1].list_of_lists[2][2][2]
    _values_vec_out[113] = (
        -values_vec[1].list_of_lists[2][2][0] ** 2
        - values_vec[1].list_of_lists[2][2][1] ** 2
        - values_vec[1].list_of_lists[2][2][2] ** 2
        + values_vec[1].list_of_lists[2][2][3] ** 2
    )
    _values_vec_out[114] = 2 * values_vec[2].x
    _values_vec_out[115] = 2 * values_vec[2].y
    _values_vec_out[116] = _tmp27 * values_vec[2].rot[0]
    _values_vec_out[117] = _tmp27 * values_vec[2].rot[1]
    _values_vec_out[118] = _tmp27 * values_vec[2].rot[2]
    _values_vec_out[119] = (
        -values_vec[2].rot[0] ** 2
        - values_vec[2].rot[1] ** 2
        - values_vec[2].rot[2] ** 2
        + values_vec[2].rot[3] ** 2
    )
    _values_vec_out[120] = _tmp28 * values_vec[2].rot_vec[0][0]
    _values_vec_out[121] = _tmp28 * values_vec[2].rot_vec[0][1]
    _values_vec_out[122] = _tmp28 * values_vec[2].rot_vec[0][2]
    _values_vec_out[123] = (
        -values_vec[2].rot_vec[0][0] ** 2
        - values_vec[2].rot_vec[0][1] ** 2
        - values_vec[2].rot_vec[0][2] ** 2
        + values_vec[2].rot_vec[0][3] ** 2
    )
    _values_vec_out[124] = _tmp29 * values_vec[2].rot_vec[1][0]
    _values_vec_out[125] = _tmp29 * values_vec[2].rot_vec[1][1]
    _values_vec_out[126] = _tmp29 * values_vec[2].rot_vec[1][2]
    _values_vec_out[127] = (
        -values_vec[2].rot_vec[1][0] ** 2
        - values_vec[2].rot_vec[1][1] ** 2
        - values_vec[2].rot_vec[1][2] ** 2
        + values_vec[2].rot_vec[1][3] ** 2
    )
    _values_vec_out[128] = _tmp30 * values_vec[2].rot_vec[2][0]
    _values_vec_out[129] = _tmp30 * values_vec[2].rot_vec[2][1]
    _values_vec_out[130] = _tmp30 * values_vec[2].rot_vec[2][2]
    _values_vec_out[131] = (
        -values_vec[2].rot_vec[2][0] ** 2
        - values_vec[2].rot_vec[2][1] ** 2
        - values_vec[2].rot_vec[2][2] ** 2
        + values_vec[2].rot_vec[2][3] ** 2
    )
    _values_vec_out[132] = 2 * values_vec[2].scalar_vec[0]
    _values_vec_out[133] = 2 * values_vec[2].scalar_vec[1]
    _values_vec_out[134] = 2 * values_vec[2].scalar_vec[2]
    _values_vec_out[135] = _tmp31 * values_vec[2].list_of_lists[0][0][0]
    _values_vec_out[136] = _tmp31 * values_vec[2].list_of_lists[0][0][1]
    _values_vec_out[137] = _tmp31 * values_vec[2].list_of_lists[0][0][2]
    _values_vec_out[138] = (
        -values_vec[2].list_of_lists[0][0][0] ** 2
        - values_vec[2].list_of_lists[0][0][1] ** 2
        - values_vec[2].list_of_lists[0][0][2] ** 2
        + values_vec[2].list_of_lists[0][0][3] ** 2
    )
    _values_vec_out[139] = _tmp32 * values_vec[2].list_of_lists[0][1][0]
    _values_vec_out[140] = _tmp32 * values_vec[2].list_of_lists[0][1][1]
    _values_vec_out[141] = _tmp32 * values_vec[2].list_of_lists[0][1][2]
    _values_vec_out[142] = (
        -values_vec[2].list_of_lists[0][1][0] ** 2
        - values_vec[2].list_of_lists[0][1][1] ** 2
        - values_vec[2].list_of_lists[0][1][2] ** 2
        + values_vec[2].list_of_lists[0][1][3] ** 2
    )
    _values_vec_out[143] = _tmp33 * values_vec[2].list_of_lists[0][2][0]
    _values_vec_out[144] = _tmp33 * values_vec[2].list_of_lists[0][2][1]
    _values_vec_out[145] = _tmp33 * values_vec[2].list_of_lists[0][2][2]
    _values_vec_out[146] = (
        -values_vec[2].list_of_lists[0][2][0] ** 2
        - values_vec[2].list_of_lists[0][2][1] ** 2
        - values_vec[2].list_of_lists[0][2][2] ** 2
        + values_vec[2].list_of_lists[0][2][3] ** 2
    )
    _values_vec_out[147] = _tmp34 * values_vec[2].list_of_lists[1][0][0]
    _values_vec_out[148] = _tmp34 * values_vec[2].list_of_lists[1][0][1]
    _values_vec_out[149] = _tmp34 * values_vec[2].list_of_lists[1][0][2]
    _values_vec_out[150] = (
        -values_vec[2].list_of_lists[1][0][0] ** 2
        - values_vec[2].list_of_lists[1][0][1] ** 2
        - values_vec[2].list_of_lists[1][0][2] ** 2
        + values_vec[2].list_of_lists[1][0][3] ** 2
    )
    _values_vec_out[151] = _tmp35 * values_vec[2].list_of_lists[1][1][0]
    _values_vec_out[152] = _tmp35 * values_vec[2].list_of_lists[1][1][1]
    _values_vec_out[153] = _tmp35 * values_vec[2].list_of_lists[1][1][2]
    _values_vec_out[154] = (
        -values_vec[2].list_of_lists[1][1][0] ** 2
        - values_vec[2].list_of_lists[1][1][1] ** 2
        - values_vec[2].list_of_lists[1][1][2] ** 2
        + values_vec[2].list_of_lists[1][1][3] ** 2
    )
    _values_vec_out[155] = _tmp36 * values_vec[2].list_of_lists[1][2][0]
    _values_vec_out[156] = _tmp36 * values_vec[2].list_of_lists[1][2][1]
    _values_vec_out[157] = _tmp36 * values_vec[2].list_of_lists[1][2][2]
    _values_vec_out[158] = (
        -values_vec[2].list_of_lists[1][2][0] ** 2
        - values_vec[2].list_of_lists[1][2][1] ** 2
        - values_vec[2].list_of_lists[1][2][2] ** 2
        + values_vec[2].list_of_lists[1][2][3] ** 2
    )
    _values_vec_out[159] = _tmp37 * values_vec[2].list_of_lists[2][0][0]
    _values_vec_out[160] = _tmp37 * values_vec[2].list_of_lists[2][0][1]
    _values_vec_out[161] = _tmp37 * values_vec[2].list_of_lists[2][0][2]
    _values_vec_out[162] = (
        -values_vec[2].list_of_lists[2][0][0] ** 2
        - values_vec[2].list_of_lists[2][0][1] ** 2
        - values_vec[2].list_of_lists[2][0][2] ** 2
        + values_vec[2].list_of_lists[2][0][3] ** 2
    )
    _values_vec_out[163] = _tmp38 * values_vec[2].list_of_lists[2][1][0]
    _values_vec_out[164] = _tmp38 * values_vec[2].list_of_lists[2][1][1]
    _values_vec_out[165] = _tmp38 * values_vec[2].list_of_lists[2][1][2]
    _values_vec_out[166] = (
        -values_vec[2].list_of_lists[2][1][0] ** 2
        - values_vec[2].list_of_lists[2][1][1] ** 2
        - values_vec[2].list_of_lists[2][1][2] ** 2
        + values_vec[2].list_of_lists[2][1][3] ** 2
    )
    _values_vec_out[167] = _tmp39 * values_vec[2].list_of_lists[2][2][0]
    _values_vec_out[168] = _tmp39 * values_vec[2].list_of_lists[2][2][1]
    _values_vec_out[169] = _tmp39 * values_vec[2].list_of_lists[2][2][2]
    _values_vec_out[170] = (
        -values_vec[2].list_of_lists[2][2][0] ** 2
        - values_vec[2].list_of_lists[2][2][1] ** 2
        - values_vec[2].list_of_lists[2][2][2] ** 2
        + values_vec[2].list_of_lists[2][2][3] ** 2
    )
    _values_vec_2D_out = [0.0] * 114
    _values_vec_2D_out[0] = 2 * values_vec_2D[0][0].x
    _values_vec_2D_out[1] = 2 * values_vec_2D[0][0].y
    _values_vec_2D_out[2] = _tmp40 * values_vec_2D[0][0].rot[0]
    _values_vec_2D_out[3] = _tmp40 * values_vec_2D[0][0].rot[1]
    _values_vec_2D_out[4] = _tmp40 * values_vec_2D[0][0].rot[2]
    _values_vec_2D_out[5] = (
        -values_vec_2D[0][0].rot[0] ** 2
        - values_vec_2D[0][0].rot[1] ** 2
        - values_vec_2D[0][0].rot[2] ** 2
        + values_vec_2D[0][0].rot[3] ** 2
    )
    _values_vec_2D_out[6] = _tmp41 * values_vec_2D[0][0].rot_vec[0][0]
    _values_vec_2D_out[7] = _tmp41 * values_vec_2D[0][0].rot_vec[0][1]
    _values_vec_2D_out[8] = _tmp41 * values_vec_2D[0][0].rot_vec[0][2]
    _values_vec_2D_out[9] = (
        -values_vec_2D[0][0].rot_vec[0][0] ** 2
        - values_vec_2D[0][0].rot_vec[0][1] ** 2
        - values_vec_2D[0][0].rot_vec[0][2] ** 2
        + values_vec_2D[0][0].rot_vec[0][3] ** 2
    )
    _values_vec_2D_out[10] = _tmp42 * values_vec_2D[0][0].rot_vec[1][0]
    _values_vec_2D_out[11] = _tmp42 * values_vec_2D[0][0].rot_vec[1][1]
    _values_vec_2D_out[12] = _tmp42 * values_vec_2D[0][0].rot_vec[1][2]
    _values_vec_2D_out[13] = (
        -values_vec_2D[0][0].rot_vec[1][0] ** 2
        - values_vec_2D[0][0].rot_vec[1][1] ** 2
        - values_vec_2D[0][0].rot_vec[1][2] ** 2
        + values_vec_2D[0][0].rot_vec[1][3] ** 2
    )
    _values_vec_2D_out[14] = _tmp43 * values_vec_2D[0][0].rot_vec[2][0]
    _values_vec_2D_out[15] = _tmp43 * values_vec_2D[0][0].rot_vec[2][1]
    _values_vec_2D_out[16] = _tmp43 * values_vec_2D[0][0].rot_vec[2][2]
    _values_vec_2D_out[17] = (
        -values_vec_2D[0][0].rot_vec[2][0] ** 2
        - values_vec_2D[0][0].rot_vec[2][1] ** 2
        - values_vec_2D[0][0].rot_vec[2][2] ** 2
        + values_vec_2D[0][0].rot_vec[2][3] ** 2
    )
    _values_vec_2D_out[18] = 2 * values_vec_2D[0][0].scalar_vec[0]
    _values_vec_2D_out[19] = 2 * values_vec_2D[0][0].scalar_vec[1]
    _values_vec_2D_out[20] = 2 * values_vec_2D[0][0].scalar_vec[2]
    _values_vec_2D_out[21] = _tmp44 * values_vec_2D[0][0].list_of_lists[0][0][0]
    _values_vec_2D_out[22] = _tmp44 * values_vec_2D[0][0].list_of_lists[0][0][1]
    _values_vec_2D_out[23] = _tmp44 * values_vec_2D[0][0].list_of_lists[0][0][2]
    _values_vec_2D_out[24] = (
        -values_vec_2D[0][0].list_of_lists[0][0][0] ** 2
        - values_vec_2D[0][0].list_of_lists[0][0][1] ** 2
        - values_vec_2D[0][0].list_of_lists[0][0][2] ** 2
        + values_vec_2D[0][0].list_of_lists[0][0][3] ** 2
    )
    _values_vec_2D_out[25] = _tmp45 * values_vec_2D[0][0].list_of_lists[0][1][0]
    _values_vec_2D_out[26] = _tmp45 * values_vec_2D[0][0].list_of_lists[0][1][1]
    _values_vec_2D_out[27] = _tmp45 * values_vec_2D[0][0].list_of_lists[0][1][2]
    _values_vec_2D_out[28] = (
        -values_vec_2D[0][0].list_of_lists[0][1][0] ** 2
        - values_vec_2D[0][0].list_of_lists[0][1][1] ** 2
        - values_vec_2D[0][0].list_of_lists[0][1][2] ** 2
        + values_vec_2D[0][0].list_of_lists[0][1][3] ** 2
    )
    _values_vec_2D_out[29] = _tmp46 * values_vec_2D[0][0].list_of_lists[0][2][0]
    _values_vec_2D_out[30] = _tmp46 * values_vec_2D[0][0].list_of_lists[0][2][1]
    _values_vec_2D_out[31] = _tmp46 * values_vec_2D[0][0].list_of_lists[0][2][2]
    _values_vec_2D_out[32] = (
        -values_vec_2D[0][0].list_of_lists[0][2][0] ** 2
        - values_vec_2D[0][0].list_of_lists[0][2][1] ** 2
        - values_vec_2D[0][0].list_of_lists[0][2][2] ** 2
        + values_vec_2D[0][0].list_of_lists[0][2][3] ** 2
    )
    _values_vec_2D_out[33] = _tmp47 * values_vec_2D[0][0].list_of_lists[1][0][0]
    _values_vec_2D_out[34] = _tmp47 * values_vec_2D[0][0].list_of_lists[1][0][1]
    _values_vec_2D_out[35] = _tmp47 * values_vec_2D[0][0].list_of_lists[1][0][2]
    _values_vec_2D_out[36] = (
        -values_vec_2D[0][0].list_of_lists[1][0][0] ** 2
        - values_vec_2D[0][0].list_of_lists[1][0][1] ** 2
        - values_vec_2D[0][0].list_of_lists[1][0][2] ** 2
        + values_vec_2D[0][0].list_of_lists[1][0][3] ** 2
    )
    _values_vec_2D_out[37] = _tmp48 * values_vec_2D[0][0].list_of_lists[1][1][0]
    _values_vec_2D_out[38] = _tmp48 * values_vec_2D[0][0].list_of_lists[1][1][1]
    _values_vec_2D_out[39] = _tmp48 * values_vec_2D[0][0].list_of_lists[1][1][2]
    _values_vec_2D_out[40] = (
        -values_vec_2D[0][0].list_of_lists[1][1][0] ** 2
        - values_vec_2D[0][0].list_of_lists[1][1][1] ** 2
        - values_vec_2D[0][0].list_of_lists[1][1][2] ** 2
        + values_vec_2D[0][0].list_of_lists[1][1][3] ** 2
    )
    _values_vec_2D_out[41] = _tmp49 * values_vec_2D[0][0].list_of_lists[1][2][0]
    _values_vec_2D_out[42] = _tmp49 * values_vec_2D[0][0].list_of_lists[1][2][1]
    _values_vec_2D_out[43] = _tmp49 * values_vec_2D[0][0].list_of_lists[1][2][2]
    _values_vec_2D_out[44] = (
        -values_vec_2D[0][0].list_of_lists[1][2][0] ** 2
        - values_vec_2D[0][0].list_of_lists[1][2][1] ** 2
        - values_vec_2D[0][0].list_of_lists[1][2][2] ** 2
        + values_vec_2D[0][0].list_of_lists[1][2][3] ** 2
    )
    _values_vec_2D_out[45] = _tmp50 * values_vec_2D[0][0].list_of_lists[2][0][0]
    _values_vec_2D_out[46] = _tmp50 * values_vec_2D[0][0].list_of_lists[2][0][1]
    _values_vec_2D_out[47] = _tmp50 * values_vec_2D[0][0].list_of_lists[2][0][2]
    _values_vec_2D_out[48] = (
        -values_vec_2D[0][0].list_of_lists[2][0][0] ** 2
        - values_vec_2D[0][0].list_of_lists[2][0][1] ** 2
        - values_vec_2D[0][0].list_of_lists[2][0][2] ** 2
        + values_vec_2D[0][0].list_of_lists[2][0][3] ** 2
    )
    _values_vec_2D_out[49] = _tmp51 * values_vec_2D[0][0].list_of_lists[2][1][0]
    _values_vec_2D_out[50] = _tmp51 * values_vec_2D[0][0].list_of_lists[2][1][1]
    _values_vec_2D_out[51] = _tmp51 * values_vec_2D[0][0].list_of_lists[2][1][2]
    _values_vec_2D_out[52] = (
        -values_vec_2D[0][0].list_of_lists[2][1][0] ** 2
        - values_vec_2D[0][0].list_of_lists[2][1][1] ** 2
        - values_vec_2D[0][0].list_of_lists[2][1][2] ** 2
        + values_vec_2D[0][0].list_of_lists[2][1][3] ** 2
    )
    _values_vec_2D_out[53] = _tmp52 * values_vec_2D[0][0].list_of_lists[2][2][0]
    _values_vec_2D_out[54] = _tmp52 * values_vec_2D[0][0].list_of_lists[2][2][1]
    _values_vec_2D_out[55] = _tmp52 * values_vec_2D[0][0].list_of_lists[2][2][2]
    _values_vec_2D_out[56] = (
        -values_vec_2D[0][0].list_of_lists[2][2][0] ** 2
        - values_vec_2D[0][0].list_of_lists[2][2][1] ** 2
        - values_vec_2D[0][0].list_of_lists[2][2][2] ** 2
        + values_vec_2D[0][0].list_of_lists[2][2][3] ** 2
    )
    _values_vec_2D_out[57] = 2 * values_vec_2D[1][0].x
    _values_vec_2D_out[58] = 2 * values_vec_2D[1][0].y
    _values_vec_2D_out[59] = _tmp53 * values_vec_2D[1][0].rot[0]
    _values_vec_2D_out[60] = _tmp53 * values_vec_2D[1][0].rot[1]
    _values_vec_2D_out[61] = _tmp53 * values_vec_2D[1][0].rot[2]
    _values_vec_2D_out[62] = (
        -values_vec_2D[1][0].rot[0] ** 2
        - values_vec_2D[1][0].rot[1] ** 2
        - values_vec_2D[1][0].rot[2] ** 2
        + values_vec_2D[1][0].rot[3] ** 2
    )
    _values_vec_2D_out[63] = _tmp54 * values_vec_2D[1][0].rot_vec[0][0]
    _values_vec_2D_out[64] = _tmp54 * values_vec_2D[1][0].rot_vec[0][1]
    _values_vec_2D_out[65] = _tmp54 * values_vec_2D[1][0].rot_vec[0][2]
    _values_vec_2D_out[66] = (
        -values_vec_2D[1][0].rot_vec[0][0] ** 2
        - values_vec_2D[1][0].rot_vec[0][1] ** 2
        - values_vec_2D[1][0].rot_vec[0][2] ** 2
        + values_vec_2D[1][0].rot_vec[0][3] ** 2
    )
    _values_vec_2D_out[67] = _tmp55 * values_vec_2D[1][0].rot_vec[1][0]
    _values_vec_2D_out[68] = _tmp55 * values_vec_2D[1][0].rot_vec[1][1]
    _values_vec_2D_out[69] = _tmp55 * values_vec_2D[1][0].rot_vec[1][2]
    _values_vec_2D_out[70] = (
        -values_vec_2D[1][0].rot_vec[1][0] ** 2
        - values_vec_2D[1][0].rot_vec[1][1] ** 2
        - values_vec_2D[1][0].rot_vec[1][2] ** 2
        + values_vec_2D[1][0].rot_vec[1][3] ** 2
    )
    _values_vec_2D_out[71] = _tmp56 * values_vec_2D[1][0].rot_vec[2][0]
    _values_vec_2D_out[72] = _tmp56 * values_vec_2D[1][0].rot_vec[2][1]
    _values_vec_2D_out[73] = _tmp56 * values_vec_2D[1][0].rot_vec[2][2]
    _values_vec_2D_out[74] = (
        -values_vec_2D[1][0].rot_vec[2][0] ** 2
        - values_vec_2D[1][0].rot_vec[2][1] ** 2
        - values_vec_2D[1][0].rot_vec[2][2] ** 2
        + values_vec_2D[1][0].rot_vec[2][3] ** 2
    )
    _values_vec_2D_out[75] = 2 * values_vec_2D[1][0].scalar_vec[0]
    _values_vec_2D_out[76] = 2 * values_vec_2D[1][0].scalar_vec[1]
    _values_vec_2D_out[77] = 2 * values_vec_2D[1][0].scalar_vec[2]
    _values_vec_2D_out[78] = _tmp57 * values_vec_2D[1][0].list_of_lists[0][0][0]
    _values_vec_2D_out[79] = _tmp57 * values_vec_2D[1][0].list_of_lists[0][0][1]
    _values_vec_2D_out[80] = _tmp57 * values_vec_2D[1][0].list_of_lists[0][0][2]
    _values_vec_2D_out[81] = (
        -values_vec_2D[1][0].list_of_lists[0][0][0] ** 2
        - values_vec_2D[1][0].list_of_lists[0][0][1] ** 2
        - values_vec_2D[1][0].list_of_lists[0][0][2] ** 2
        + values_vec_2D[1][0].list_of_lists[0][0][3] ** 2
    )
    _values_vec_2D_out[82] = _tmp58 * values_vec_2D[1][0].list_of_lists[0][1][0]
    _values_vec_2D_out[83] = _tmp58 * values_vec_2D[1][0].list_of_lists[0][1][1]
    _values_vec_2D_out[84] = _tmp58 * values_vec_2D[1][0].list_of_lists[0][1][2]
    _values_vec_2D_out[85] = (
        -values_vec_2D[1][0].list_of_lists[0][1][0] ** 2
        - values_vec_2D[1][0].list_of_lists[0][1][1] ** 2
        - values_vec_2D[1][0].list_of_lists[0][1][2] ** 2
        + values_vec_2D[1][0].list_of_lists[0][1][3] ** 2
    )
    _values_vec_2D_out[86] = _tmp59 * values_vec_2D[1][0].list_of_lists[0][2][0]
    _values_vec_2D_out[87] = _tmp59 * values_vec_2D[1][0].list_of_lists[0][2][1]
    _values_vec_2D_out[88] = _tmp59 * values_vec_2D[1][0].list_of_lists[0][2][2]
    _values_vec_2D_out[89] = (
        -values_vec_2D[1][0].list_of_lists[0][2][0] ** 2
        - values_vec_2D[1][0].list_of_lists[0][2][1] ** 2
        - values_vec_2D[1][0].list_of_lists[0][2][2] ** 2
        + values_vec_2D[1][0].list_of_lists[0][2][3] ** 2
    )
    _values_vec_2D_out[90] = _tmp60 * values_vec_2D[1][0].list_of_lists[1][0][0]
    _values_vec_2D_out[91] = _tmp60 * values_vec_2D[1][0].list_of_lists[1][0][1]
    _values_vec_2D_out[92] = _tmp60 * values_vec_2D[1][0].list_of_lists[1][0][2]
    _values_vec_2D_out[93] = (
        -values_vec_2D[1][0].list_of_lists[1][0][0] ** 2
        - values_vec_2D[1][0].list_of_lists[1][0][1] ** 2
        - values_vec_2D[1][0].list_of_lists[1][0][2] ** 2
        + values_vec_2D[1][0].list_of_lists[1][0][3] ** 2
    )
    _values_vec_2D_out[94] = _tmp61 * values_vec_2D[1][0].list_of_lists[1][1][0]
    _values_vec_2D_out[95] = _tmp61 * values_vec_2D[1][0].list_of_lists[1][1][1]
    _values_vec_2D_out[96] = _tmp61 * values_vec_2D[1][0].list_of_lists[1][1][2]
    _values_vec_2D_out[97] = (
        -values_vec_2D[1][0].list_of_lists[1][1][0] ** 2
        - values_vec_2D[1][0].list_of_lists[1][1][1] ** 2
        - values_vec_2D[1][0].list_of_lists[1][1][2] ** 2
        + values_vec_2D[1][0].list_of_lists[1][1][3] ** 2
    )
    _values_vec_2D_out[98] = _tmp62 * values_vec_2D[1][0].list_of_lists[1][2][0]
    _values_vec_2D_out[99] = _tmp62 * values_vec_2D[1][0].list_of_lists[1][2][1]
    _values_vec_2D_out[100] = _tmp62 * values_vec_2D[1][0].list_of_lists[1][2][2]
    _values_vec_2D_out[101] = (
        -values_vec_2D[1][0].list_of_lists[1][2][0] ** 2
        - values_vec_2D[1][0].list_of_lists[1][2][1] ** 2
        - values_vec_2D[1][0].list_of_lists[1][2][2] ** 2
        + values_vec_2D[1][0].list_of_lists[1][2][3] ** 2
    )
    _values_vec_2D_out[102] = _tmp63 * values_vec_2D[1][0].list_of_lists[2][0][0]
    _values_vec_2D_out[103] = _tmp63 * values_vec_2D[1][0].list_of_lists[2][0][1]
    _values_vec_2D_out[104] = _tmp63 * values_vec_2D[1][0].list_of_lists[2][0][2]
    _values_vec_2D_out[105] = (
        -values_vec_2D[1][0].list_of_lists[2][0][0] ** 2
        - values_vec_2D[1][0].list_of_lists[2][0][1] ** 2
        - values_vec_2D[1][0].list_of_lists[2][0][2] ** 2
        + values_vec_2D[1][0].list_of_lists[2][0][3] ** 2
    )
    _values_vec_2D_out[106] = _tmp64 * values_vec_2D[1][0].list_of_lists[2][1][0]
    _values_vec_2D_out[107] = _tmp64 * values_vec_2D[1][0].list_of_lists[2][1][1]
    _values_vec_2D_out[108] = _tmp64 * values_vec_2D[1][0].list_of_lists[2][1][2]
    _values_vec_2D_out[109] = (
        -values_vec_2D[1][0].list_of_lists[2][1][0] ** 2
        - values_vec_2D[1][0].list_of_lists[2][1][1] ** 2
        - values_vec_2D[1][0].list_of_lists[2][1][2] ** 2
        + values_vec_2D[1][0].list_of_lists[2][1][3] ** 2
    )
    _values_vec_2D_out[110] = _tmp65 * values_vec_2D[1][0].list_of_lists[2][2][0]
    _values_vec_2D_out[111] = _tmp65 * values_vec_2D[1][0].list_of_lists[2][2][1]
    _values_vec_2D_out[112] = _tmp65 * values_vec_2D[1][0].list_of_lists[2][2][2]
    _values_vec_2D_out[113] = (
        -values_vec_2D[1][0].list_of_lists[2][2][0] ** 2
        - values_vec_2D[1][0].list_of_lists[2][2][1] ** 2
        - values_vec_2D[1][0].list_of_lists[2][2][2] ** 2
        + values_vec_2D[1][0].list_of_lists[2][2][3] ** 2
    )
    return _foo, _bar, _scalar_vec_out, _values_vec_out, _values_vec_2D_out

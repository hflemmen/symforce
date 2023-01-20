// -----------------------------------------------------------------------------
// This file was autogenerated by symforce from template:
//     function/FUNCTION.h.jinja
// Do NOT modify by hand.
// -----------------------------------------------------------------------------

#pragma once

#include <Eigen/Dense>

#include <sym/rot3.h>

namespace sym {

/**
 * Residual that penalizes the difference between a value and prior (desired / measured value).
 *
 * In vector space terms that would be:
 *     prior - value
 *
 * In lie group terms:
 *     to_tangent(compose(inverse(value), prior))
 *
 * Args:
 *     sqrt_info: Square root information matrix to whiten residual. This can be computed from
 *                a covariance matrix as the cholesky decomposition of the inverse. In the case
 *                of a diagonal it will contain 1/sigma values. Pass in a single scalar if
 *                isotropic, a vector if diagonal, and a square matrix otherwise.
 *     jacobian: (3x3) jacobian of res wrt arg value (3)
 *     hessian: (3x3) Gauss-Newton hessian for arg value (3)
 *     rhs: (3x1) Gauss-Newton rhs for arg value (3)
 */
template <typename Scalar>
void PriorFactorRot3Isotropic(const sym::Rot3<Scalar>& value, const sym::Rot3<Scalar>& prior,
                              const Scalar sqrt_info, const Scalar epsilon,
                              Eigen::Matrix<Scalar, 3, 1>* const res = nullptr,
                              Eigen::Matrix<Scalar, 3, 3>* const jacobian = nullptr,
                              Eigen::Matrix<Scalar, 3, 3>* const hessian = nullptr,
                              Eigen::Matrix<Scalar, 3, 1>* const rhs = nullptr) {
  // Total ops: 202

  // Input arrays
  const Eigen::Matrix<Scalar, 4, 1>& _value = value.Data();
  const Eigen::Matrix<Scalar, 4, 1>& _prior = prior.Data();

  // Intermediate terms (69)
  const Scalar _tmp0 = _prior[3] * _value[0];
  const Scalar _tmp1 = _prior[0] * _value[3];
  const Scalar _tmp2 = _prior[2] * _value[1];
  const Scalar _tmp3 = _prior[1] * _value[2];
  const Scalar _tmp4 = _tmp0 - _tmp1 + _tmp2 - _tmp3;
  const Scalar _tmp5 = _prior[3] * _value[3];
  const Scalar _tmp6 = _prior[0] * _value[0];
  const Scalar _tmp7 = _prior[2] * _value[2];
  const Scalar _tmp8 = _prior[1] * _value[1];
  const Scalar _tmp9 = -_tmp6 - _tmp7 - _tmp8;
  const Scalar _tmp10 = _tmp5 - _tmp9;
  const Scalar _tmp11 = 1 - epsilon;
  const Scalar _tmp12 = std::min<Scalar>(_tmp11, std::fabs(_tmp10));
  const Scalar _tmp13 =
      sqrt_info * (2 * std::min<Scalar>(0, (((_tmp10) > 0) - ((_tmp10) < 0))) + 1);
  const Scalar _tmp14 = 2 * _tmp13;
  const Scalar _tmp15 =
      _tmp14 * std::acos(_tmp12) / std::sqrt(Scalar(1 - std::pow(_tmp12, Scalar(2))));
  const Scalar _tmp16 = _tmp15 * _tmp4;
  const Scalar _tmp17 = _prior[3] * _value[1];
  const Scalar _tmp18 = _prior[0] * _value[2];
  const Scalar _tmp19 = _prior[2] * _value[0];
  const Scalar _tmp20 = _prior[1] * _value[3];
  const Scalar _tmp21 = _tmp17 + _tmp18 - _tmp19 - _tmp20;
  const Scalar _tmp22 = _tmp15 * _tmp21;
  const Scalar _tmp23 = _prior[3] * _value[2];
  const Scalar _tmp24 = _prior[0] * _value[1];
  const Scalar _tmp25 = _prior[2] * _value[3];
  const Scalar _tmp26 = _prior[1] * _value[0];
  const Scalar _tmp27 = _tmp23 - _tmp24 - _tmp25 + _tmp26;
  const Scalar _tmp28 = _tmp15 * _tmp27;
  const Scalar _tmp29 = std::fabs(_tmp5 + _tmp6 + _tmp7 + _tmp8);
  const Scalar _tmp30 = std::min<Scalar>(_tmp11, _tmp29);
  const Scalar _tmp31 = 1 - std::pow(_tmp30, Scalar(2));
  const Scalar _tmp32 = std::acos(_tmp30);
  const Scalar _tmp33 = _tmp14 * _tmp32 / std::sqrt(_tmp31);
  const Scalar _tmp34 =
      _tmp33 * ((Scalar(1) / Scalar(2)) * _tmp5 + (Scalar(1) / Scalar(2)) * _tmp6 +
                (Scalar(1) / Scalar(2)) * _tmp7 + (Scalar(1) / Scalar(2)) * _tmp8);
  const Scalar _tmp35 = (Scalar(1) / Scalar(2)) * _tmp0;
  const Scalar _tmp36 = (Scalar(1) / Scalar(2)) * _tmp1;
  const Scalar _tmp37 = (Scalar(1) / Scalar(2)) * _tmp2;
  const Scalar _tmp38 = (Scalar(1) / Scalar(2)) * _tmp3;
  const Scalar _tmp39 = _tmp35 - _tmp36 + _tmp37 - _tmp38;
  const Scalar _tmp40 = _tmp13 * ((((_tmp11 - _tmp29) > 0) - ((_tmp11 - _tmp29) < 0)) + 1) *
                        (((-_tmp5 + _tmp9) > 0) - ((-_tmp5 + _tmp9) < 0));
  const Scalar _tmp41 = _tmp30 * _tmp32 * _tmp40 / (_tmp31 * std::sqrt(_tmp31));
  const Scalar _tmp42 = _tmp39 * _tmp41;
  const Scalar _tmp43 = _tmp40 / _tmp31;
  const Scalar _tmp44 = _tmp4 * _tmp43;
  const Scalar _tmp45 = _tmp34 - _tmp39 * _tmp44 + _tmp4 * _tmp42;
  const Scalar _tmp46 = (Scalar(1) / Scalar(2)) * _tmp23;
  const Scalar _tmp47 = (Scalar(1) / Scalar(2)) * _tmp24;
  const Scalar _tmp48 = (Scalar(1) / Scalar(2)) * _tmp25;
  const Scalar _tmp49 = (Scalar(1) / Scalar(2)) * _tmp26;
  const Scalar _tmp50 = _tmp46 - _tmp47 - _tmp48 + _tmp49;
  const Scalar _tmp51 = _tmp21 * _tmp43;
  const Scalar _tmp52 = _tmp21 * _tmp42 + _tmp33 * _tmp50 - _tmp39 * _tmp51;
  const Scalar _tmp53 = _tmp27 * _tmp41;
  const Scalar _tmp54 = _tmp27 * _tmp43;
  const Scalar _tmp55 = (Scalar(1) / Scalar(2)) * _tmp17;
  const Scalar _tmp56 = (Scalar(1) / Scalar(2)) * _tmp18;
  const Scalar _tmp57 = (Scalar(1) / Scalar(2)) * _tmp19;
  const Scalar _tmp58 = (Scalar(1) / Scalar(2)) * _tmp20;
  const Scalar _tmp59 =
      _tmp33 * (-_tmp55 - _tmp56 + _tmp57 + _tmp58) + _tmp39 * _tmp53 - _tmp39 * _tmp54;
  const Scalar _tmp60 = _tmp55 + _tmp56 - _tmp57 - _tmp58;
  const Scalar _tmp61 = _tmp41 * _tmp60;
  const Scalar _tmp62 =
      _tmp33 * (-_tmp46 + _tmp47 + _tmp48 - _tmp49) + _tmp4 * _tmp61 - _tmp44 * _tmp60;
  const Scalar _tmp63 = _tmp21 * _tmp61 + _tmp34 - _tmp51 * _tmp60;
  const Scalar _tmp64 = _tmp33 * _tmp39 + _tmp53 * _tmp60 - _tmp54 * _tmp60;
  const Scalar _tmp65 = _tmp41 * _tmp50;
  const Scalar _tmp66 = _tmp33 * _tmp60 + _tmp4 * _tmp65 - _tmp44 * _tmp50;
  const Scalar _tmp67 =
      _tmp21 * _tmp65 + _tmp33 * (-_tmp35 + _tmp36 - _tmp37 + _tmp38) - _tmp50 * _tmp51;
  const Scalar _tmp68 = _tmp34 + _tmp50 * _tmp53 - _tmp50 * _tmp54;

  // Output terms (4)
  if (res != nullptr) {
    Eigen::Matrix<Scalar, 3, 1>& _res = (*res);

    _res(0, 0) = _tmp16;
    _res(1, 0) = _tmp22;
    _res(2, 0) = _tmp28;
  }

  if (jacobian != nullptr) {
    Eigen::Matrix<Scalar, 3, 3>& _jacobian = (*jacobian);

    _jacobian(0, 0) = _tmp45;
    _jacobian(1, 0) = _tmp52;
    _jacobian(2, 0) = _tmp59;
    _jacobian(0, 1) = _tmp62;
    _jacobian(1, 1) = _tmp63;
    _jacobian(2, 1) = _tmp64;
    _jacobian(0, 2) = _tmp66;
    _jacobian(1, 2) = _tmp67;
    _jacobian(2, 2) = _tmp68;
  }

  if (hessian != nullptr) {
    Eigen::Matrix<Scalar, 3, 3>& _hessian = (*hessian);

    _hessian(0, 0) =
        std::pow(_tmp45, Scalar(2)) + std::pow(_tmp52, Scalar(2)) + std::pow(_tmp59, Scalar(2));
    _hessian(1, 0) = _tmp45 * _tmp62 + _tmp52 * _tmp63 + _tmp59 * _tmp64;
    _hessian(2, 0) = _tmp45 * _tmp66 + _tmp52 * _tmp67 + _tmp59 * _tmp68;
    _hessian(0, 1) = 0;
    _hessian(1, 1) =
        std::pow(_tmp62, Scalar(2)) + std::pow(_tmp63, Scalar(2)) + std::pow(_tmp64, Scalar(2));
    _hessian(2, 1) = _tmp62 * _tmp66 + _tmp63 * _tmp67 + _tmp64 * _tmp68;
    _hessian(0, 2) = 0;
    _hessian(1, 2) = 0;
    _hessian(2, 2) =
        std::pow(_tmp66, Scalar(2)) + std::pow(_tmp67, Scalar(2)) + std::pow(_tmp68, Scalar(2));
  }

  if (rhs != nullptr) {
    Eigen::Matrix<Scalar, 3, 1>& _rhs = (*rhs);

    _rhs(0, 0) = _tmp16 * _tmp45 + _tmp22 * _tmp52 + _tmp28 * _tmp59;
    _rhs(1, 0) = _tmp16 * _tmp62 + _tmp22 * _tmp63 + _tmp28 * _tmp64;
    _rhs(2, 0) = _tmp16 * _tmp66 + _tmp22 * _tmp67 + _tmp28 * _tmp68;
  }
}  // NOLINT(readability/fn_size)

// NOLINTNEXTLINE(readability/fn_size)
}  // namespace sym

// -----------------------------------------------------------------------------
// This file was autogenerated by symforce from template:
//     function/FUNCTION.h.jinja
// Do NOT modify by hand.
// -----------------------------------------------------------------------------

#pragma once

#include <Eigen/Dense>

#include <sym/pose2.h>

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
void PriorFactorPose2Isotropic(const sym::Pose2<Scalar>& value, const sym::Pose2<Scalar>& prior,
                               const Scalar sqrt_info, const Scalar epsilon,
                               Eigen::Matrix<Scalar, 3, 1>* const res = nullptr,
                               Eigen::Matrix<Scalar, 3, 3>* const jacobian = nullptr,
                               Eigen::Matrix<Scalar, 3, 3>* const hessian = nullptr,
                               Eigen::Matrix<Scalar, 3, 1>* const rhs = nullptr) {
  // Total ops: 38

  // Input arrays
  const Eigen::Matrix<Scalar, 4, 1>& _value = value.Data();
  const Eigen::Matrix<Scalar, 4, 1>& _prior = prior.Data();

  // Intermediate terms (13)
  const Scalar _tmp0 = _prior[0] * _value[1];
  const Scalar _tmp1 = _prior[1] * _value[0];
  const Scalar _tmp2 = _tmp0 - _tmp1;
  const Scalar _tmp3 = _prior[0] * _value[0] + _prior[1] * _value[1];
  const Scalar _tmp4 = _tmp3 + epsilon * ((((_tmp3) > 0) - ((_tmp3) < 0)) + Scalar(0.5));
  const Scalar _tmp5 = std::atan2(_tmp2, _tmp4);
  const Scalar _tmp6 = -_prior[2] + _value[2];
  const Scalar _tmp7 = -_prior[3] + _value[3];
  const Scalar _tmp8 = std::pow(_tmp4, Scalar(2));
  const Scalar _tmp9 = -_tmp2 * (-_tmp0 + _tmp1) / _tmp8 + _tmp3 / _tmp4;
  const Scalar _tmp10 = std::pow(_tmp2, Scalar(2)) + _tmp8;
  const Scalar _tmp11 = _tmp8 * _tmp9 / _tmp10;
  const Scalar _tmp12 = std::pow(sqrt_info, Scalar(2));

  // Output terms (4)
  if (res != nullptr) {
    Eigen::Matrix<Scalar, 3, 1>& _res = (*res);

    _res(0, 0) = _tmp5 * sqrt_info;
    _res(1, 0) = _tmp6 * sqrt_info;
    _res(2, 0) = _tmp7 * sqrt_info;
  }

  if (jacobian != nullptr) {
    Eigen::Matrix<Scalar, 3, 3>& _jacobian = (*jacobian);

    _jacobian.setZero();

    _jacobian(0, 0) = _tmp11 * sqrt_info;
    _jacobian(1, 1) = sqrt_info;
    _jacobian(2, 2) = sqrt_info;
  }

  if (hessian != nullptr) {
    Eigen::Matrix<Scalar, 3, 3>& _hessian = (*hessian);

    _hessian.setZero();

    _hessian(0, 0) = _tmp12 * std::pow(_tmp4, Scalar(4)) * std::pow(_tmp9, Scalar(2)) /
                     std::pow(_tmp10, Scalar(2));
    _hessian(1, 1) = _tmp12;
    _hessian(2, 2) = _tmp12;
  }

  if (rhs != nullptr) {
    Eigen::Matrix<Scalar, 3, 1>& _rhs = (*rhs);

    _rhs(0, 0) = _tmp11 * _tmp12 * _tmp5;
    _rhs(1, 0) = _tmp12 * _tmp6;
    _rhs(2, 0) = _tmp12 * _tmp7;
  }
}  // NOLINT(readability/fn_size)

// NOLINTNEXTLINE(readability/fn_size)
}  // namespace sym

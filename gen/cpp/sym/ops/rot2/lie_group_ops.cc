// -----------------------------------------------------------------------------
// This file was autogenerated by symforce from template:
//     cpp_templates/geo_package/ops/CLASS/lie_group_ops.cc.jinja
// Do NOT modify by hand.
// -----------------------------------------------------------------------------

#include "./lie_group_ops.h"

#include <algorithm>
#include <cmath>

#include <sym/rot2.h>

namespace sym {

template <typename Scalar>
sym::Rot2<Scalar> LieGroupOps<Rot2<Scalar>>::FromTangent(const TangentVec& vec,
                                                         const Scalar epsilon) {
  // Total ops: 2

  // Input arrays

  // Intermediate terms (0)

  // Output terms (1)
  Eigen::Matrix<Scalar, 2, 1> _res;

  _res[0] = std::cos(vec(0, 0));
  _res[1] = std::sin(vec(0, 0));

  return sym::Rot2<Scalar>(_res);
}

template <typename Scalar>
typename LieGroupOps<Rot2<Scalar>>::TangentVec LieGroupOps<Rot2<Scalar>>::ToTangent(
    const sym::Rot2<Scalar>& a, const Scalar epsilon) {
  // Total ops: 5

  // Input arrays
  const Eigen::Matrix<Scalar, 2, 1>& _a = a.Data();

  // Intermediate terms (0)

  // Output terms (1)
  Eigen::Matrix<Scalar, 1, 1> _res;

  _res(0, 0) = std::atan2(_a[1], _a[0] + epsilon * ((((_a[0]) > 0) - ((_a[0]) < 0)) + Scalar(0.5)));

  return _res;
}

template <typename Scalar>
sym::Rot2<Scalar> LieGroupOps<Rot2<Scalar>>::Retract(const sym::Rot2<Scalar>& a,
                                                     const TangentVec& vec, const Scalar epsilon) {
  // Total ops: 9

  // Input arrays
  const Eigen::Matrix<Scalar, 2, 1>& _a = a.Data();

  // Intermediate terms (2)
  const Scalar _tmp0 = std::sin(vec(0, 0));
  const Scalar _tmp1 = std::cos(vec(0, 0));

  // Output terms (1)
  Eigen::Matrix<Scalar, 2, 1> _res;

  _res[0] = _a[0] * _tmp1 - _a[1] * _tmp0;
  _res[1] = _a[0] * _tmp0 + _a[1] * _tmp1;

  return sym::Rot2<Scalar>(_res);
}

template <typename Scalar>
typename LieGroupOps<Rot2<Scalar>>::TangentVec LieGroupOps<Rot2<Scalar>>::LocalCoordinates(
    const sym::Rot2<Scalar>& a, const sym::Rot2<Scalar>& b, const Scalar epsilon) {
  // Total ops: 12

  // Input arrays
  const Eigen::Matrix<Scalar, 2, 1>& _a = a.Data();
  const Eigen::Matrix<Scalar, 2, 1>& _b = b.Data();

  // Intermediate terms (1)
  const Scalar _tmp0 = _a[0] * _b[0] + _a[1] * _b[1];

  // Output terms (1)
  Eigen::Matrix<Scalar, 1, 1> _res;

  _res(0, 0) = std::atan2(_a[0] * _b[1] - _a[1] * _b[0],
                          _tmp0 + epsilon * ((((_tmp0) > 0) - ((_tmp0) < 0)) + Scalar(0.5)));

  return _res;
}

}  // namespace sym

// Explicit instantiation
template struct sym::LieGroupOps<sym::Rot2<double>>;
template struct sym::LieGroupOps<sym::Rot2<float>>;

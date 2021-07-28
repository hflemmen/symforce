//  ----------------------------------------------------------------------------
// This file was autogenerated by symforce. Do NOT modify by hand.
// -----------------------------------------------------------------------------
#pragma once

#include <Eigen/Dense>
#include <sym/rot3.h>

namespace sym {

/**
 * C++ GroupOps implementation for <class 'symforce.geo.rot3.Rot3'>.
 */
template <typename Scalar>
struct GroupOps<Rot3<Scalar>> {
  using SelfJacobian = Eigen::Matrix<Scalar, LieGroupOps<Rot3<Scalar>>::TangentDim(),
                                     LieGroupOps<Rot3<Scalar>>::TangentDim()>;

  static sym::Rot3<Scalar> Identity();
  static sym::Rot3<Scalar> Inverse(const sym::Rot3<Scalar>& a);
  static sym::Rot3<Scalar> Compose(const sym::Rot3<Scalar>& a, const sym::Rot3<Scalar>& b);
  static sym::Rot3<Scalar> Between(const sym::Rot3<Scalar>& a, const sym::Rot3<Scalar>& b);
  static sym::Rot3<Scalar> InverseWithJacobian(
      const sym::Rot3<Scalar>& a, Eigen::Matrix<Scalar, 3, 3>* const res_D_a = nullptr);
  static sym::Rot3<Scalar> ComposeWithJacobians(
      const sym::Rot3<Scalar>& a, const sym::Rot3<Scalar>& b,
      Eigen::Matrix<Scalar, 3, 3>* const res_D_a = nullptr,
      Eigen::Matrix<Scalar, 3, 3>* const res_D_b = nullptr);
  static sym::Rot3<Scalar> BetweenWithJacobians(
      const sym::Rot3<Scalar>& a, const sym::Rot3<Scalar>& b,
      Eigen::Matrix<Scalar, 3, 3>* const res_D_a = nullptr,
      Eigen::Matrix<Scalar, 3, 3>* const res_D_b = nullptr);
};

}  // namespace sym

// Explicit instantiation
extern template struct sym::GroupOps<sym::Rot3<double>>;
extern template struct sym::GroupOps<sym::Rot3<float>>;

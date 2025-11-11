/*

CE LINK: https://godbolt.org/z/s1nT56aev

This is an artificially hard example, not least because it lacks
the context of a real task or any code that calls it.

TODO: How would you approach testing this code?
 - Would you test it as-is?
 - Do you understand what it's supposed to be doing?
 - How would you discover the expected properties and invariants
   of the system?
*/

#pragma once
#include <algorithm>
#include <cmath>
#include <numeric>
#include <vector>

struct Point {
  double x;
  double y;
};

class Complicated {
public:
  Complicated(std::vector<Point> &points, std::vector<double> &weights)
      : points(points), sqrt_weights(weights.size()), attenuation_rate(0.5),
        left_val(0) {
    std::transform(weights.begin(), weights.end(), sqrt_weights.begin(),
                   [](double w) { return std::sqrt(w); });
  }

  void set_left_comparator(std::vector<Point> points,
                           std::vector<double> points_values) {
    std::vector<double> points_distances;
    points_distances.reserve(points.size());
    for (std::size_t i = 0; i < points.size(); ++i) {
      auto distance = std::hypot(this->points[i].x - points[i].x,
                                 this->points[i].y - points[i].y);
      points_distances.push_back(distance);
    }

    std::vector<double> effective_point_values;
    effective_point_values.reserve(points_distances.size());
    for (std::size_t i = 0; i < points_distances.size(); ++i) {
      auto weighted_value =
          points_values[i] - attenuation_rate * points_distances[i];
      effective_point_values.push_back(weighted_value);
    }

    this->left_val = std::move(effective_point_values);
  }

  double compare(const std::vector<double> &right_val) {
    // we just assume the right points are all on-grid
    std::vector<double> weighted_right_points(right_val.size());
    std::transform(right_val.begin(), right_val.end(), sqrt_weights.begin(),
                   weighted_right_points.begin(),
                   [](double rv, double w) { return rv * w; });

    std::vector<double> prods(weighted_right_points.size());
    std::transform(left_val.begin(), left_val.end(),
                   weighted_right_points.begin(), prods.begin(),
                   [](double lv, double wv) { return lv * wv; });

    return std::accumulate(prods.begin(), prods.end(), 0.0);
  }

private:
  std::vector<Point> points;
  std::vector<double> sqrt_weights;
  double attenuation_rate;
  std::vector<double> left_val;
};

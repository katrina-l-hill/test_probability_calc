import math
import pytest
from app import calculate_probabilities  # Replace 'your_module_name' with the actual module name

# Normal test cases
def test_typical_values():
    prevalence = 0.05
    sensitivity = 0.9
    specificity = 0.95
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert isinstance(result, tuple)
    assert result[0] >= 0 and result[0] <= 1
    assert result[1] >= 0 and result[1] <= 1

def test_moderate_prevalence():
    prevalence = 0.3
    sensitivity = 0.85
    specificity = 0.9
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert isinstance(result, tuple)
    assert result[0] >= 0 and result[0] <= 1
    assert result[1] >= 0 and result[1] <= 1

def test_high_sensitivity_specificity():
    prevalence = 0.1
    sensitivity = 0.98
    specificity = 0.98
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert result[0] >= 0 and result[0] <= 1
    assert result[1] >= 0 and result[1] <= 1

# Edge test cases
def test_zero_prevalence():
    prevalence = 0.0
    sensitivity = 0.9
    specificity = 0.9
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert result[0] == 0.0  # Probability for positive test should be 0
    assert result[1] == 0.0  # Probability for negative test should also be 0

def test_perfect_sensitivity_zero_specificity():
    prevalence = 0.5
    sensitivity = 1.0
    specificity = 0.0
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert result[0] > 0  # The probability for positive test will be non-zero due to false positives
    assert result[1] == 0  # Probability for negative test is 0 due to perfect specificity

def test_perfect_specificity_zero_sensitivity():
    prevalence = 0.1
    sensitivity = 0.0
    specificity = 1.0
    result = calculate_probabilities(prevalence, sensitivity, specificity)
    assert result[0] == 0.0  # No disease detected for positive test due to zero sensitivity
    assert result[1] == 0.1  # Probability of disease given negative test should be 0.1

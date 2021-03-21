from solution import roman
import pytest


class TestSolution:
    """Test integer to roman number conversion."""

    def test_coversion(self):
        """Test with valid input."""

        test_set = [
            (15, 'XV'), (16, 'XVI'), (18, 'XVIII'),
            (28, 'XXVIII'), (37, 'XXXVII'), (48, 'XLVIII'),
            (58, 'LVIII'), (74, 'LXXIV'), (86, 'LXXXVI'),
            (89, 'LXXXIX'), (800, 'DCCC'), (2596, 'MMDXCVI'),
            (3000, 'MMM'), (4889, 'MMMMDCCCLXXXIX'), (6000, 'MMMMMM'),
        ]

        for input_value, expected_output in test_set:
            assert expected_output == roman(input_value)

    def test_invalid_input(self):
        """Test with invalid input type."""

        with pytest.raises(TypeError):
            roman('something')

    def test_negative_input(self):
        """Test negative input value."""

        with pytest.raises(ValueError):
            roman(-20)

    def test_zero_input(self):
        """Test zero as input."""

        with pytest.raises(ValueError):
            roman(0)

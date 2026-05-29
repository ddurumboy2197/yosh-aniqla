**Python (Pytest)**
```python
import pytest

def calculate_age(year_of_birth):
    return 2024 - year_of_birth

@pytest.mark.parametrize("year_of_birth, expected_age", [
    (1990, 34),
    (2000, 24),
    (2010, 14),
])
def test_calculate_age(year_of_birth, expected_age):
    assert calculate_age(year_of_birth) == expected_age

def test_calculate_age_invalid_year():
    with pytest.raises(TypeError):
        calculate_age("invalid_year")
```

**JavaScript (Jest)**
```javascript
function calculateAge(yearOfBirth) {
    return 2024 - yearOfBirth;
}

describe("calculateAge", () => {
    it("should calculate age correctly", () => {
        expect(calculateAge(1990)).toBe(34);
        expect(calculateAge(2000)).toBe(24);
        expect(calculateAge(2010)).toBe(14);
    });

    it("should throw error for invalid year", () => {
        expect(() => calculateAge("invalid_year")).toThrow();
    });
});
```

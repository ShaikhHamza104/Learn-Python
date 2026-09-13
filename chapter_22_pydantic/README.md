# 📚 Topic: Pydantic & Data Validation

In production Python systems and data pipelines, untrusted external input (from web APIs, user forms, CSV files, or databases) must be validated before it enters core business logic. Python's standard type hints do not perform runtime checks by default. **Pydantic** bridges this gap by enforcing type hints at runtime, automatically coercing compatible types, catching malformed data with detailed `ValidationError` messages, and enabling complex data validation rules.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_basic_models.py` | Defining `BaseModel` classes, type annotations, automatic type coercion, optional fields with defaults, and catching `ValidationError` |
| `02_field_validation.py` | Adding numeric and length boundaries via `Field()` (`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`), default values, and `Annotated` syntax |
| `03_custom_validators.py` | Writing custom business validation using `@field_validator` (single field) and `@model_validator(mode="after")` (cross-field logic) |
| `04_pydantic_for_data_science .py` | Real-world data engineering: nested models, batch row validation, and segregating clean records from rejected records before downstream analytics |

---

## 💡 Key points

1. **BaseModel Foundation (`01_basic_models.py`)**: Inheriting from `pydantic.BaseModel` transforms standard class definitions into self-validating data schemas.
2. **Type Coercion vs Strict Checking (`01_basic_models.py`)**: Pydantic intelligently coerces compatible input types (e.g., string `"25"` becomes integer `25`) while failing fast and raising a `ValidationError` when data cannot be safely cast.
3. **Field Constraints (`02_field_validation.py`)**: `Field()` allows setting numerical bounds (`gt=0`, `le=100`), string constraints (`min_length=1`), and default values directly alongside type annotations.
4. **Field Validators (`03_custom_validators.py`)**: The `@field_validator` decorator defines custom checks on individual attributes (e.g. verifying email formats or lowercasing usernames).
5. **Model-Level Cross-Field Validation (`03_custom_validators.py`)**: The `@model_validator(mode="after")` decorator allows inspecting multiple fields together (e.g. verifying `password == confirm_password`).
6. **Defensive Data Loading for Data Science (`04_pydantic_for_data_science .py`)**: Validating batches of raw dictionary rows catches corrupt records at the boundary, preventing silent data pollution in pandas DataFrames and machine learning pipelines.

---

## 🧠 Beginner tip

Pydantic is an external library that is not part of Python's standard library. Ensure you install it in your virtual environment:

```bash
pip install pydantic
# or with uv
uv pip install pydantic
```

Always use `ValidationError` to catch errors gracefully:

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str

try:
    user = User(id="invalid_id", name="Alice")
except ValidationError as e:
    print("Invalid data:", e)
```

---

## 📊 Where this is used in Data Science

- **Data Ingestion & Quality Gates**: Validating incoming raw data rows from CSV files, databases, or third-party APIs before appending them to feature stores or training tables.
- **FastAPI Endpoints & Inference Serving**: Serving ML models where request payloads (features) and response payloads (predictions, confidence intervals) are strictly validated.
- **Configuration Management**: Managing environment variables and model hyperparameters safely using `pydantic-settings`.

---

## 🛠️ Code Examples

### Basic Model Definition
```python
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(min_length=2)
    salary: float = Field(gt=0)
    is_active: bool = True

emp = Employee(id="101", name="Hamza", salary=75000.0)
print(emp.model_dump())
```

### Custom Field Validator
```python
from pydantic import BaseModel, field_validator

class Account(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value.lower()
```

---

## 🏃 Running the Lessons

Run any lesson script from your terminal:

```bash
python chapter_22_pydantic/01_basic_models.py
python chapter_22_pydantic/02_field_validation.py
python chapter_22_pydantic/03_custom_validators.py
python "chapter_22_pydantic/04_pydantic_for_data_science .py"
```

---

## ⏭️ Next Step

Test your understanding with hands-on practice in **[Chapter 22 Exercises](../chapter_22_exercises/README.md)**!

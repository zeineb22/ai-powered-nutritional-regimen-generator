from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    role: str

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    first_name: str
    last_name: str
    date_of_birth: date
    weight: float
    height: float
    medical_conditions: Optional[str] = None
class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    calories: float
    proteins: float
    carbohydrates: float
    fats: float
    unit_measure: str

class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    preparation_time: Optional[int] = None
    cooking_time: Optional[int] = None
    total_calories: Optional[float] = None
    protein_content: Optional[float] = None
    carb_content: Optional[float] = None
    fat_content: Optional[float] = None

class RecipeIngredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    recipe_id: int = Field(foreign_key='recipe.id')
    ingredient_id: int = Field(foreign_key='ingredient.id')
    quantity: float
    unit: str

class DietPlan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key='patient.id')
    recipe_id: int = Field(foreign_key='recipe.id')
    meal_type: str
    day_of_week: str
    portion_size: float

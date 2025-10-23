from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Annotated
from datetime import datetime
from pydantic import constr, conint, conlist

class User(BaseModel):
    name: Annotated[str, constr(min_length=1, max_length=100)]
    age: Annotated[int, conint(ge=0, le=150)]
    email: EmailStr
    phone: Annotated[str, constr(pattern=r"^\+?1?\d{9,15}$")]
    address: Annotated[str, constr(min_length=5)]
    city: Annotated[str, constr(min_length=1)]
    state: Annotated[str, constr(min_length=2, max_length=2)]
    zip_code: Annotated[str, constr(pattern=r"^\d{5}(-\d{4})?$")]
    created_at: datetime = Field(default_factory=datetime.now)
    
    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old and lives in {self.city}, {self.state} {self.zip_code}"

class UserCollection(BaseModel):
    users: List[User] = Field(default_factory=list)
    total_count: int = Field(default=0)
    
    def add_user(self, user: User) -> None:
        self.users.append(user)
        self.total_count += 1
    
    def get_users_by_city(self, city: str) -> List[User]:
        return [user for user in self.users if user.city.lower() == city.lower()]

class MathOperation(BaseModel):
    numbers: Annotated[List[int], Field(min_length=1, max_length=26)]
    operation: Annotated[str, constr(pattern=r"^(add|multiply|average)$")]
    
    def calculate(self) -> float:
        if self.operation == "add":
            return sum(self.numbers)
        elif self.operation == "multiply":
            result = 1
            for num in self.numbers:
                result *= num
            return result
        else:
            return sum(self.numbers) / len(self.numbers)

user1 = User(
    name="John Doe",
    age=30,
    email="john.doe@example.com",
    phone="+1234567890",
    address="123 Main St",
    city="New York",
    state="NY",
    zip_code="10001"
)

user2 = User(
    name="Jane Smith",
    age=25,
    email="jane.smith@example.com",
    phone="+1987654321",
    address="456 Oak Ave",
    city="Los Angeles",
    state="CA",
    zip_code="90210"
)

collection: UserCollection = UserCollection()
collection.add_user(user1)
collection.add_user(user2)

math_op: MathOperation = MathOperation(numbers=[1, 2, 3, 4, 5], operation="add")
result: float = math_op.calculate()

print(f"User info: {user1.get_info()}")
print(f"Total users: {collection.total_count}")
print(f"Math result: {result}")

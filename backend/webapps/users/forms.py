from typing import List, Optional
from fastapi import Request

class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = 'test'
        self.email: Optional[str] = 'test'
        self.password: Optional[str] = 'test'


    async def load_data(self):
        form = await self.request.form()
        print(form)
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not len(self.username) > 3:
            self.errors.append("username should be > 3 chars")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("email is required")
        if not self.password or not len(self.password) > 4:
            self.errors.append("password must be > 4 chars")
        if not self.errors:
            return True
        return False

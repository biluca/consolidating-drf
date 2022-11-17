from django.db.models import Model, CharField, BooleanField, DateTimeField


class Todo(Model):
    name = CharField(max_length=120)
    done = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

from django.db import models


class Todo(models.Model):
	title = models.CharField(max_length=64)
	created_at = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.title} at {self.created_at}'
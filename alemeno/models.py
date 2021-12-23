from django.db import models
from django.utils.html import format_html

# Create your models here.


class Kid(models.Model):
    kid_name = models.CharField(max_length=200)
    kid_age = models.IntegerField()
    parent_number = models.CharField(max_length=15)
    parent_email_address = models.EmailField()


class Image(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="uploads/")

    def image_tag(self):
        from django.utils.html import mark_safe

        return mark_safe(
            '<img src="%s" width="200px" height="200px" />' % (self.image.url)
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=200)
    food_choices = [
        ("VEG", "Veg"),
        ("FRUIT", "Fruit"),
        ("GRAIN", "Grain"),
        ("PROTEIN", "Protein"),
        ("DAIRY", "Dairy"),
        ("CONFECTIONARY", "Confectionary"),
        ("UNKOWN", "Unknown"),
    ]
    food_group = models.CharField(
        choices=food_choices, max_length=200, default="UNKOWN"
    )

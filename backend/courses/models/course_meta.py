from django.db import models
from .course import Course
from django.dispatch import receiver
from django.db.models.signals import post_save


class CourseMeta(models.Model):
    course_id = models.OneToOneField(Course, null=True, on_delete=models.PROTECT)
    cover_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'course_meta'
        verbose_name_plural = 'Доп инфо Курса'
        verbose_name = 'Доп инфо Курса'
        ordering = ['-created_at']

    def __str__(self):
        return f"ID:{self.id}   {self.course_id}"


@receiver(post_save, sender=Course)
def create_course_meta(sender, instance, created, **kwargs):
    if created:
        CourseMeta.objects.create(course_id=instance)


@receiver(post_save, sender=Course)
def save_course_meta(sender, instance, **kwargs):
    instance.coursemeta.save()

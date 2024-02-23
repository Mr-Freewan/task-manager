from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name=_('Name'),
                            unique=True)
    description = models.TextField(max_length=1024,
                                   verbose_name=_('Description'))
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='author',
                               verbose_name=_('Author'))
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 related_name='executor',
                                 verbose_name=_('Executor'))
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               related_name='status',
                               verbose_name=_('Status'))
    labels = models.ManyToManyField(Label,
                                    through='TaskLabelRelation',
                                    through_fields=('task', 'label'),
                                    blank=True,
                                    related_name='labels',
                                    verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Creation date'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ['id']

    def __str__(self):
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True, verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class AbdulBookManager(models.Manager):
    def get_queryset(self):
        return super(AbdulBookManager, self).get_queryset().filter(authors__first_name__icontains='a')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)
    objects = BookManager()
    abdul_objects = AbdulBookManager()

    def __str__(self):
        return self.title


class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(sex='M')


class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex='F')


class person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birth_date = models.DateField()
    people = models.Manager()
    men = MaleManager()
    female = FemaleManager()

    def baby_boomer_status(self):
        # "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    def get_full_name(self):
        # "Return's the person full name."
        return "%s %s" % (self.first_name, self.last_name)

    full_name = property(get_full_name)

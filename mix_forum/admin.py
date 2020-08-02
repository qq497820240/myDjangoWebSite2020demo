from django.contrib import admin
from .models import Train,Diesel,Electric,Steam

# Register your models here.

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'train_database'
    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using='train_database')

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

class TrainAdmin(MultiDBModelAdmin):
    list_display = ['Ttype','Tnum']
    list_per_page = 5
class DieselAdmin(MultiDBModelAdmin):
    list_per_page = 5
    list_display = ['D_name','D_first_date','D_num','D_type']
admin.site.register(Train,TrainAdmin)
admin.site.register(Diesel,DieselAdmin)
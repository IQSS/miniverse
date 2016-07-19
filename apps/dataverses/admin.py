from django.contrib import admin

from .models import Dataverse, CitationPageCheck, DataverseTheme, Template
from apps.datasets.models import Dataset

"""
class DatasetInline(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': ('id', 'protocol', 'identifier', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('doiseparator', 'fileaccessrequest', 'globalidcreatetime')
        }),
    )
    model = Dataset
    extra = 0
"""

class DataverseAdmin(admin.ModelAdmin):
    #inlines = (DatasetInline,)
    save_on_top = True
    list_display = ('id',  'name', 'alias', 'affiliation', 'dataversetype', )
    #readonly_fields = ('createdate', 'modificationtime')
    list_filter= ('permissionroot', 'dataversetype', )
    list_display_links = ('id', 'name')
admin.site.register(Dataverse, DataverseAdmin)

class DataverseThemeAdmin(admin.ModelAdmin):
    #inlines = (DatasetInline,)
    save_on_top = True
    list_display = ('dataverse',  'tagline', 'logo',)
    #readonly_fields = ('createdate', 'modificationtime')
admin.site.register(DataverseTheme, DataverseThemeAdmin)
"""
class DataverseTheme(models.Model):
    backgroundcolor = models.CharField(max_length=255, blank=True, null=True)
    linkcolor = models.CharField(max_length=255, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    logoalignment = models.CharField(max_length=255, blank=True, null=True)
    logobackgroundcolor = models.CharField(max_length=255, blank=True, null=True)
    logoformat = models.CharField(max_length=255, blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    textcolor = models.CharField(max_length=255, blank=True, null=True)
    dataverse = models.ForeignKey('Dvobject', blank=True, null=True)
"""
class CitationPageCheckAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dataverse',  'citation_found', 'modified', 'created', 'citation_url', )
    readonly_fields = ('created', 'modified')
    list_filter= ('citation_found',)
admin.site.register(CitationPageCheck, CitationPageCheckAdmin)



class TemplateAdmin(admin.ModelAdmin ):
    save_on_top = True
    list_display = ('name', 'dataverse', 'usagecount', 'createtime',)
    readonly_fields = ('createtime',)
    list_filter= ('dataverse', )
    list_display_links = ('name', )
admin.site.register(Template, TemplateAdmin)

from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import (Crop,Crop_Varieties,Crop_growth_stage_lists,variety_growth_stage,reco_Category,
                     tbl_ag_growth_stage_recos,growth_stage_recos_variety_flags,affliation_mask,
                     growth_stage_abiotic_stresses_alerts_recos,growth_stage_abiotic_stresses_alerts_variety_flags,
                     stress_type_list,stress_list,product_type_list,agro_input_product_list,growth_stage_pests_alerts_recos,
                     growth_stage_pests_alerts_variety_flags,growth_stage_weeds_alerts_recos,
                     growth_stage_weeds_alerts_variety_flags,brand_list,country_table,country_region_list,
                     agro_input_product_branded_list)


# <------------------------------------------------------------------------------------>
#Admin Table modelling

class CropAdmin(admin.ModelAdmin):
    list_display = ("crop_name","comments",)
    search_fields = ("crop_name",)
    ordering = ("crop_name",)

class Crop_VarietiesAdmin(admin.ModelAdmin):
    list_display = ("variety_name","seed_producer","potential_yield_lower","potential_yield_higher","potential_yiled_unit",
                    "days_to_maturity","r_to_r_spacing","p_to_p_spacing","spacing_units","planting_density","planting_density_units",
                    "min_base_temp","max_base_temp","color","hardness","links","remark",)
    search_fields = ("seed_producer","variety_name",)
    ordering = ("variety_name","seed_producer",)
    #exclude = ("crop_name",)

class CropgrowthstageAdmin(admin.ModelAdmin):
    list_display = ("growth_stage_name","growth_stage_num","comment","photo",)
    search_fields = ("growth_stage_name",)
    ordering = ("growth_stage_num",)
   # exclude = ("crop_name","variety_name",)

class varietygrowthstageAdmin(admin.ModelAdmin):
    list_display = ("gdd","cumulative_gdd","days","cumulative_days",)
    search_fields = ("gdd","days",)
    ordering = ("gdd","days",)
   # exclude = ("crop_name","variety_name",)

class recoCategoryAdmin(admin.ModelAdmin):
    list_display = ("reco_category_name","crop_name",)
    search_fields = ("crop_name","reco_category_name",)
    ordering = ("crop_name","reco_category_name",)
    #exclude = ("crop_name", "variety_name",)

class growth_stage_recosAdmin(admin.ModelAdmin):
    list_display = ("rec_product","rec_txt",  "rec_product_quantity", "rec_units","application_methods","stress_name",)
    search_fields = ("rec_product",)
    ordering = ("rec_product", "rec_product_quantity",)
    #exclude = ("crop_name", "variety_name","reco_category_name",)

class growth_stage_recos_variety_flagsAdmin(admin.ModelAdmin):
    list_display = ("crop","variety","reco_id","switch","comment",)
    list_filter =  ("switch",)
    search_fields = ["crop","variety"]
    actions = ['make_active','make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(switch=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(switch=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"

class affliation_maskAdmin(admin.ModelAdmin):
    list_display = ("affliation_name","comment",)
    search_fields = ("affliation_name",)
    ordering = ("affliation_name",)


class growth_stage_abiotic_stresses_alerts_recosAdmin(admin.ModelAdmin):
    list_display = ("crop","growth_stage","affiliation","min_flag","max_flag","min_threshold","max_threshold","unit","min_breach_alert_txt",)
    list_filter =  ("min_flag","max_flag",)
    search_fields = ["crop","growth_stage","affiliation",]
    actions = ['make_active','make_inactive','make_active1','make_inactive1']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(min_flag=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected min flags as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(min_flag=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected min flags as inactive"

    def make_active1(self, request, queryset):
        rows_updated = queryset.update(max_flag=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active1.short_description = "Mark selected max flags as active"

    def make_inactive1(self, request, queryset):
        rows_updated1 = queryset.update(max_flag=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive1.short_description = "Mark selected max flags as inactive"

class growth_stage_abiotic_stresses_alerts_variety_flagsAdmin(admin.ModelAdmin):
    list_display = ("crop","variety","abiotic_alert","switch","comment",)
    list_filter =  ("switch",)
    search_fields = ["crop","variety"]
    actions = ['make_active','make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(switch=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(switch=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"

class stress_type_listAdmin(admin.ModelAdmin):
    list_display = ("stress_type",)
    search_fields = ("stress_type",)
    ordering = ("stress_type",)

class stress_listAdmin(admin.ModelAdmin):
    list_display = ("stress_name","stress","min_favourable_temp","max_favourable_temp","unit","moisture","initial_symptoms",
                    "later_symptoms","comment",)
    search_fields = ("stress_name","stress",)
    ordering = ("stress_name",)

class product_type_listAdmin(admin.ModelAdmin):
    list_display = ("product_type",)
    search_fields = ("product_type",)
    ordering = ("product_type",)

class agro_input_product_listAdmin(admin.ModelAdmin):
    list_display = (
    "product_name", "producttype", "organic_flag",)
    search_fields = ("product_name", "producttype",)
    list_filter = ("organic_flag",)
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(organic_flag=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(organic_flag=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"

class growth_stage_pests_alerts_recosAdmin(admin.ModelAdmin):
    list_display = ("crop","growth_stage","stress_list","affiliation","alert_text","reco_category","productlist",
                    "rec_txt","rec_product_quantity","rec_units","application_method",)
    search_fields = ("crop","growth_stage",)
    ordering = ("growth_stage",)

class growth_stage_pests_alerts_variety_flagsAdmin(admin.ModelAdmin):
    list_display = ("crop", "variety", "pest_alert", "switch", "comment",)
    list_filter = ("switch",)
    search_fields = ["crop", "variety"]
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(switch=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(switch=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"

class growth_stage_weeds_alerts_recosAdmin(admin.ModelAdmin):
    list_display = ("crop", "growth_stage", "stress_list", "affiliation","min_favourable_temp","max_favourable_temp",
                    "alert_text", "reco_category", "productlist",
                    "rec_product", "rec_product_quantity", "rec_units", "application_method",)
    search_fields = ("crop", "growth_stage",)
    ordering = ("growth_stage",)

class growth_stage_weeds_alerts_variety_flagsAdmin(admin.ModelAdmin):

    #change_form_template = 'growth_stage_weeds_alerts_variety_flags'
    list_display = ("crop","variety","switch", "comment",)
    list_filter = ("switch",)
    search_fields = ["crop", "variety"]
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(switch=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(switch=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"


'''
    def get_crop_name(self,obj):
        return obj.crop.crop_name

    get_crop_name.short_description = "Crop name"

    def get_variety_name(self,obj):
        return  obj.variety.variety_name

    get_variety_name.short_description = "Variety name"

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == "POST":
            if request.POST.get("crop") and request.POST.get("variety"):
                for i in request.POST.getlist("recovLaLL"):
                    if growth_stage_weeds_alerts_variety_flags.objects.filter(crop_id=request.POST.get("crop"),
                                                                        variety_id = request.POST.get("variety"),
                                                                        weed_alert_id = i).exists():
                        obj =  growth_stage_weeds_alerts_variety_flags.objects.get(crop_id=request.POST.get("crop"),
                                                                                   variety_id=request.POST.get("variety"),
                                                                                weed_alert_id=i)
                        obj.switch = True if i in request.POST.getlist("recovLaLL") else False
                        obj.comment = request.POST.get("comment", ''.format(i), )
                        obj.save()
                    else:
                        growth_stage_weeds_alerts_variety_flags.objects.create(crop_id=request.POST.get("crop"),
                                                                               variety_id=request.POST.get("variety"),
                                                                               weed_alert_id=i,
                                                                               switch=True if i in request.POST.getlist() else False ,
                                                                               comment=request.POST.get("comment",
                                                                                                        ''.format(i), ))
                return HttpResponseRedirect("/models/growth_stage_weeds_alerts_variety_flags")
        return admin.ModelAdmin.add_view(self, request, form_url=form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if object_id:
            if request.method == "GET":
                object_id = growth_stage_weeds_alerts_variety_flags.objects.get(id = object_id)
                obj_list = growth_stage_weeds_alerts_variety_flags.objects.filter(crop = object_id.crop,
                                                                                  variety = object_id.variety)
                extra_context = {"method" : obj_list}
                if request.method == "POST":
                    return self.add_view(request, form_url, extra_context)
            return admin.ModelAdmin.change_view(self, request, object_id, form_url=form_url, extra_context=extra_context)
'''
class brand_listAdmin(admin.ModelAdmin):
    list_display = ("brand_name",)
    search_fields = ("brand_name",)
    ordering = ("brand_name",)

class country_tableAdmin(admin.ModelAdmin):
    list_display = ("country_name", "country_code_2", "country_code_num", "gbl_region", "gbl_sub_region",
                    "gbl_region_code",
                    "gbl_sub_region_code",
                    )
    search_fields = ("country_name", "country_code_2",)
    ordering = ("country_name", "country_code_2",)

class country_region_listAdmin(admin.ModelAdmin):
    list_display = ("country", "region_name",)
    search_fields = ("country", "region_name",)
    ordering = ("region_name",)

class agro_input_product_branded_listAdmin(admin.ModelAdmin):
    list_display = ("brand", "country", "region", "product_trade_name", "producttype","comb_flag","productlist",
                    "affiliation","component_num","component_fraction","product_physical_form",
                    "application_physical_state","recommended_application_method","target_insects",
                    "growth_stage","links",)
    list_filter = ("comb_flag",)
    search_fields = ["brand", "country"]
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        rows_updated = queryset.update(comb_flag=True)
        if rows_updated == 1:
            message_bit = "1 element was"
        else:
            message_bit = "%s elements were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)

    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        rows_updated1 = queryset.update(comb_flag=False)
        if rows_updated1 == 1:
            message_bit1 = "1 element was"
        else:
            message_bit1 = "%s elements were" % rows_updated1
        self.message_user(request, "%s successfully marked as inactive." % message_bit1)

    make_inactive.short_description = "Mark selected as inactive"

#admin.site.disable_action('delete_selected')
admin.site.site_title = 'Agronomy Admin'
admin.site.site_header = 'Agronomy Admin'

# <----------------------Admin Site Register---------------------------->

admin.site.register(Crop,CropAdmin)
admin.site.register(Crop_Varieties,Crop_VarietiesAdmin)
admin.site.register(Crop_growth_stage_lists,CropgrowthstageAdmin)
admin.site.register(variety_growth_stage,varietygrowthstageAdmin)
admin.site.register(reco_Category,recoCategoryAdmin)
admin.site.register(tbl_ag_growth_stage_recos,growth_stage_recosAdmin)
admin.site.register(growth_stage_recos_variety_flags,growth_stage_recos_variety_flagsAdmin)
admin.site.register(affliation_mask,affliation_maskAdmin)
admin.site.register(growth_stage_abiotic_stresses_alerts_recos,growth_stage_abiotic_stresses_alerts_recosAdmin)
admin.site.register(growth_stage_abiotic_stresses_alerts_variety_flags,growth_stage_abiotic_stresses_alerts_variety_flagsAdmin)
admin.site.register(stress_type_list,stress_type_listAdmin)
admin.site.register(stress_list,stress_listAdmin)
admin.site.register(product_type_list,product_type_listAdmin)
admin.site.register(agro_input_product_list,agro_input_product_listAdmin)
admin.site.register(growth_stage_pests_alerts_recos,growth_stage_pests_alerts_recosAdmin)
admin.site.register(growth_stage_pests_alerts_variety_flags,growth_stage_pests_alerts_variety_flagsAdmin)
admin.site.register(growth_stage_weeds_alerts_recos,growth_stage_weeds_alerts_recosAdmin)
admin.site.register(growth_stage_weeds_alerts_variety_flags,growth_stage_weeds_alerts_variety_flagsAdmin)
admin.site.register(brand_list,brand_listAdmin)
admin.site.register(country_table,country_tableAdmin)
admin.site.register(country_region_list,country_region_listAdmin)
admin.site.register(agro_input_product_branded_list,agro_input_product_branded_listAdmin)

from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Table modeling for all the Tables

class Crop(models.Model):
    crop_name = models.CharField(max_length=100, verbose_name="Crop Name", unique=True)
    comments = models.TextField(blank=True, null=True, verbose_name="Comments")

    class Meta:
        verbose_name = "Crops"
        db_table = "tbl_ag_crops"
        verbose_name_plural = "Crops"

    def __str__(self):
        return self.crop_name


class Crop_Varieties(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety_name = models.CharField(max_length=500, verbose_name="Variety Name", unique=True)
    seed_producer = models.CharField(max_length=100, verbose_name="Seed Producer")
    potential_yield_lower = models.FloatField(null=True, verbose_name="Potential Yield Lower")
    potential_yield_higher = models.FloatField(null=True, verbose_name="Potential Yield Higher")
    potential_yiled_unit = models.CharField(max_length=100, null=True, verbose_name="Potential Yield Unit")
    days_to_maturity = models.IntegerField(null=True, verbose_name="Days to Maturity")
    r_to_r_spacing = models.FloatField(null=True, verbose_name="R to R Spacing")
    p_to_p_spacing = models.FloatField(null=True, verbose_name="P to P Spacing")
    spacing_units = models.CharField(max_length=100, null=True, verbose_name="Spacing Units")
    planting_density = models.IntegerField(null=True, verbose_name="Planting Density")
    planting_density_units = models.CharField(max_length=100, null=True, verbose_name="Planting Density units")
    min_base_temp = models.IntegerField(null=True)
    max_base_temp = models.IntegerField(null=True)
    color = models.CharField(max_length=100, null=True, verbose_name="Color")
    hardness = models.CharField(max_length=100, null=True, verbose_name="Hardness")
    links = models.TextField(blank=True, null=True, verbose_name="Links")
    remark = models.TextField(blank=True, null=True, verbose_name="Remarks")

    class Meta:
        verbose_name = "Crop Varities"
        db_table = "tbl_ag_crop_varities"
        verbose_name_plural = "Crop Varities"

    def __str__(self):
        return self.variety_name


class Crop_growth_stage_lists(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growth_stage_name = models.CharField(max_length=100, verbose_name="Growth stage name")
    growth_stage_num = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Crop Stage Lists"
        db_table = "tbl_ag_crop_stage_lists"
        verbose_name_plural = "Crop Stage Lists"

    def __str__(self):
        return self.growth_stage_name


class variety_growth_stage(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = ChainedForeignKey(
        Crop_Varieties,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True)

    growth_stage = ChainedForeignKey(
        Crop_growth_stage_lists,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True)

    gdd = models.IntegerField()
    cumulative_gdd = models.IntegerField()
    days = models.IntegerField()
    cumulative_days = models.IntegerField()

    class Meta:
        verbose_name = "Variety Growth Stage Gdd"
        db_table = "tbl_ag_variety_growth_stage_gdd"
        verbose_name_plural = "Variety Growth Stage Gdd"


class reco_Category(models.Model):
    crop_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Crop Name")
    reco_category_name = models.CharField(max_length=100, verbose_name="Reco Category Name")

    class Meta:
        verbose_name = "Reco Category"
        db_table = "tbl_ag_reco_category"
        verbose_name_plural = "Reco Category"

    def __str__(self):
        return self.reco_category_name


class tbl_ag_growth_stage_recos(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    growth_stage = ChainedForeignKey(
        Crop_growth_stage_lists,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )

    reco_category = ChainedForeignKey(
        reco_Category,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )
    rec_txt = models.TextField(blank=True, null=True, verbose_name="Rec Text")
    rec_product = models.CharField(max_length=100, verbose_name="Rec Product")
    rec_product_quantity = models.FloatField()
    rec_units = models.CharField(max_length=100, verbose_name="Rec Units")
    application_methods = models.TextField(blank=True, null=True, verbose_name="Rec Units")
    stress_name = models.CharField(max_length=100, null=True, verbose_name="Stress Name")

    class Meta:
        verbose_name = "Growth Stage Recos"
        db_table = "tbl_ag_growth_stage_recos"
        verbose_name_plural = "Growth Stage Recos"

    def __str__(self):
        return self.rec_product


class growth_stage_recos_variety_flags(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.ForeignKey(Crop_Varieties, on_delete=models.CASCADE)
    reco_id = models.ForeignKey(tbl_ag_growth_stage_recos, on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)
    comment = models.TextField()

    class Meta:
        verbose_name = "Growth Stage Recos Variety Flags"
        db_table = "tbl_ag_growth_stage_recos_variety_flags"
        verbose_name_plural = "Growth Stage Recos Variety Flags"


class affliation_mask(models.Model):
    affliation_name = models.CharField(max_length=25, verbose_name="affliation_name")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")

    class Meta:
        verbose_name = "Affliation Mask"
        db_table = "tbl_ag_affliation_mask"
        verbose_name_plural = "Affliation Mask"

    def __str__(self):
        return self.affliation_name


class growth_stage_abiotic_stresses_alerts_recos(models.Model):
    affiliation = models.ForeignKey(affliation_mask, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growth_stage = ChainedForeignKey(
        Crop_growth_stage_lists,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )
    min_flag = models.BooleanField(default=False)
    max_flag = models.BooleanField(default=True)
    min_threshold = models.FloatField(null=True, verbose_name="min_threshold")
    max_threshold = models.FloatField(null=True, verbose_name="max_threshold")
    unit = models.CharField(max_length=25, verbose_name="unit")
    min_breach_alert_txt = models.TextField(blank=True, null=True, verbose_name="min_breach_alert_txt")

    class Meta:
        verbose_name = "Growth Stage Abiotic Stresses Alerts Recos"
        db_table = "growth_stage_abiotic_stresses_alerts_recos"
        verbose_name_plural = "Growth Stage Abiotic Stresses Alerts Recos"

    def __str__(self):
        return self.unit


class growth_stage_abiotic_stresses_alerts_variety_flags(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.ForeignKey(Crop_Varieties, on_delete=models.CASCADE)
    abiotic_alert = models.ForeignKey(growth_stage_abiotic_stresses_alerts_recos, on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)
    comment = models.TextField()

    class Meta:
        verbose_name = "Growth Stage Abiotic Stresses Alerts Variety Flags"
        db_table = "tbl_ag_growth_stage_abiotic_stresses_alerts_variety_flags"
        verbose_name_plural = "Growth Stage Abiotic Stresses Alerts Variety Flags"


class stress_type_list(models.Model):
    stress_type = models.CharField(max_length=50, verbose_name="Stress Type")

    class Meta:
        verbose_name = "Stress Type List"
        db_table = "tbl_ag_stress_type_list"
        verbose_name_plural = "Stress Type List"

    def __str__(self):
        return self.stress_type


class stress_list(models.Model):
    stress_name = models.CharField(max_length=50, verbose_name="Stress Name")
    stress = models.ForeignKey(stress_type_list, on_delete=models.CASCADE)
    min_favourable_temp = models.IntegerField()
    max_favourable_temp = models.IntegerField()
    unit = models.CharField(max_length=50, verbose_name="Unit")
    moisture = models.CharField(max_length=50, verbose_name="Moisture")
    initial_symptoms = models.CharField(max_length=50, verbose_name="initial symptoms")
    later_symptoms = models.CharField(max_length=50, verbose_name="later symptoms")
    comment = models.TextField(blank=True, null=True, verbose_name="comment")

    class Meta:
        verbose_name = "Stress List"
        db_table = "tbl_ag_stress_list"
        verbose_name_plural = "Stress List"

    def __str__(self):
        return self.stress_name


class product_type_list(models.Model):
    product_type = models.CharField(max_length=50, verbose_name="Product Type")

    class Meta:
        verbose_name = "Product Type List"
        db_table = "tbl_ag_product_type_list"
        verbose_name_plural = "Product Type List"

    def __str__(self):
        return self.product_type


class agro_input_product_list(models.Model):
    producttype = models.ForeignKey(product_type_list, on_delete=models.CASCADE)
    organic_flag = models.BooleanField(default=False)
    product_name = models.CharField(max_length=50, verbose_name="Product Name")

    class Meta:
        verbose_name = "Agro Input Product List"
        db_table = "tbl_ag_agro_input_product_list"
        verbose_name_plural = "Agro Input Product List"

    def __str__(self):
        return self.product_name


class growth_stage_pests_alerts_recos(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growth_stage = ChainedForeignKey(
        Crop_growth_stage_lists,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )
    stress_list = ChainedForeignKey(
        stress_list,
        chained_field="stress",
        chained_model_field="stress",
        show_all=False,
        auto_choose=True,
        sort=True, )
    affiliation = models.ForeignKey(affliation_mask, on_delete=models.CASCADE)
    alert_text = models.TextField()
    reco_category = models.ForeignKey(reco_Category, on_delete=models.CASCADE)
    productlist = models.ForeignKey(agro_input_product_list, on_delete=models.CASCADE)
    rec_txt = models.TextField()
    rec_product_quantity = models.FloatField()
    rec_units = models.CharField(max_length=50, verbose_name="Rec Units")
    application_method = models.TextField(null=True)

    class Meta:
        verbose_name = "Growth Stage Pests Alerts Recos",
        db_table = "tbl_ag_growth_stage_pests_alerts_recos"
        verbose_name_plural = "Growth Stage Pests Alerts Recos"

    def __str__(self):
        return self.rec_units


class growth_stage_pests_alerts_variety_flags(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.ForeignKey(Crop_Varieties, on_delete=models.CASCADE)
    pest_alert = models.ForeignKey(growth_stage_pests_alerts_recos, on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Growth Stage Pests Alerts Variety Flags"
        db_table = "tbl_ag_growth_stage_pests_alerts_variety_flags"
        verbose_name_plural = "Growth Stage Pests Alerts Variety Flags"


class growth_stage_weeds_alerts_recos(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growth_stage = ChainedForeignKey(
        Crop_growth_stage_lists,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )
    stress_list = ChainedForeignKey(
        stress_list,
        chained_field="stress",
        chained_model_field="stress",
        show_all=False,
        auto_choose=True,
        sort=True, )
    affiliation = models.ForeignKey(affliation_mask, on_delete=models.CASCADE)
    min_favourable_temp = models.IntegerField()
    max_favourable_temp = models.IntegerField()
    relative_humidity = models.CharField(max_length=50, verbose_name="relative humidity")
    alert_text = models.TextField(blank=True, null=True)
    reco_category = ChainedForeignKey(
        reco_Category,
        chained_field="crop",
        chained_model_field="crop",
        show_all=False,
        auto_choose=True,
        sort=True, )
    productlist = models.ForeignKey(agro_input_product_list, on_delete=models.CASCADE)
    rec_product = models.CharField(max_length=50, verbose_name="rec product")
    rec_product_quantity = models.FloatField()
    rec_units = models.CharField(max_length=50, verbose_name="rec units")
    application_method = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Growth Stage Weeds Alerts Recos"
        db_table = "tbl_ag_growth_stage_weeds_alerts_recos"
        verbose_name_plural = "Growth Stage Weeds Alerts Recos"

    def __str__(self):
        return self.rec_product


class growth_stage_weeds_alerts_variety_flags(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    variety = models.ForeignKey(Crop_Varieties, on_delete=models.CASCADE)
    weed_alert = models.ForeignKey(growth_stage_weeds_alerts_recos, on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Growth Stage Weeds Alerts Variety Flags"
        db_table = "tbl_ag_growth_stage_weeds_alerts_variety_flags"
        verbose_name_plural = "Growth Stage Weeds Alerts Variety Flags"


class brand_list(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name="brand name")

    class Meta:
        verbose_name = "Brand List"
        db_table = "tbl_ag_brand_list"
        verbose_name_plural = "Brand List"

    def __str__(self):
        return self.brand_name


class country_table(models.Model):
    country_name = models.CharField(max_length=50, verbose_name="country name")
    country_code_2 = models.CharField(max_length=50, verbose_name="country code 2")
    country_code_num = models.IntegerField()
    gbl_region = models.CharField(max_length=50, verbose_name="gbl region")
    gbl_sub_region = models.CharField(max_length=50, verbose_name="gbl sub region")
    gbl_region_code = models.IntegerField()
    gbl_sub_region_code = models.IntegerField()

    class Meta:
        verbose_name = "Country Table"
        db_table = "tbl_ag_country_table"
        verbose_name_plural = "Country Table"

    def __str__(self):
        return self.country_name


class country_region_list(models.Model):
    country = models.ForeignKey(country_table, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=50, verbose_name="region name")

    class Meta:
        verbose_name = "Country Region List"
        db_table = "tbl_ag_country_region_list"
        verbose_name_plural = "Country Region List"

    def __str__(self):
        return self.region_name


class agro_input_product_branded_list(models.Model):
    brand = models.ForeignKey(brand_list, on_delete=models.CASCADE)
    country = models.ForeignKey(country_table, on_delete=models.CASCADE)
    region = models.ForeignKey(country_region_list, on_delete=models.CASCADE)
    product_trade_name = models.CharField(max_length=100, verbose_name="product trade name")
    producttype = models.ForeignKey(product_type_list, on_delete=models.CASCADE)
    comb_flag = models.BooleanField(default=False)
    productlist = models.ForeignKey(agro_input_product_list, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(affliation_mask, on_delete=models.CASCADE)
    component_num = models.IntegerField()
    component_fraction = models.FloatField()
    product_physical_form = models.CharField(max_length=100, verbose_name="")
    application_physical_state = models.CharField(max_length=100, verbose_name="")
    recommended_application_method = models.TextField(blank=True, null=True)
    target_insects = models.CharField(max_length=100, verbose_name="")
    growth_stage = models.CharField(max_length=100, verbose_name="")
    links = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Input Product Branded List"
        db_table = "tbl_ag_agro_input_product_branded_list"
        verbose_name_plural = "Input Product Branded List"

    def __str__(self):
        return self.product_trade_name
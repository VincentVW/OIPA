from api.backend.filters import FilterField, BasicFilter
import iati


class ActivityFilter(BasicFilter):
    recipient_countries = FilterField(lookup_type='in', field='recipient_country')
    recipient_regions = FilterField(lookup_type='in', field='recipient_region')
    sectors = FilterField(lookup_type='in', field='sector')
    participating_organisations = FilterField(lookup_type='in', field='participating_organisation')
    min_total_budget = FilterField(lookup_type='gte', field='total_budget')
    max_total_budget = FilterField(lookup_type='lte', field='total_budget')

    class Meta:
        model = iati.models.Activity
        fields = [
            'recipient_countries',
            'recipient_regions',
            'sectors',
            'participating_organisations',
            'min_total_budget',
            'max_total_budget'
        ]
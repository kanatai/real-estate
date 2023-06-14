from drf_yasg.inspectors import SwaggerAutoSchema


class CustomActionNoParametersSchema(SwaggerAutoSchema):

    def get_query_parameters(self):
        return []
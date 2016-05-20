from marshmallow import Schema, fields, ValidationError, pre_load

class UsersSchema(Schema):
	id = fields.UUID(dump_only=True)
	username = fields.str(required=True, validate=must_not_be_blank)
	password = fields.str(required=True, validate=must_not_be_blank)
	first_name = fields.str(required=True, validate=must_not_be_blank)
	last_name = fields.str(required=True, validate=must_not_be_blank)
	formatted_name = fields.Method("format_name", dump_only=True)

	def format_name(self, users):
		return "{}, {}".format(author.first_name, author.last_name)

	@pre_load
    def process_author(self, data):
        name = data.get('name')
        if name:
            first, last = name.split(' ')

        data['first_name'] = first
        data['last_name'] = last
        return data

class PostSchema(Schema):
	id = fields.UUID()
	user_id = fields.UUID()
	post = fields.str(required=True)

# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

userschema = UsersSchema()
postschema = PostSchema()
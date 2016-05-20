#Simple function to create a JSON object to return in a response.
def json_message(value):
	json_a = {"message": value}
	json_response = json.dumps(json_a)

	return json_response
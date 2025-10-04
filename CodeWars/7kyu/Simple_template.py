# Implement function createTemplate which takes string with tags wrapped in {{brackets}} as input and returns closure, which can fill string with data (flat object, where keys are tag names).
#
# template = create_template("{{name}} likes {{animalType}}")
# template(name="John", animalType="dogs") # John likes dogs
# When key doesn't exist in the map, put there empty string.
#
# StringsRegular ExpressionsFundamentals